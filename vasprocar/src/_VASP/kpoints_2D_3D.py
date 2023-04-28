# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print("#######################################################")
print("#### KPOINTS File Generator (2D Plane or 3D Mesh): ####")
print("#######################################################")
print(" ")

#=========================================================================
# Checking the presence or not of the CONTCAR, OUTCAR and PROCAR files: --
#=========================================================================

n_contcar = 0
n_outcar  = 0
n_procar  = 0

try:
    f = open(dir_files + '/CONTCAR')
    f.close()
    n_contcar = 1
except: 0 == 0

try:
    f = open(dir_files + '/OUTCAR')
    f.close()
    n_outcar = 1
except: 0 == 0

try:
    f = open(dir_files + '/PROCAR')
    f.close()
    n_procar = 1
except: 0 == 0

try:
    f = open(dir_files + '/PROCAR.1')
    f.close()
    n_procar = 1
except: 0 == 0    

if (n_contcar != 0 and n_outcar != 0 and n_procar != 0): 
   execute_python_file(filename = DFT + '_info_b.py')

   print("##############################################################")
   print("# Obtaining information from the calculation performed: ==== #")
   print("##############################################################")

   print(" ")
   print(".........................")
   print("..... Wait a moment .....")
   print(".........................")
   print(" ")

#=========================================================================
# Getting input parameters: ----------------------------------------------
#=========================================================================

print("#######################################################")
print("## What kind of KPOINTS do you want to generate?     ##")
print("#######################################################")
print("## [1] 2D plan in the Brillouin Zone                 ##")
print("## [2] 3D Mesh in the Brillouin Zone                 ##")
print("#######################################################")
tipo = input (" "); tipo = int(tipo)
print(" ")

print("#######################################################")
print("Want to split k-points into multiple KPOINTS files?    ")
print("#######################################################")
print("## [0] NOT                                           ##")
print("## [1] YES                                           ##")
print("#######################################################")
split = input (" "); split = int(split)
if (split != 0 and split != 1):
   split = 0
print(" ")

if (split == 1):
   estrutura = 0
   print("#######################################################")
   print("How many k-points do you want per KPOINTS file? =======")
   print("#######################################################")
   nk_split = input (" "); nk_split = int(nk_split)
   print(" ")

if (split == 0):
   print("#######################################################")
   print("# As for the structure of the KPOINTS file, do you want")
   print("#######################################################")
   print("## [0] Each k-point is written explicitly            ##")
   print("## [1] Each k-point be written in line mode          ##")
   print("#######################################################")
   estrutura = input (" "); estrutura = int(estrutura)
   print(" ")

print("#######################################################")
print("## Do you want to choose a central k-point ? ======= ##")
print("#######################################################")
print("## [0] YES                                           ##")
print("## [1] NOT                                           ##")
print("#######################################################")
point = input (" "); point = int(point)
print(" ")

if (n_contcar != 0 and n_outcar != 0 and n_procar != 0): 
   print("=======================================================")
   print("Primitive Vectors of the Reciprocal Network:           ")
   print("-------------------------------------------------------")
   print(f'Param. = {Parametro} Angs.                            ')
   print(f'B1 = 2pi/Param.({B1x}, {B1y}, {B1z})                  ')
   print(f'B2 = 2pi/Param.({B2x}, {B2y}, {B2z})                  ')
   print(f'B3 = 2pi/Param.({B3x}, {B3y}, {B3z})                  ')
   print("=======================================================")
   print(" ")

print("#######################################################")
print("## Which coordinate system do you want to adopt? === ##")
print("#######################################################")
print("## [1] Direct Coordinates (k1, k2, k3):              ##")
print("##     K =  k1*B1 + k2*B2 + k3*B3                    ##")
print("## [2] Cartesian Coordinates (kx, ky, kz)            ##")
print("##     K =  2pi/Param.(kx, ky, kz)                   ##")
print("#######################################################")
coord = input (" "); coord = int(coord)
print(" ")

if (coord == 1):
   ch1 = 'k1'; ch2 = 'k2'; ch3 = 'k3'
if (coord == 2):
   ch1 = 'kx'; ch2 = 'ky'; ch3 = 'kz' 

if (tipo == 1):
   print("#######################################################")
   print("## Define which plan you want to scan in ZB: ======= ##")
   print(f'## [1] {ch1}{ch2} Plane ({ch3} fixed) ======================= ##')
   print(f'## [2] {ch1}{ch3} Plane ({ch2} fixed) ======================= ##')
   print(f'## [3] {ch2}{ch3} Plane ({ch1} fixed) ======================= ##')
   print("#######################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

print("#######################################################")
print("########## Define the coordinates to be used ##########")
if (point == 1):
   print("## ================================================= ##")
   print("## Example -- 2D plane:                              ##")
   print(f'## {ch1}_initial {ch1}_final Grid_points: -0.25 0.25 25    ##')
   print(f'## {ch2}_initial {ch2}_final Grid_points:  0.35 0.50 31    ##')
   print(f'## Fixed_Coordinate_{ch3}:                 0.50         ##')
   print("## ================================================= ##")
   print("## Example Mesh -- 3D:                               ##")
   print(f'## {ch1}_initial {ch1}_final Grid_points: -0.10 0.10 25    ##')
   print(f'## {ch2}_initial {ch2}_final Grid_points: -0.15 0.15 15    ##')
   print(f'## {ch3}_initial {ch3}_final Grid_points:  0.00 0.50 31    ##')
   print("## ================================================= ##")
if (point == 0):
   print("## ================================================= ##")
   print("## Example -- 2D plane:                              ##")
   print(f'## Central_Point ({ch1} {ch2} {ch3}):           0.5  0.0  0.0 ##')
   print(f'## (axis-{ch1}) Length GRID_points:  0.25 25            ##')
   print(f'## (axis-{ch2}) Length GRID_points:  0.10 15            ##')
   print("## ================================================= ##")
   print("## Example Mesh -- 3D:                               ##")
   print(f'## Central_Point ({ch1} {ch2} {ch3}):           0.0  0.0  0.0 ##')
   print(f'## (axis-{ch1}) Length GRID_points:  0.50 31            ##')
   print(f'## (axis-{ch2}) Length GRID_points:  0.25 25            ##')
   print(f'## (axis-{ch3}) Length GRID_points:  0.11 15            ##')
   print("## ================================================= ##")
print("#######################################################")
print(" ")

#=========================================================================
# Defining 2D Plane or 3D Mesh boundaries manually: ----------------------
#=========================================================================

if (point == 1):
   
   if ((tipo == 1 and esc != 3) or (tipo == 2)):
      print(f'eixo-{ch1} --------------------------------------------')
      c1_i, c1_f, grid_1 = input (f'{ch1}_initial {ch1}_final Grid_points: ').split()
      c1_i = float(c1_i); c1_f = float(c1_f); grid_1 = int(grid_1)
   #---------------------------  
   if (tipo == 1 and esc == 3):
      print(f'eixo-{ch1} --------------------------------------------')
      c1_i = input (f'Fixed_Coordinate_{ch1}: '); c1_i = float(c1_i)
      c1_f = c1_i; grid_1 = 1
   #---------------------------    
   print(" ")

   if ((tipo == 1 and esc != 2) or (tipo == 2)):
      print(f'eixo-{ch2} --------------------------------------------')
      c2_i, c2_f, grid_2 = input (f'{ch2}_initial {ch2}_final Grid_points: ').split()
      c2_i = float(c2_i); c2_f = float(c2_f); grid_2 = int(grid_2)
   #---------------------------    
   if (tipo == 1 and esc == 2):
      print(f'eixo-{ch2} --------------------------------------------')
      c2_i = input (f'Fixed_Coordinate_{ch2}: '); c2_i = float(c2_i)
      c2_f = c2_i; grid_2 = 1
   #---------------------------    
   print(" ")

   if ((tipo == 1 and esc != 1) or (tipo == 2)):
      print(f'eixo-{ch3} --------------------------------------------')
      c3_i, c3_f, grid_3 = input (f'{ch3}_initial {ch3}_final Grid_points: ').split()
      c3_i = float(c3_i); c3_f = float(c3_f); grid_3 = int(grid_3)
   #---------------------------    
   if (tipo == 1 and esc == 1):
      print(f'eixo-{ch3} --------------------------------------------')
      c3_i = input (f'Fixed_Coordinate_{ch3}: '); c3_i = float(c3_i)
      c3_f = c3_i; grid_3 = 1
   #---------------------------    
   print(" ")

#=====================================================================================================
# Obtaining the limits of the 2D Plane or the 3D Mesh according to the choice of the center point: ---
#=====================================================================================================

if (point == 0):
   
   print("----------------------------------------------------")
   print(f'Enter the coordinates ({ch1}, {ch2}, {ch3}) of the Central_Point: ')
   pc_1, pc_2, pc_3 = input (f'Central_Point ({ch1} {ch2} {ch3}): ').split()
   pc_1 = float(pc_1); pc_2 = float(pc_2); pc_3 = float(pc_3)
   print(" ")

   print("----------------------------------------------------")
   print("For each axis, enter the length to be scanned on    ")
   print("that axis, as well as the k-point Grid to be used.  ")
   print("----------------------------------------------------")   
   print("Use an ODD number for the k-point Grid -------------")
   print("----------------------------------------------------")
   print(" ")
   
   if ((tipo == 1 and (esc == 1 or esc == 2)) or tipo == 2):
      print(f'eixo-{ch1} ----------------------------------------')
      comp_1, grid_1 = input (f'Length Grid_points: ').split()
      comp_1 = float(comp_1); grid_1 = int(grid_1)
      print(" ")

   if ((tipo == 1 and (esc == 1 or esc == 3)) or tipo == 2):
      print(f'eixo-{ch2} ----------------------------------------')
      comp_2, grid_2 = input (f'Length Grid_pionts: ').split()
      comp_2 = float(comp_2); grid_2 = int(grid_2)
      print(" ")

   if ((tipo == 1 and (esc == 2 or esc == 3)) or tipo == 2):
      print(f'eixo-{ch3} ----------------------------------------')
      comp_3, grid_3 = input (f'Length Grid_points: ').split()
      comp_3 = float(comp_3); grid_3 = int(grid_3)
      print(" ")

   if (tipo == 1 and esc == 1):
      grid_3 = 1; comp_3 = 0.0
   if (tipo == 1 and esc == 2):
      grid_2 = 1; comp_2 = 0.0
   if (tipo == 1 and esc == 3):
      grid_1 = 1; comp_1 = 0.0

   #----------------------------------------------------

   resto1 = (grid_1 % 2)
   resto2 = (grid_2 % 2)
   resto3 = (grid_3 % 2)
   
   if (resto1 == 0): grid_1 = grid_1 + 1
   if (resto2 == 0): grid_2 = grid_2 + 1
   if (resto3 == 0): grid_3 = grid_3 + 1 

   #----------------------------------------------------

   c1_i = pc_1 - (comp_1/2); c1_f = pc_1 + (comp_1/2)
   c2_i = pc_2 - (comp_2/2); c2_f = pc_2 + (comp_2/2)
   c3_i = pc_3 - (comp_3/2); c3_f = pc_3 + (comp_3/2)

#=========================================================================
# Initialization of vectors k1, k2 and k3 --------------------------------
#=========================================================================

c1 = [0]*(grid_1 + 1)
c2 = [0]*(grid_2 + 1)
c3 = [0]*(grid_3 + 1)

#=========================================================================
# Obtaining the Loop order and writing the k-points in the KPOINTS file ==
#=========================================================================

# 2D plan in ZB ==========================================================

if (tipo == 1 and estrutura == 1):

   if (esc == 1):
      grid_e1 = grid_1
      grid_e2 = grid_2

   if (esc == 2):
      grid_e1 = grid_1
      grid_e2 = grid_3
   
   if (esc == 3):
      grid_e1 = grid_2
      grid_e2 = grid_3

# 3D mesh in ZB ==========================================================

if (tipo == 2 and estrutura == 1):

   c_e = 1
   grid_e1 = grid_1
   grid_e2 = grid_2
   grid_e3 = grid_3

   if (grid_2 > grid_e1):
      c_e = 2
      grid_e1 = grid_2
      grid_e2 = grid_1
      grid_e3 = grid_3
   
   if (grid_3 > grid_e1):
      c_e = 3
      grid_e1 = grid_3
      grid_e2 = grid_1
      grid_e3 = grid_2

#=========================================================================
# KPOINTS file writing ---------------------------------------------------
#=========================================================================

#-------------------------------------------------
kpoints = open(dir_files + '/output/KPOINTS', 'w')
#-------------------------------------------------

if (tipo == 1):
   kpoints.write(f'2D Plan - VASProcar ({grid_1*grid_2*grid_3} k-points) \n')
if (tipo == 2):
   kpoints.write(f'3D Mesh - VASProcar ({grid_1*grid_2*grid_3} k-points) \n')

if (estrutura == 1):
   kpoints.write(f'{grid_e1} \n')
if (estrutura == 0):   
   kpoints.write(f'1 \n')

kpoints.write("Line-mode \n")

if (coord == 1):
   kpoints.write("Reciprocal \n")
if (coord == 2):
   kpoints.write("Cartesian \n")

# 2D plane in ZB (line mode) =============================================

if (tipo == 1 and estrutura == 1):

   for i in range (1,(grid_e2+1)):

       if (tipo == 1 and esc == 1):
          #----------------------------------------------
          c2[i] = c2_i + (i-1)*(c2_f - c2_i)/(grid_2 - 1)
          c3_fixo = c3_i
          #----------------------------------------------
          kpoints.write(f'{c1_i:17.12f} {c2[i]:17.12f} {c3_fixo:17.12f} \n')
          kpoints.write(f'{c1_f:17.12f} {c2[i]:17.12f} {c3_fixo:17.12f} \n')

       if (tipo == 1 and esc == 2):
          #----------------------------------------------
          c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
          c2_fixo = c2_i
          #----------------------------------------------            
          kpoints.write(f'{c1_i:17.12f} {c2_fixo:17.12f} {c3[i]:17.12f} \n')
          kpoints.write(f'{c1_f:17.12f} {c2_fixo:17.12f} {c3[i]:17.12f} \n')

       if (tipo == 1 and esc == 3):
          #----------------------------------------------
          c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
          c1_fixo = c1_i
          #----------------------------------------------            
          kpoints.write(f'{c1_fixo:17.12f} {c2_i:17.12f} {c3[i]:17.12f} \n')
          kpoints.write(f'{c1_fixo:17.12f} {c2_f:17.12f} {c3[i]:17.12f} \n')

       kpoints.write(" \n")

# 3D mesh in ZB (line mode) ==============================================

if (tipo == 2 and estrutura == 1):

   for i in range (1,(grid_e2+1)):
       for j in range (1,(grid_e3+1)):

           if (c_e == 1):
              #----------------------------------------------
              c2[i] = c2_i + (i-1)*(c2_f - c2_i)/(grid_2 - 1)
              c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
              #----------------------------------------------
              kpoints.write(f'{c1_i:17.12f} {c2[i]:17.12f} {c3[j]:17.12f} \n')
              kpoints.write(f'{c1_f:17.12f} {c2[i]:17.12f} {c3[j]:17.12f} \n')

           if (c_e == 2):
              #----------------------------------------------
              c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
              c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
              #----------------------------------------------            
              kpoints.write(f'{c1[i]:17.12f} {c2_i:17.12f} {c3[j]:17.12f} \n')
              kpoints.write(f'{c1[i]:17.12f} {c2_f:17.12f} {c3[j]:17.12f} \n')

           if (c_e == 3):
              #----------------------------------------------
              c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
              c2[j] = c2_i + (j-1)*(c2_f - c2_i)/(grid_2 - 1)
              #----------------------------------------------            
              kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3_i:17.12f} \n')
              kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3_f:17.12f} \n')

           kpoints.write(" \n")

# Writing each k-point explicitly to the KPOINTS file ====================

for i in range (1,(grid_1+1)):
    if (grid_1 > 1):
       c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
    if (grid_1 == 1):
       c1[i] = c1_i
       
    for j in range (1,(grid_2+1)):
        if (grid_2 > 1):
           c2[j] = c2_i + (j-1)*(c2_f - c2_i)/(grid_2 - 1)
        if (grid_2 == 1):
           c2[j] = c2_i    
     
        for k in range (1,(grid_3+1)):
            if (grid_3 > 1):
               c3[k] = c3_i + (k-1)*(c3_f - c3_i)/(grid_3 - 1)
            if (grid_3 == 1):
               c3[k] = c3_i   
            
            if (estrutura == 0):
               kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3[k]:17.12f} \n')

#============================================================================================           

#--------------
kpoints.close()
#--------------

#============================================================================================     
# Splitting the KPOINTS file ================================================================
#============================================================================================

if (split == 1):

   if (nk_split > (grid_1*grid_2*grid_3)):
      nk_split = (grid_1*grid_2*grid_3)
   
   passo = (grid_1*grid_2*grid_3)/nk_split
   resto = passo - int(passo)
   if (resto == 0): passo = int(passo)
   if (resto != 0): passo = int(passo) + 1

   number = 0

   #---------------------------------------------------
   r_kpoints = open(dir_files + '/output/KPOINTS', 'r')
   #---------------------------------------------------

   for i in range(4):
       VTemp = r_kpoints.readline()

   for i in range(1,(passo+1)):
       #-----------------------------------------------------------
       kpoints = open(dir_files + '/output/KPOINTS.' + str(i), 'w')      
       #-----------------------------------------------------------       

       number_k = 0

       if (tipo == 1):
          kpoints.write(f'2D Plan - VASProcar \n')
       if (tipo == 2):
          kpoints.write(f'3D mesh - VASProcar \n')
   
       kpoints.write(f'1 \n')
       kpoints.write("Line-mode \n")

       if (coord == 1):
          kpoints.write("Reciprocal \n")
       if (coord == 2):
          kpoints.write("Cartesian \n")

       #=====================================================================================

       for j in range(1,(nk_split+1)):
           #------------
           number += 1
           number_k += 1
           #------------

           if (number <= (grid_1*grid_2*grid_3)):
              VTemp = r_kpoints.readline().split()
              #-------------------------------------------------------------------------
              if (i != 1 and j == 1):
                 kpoints.write(f'{temp_k1:17.12f} {temp_k2:17.12f} {temp_k3:17.12f} \n')
              #-------------------------------------------------------------------------
              coord1 = float(VTemp[0])
              coord2 = float(VTemp[1])
              coord3 = float(VTemp[2])
              kpoints.write(f'{coord1:17.12f} {coord2:17.12f} {coord3:17.12f} \n')
              #-------------------------------------------------------------------------
              if (i != passo and j == nk_split):
                 temp_k1 = coord1; temp_k2 = coord2; temp_k3 = coord3
              #-------------------------------------------------------------------------
              if (i == passo and number == (grid_1*grid_2*grid_3)):
                 temp_k1 = coord1; temp_k2 = coord2; temp_k3 = coord3
              #-------------------------------------------------------------------------
              if (i == 1 and j == nk_split):
                 kpoints.write(f'{temp_k1:17.12f} {temp_k2:17.12f} {temp_k3:17.12f} \n')
              #-------------------------------------------------------------------------
           
           if (i == passo and number > (grid_1*grid_2*grid_3)):
              kpoints.write(f'{temp_k1:17.12f} {temp_k2:17.12f} {temp_k3:17.12f} \n')

       #--------------
       kpoints.close()
       #--------------

#----------------
r_kpoints.close()
#----------------

#=================================================================================================
# Obtaining the Cartesian coordinates (kx,ky,kz) of the k-points generated in the KPOINTS file ---
#=================================================================================================

if (n_contcar != 0 and n_outcar != 0 and n_procar != 0): 

   if (coord == 1):
      #-------------------------------------------------------------------------
      pontos_k = open(dir_files + '/output/k-points_Coord_Cartesianas.txt', 'w')
      #-------------------------------------------------------------------------

      pontos_k.write(" \n")
      pontos_k.write("============================================================================================== \n")
      pontos_k.write("K-points from the KPOINTS file in Cartesian Coordinates (kx,ky,kz) as a function of 2pi/Param. \n")
      pontos_k.write("============================================================================================== \n")
      pontos_k.write(" \n")

      for i in range (1,(grid_1+1)):
          for j in range (1,(grid_2+1)):
              for k in range (1,(grid_3+1)):
                  Coord_X = ((c1[i]*B1x) + (c2[j]*B2x) + (c3[k]*B3x))
                  Coord_Y = ((c1[i]*B1y) + (c2[j]*B2y) + (c3[k]*B3y))
                  Coord_Z = ((c1[i]*B1z) + (c2[j]*B2z) + (c3[k]*B3z))
                  pontos_k.write(f'{Coord_X:17.12f} {Coord_Y:17.12f} {Coord_Z:17.12f} \n')  

      #---------------
      pontos_k.close()
      #---------------

#============================================================================================
# Informing the amount of k-points that the KPOINTS file provides ---------------------------
#============================================================================================

print("#########################################################")
print(f'# The generated KPOINTS file provides {grid_1*grid_2*grid_3} k-points in ZB')
print("#########################################################")   

if (coord == 1):
   print("## A file with the Cartesian coordinates of the points ##")
   print("## from the KPOINTS file is in the output folder.      ##")
   print("#########################################################")

#---------------------------------------------------------------
print(" ")
print("======================= Completed =====================")
#---------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
