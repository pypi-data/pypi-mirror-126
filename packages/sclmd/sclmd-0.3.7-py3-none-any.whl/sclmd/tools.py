#!/usr/bin/env python
# -*- coding: utf-8 -*

import numpy as np


def dumpdisp(lammpsdata, trajectoriesfiles, index=[1], outputname="dispstructure"):
    def sumdisp(inputlist):
        return sum([_ ** 2 for _ in inputlist])
    def matdisp(matrix):
        return [sumdisp(_) for _ in matrix]
    def giveindex(matrix, index):
        needindex = []
        for i in index:
            disp = matdisp(matrix)
            # needvaule = np.sort(disp)[-index]
            needindex.append(np.argsort(disp)[-i])
        return needindex
    from ovito.io import export_file, import_file
    print("import LAMMPS data file %s" % lammpsdata)
    data = import_file(lammpsdata).source.compute(0)
    intposition = np.array(data.particles.positions).flatten()
    positionmatrix = []
    for trajfile in trajectoriesfiles:
        print("import trajectorie file %s" % trajfile)
        traj = import_file(trajfile, columns=[
            "Particle Type", "Position.X", "Position.Y", "Position.Z"])
        for frame_index in range(traj.source.num_frames):
            positionmatrix.append(np.array(traj.source.compute(
                frame_index).particles.positions).flatten())
    #print(giveindex(positionmatrix-intposition, index))
    for i, val in enumerate(giveindex(positionmatrix-intposition, index)):
        data.particles_.positions_[:] = positionmatrix[val].reshape(int(len(positionmatrix[val])/3),3)
        print("export LAMMPS data file %d" % index[i])
        export_file(data, outputname+"."+str(index[i])+".data", "lammps/data", atom_style="full")


def dumpavetraj(lammpsdata, trajectoriesfiles, position_only=False, outputname="avestructure.data"):
    from ovito.io import export_file, import_file

    # export average atom postions from MD trajectories files
    print("import LAMMPS data file %s" % lammpsdata)
    data = import_file(lammpsdata).source.compute(0)
    aveposition = np.zeros(
        [len(trajectoriesfiles), data.number_of_particles, 3])
    if position_only:
        for i, trajfile in enumerate(trajectoriesfiles):
            print("import trajectorie file %s" % trajfile)
            traj = import_file(trajfile, columns=[
                "Particle Type", "Position.X", "Position.Y", "Position.Z"])
            for frame_index in range(traj.source.num_frames):
                position = np.array(traj.source.compute(
                    frame_index).particles.positions)
                aveposition[i] = (aveposition[i]*frame_index +
                                  position)/(frame_index+1)
    else:
        for i, trajfile in enumerate(trajectoriesfiles):
            print("import trajectorie file %s" % trajfile)
            traj = import_file(trajfile, columns=[
                "Particle Type", "Position.X", "Position.Y", "Position.Z", "Force.X", "Force.Y", "Force.Z"])
            for frame_index in range(traj.source.num_frames):
                position = np.array(traj.source.compute(
                    frame_index).particles.positions)
                aveposition[i] = (aveposition[i]*frame_index +
                                  position)/(frame_index+1)
    data.particles_.positions_[:] = np.mean(aveposition, axis=0)
    print("export LAMMPS data file %s" % outputname)
    export_file(data, outputname, "lammps/data", atom_style="full")


def calHF(dlist=1, bathnum=2):
    import glob

    # calculate average heat flux
    print("Calculate heat flux.")
    # temperture=temp
    for filename in glob.glob('kappa.*.bath0.run0.dat'):
        with open(filename, 'r') as f:
            for line in f:
                temperture = float(line.split()[1])

    dlist = list(range(dlist))
    times = int(len(glob.glob('kappa.*.bath0.run*.dat')))
    kb = np.empty([bathnum, times])

    for i in range(bathnum):
        for j in range(times):
            kappafile = "kappa." + \
                str(int(temperture))+".bath"+str(i)+".run"+str(j)+".dat"
            for files in glob.glob(kappafile):
                with open(files, 'r') as f:
                    for line in f:
                        kb[i][j] = line.split()[2]
#                        temperture=float(line.split()[1])
    oldkb = np.delete(kb, dlist, axis=1)
    balancekb = np.delete(kb, dlist, axis=1)
    for i in range(balancekb.shape[0]):
        for j in range(balancekb.shape[1]):
            balancekb[i][j] = np.mean(oldkb[i][0:j+1])

    np.savetxt('heatflux.'+str(int(temperture)) +
               '.dat', np.transpose(balancekb))


def calTC(delta, dlist=1, L=None, A=None):
    # L，A units in Angstrom and Angstrom**2, respectively
    import glob

    # calculate thermal conductance
    print("Calculate thermal conductance.")
    delta = delta
    # temperture=temp
    for filename in glob.glob('kappa.*.bath0.run0.dat'):
        with open(filename, 'r') as f:
            for line in f:
                temperture = float(line.split()[1])
    dlist = list(range(dlist))
    times = int(len(glob.glob('kappa.*.bath*.run*.dat'))/2)
    kb = np.empty([2, times])

    for i in range(2):
        for j in range(times):
            kappafile = "kappa." + \
                str(int(temperture))+".bath"+str(i)+".run"+str(j)+".dat"
            for files in glob.glob(kappafile):
                with open(files, 'r') as f:
                    for line in f:
                        kb[i][j] = line.split()[2]
#                        temperture=float(line.split()[1])
    if delta != 0:
        kappa = (kb[0]-kb[1])/2/(delta*temperture)
        kappa = np.delete(kappa, dlist)
        # for i in range(len(kappa)):
        #    kappa[i]=np.mean(kappa[0:i+1])

        np.savetxt('thermalconductance.'+str(int(temperture))+'.dat',
                   (np.mean(kappa), np.std(kappa)), header="Mean(nW/K) Std(nW/K)")
        if L is not None and A is not None:
            np.savetxt('thermalconductivity.'+str(int(temperture))+'.dat',
                       (np.mean(kappa*L/A*10), np.std(kappa*L/A*10)), header="Mean(W/m-K) Std(W/m-K)")
    else:
        print("delta=0, no thermal conductance/conductivity calculated.")


def get_atomname(mass):
    """
    get the element name from its atomic mass by checking the dictionary
    """
    import sclmd.units as U

    for key, value in list(U.AtomicMassTable.items()):
        if abs(mass-value) < 0.01:
            return key


def eff():
    '''
    eliminate false frequencies
    '''
    dynmatdat = np.loadtxt('dynmat.dat')
    dynlen = int(3*np.sqrt(len(dynmatdat)/3))
    dynmat = dynmatdat.reshape((dynlen, dynlen))
    #dynmat = (dynmat+dynmat.conjugate().transpose())/2
    eigvals, eigvecs = np.linalg.eigh(dynmat)
    while not (eigvals > 0).all():
        for i, val in enumerate(eigvals):
            if val < 0:
                print('False frequency exists in system DOF %i ' % i)
                eigvals[i] = 0
        dynmat = np.linalg.multi_dot([eigvecs, np.identity(
            len(eigvals))*eigvals, np.linalg.inv(eigvecs)])
        eigvals, eigvecs = np.linalg.eigh(dynmat)
    np.savetxt('dynmatmod.dat', dynmat)


if __name__ == "__main__":
    from sclmd.tools import dumpavetraj
    lammps = "structure.data"
    trajectories = ["trajectories.300.run0.ani", "trajectories.300.run1.ani",
                    "trajectories.300.run2.ani", "trajectories.300.run3.ani", "trajectories.300.run4.ani"]
    dumpavetraj(lammps, trajectories, position_only=False,
                outputname="avetrajectories.data")
    avefiles = ["avestructure.300.run0.dat", "avestructure.300.run1.dat",
                "avestructure.300.run2.dat", "avestructure.300.run3.dat", "avestructure.300.run4.dat"]
    dumpavetraj(lammps, avefiles, position_only=True,
                outputname="avestructure.data")
                
    from sclmd.tools import dumpdisp
    lammps = "avestructure.data"
    trajectories = ["trajectories.100.run0.ani", "trajectories.100.run1.ani",
                    "trajectories.100.run2.ani", "trajectories.100.run3.ani", 
                    "trajectories.100.run4.ani", "trajectories.100.run5.ani",
                    "trajectories.100.run6.ani", "trajectories.100.run7.ani",
                    "trajectories.100.run8.ani", "trajectories.100.run9.ani",
                    "trajectories.100.run10.ani", "trajectories.100.run11.ani",
                    "trajectories.100.run12.ani", "trajectories.100.run13.ani",
                    "trajectories.100.run14.ani", "trajectories.100.run15.ani",
                    "trajectories.100.run16.ani", "trajectories.100.run17.ani",
                    "trajectories.100.run18.ani", "trajectories.100.run19.ani",
                    ]
    dumpdisp(lammps, trajectories, index=[1,10,100], outputname="dispstructure")
