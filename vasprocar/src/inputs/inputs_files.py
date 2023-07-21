# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print("#######################################################")
print("################ input Files Generator ################")
print("#######################################################")
print(" ")

# ------------------------------------------------------------------------------
# Checking if the "inputs" folder exists, if it does not exist it is created ---
# ------------------------------------------------------------------------------
if os.path.isdir(dir_files + '/inputs'):
    0 == 0
else:
    os.mkdir(dir_files + '/inputs')
# --------------------------------

print("#######################################################")
print("# Which input file do you want?                      ##")
print("#######################################################")
print("# [1] Bands (Plot 2D)                                ##")
print("# [2] Projection of Spin components                  ##")
print("# [3] Projection of Orbitals                         ##")
print("# [4] Projection of the REGIONS (Location)           ##")
print("# [5] DOS                                            ##")
print("# [6] All input files                                ##")
print("#######################################################")
tipo = input (" "); tipo = int(tipo)
print(" ")

#----------------------------------------------------------------------
# Copy [input files] to the input folder directory --------------------
#----------------------------------------------------------------------

if (tipo == 1 or tipo == 6):
   try: f = open(dir_files + '/inputs/input.vasprocar.bands'); f.close(); os.remove(dir_files + '/inputs/input.vasprocar.bands')
   except: 0 == 0
   #--------------------------------------------------
   source = main_dir + '/inputs/input.vasprocar.bands'
   destination = dir_files + '/inputs/input.vasprocar.bands'
   shutil.copyfile(source, destination)

if (tipo == 2 or tipo == 6):
   try: f = open(dir_files + '/inputs/input.vasprocar.spin'); f.close(); os.remove(dir_files + '/inputs/input.vasprocar.spin')
   except: 0 == 0
   #--------------------------------------------------
   source = main_dir + '/inputs/input.vasprocar.spin'
   destination = dir_files + '/inputs/input.vasprocar.spin'
   shutil.copyfile(source, destination)

if (tipo == 3 or tipo == 6):
   try: f = open(dir_files + '/inputs/input.vasprocar.orbitals'); f.close(); os.remove(dir_files + '/inputs/input.vasprocar.orbitals')
   except: 0 == 0
   #--------------------------------------------------
   source = main_dir + '/inputs/input.vasprocar.orbitals'
   destination = dir_files + '/inputs/input.vasprocar.orbitals'
   shutil.copyfile(source, destination)

if (tipo == 4 or tipo == 6):
   try: f = open(dir_files + '/inputs/input.vasprocar.location'); f.close(); os.remove(dir_files + '/inputs/input.vasprocar.location')
   except: 0 == 0
   #--------------------------------------------------
   source = main_dir + '/inputs/input.vasprocar.location'
   destination = dir_files + '/inputs/input.vasprocar.location'
   shutil.copyfile(source, destination)

if (tipo == 5 or tipo == 6):
   try: f = open(dir_files + '/inputs/input.vasprocar.dos'); f.close(); os.remove(dir_files + '/inputs/input.vasprocar.dos')
   except: 0 == 0
   #--------------------------------------------------
   source = main_dir + '/inputs/input.vasprocar.dos'
   destination = dir_files + '/inputs/input.vasprocar.dos'
   shutil.copyfile(source, destination)

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
print(" ")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
if (len(inputs) == 0):
   execute_python_file(filename = '_loop.py')
