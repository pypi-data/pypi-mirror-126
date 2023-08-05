import time
import numpy as np
from numba import njit
from spins2cpu import functions

def iteration3(latt, X_s, Y_s, Ja, J0, J1, Aa, val, nequilibrium, nworks):
    t0 = time.time()
    ju = abs(J0) * val
    if ju > 6:
        nequilibrium = nequilibrium * 3
        nworks = nworks * 3
    elif ju > 3:
        nequilibrium = nequilibrium * 2
        nworks = nworks * 2
    Nw = np.zeros((nworks, 8))
    Ew = np.zeros(nworks)
    for i in range(nequilibrium):
        laRn = functions.NormalrandNN(3, 4, Y_s, X_s)
        randvals = np.random.rand(3, 4, Y_s, X_s)
        latZ = energy_A(latt, Aa)
        laRZ = energy_A(laRn, Aa)
        Etot = update3(latt, latZ, laRn, laRZ, randvals, X_s, Y_s, Ja, J0, J1, val)
    for i in range(nworks):
        laRn = functions.NormalrandNN(3, 4, Y_s, X_s)
        randvals = np.random.rand(3, 4, Y_s, X_s)
        latZ = energy_A(latt, Aa)
        laRZ = energy_A(laRn, Aa)
        Etot = update3(latt, latZ, laRn, laRZ, randvals, X_s, Y_s, Ja, J0, J1, val)
        Ew[i] = Etot
        Nw[i] = functions.Average(latt[0,0,:,:,2]), functions.Average(latt[0,1,:,:,2]), functions.Average(latt[0,2,:,:,2]), functions.Average(latt[0,3,:,:,2]),\
                functions.Average(latt[1,0,:,:,2]), functions.Average(latt[1,1,:,:,2]), functions.Average(latt[1,2,:,:,2]), functions.Average(latt[1,3,:,:,2])
    t = time.time() - t0
    return t, Nw, Ew

def energy_A(latt, Aa):
    latt_2 = latt ** 2
    if Aa > 0:
        L_z_2 = latt_2[:,:,:,:,2]
        return ( -Aa * L_z_2 )
    else:
        L_y_2 = latt_2[:,:,:,:,1]
        return ( -Aa * L_y_2 )

@njit(cache=True)
def update3(latt, latZ, laRn, laRZ, randvals, X_s, Y_s, Ja, J0, J1, val):
    nn_sum = 0
    nn_p = 0
    for l in range(3):
        for k in range(4):
            for j in range(Y_s):
                for i in range(X_s):
                    k1  = 3 - k
                    k2  = (5 - k) if k > 1 else (1 - k)
                    k3  = (2 - k) if k%2 == 0 else (4 - k)
                    ipp = (i + 1) if (i + 1) < X_s else 0
                    inn = (i - 1) if (i - 1) > -1  else (X_s - 1)
                    jpp = (j + 1) if (j + 1) < Y_s else 0
                    jnn = (j - 1) if (j - 1) > -1  else (Y_s - 1)
                    if k == 0:
                        x_inn = i
                        x_ipp = ipp
                        y_jnn = j
                        y_jpp = jpp
                    elif k == 1:
                        x_inn = i
                        x_ipp = ipp
                        y_jnn = jnn
                        y_jpp = j
                    elif k == 2:
                        x_inn = inn
                        x_ipp = i
                        y_jnn = jnn
                        y_jpp = j
                    else:
                        x_inn = inn
                        x_ipp = i
                        y_jnn = j
                        y_jpp = jpp

                    if l == 0 or l == 2:
                        energy = ( latt[l,k,j,i,0] * ( -Ja * ( latt[l,k1,j    ,x_ipp,0] + latt[l,k1,j    ,x_inn,0] +
                                                               latt[l,k2,y_jpp,i    ,0] + latt[l,k2,y_jnn,i    ,0] +
                                                               latt[l,k3,y_jnn,x_inn,0] + latt[l,k3,y_jpp,x_ipp,0] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,0] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,0] + latt[1,k1,j    ,x_inn,0] +
                                                               latt[1,k2,y_jpp,i    ,0] + latt[1,k2,y_jnn,i    ,0] +
                                                               latt[1,k3,y_jnn,x_inn,0] + latt[1,k3,y_jpp,x_ipp,0] ) ) +
                                   latt[l,k,j,i,1] * ( -Ja * ( latt[l,k1,j    ,x_ipp,1] + latt[l,k1,j,x_inn    ,1] +
                                                               latt[l,k2,y_jpp,i    ,1] + latt[l,k2,y_jnn,i    ,1] +
                                                               latt[l,k3,y_jnn,x_inn,1] + latt[l,k3,y_jpp,x_ipp,1] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,1] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,1] + latt[1,k1,j    ,x_inn,1] +
                                                               latt[1,k2,y_jpp,i    ,1] + latt[1,k2,y_jnn,i    ,1] +
                                                               latt[1,k3,y_jnn,x_inn,1] + latt[1,k3,y_jpp,x_ipp,1] ) ) +
                                   latt[l,k,j,i,2] * ( -Ja * ( latt[l,k1,j    ,x_ipp,2] + latt[l,k1,j    ,x_inn,2] +
                                                               latt[l,k2,y_jpp,i    ,2] + latt[l,k2,y_jnn,i    ,2] +
                                                               latt[l,k3,y_jnn,x_inn,2] + latt[l,k3,y_jpp,x_ipp,2] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,2] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,2] + latt[1,k1,j    ,x_inn,2] +
                                                               latt[1,k2,y_jpp,i    ,2] + latt[1,k2,y_jnn,i    ,2] +
                                                               latt[1,k3,y_jnn,x_inn,2] + latt[1,k3,y_jpp,x_ipp,2] ) ) )
                        Erandn = ( laRn[l,k,j,i,0] * ( -Ja * ( latt[l,k1,j    ,x_ipp,0] + latt[l,k1,j    ,x_inn,0] +
                                                               latt[l,k2,y_jpp,i    ,0] + latt[l,k2,y_jnn,i    ,0] +
                                                               latt[l,k3,y_jnn,x_inn,0] + latt[l,k3,y_jpp,x_ipp,0] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,0] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,0] + latt[1,k1,j    ,x_inn,0] +
                                                               latt[1,k2,y_jpp,i    ,0] + latt[1,k2,y_jnn,i    ,0] +
                                                               latt[1,k3,y_jnn,x_inn,0] + latt[1,k3,y_jpp,x_ipp,0] ) ) +
                                   laRn[l,k,j,i,1] * ( -Ja * ( latt[l,k1,j    ,x_ipp,1] + latt[l,k1,j,x_inn    ,1] +
                                                               latt[l,k2,y_jpp,i    ,1] + latt[l,k2,y_jnn,i    ,1] +
                                                               latt[l,k3,y_jnn,x_inn,1] + latt[l,k3,y_jpp,x_ipp,1] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,1] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,1] + latt[1,k1,j    ,x_inn,1] +
                                                               latt[1,k2,y_jpp,i    ,1] + latt[1,k2,y_jnn,i    ,1] +
                                                               latt[1,k3,y_jnn,x_inn,1] + latt[1,k3,y_jpp,x_ipp,1] ) ) +
                                   laRn[l,k,j,i,2] * ( -Ja * ( latt[l,k1,j    ,x_ipp,2] + latt[l,k1,j    ,x_inn,2] +
                                                               latt[l,k2,y_jpp,i    ,2] + latt[l,k2,y_jnn,i    ,2] +
                                                               latt[l,k3,y_jnn,x_inn,2] + latt[l,k3,y_jpp,x_ipp,2] ) -
                                                        J0 *   latt[1,k ,j    ,i    ,2] -
                                                        J1 * ( latt[1,k1,j    ,x_ipp,2] + latt[1,k1,j    ,x_inn,2] +
                                                               latt[1,k2,y_jpp,i    ,2] + latt[1,k2,y_jnn,i    ,2] +
                                                               latt[1,k3,y_jnn,x_inn,2] + latt[1,k3,y_jpp,x_ipp,2] ) ) )
                    else:
                        energy = ( latt[l,k,j,i,0] * ( -Ja * ( latt[l,k1,j    ,x_ipp,0] + latt[l,k1,j    ,x_inn,0] +
                                                               latt[l,k2,y_jpp,i    ,0] + latt[l,k2,y_jnn,i    ,0] +
                                                               latt[l,k3,y_jnn,x_inn,0] + latt[l,k3,y_jpp,x_ipp,0] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,0] + latt[2,k ,j    ,i    ,0] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,0] + latt[0,k1,j    ,x_inn,0] +
                                                               latt[0,k2,y_jpp,i    ,0] + latt[0,k2,y_jnn,i    ,0] +
                                                               latt[0,k3,y_jnn,x_inn,0] + latt[0,k3,y_jpp,x_ipp,0] +
                                                               latt[2,k1,j    ,x_ipp,0] + latt[2,k1,j    ,x_inn,0] +
                                                               latt[2,k2,y_jpp,i    ,0] + latt[2,k2,y_jnn,i    ,0] +
                                                               latt[2,k3,y_jnn,x_inn,0] + latt[2,k3,y_jpp,x_ipp,0] ) ) +
                                   latt[l,k,j,i,1] * ( -Ja * ( latt[l,k1,j    ,x_ipp,1] + latt[l,k1,j    ,x_inn,1] +
                                                               latt[l,k2,y_jpp,i    ,1] + latt[l,k2,y_jnn,i    ,1] +
                                                               latt[l,k3,y_jnn,x_inn,1] + latt[l,k3,y_jpp,x_ipp,1] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,1] + latt[2,k ,j    ,i    ,1] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,1] + latt[0,k1,j    ,x_inn,1] +
                                                               latt[0,k2,y_jpp,i    ,1] + latt[0,k2,y_jnn,i    ,1] +
                                                               latt[0,k3,y_jnn,x_inn,1] + latt[0,k3,y_jpp,x_ipp,1] +
                                                               latt[2,k1,j    ,x_ipp,1] + latt[2,k1,j    ,x_inn,1] +
                                                               latt[2,k2,y_jpp,i    ,1] + latt[2,k2,y_jnn,i    ,1] +
                                                               latt[2,k3,y_jnn,x_inn,1] + latt[2,k3,y_jpp,x_ipp,1] ) ) +
                                   latt[l,k,j,i,2] * ( -Ja * ( latt[l,k1,j    ,x_ipp,2] + latt[l,k1,j    ,x_inn,2] +
                                                               latt[l,k2,y_jpp,i    ,2] + latt[l,k2,y_jnn,i    ,2] +
                                                               latt[l,k3,y_jnn,x_inn,2] + latt[l,k3,y_jpp,x_ipp,2] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,2] + latt[2,k ,j    ,i    ,2] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,2] + latt[0,k1,j    ,x_inn,2] +
                                                               latt[0,k2,y_jpp,i    ,2] + latt[0,k2,y_jnn,i    ,2] +
                                                               latt[0,k3,y_jnn,x_inn,2] + latt[0,k3,y_jpp,x_ipp,2] +
                                                               latt[2,k1,j    ,x_ipp,2] + latt[2,k1,j    ,x_inn,2] +
                                                               latt[2,k2,y_jpp,i    ,2] + latt[2,k2,y_jnn,i    ,2] +
                                                               latt[2,k3,y_jnn,x_inn,2] + latt[2,k3,y_jpp,x_ipp,2] ) ) )
                        Erandn = ( laRn[l,k,j,i,0] * ( -Ja * ( latt[l,k1,j    ,x_ipp,0] + latt[l,k1,j    ,x_inn,0] +
                                                               latt[l,k2,y_jpp,i    ,0] + latt[l,k2,y_jnn,i    ,0] +
                                                               latt[l,k3,y_jnn,x_inn,0] + latt[l,k3,y_jpp,x_ipp,0] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,0] + latt[2,k ,j    ,i    ,0] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,0] + latt[0,k1,j    ,x_inn,0] +
                                                               latt[0,k2,y_jpp,i    ,0] + latt[0,k2,y_jnn,i    ,0] +
                                                               latt[0,k3,y_jnn,x_inn,0] + latt[0,k3,y_jpp,x_ipp,0] +
                                                               latt[2,k1,j    ,x_ipp,0] + latt[2,k1,j    ,x_inn,0] +
                                                               latt[2,k2,y_jpp,i    ,0] + latt[2,k2,y_jnn,i    ,0] +
                                                               latt[2,k3,y_jnn,x_inn,0] + latt[2,k3,y_jpp,x_ipp,0] ) ) +
                                   laRn[l,k,j,i,1] * ( -Ja * ( latt[l,k1,j    ,x_ipp,1] + latt[l,k1,j    ,x_inn,1] +
                                                               latt[l,k2,y_jpp,i    ,1] + latt[l,k2,y_jnn,i    ,1] +
                                                               latt[l,k3,y_jnn,x_inn,1] + latt[l,k3,y_jpp,x_ipp,1] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,1] + latt[2,k ,j    ,i    ,1] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,1] + latt[0,k1,j    ,x_inn,1] +
                                                               latt[0,k2,y_jpp,i    ,1] + latt[0,k2,y_jnn,i    ,1] +
                                                               latt[0,k3,y_jnn,x_inn,1] + latt[0,k3,y_jpp,x_ipp,1] +
                                                               latt[2,k1,j    ,x_ipp,1] + latt[2,k1,j    ,x_inn,1] +
                                                               latt[2,k2,y_jpp,i    ,1] + latt[2,k2,y_jnn,i    ,1] +
                                                               latt[2,k3,y_jnn,x_inn,1] + latt[2,k3,y_jpp,x_ipp,1] ) ) +
                                   laRn[l,k,j,i,2] * ( -Ja * ( latt[l,k1,j    ,x_ipp,2] + latt[l,k1,j    ,x_inn,2] +
                                                               latt[l,k2,y_jpp,i    ,2] + latt[l,k2,y_jnn,i    ,2] +
                                                               latt[l,k3,y_jnn,x_inn,2] + latt[l,k3,y_jpp,x_ipp,2] ) -
                                                        J0 * ( latt[0,k ,j    ,i    ,2] + latt[2,k ,j    ,i    ,2] ) -
                                                        J1 * ( latt[0,k1,j    ,x_ipp,2] + latt[0,k1,j    ,x_inn,2] +
                                                               latt[0,k2,y_jpp,i    ,2] + latt[0,k2,y_jnn,i    ,2] +
                                                               latt[0,k3,y_jnn,x_inn,2] + latt[0,k3,y_jpp,x_ipp,2] +
                                                               latt[2,k1,j    ,x_ipp,2] + latt[2,k1,j    ,x_inn,2] +
                                                               latt[2,k2,y_jpp,i    ,2] + latt[2,k2,y_jnn,i    ,2] +
                                                               latt[2,k3,y_jnn,x_inn,2] + latt[2,k3,y_jpp,x_ipp,2] ) ) )

                    ez = latZ[l,k,j,i]
                    Ez = laRZ[l,k,j,i]
                    if val == 0:
                        if energy < 0:
                            pass
                            DeltaE = ez + energy - Ez - Erandn
                        else:
                            latt[l,k,j,i] *= -1
                            DeltaE = ez - energy - Ez - Erandn
                        if DeltaE < 0:
                            pass
                        else:
                            latt[l,k,j,i] = laRn[l,k,j,i]
                    else:
                        if energy < 0:
                            if randvals[l,k,j,i] < np.exp( 2.0 * val * energy ):
                                latt[l,k,j,i] *= -1
                                DeltaE = ez - energy - Ez - Erandn
                            else:
                                DeltaE = ez + energy - Ez - Erandn
                        else:
                            latt[l,k,j,i] *= -1
                            DeltaE = ez - energy - Ez - Erandn
                        if DeltaE < 0:
                            if randvals[l,k,j,i] < np.exp( val * DeltaE ):
                                latt[l,k,j,i] = laRn[l,k,j,i]
                        else:
                            latt[l,k,j,i] = laRn[l,k,j,i]

                    nn_sum += energy
                    nn_p += ez
    return ( nn_p + nn_sum / 2.0 )
