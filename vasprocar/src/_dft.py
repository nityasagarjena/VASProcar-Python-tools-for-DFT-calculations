# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#######################################################################
# Checking the presence of VASP files #################################
#######################################################################

vasp_files = 0

try: f = open(dir_files + '/CONTCAR'); f.close(); vasp_files += 1
except: 0 == 0

try: f = open(dir_files + '/POSCAR'); f.close(); vasp_files += 1
except: 0 == 0

try: f = open(dir_files + '/OUTCAR'); f.close(); vasp_files += 1
except: 0 == 0

try: f = open(dir_files + '/PROCAR'); f.close(); vasp_files += 1
except: 0 == 0 

try: f = open(dir_files + '/PROCAR.1'); f.close(); vasp_files += 1
except: 0 == 0

try: f = open(dir_files + '/KPOINTS'); f.close(); vasp_files += 1
except: 0 == 0

#######################################################################
# Checking the presence of QE files ###################################
#######################################################################

qe_files = 0

try: f = open(dir_files + '/scf.in'); f.close(); qe_files += 1
except: 0 == 0

try: f = open(dir_files + '/scf.out'); f.close(); qe_files += 1
except: 0 == 0

try: f = open(dir_files + '/nscf.in'); f.close(); qe_files += 1
except: 0 == 0 

try: f = open(dir_files + '/nscf.out'); f.close(); qe_files += 1
except: 0 == 0

try: f = open(dir_files + '/bands.in'); f.close(); qe_files += 1
except: 0 == 0 

try: f = open(dir_files + '/bands.out'); f.close(); qe_files += 1
except: 0 == 0 

#######################################################################
#######################################################################
#######################################################################

if (vasp_files != 0 and qe_files == 0): DFT = '_VASP/'
if (vasp_files == 0 and qe_files != 0): DFT = '_QE/' 
if (vasp_files == 0 and qe_files == 0): DFT = '_?/' 
if (vasp_files != 0 and qe_files != 0): DFT = '_?/' 
