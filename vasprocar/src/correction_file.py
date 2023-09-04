# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print ("##################################################################")
print ("## Type the file name to be fixed: ============================ ##")
print ("## E.g: PROCAR, DOSCAR, PARCHG, OUTCAR ======================== ##")
print ("##################################################################") 
print ("This is an example of how the corrected file should look like ... ")
print ("0.50000000-0.50000000   >>   0.50000000 -0.50000000               ")
print ("0.12345000-123   >>   0.12345000e-123                             ")
print ("0.86000000-209   >>   0.86000000e-209                             ")
print ("##################################################################") 

name = input ("name: "); name = str(name)
print (" ")

print ("..................")
print ("..... Fixing .....")
print ("..................")
print (" ")

#---------------------------------------------------------------------------

original = dir_files + '/' + name
copia    = dir_files + '/' + name + '_Original'
shutil.copyfile(original, copia)

#---------------------------------------------------------------------------

with open(dir_files + '/' + name, 'rt') as file:
     r = file.read()

for i in range (10):     
    with open(dir_files + '/' + name, 'wt') as file:
         r = r.replace('-' + str(i) + '.', ' -' + str(i) + '.')
         file.write(r)

for i in range (10):     
    with open(dir_files + '/' + name, 'wt') as file:
         r = r.replace(str(i) + '-', str(i) + 'E-')
         file.write(r)

file.close()

#-----------------------------------------------------------------
print("======================= Finished ! ======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
