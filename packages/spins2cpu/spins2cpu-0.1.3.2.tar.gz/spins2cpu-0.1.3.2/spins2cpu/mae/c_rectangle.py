import logging
import numpy as np
from spins2cpu import functions
from spins2cpu.mae import c_rectangle_update

kB = 8.61733e-2 # 玻尔兹曼常数(meV/K)

def run(file, init, X, Y, J, JX, JY, A, arrays_temperatures, nequilibrium, nworks):
    logging.basicConfig(level=logging.INFO,format="%(message)s",filename=file,filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    num = X * Y
    N = num / 2
    logging.info("{} {:<12} {} {} × {:<8} {} {} + {:<8} {} {}".format(
        "configuration:", file.split('_')[0], "lattice dimensions:", X, Y, "iterations:", nequilibrium, nworks, "Atom number:", num))
    np.seterr(divide='ignore', invalid='ignore')
    arrays_values = np.where(arrays_temperatures < 0.01, 0, 1.0/(arrays_temperatures * kB))
    lav = arrays_values.shape[0]
    p = len(J)
    if p == 1:
        J = [J[0], J[0], 0.0, 0.0, 0.0]
        p = 5
    elif p == 2:
        J = [J[0], J[1], 0.0, 0.0, 0.0]
        p = 5
    elif p == 3:
        J = [J[0], J[1], J[2], 0.0, 0.0]
        p = 5
    elif p == 4:
        J = [J[0], J[1], J[2], J[3], J[3]]
        p = 5
    q = len(JX)
    if q == 0:
        JX = J
    elif q == 1:
        JX = [JX[0], JX[0], 0.0, 0.0, 0.0]
    elif q == 2:
        JX = [JX[0], JX[1], 0.0, 0.0, 0.0]
    elif q == 3:
        JX = [JX[0], JX[1], JX[2], 0.0, 0.0]
    elif q == 4:
        JX = [JX[0], JX[1], JX[2], JX[3], JX[3]]
    q = len(JY)
    if q == 0:
        JY = J
    elif q == 1:
        JY = [JY[0], JY[0], 0.0, 0.0, 0.0]
    elif q == 2:
        JY = [JY[0], JY[1], 0.0, 0.0, 0.0]
    elif q == 3:
        JY = [JY[0], JY[1], JY[2], 0.0, 0.0]
    elif q == 4:
        JY = [JY[0], JY[1], JY[2], JY[3], JY[3]]
    q = len(A)
    if q == 1:
        A = [A[0], A[0]]

    if p == 5:
        Ja, Jb, Jc, Jd, Je = J[0], J[1], J[2], J[3], J[4]
        Jax, Jbx, Jcx, Jdx, Jex = JX[0], JX[1], JX[2], JX[3], JX[4]
        Jay, Jby, Jcy, Jdy, Jey = JY[0], JY[1], JY[2], JY[3], JY[4]
        Aa, Ab = A[0], A[1]
        X_s = X // 4
        Y_s = Y // 4
        logging.info("{} {:<8} {} {:<8} {:<8} {:<8} {:<8} {:<8} {} {:<8} {:<8}".format(
            "init:", init, "parameters(meV):", Ja, Jb, Jc, Jd, Je, "anisotropy(meV):", Aa, Ab))
        logging.info("{:<32}{:<8} {:<8} {:<8} {:<8} {:<8}".format("",Jax, Jbx, Jcx, Jdx, Jex))
        logging.info("{:<32}{:<8} {:<8} {:<8} {:<8} {:<8}".format("",Jay, Jby, Jcy, Jdy, Jey))
        if init == "fm":
            logging.info("{:>16} {:>16}".format("Round", "magnetism(e)"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            m_ave = functions.Average(latt[:,:,:,:,2])
            logging.info("{:>16} {:>16.6}".format(0, m_ave))
            logging.info("{:>16} {:>16} {:>18} {:>16} {:>16}".format(
                "Temperature", "magnetism(e)", "susceptibility(e)", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
                m_ave = functions.Average(Nw)
                s_ave = functions.Average2(Nw)
                susceptibility = arrays_values[i] * num * (s_ave - m_ave ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>18.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave, susceptibility, Cv, t))
        elif init == "afm1":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0(e)", "magnetism1(e)"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            latt[[1,3],:,:,:,2] = -1
            m_ave0 = functions.Average(latt[[0,2],:,:,:,2])
            m_ave1 = functions.Average(latt[[1,3],:,:,:,2])
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>18} {:>18} {:>16} {:>16}".format(
                "Temperature", "magnetism0(e)", "magnetism1(e)", "susceptibility0(e)", "susceptibility1(e)", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
                arr_a, arr_b = Nw[:,[0,1,2,3,8,9,10,11]], Nw[:,[4,5,6,7,12,13,14,15]]
                m_ave0 = functions.Average(arr_a)
                m_ave1 = functions.Average(arr_b)
                s_ave0 = functions.Average2(arr_a)
                s_ave1 = functions.Average2(arr_b)
                susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>18.6f} {:>18.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        elif init == "afm2":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0(e)", "magnetism1(e)"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            latt[[0,1],1::2,:,:,2] = -1
            latt[[2,3],::2,:,:,2] = -1
            m_ave0 = functions.Average(latt[[0,1],::2,:,:,2] + latt[[2,3],1::2,:,:,2]) / 2
            m_ave1 = functions.Average(latt[[0,1],1::2,:,:,2] + latt[[2,3],::2,:,:,2]) / 2
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>18} {:>18} {:>16} {:>16}".format(
                "Temperature", "magnetism0(e)", "magnetism1(e)", "susceptibility0(e)", "susceptibility1(e)", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
                arr_a, arr_b = Nw[:,[0,2,4,6,9,11,13,15]], Nw[:,[1,3,5,7,8,10,12,14]]
                m_ave0 = functions.Average(arr_a)
                m_ave1 = functions.Average(arr_b)
                s_ave0 = functions.Average2(arr_a)
                s_ave1 = functions.Average2(arr_b)
                susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>18.6f} {:>18.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        elif init == "afm3":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0(e)", "magnetism1(e)"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            latt[:,[1,3],:,:,2] = -1
            m_ave0 = functions.Average(latt[:,[0,2],:,:,2])
            m_ave1 = functions.Average(latt[:,[1,3],:,:,2])
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>18} {:>18} {:>16} {:>16}".format(
                "Temperature", "magnetism0(e)", "magnetism1(e)", "susceptibility0(e)", "susceptibility1(e)", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
                arr_a, arr_b = Nw[:,::2], Nw[:,1::2]
                m_ave0 = functions.Average(arr_a)
                m_ave1 = functions.Average(arr_b)
                s_ave0 = functions.Average2(arr_a)
                s_ave1 = functions.Average2(arr_b)
                susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>18.6f} {:>18.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        elif init == "afm4":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0", "magnetism1"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            latt[:,[2,3],:,:,2] = -1
            m_ave0 = functions.Average(latt[:,[0,1],:,:,2])
            m_ave1 = functions.Average(latt[:,[2,3],:,:,2])
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>16} {:>16} {:>16} {:>16}".format(
                "Temperature", "magnetism0", "magnetism1", "susceptibility0", "susceptibility1", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
                arr_a, arr_b = Nw[:,[0,1,4,5,8,9,12,13]], Nw[:,[2,3,6,7,10,11,14,15]]
                m_ave0 = functions.Average(arr_a)
                m_ave1 = functions.Average(arr_b)
                s_ave0 = functions.Average2(arr_a)
                s_ave1 = functions.Average2(arr_b)
                susceptibility0 = arrays_values[i] * N * (s_ave0 - m_ave0 ** 2)
                susceptibility1 = arrays_values[i] * N * (s_ave1 - m_ave1 ** 2)
                Cv = arrays_values[i] ** 2 * (functions.Average2(Ew) - functions.Average(Ew) ** 2) / num
                logging.info("{:>16.2f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f} {:>16.6f}".format(
                    arrays_temperatures[i], m_ave0, m_ave1, susceptibility0, susceptibility1, Cv, t))
        elif init == "afm5":
            logging.info("{:>16} {:>16} {:>16}".format("Round", "magnetism0", "magnetism1"))
            latt = functions.OnesZNN(4, 4, Y_s, X_s)
            latt[[2,3],:,:,:,2] = -1
            m_ave0 = functions.Average(latt[[0,1],:,:,:,2])
            m_ave1 = functions.Average(latt[[2,3],:,:,:,2])
            logging.info("{:>16} {:>16.6} {:>16.6}".format(0, m_ave0, m_ave1))
            logging.info("{:>16} {:>16} {:>16} {:>16} {:>16} {:>16} {:>16}".format(
                "Temperature", "magnetism0", "magnetism1", "susceptibility0", "susceptibility1", "specific heat", "time(s)"))
            for i in range(lav):
                t, Nw, Ew = c_rectangle_update.iteration5(latt, X_s, Y_s, Ja, Jb, Jc, Jd, Je, Jax, Jbx, Jcx, Jdx, Jex, Jay, Jby, Jcy, Jdy, Jey, Aa, Ab, arrays_values[i], nequilibrium, nworks)
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
