import logging
import numpy as np
from spins2cpu import functions
from spins2cpu.ising import honeycomb_update

kB = 8.61733e-2 # 玻尔兹曼常数(meV/K)

def run(file, init, X, Y, J, arrays_temperatures, nequilibrium, nworks):
    logging.basicConfig(level=logging.INFO,format="%(message)s",filename=file,filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    N = X * Y
    num = N * 2
    logging.info("{} {:<12} {} {} × {:<8} {} {} + {:<8} {} {}".format(
        "configuration:", file.split('_')[0], "lattice dimensions:", X, Y, "iterations:", nequilibrium, nworks, "Atom number:", num))
    p = len(J)
    np.seterr(divide='ignore', invalid='ignore')
    arrays_values = np.where(arrays_temperatures < 0.01, 0, 1.0/(arrays_temperatures * kB))
    lav = len(arrays_values)
    if p == 1:
        J = [J[0], 0.0, 0.0]
        p = 3
    elif p == 2:
        J = [J[0], J[1], 0.0]
        p = 3

    if p == 3:
        Ja, Jb, Jc = J[0], J[1], J[2]
        X_s = X // 2
        Y_s = Y // 2
        logging.info("{} {:<8} {} {:<8} {:<8} {:<8}".format("init:", init, "parameters(meV):", Ja, Jb, Jc))
        if init == "fm":
            logging.info("{:>16} {:>16}".format("Round", "magnetism"))
            latt = functions.Onesint4(2, 4, Y_s, X_s)
            m_ave = functions.Average(latt)
            logging.info("{:>16} {:>16.6}".format(0, m_ave))
            logging.info("{:>16} {:>16} {:>16} {:>16} {:>16}".format("Temperature", "magnetism", "susceptibility", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = honeycomb_update.iteration3(latt, X_s, Y_s, Ja, Jb, Jc, arrays_values[i], nequilibrium, nworks)
                m_ave = functions.Average(Nw)
                s_ave = functions.Average2(Nw)
                susceptibility = arrays_values[i] * num * (s_ave - m_ave ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f}".format(arrays_temperatures[i], m_ave, susceptibility, Cv, t))
        elif init == "afm1":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0", "magnetism1"))
            latt = functions.Onesint4(2, 4, Y_s, X_s)
            latt[1] = -1
            m_ave0 = functions.Average(latt[0])
            m_ave1 = functions.Average(latt[1])
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>16} {:>16} {:>16} {:>16}".format(
                "Temperature", "magnetism0", "magnetism1", "susceptibility0", "susceptibility1", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = honeycomb_update.iteration3(latt, X_s, Y_s, Ja, Jb, Jc, arrays_values[i], nequilibrium, nworks)
                arr_a, arr_b = np.hsplit(Nw,2)
                m_ave0 = functions.Average(arr_a)
                m_ave1 = functions.Average(arr_b)
                s_ave0 = functions.Average2(arr_a)
                s_ave1 = functions.Average2(arr_b)
                susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        elif init == "random":
            logging.info("{:>16} {:>16} {:>16} {:>16}".format("Round", "magnetism0", "magnetism1", "time(s)"))
            latt = functions.Uniformint4(2, 4, Y_s, X_s)
            m_ave0 = functions.Average(latt[0])
            m_ave1 = functions.Average(latt[1])
            logging.info("{:>16} {:>16.6f} {:>16.6f}".format(0, m_ave0, m_ave1))
            for i in range(1,21):
                val = i + np.random.rand() + 1
                t, m_ave0, m_ave1 = honeycomb_update.looping3(latt, X_s, Y_s, Ja, Jb, Jc, val, nequilibrium)
                logging.info("{:>16} {:>16.6f} {:>16.6f}{:>16.6f}".format(i, m_ave0, m_ave1, t))
                if abs(m_ave0) > 0.99 and abs(m_ave1) > 0.99:
                    break
            if m_ave0 * m_ave1 > 0.5:
                logging.info("init: fm")
                logging.info("{:>16} {:>16} {:>16} {:>16} {:>16}".format("Temperature", "magnetism", "susceptibility", "specific heat", "time(s)"))
                for i in range(lav):
                    t, Nw, Ew = honeycomb_update.iteration3(latt, X_s, Y_s, Ja, Jb, Jc, arrays_values[i], nequilibrium, nworks)
                    m_ave = functions.Average(Nw)
                    s_ave = functions.Average2(Nw)
                    susceptibility = arrays_values[i] * num * (s_ave - m_ave ** 2)
                    Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                    logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f}".format(arrays_temperatures[i], m_ave, susceptibility, Cv, t))
            elif m_ave0 * m_ave1 < -0.5:
                logging.info("init: afm1")
                logging.info("{:>16} {:>16} {:>16} {:>16} {:>16} {:>16} {:>16}".format(
                    "Temperature", "magnetism0", "magnetism1", "susceptibility0", "susceptibility1", "specific heat", "time(s)"))
                for i in range(lav):
                    t, Nw, Ew = honeycomb_update.iteration3(latt, X_s, Y_s, Ja, Jb, Jc, arrays_values[i], nequilibrium, nworks)
                    arr_a, arr_b = np.hsplit(Nw,2)
                    m_ave0 = functions.Average(arr_a)
                    m_ave1 = functions.Average(arr_b)
                    s_ave0 = functions.Average2(arr_a)
                    s_ave1 = functions.Average2(arr_b)
                    susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                    susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                    Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                    logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f}".format(
                        arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        else:
            print("Inconsistent parameters...")

    else:
        print("Inconsistent parameters...")
