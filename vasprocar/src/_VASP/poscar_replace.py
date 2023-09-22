# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import random

print("#######################################################")
print("###### POSCAR - Ion substitution in the lattice: ######")
print("#######################################################")
print(" ")

#======================================================================
# Check if POSCAR exists ==============================================
#======================================================================

try:
    f = open(dir_files + '/POSCAR')
    f.close()
except:
    print ("--------------------------------------------------------------")
    print ("Missing the file POSCAR in the current directory -------------")
    print ("Please, fix it! and press ENTER to continue ------------------")
    print ("--------------------------------------------------------------")
    confirmacao = input (" "); confirmacao = str(confirmacao)

#-------------------------------------------------------
poscar = open(dir_files + '/POSCAR', "r")
new_poscar = open(dir_files + '/output/POSCAR_new', "w")
#-------------------------------------------------------

#==============================================
# Copying the initial lines of the POSCAR file:
#==============================================

for i in range(5):
    VTemp = poscar.readline()
    VTemp = str(VTemp)
    new_poscar.write(f'{VTemp}')

#======================================================================
# Getting the total number of different types of ions from the lattice:
# Storing the labels of the different types of ions:
#======================================================================

VTemp = poscar.readline().split()
n_tipo = len(VTemp)

rotulo = []

for i in range(n_tipo):
    rotulo.append(str(VTemp[i]))

#================================================================
# Getting the total number of ions in the lattice:
# Storing the number of ions for each type of ion in the lattice:
#================================================================

ni = 0
n_ion = [0]*n_tipo

VTemp = poscar.readline().split()

for i in range(n_tipo):
    ni += int(VTemp[i])
    n_ion[i] = int(VTemp[i])

label = [0]*ni
contador = -1

for i in range(n_tipo):
    name = rotulo[i]
    for j in range(n_ion[i]):
        contador += 1
        label[contador] = name

#=========================================================
# Storing the type of coordinates used in the POSCAR file:
#=========================================================

VTemp = poscar.readline()
t_coord = str(VTemp)

#====================================================
# Storing the coordinates of all ions in the lattice:
#====================================================

ni_coord = [[0]*(4) for i in range(ni)]  # ni_coord[ni][4]

for i in range(ni):
    VTemp = poscar.readline().split()
    for j in range(4):
        if (j <= 2):
           ni_coord[i][j] = float(VTemp[j])
        if (j == 3):
           ni_coord[i][j] = label[i]

#===================================
# Obtaining the ions to be replaced: 
#===================================


print ("##############################################################")
print ("To perform the replacement, type as in the examples below: ===")
print ("--------------------------------------------------------------")
print ("ion to be replaced, new ion, number of replacements ==========")
print ("--------------------------------------------------------------")
print ("Note [1]: The ions are randomly replaced =====================")
print ("Note [2]: To exclude an ion from the lattice, use the word    ")
print ("          (null) to designate the new ion                     ")
print ("Examples: ====================================================")
print ("ion_OLD, ion_New, Replacements: C  Si 7  ")
print ("ion_OLD, ion_New, Replacements: H  N  24 ")
print ("ion_OLD, ion_New, Replacements: Se W  64 ")
print ("ion_OLD, ion_New, Replacements: O null 9 ")
print ("##############################################################")

print ("##############################################################")
print ("# current ions of the lattice: ===============================")
for j in range(n_tipo):
    print (f'# {rotulo[j]} ({n_ion[j]} ions) ===============================================')
print ("##############################################################")
print(" ")
print ("##############################################################")
print ("### Perform the replacement: =================================")
print ("##############################################################")
selected_replace = input ("ion_OLD, ion_New, Replacements:  ").replace(':',' ').replace('-',' ').replace(',',' ').replace('*',' ').replace('Null','null').replace('NULL','null').split()

ion_OLD = str(selected_replace[0])
ion_NEW = str(selected_replace[1])
Subst   = int(selected_replace[2])

#==========================================
# Getting the range of ions to be replaced: 
#==========================================

cont1 = 0

for i in range(ni):
    if (ion_OLD == ni_coord[i][3]):
       cont1 += 1
       if (cont1 == 1):
          int_i = i
          int_f = i
       if (cont1 > 1):
          int_f += 1

#===============================================
# Adding a new label to different types of ions: 
#===============================================

cont2 = 0

for i in range(n_tipo):
    if (ion_NEW == rotulo[i]):
       cont2 += 1

if (cont2 == 0 and Subst > 0):
   rotulo.append(ion_NEW)

#============================================================
# Obtaining the random sequence to perform the substitutions: 
#============================================================

sequencia_full = list(range(int_i,(int_f+1)))  # Creates a vector with numbers randomly distributed between [int_i] and [int_f]
random.shuffle(sequencia_full)

if (Subst > 0):
   sequencia = [0]*Subst
   for i in range(Subst):
       sequencia[i] = sequencia_full[i] 

sequencia = sorted(sequencia)  # Rearranges the sequence of substitutions in ascending order

#==========================
# Making the substitutions:
#==========================

cont2 = 0

for i in range(ni): 
    if (i == sequencia[cont2]):
       if (cont2 < (Subst -1)): cont2 += 1
       ni_coord[i][3] = ion_NEW

#=============================
# Writing the new POSCAR file: 
#=============================

new_n_tipo = []

for i in range(len(rotulo)):
    cont3 = 0
    for j in range(ni):
        if (ni_coord[j][3] == rotulo[i]): cont3 += 1
        if (j == (ni-1)): new_n_tipo.append(cont3)

#----------------------------------

for i in range(len(rotulo)):
    if (new_n_tipo[i] > 0 and rotulo[i] != 'null'):
       new_poscar.write(f'{rotulo[i]} ') 
new_poscar.write(f' \n')

#----------------------------------

for i in range(len(rotulo)):
    if (new_n_tipo[i] > 0 and rotulo[i] != 'null'):
       new_poscar.write(f'{new_n_tipo[i]} ')
new_poscar.write(f' \n') 

#---------------------------------- 

new_poscar.write(f'{t_coord}')

#---------------------------------- 
           
for i in range(len(rotulo)):
    name = rotulo[i]
    if (new_n_tipo[i] > 0 and rotulo[i] != 'null'):
       for j in range(ni):
           if (ni_coord[j][3] == name and rotulo[i] != 'null'):
              new_poscar.write(f'{ni_coord[j][0]} {ni_coord[j][1]} {ni_coord[j][2]} \n')

#---------------------------------- 

poscar.close()
new_poscar.close()

#---------------------------------------------------------------
print(" ")
print("======================= Completed =====================")
#---------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
