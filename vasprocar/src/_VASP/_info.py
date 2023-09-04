# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

#######################################################
############## Analyzing the OUTCAR file ##############
########## Searching for System Information ###########
#######################################################

#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r")
#--------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "w")
#--------------------------------------------------------

inform.write(" \n")
inform.write("############################################################## \n")
inform.write(f'# {VASProcar_name} \n')
inform.write(f'# {url_1} \n')
inform.write(f'# {url_2} \n')
inform.write("############################################################## \n")
inform.write(" \n")

#----------------------------------------------------------------------
# Obtaining the number of k-points (nk), bands (nb) and ions (ni): ----
#----------------------------------------------------------------------

palavra = 'Dimension'                          # Dimension is a word present on a line before the lines containing information about the number of k-points (nk), bands (nb) and ions (ni).

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
nk = int(VTemp[3])
nb = int(VTemp[14])

VTemp = outcar.readline().split()
ni = int(VTemp[11])

#-----------------------------------------------------------------------
# Check if the calculation was performed with or without SO coupling: --
#-----------------------------------------------------------------------

palavra = 'ICHARG'                             # ICHARG is a word present on a line before the line that contains information about the ISPIN variable.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
ispin = int(VTemp[2])                          # Reading the value associated with the ISPIN variable.

#------------
nb = nb*ispin
#------------
  
#-----------------------------------------------------------------------

VTemp = outcar.readline().split()
lnoncollinear = VTemp[2]                       # Reading the value associated with the LNONCOLLINEAR variable.

VTemp = outcar.readline().split()
lsorbit = VTemp[2]                             # Reading the value associated with the LSORBIT variable.

inform.write("---------------------------------------------------- \n")

if (lnoncollinear == "F"):
   LNC = 1
   inform.write("LNONCOLLINEAR = .FALSE. (Collinear Calculation) \n")
if (lnoncollinear == "T"):
   LNC = 2
   inform.write("LNONCOLLINEAR = .TRUE. (Non-collinear Calculation) \n")

if (lsorbit == "F"):
   SO = 1
   inform.write("LSORBIT = .FALSE. (Calculation without SO coupling) \n")
if (lsorbit == "T"):
   SO = 2
   inform.write("LSORBIT = .TRUE. (Calculation with SO coupling) \n")

#-----------------------------------------------------------------------
# Finding the number of electrons in the system: -----------------------
#---------------------------------------------------------------------- 
 
palavra = 'VCA'                                       # VCA is a word present on a line before the line containing information about the NELECT variable.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
n_eletrons = float(VTemp[2])                          # Reading the value associated with the NELECT variable.

inform.write("---------------------------------------------------- \n")

if (n_procar == 1):
   inform.write(f'nº k-points = {nk};  nº bands = {nb} \n')
if (n_procar > 1):
   inform.write(f'nº k-points = {nk*n_procar} (nº PROCAR files = {n_procar});  nº bands = {nb} \n')   

inform.write(f'nº ions = {ni};  nº electrons = {n_eletrons} \n')

#-----------------------------------------------------------------
# Obtaining the LORBIT used to generate the PROCAR file: ---------
#-----------------------------------------------------------------
 
palavra = 'LELF'                                    # LELF is a word present on a line before the line containing information about the LORBIT variable.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lorbit = int(VTemp[2])                              # Reading the value associated with the LORBIT variable.

inform.write("--------------------------------------------------- \n")
inform.write(f'LORBIT = {lorbit};  ISPIN = {ispin} ')
if (ispin == 1): inform.write("(without spin polarization) \n")
if (ispin == 2): inform.write("(with spin polarization) \n")
inform.write("--------------------------------------------------- \n")

#-------------
outcar.close()
#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r") 
#----------------------------------------

#-----------------------------------------------------------------------
# Finding the Fermi Energy of the System: ------------------------------
#-----------------------------------------------------------------------

palavra = 'average'                            # average is a word present on a line a little before the line that contains information about the E-fermi variable.
number = 0                                     # number represents which line contains information about the E-fermi variable.

for line in outcar:
    number += 1    
    if palavra in line: 
       break

palavra = 'E-fermi'

for line in outcar:
    number += 1    
    if palavra in line: 
       break

#-------------
outcar.close()
#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r") 
#----------------------------------------

for i in range(number):
    VTemp = outcar.readline().split()

Efermi = float(VTemp[2])                       # Reading the value associated with the E-fermi variable.

#==========================================================================

if (ispin == 1):
    
   #-----------------------------------------------------------------------
   # Checking which bands correspond to the valence and conduction bands --
   # as well as the respective energy gap ---------------------------------
   # ----------------------------------------------------------------------
   # This check only makes sense for calculations performed in a single ---
   # step (n_procar = 1), since the analyzed OUTCAR file may or may not --- 
   # contain the lowest GAP region of the system --------------------------
   # ----------------------------------------------------------------------
   # This check also does not make sense for metallic system --------------
   #-----------------------------------------------------------------------

   VTemp = outcar.readline(); VTemp = outcar.readline().split()
   
   if ((len(VTemp) >= 3) and (VTemp[0] == 'Fermi')):
      Efermi = float(VTemp[2])
      VTemp = outcar.readline()

   menor_n2 = -1000.0
   maior_n2 = +1000.0
   number = 0

   for i in range(nk):
       number += 1
    
       VTemp = outcar.readline()
       VTemp = outcar.readline()
       for j in range(nb):
           VTemp = outcar.readline().split()
           n1 = int(VTemp[0])
           n2 = float(VTemp[1])
           n3 = float(VTemp[2])
           if (n3 > 0.0):
              if (n2 > menor_n2):
                 menor_n2 = n2
                 n1_valencia = n1
                 kp1 = number
           if (n3 == 0.0):
              if (n2 < maior_n2):
                 maior_n2 = n2
                 n1_conducao = n1
                 kp2 = number
           GAP = (maior_n2 - menor_n2)
       VTemp = outcar.readline() 

   if (n_procar == 1):
      inform.write(f'Last band occuped = {n1_valencia} \n')
      inform.write(f'First band empty = {n1_conducao} \n')

      if (kp1 == kp2):
         inform.write(f'GAP (direct) = {GAP:.4f} eV  -  k-point {kp1} \n')
      if (kp1 != kp2):
         inform.write(f'GAP (indirect) = {GAP:.4f} eV  //  k-points {kp1} e {kp2} \n')

      inform.write("---------------------------------------------------- \n")

#=======================================================================

inform.write(f'Fermi energy = {Efermi} eV \n')
inform.write("--------------------------------------------------- \n")

#-----------------------------------------------------------------------
# Finding the total energy of the system: ------------------------------
#-----------------------------------------------------------------------

palavra = 'FREE'                               # FREE is a word present on a line that is four lines before the line that contains information about the variable (free energy TOTEN).
number = 0                                     # number represents which line contains the information about the variable (free energy TOTEN).

for line in outcar:
    number += 1     
    if palavra in line: 
       break

for i in range(3):
    VTemp = outcar.readline()
    
VTemp = outcar.readline().split()
energ_tot = float(VTemp[3])                     

inform.write(f'free energy TOTEN = {energ_tot} eV \n')
inform.write("--------------------------------------------------- \n")

#==========================================================================

if (ispin == 1):

   #-----------------------------------------------------------------------
   #  ---------------------------------
   #-----------------------------------------------------------------------

   if (LNC == 2):
      temp_xk = 4 + ni

      #------------------------- Magnetization (X): ---------------------------

      palavra = 'magnetization'                   # magnetization is a word present on a line that is above the lines that contain information about the magnetization of the system.
      number = 0 

      for line in outcar:
          number += 1     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()   

      VTemp = outcar.readline().split()
      mag_s_x = float(VTemp[1])
      mag_p_x = float(VTemp[2])
      mag_d_x = float(VTemp[3])
      mag_tot_x = float(VTemp[4])

      #------------------------- Magnetization (y): ---------------------------

      palavra = 'magnetization'                   # magnetization is a word present on a line that is above the lines that contain information about the magnetization of the system.
      number = 0 

      for line in outcar:
          number += 1
     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()

      VTemp = outcar.readline().split()
      mag_s_y = float(VTemp[1])
      mag_p_y = float(VTemp[2])
      mag_d_y = float(VTemp[3])
      mag_tot_y = float(VTemp[4])

      #------------------------- Magnetization (z): ---------------------------

      palavra = 'magnetization'                   # magnetization is a word present on a line that is above the lines that contain information about the magnetization of the system.
      number = 0 

      for line in outcar:
          number += 1
     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()

      VTemp = outcar.readline().split()
      mag_s_z = float(VTemp[1])
      mag_p_z = float(VTemp[2])
      mag_d_z = float(VTemp[3])
      mag_tot_z = float(VTemp[4])
   
      #-----------------------------------------------------------------------

      inform.write(" \n")
      inform.write("################ Total Magnetization ################ \n")     
      inform.write(f'X axis:  total = {mag_tot_x:.4f} \n')
      inform.write(f'Y axis:  total = {mag_tot_y:.4f} \n')
      inform.write(f'Z axis:  total = {mag_tot_z:.4f} \n')
      inform.write("##################################################### \n")

#-------------
outcar.close()
#-------------

#######################################################################
######################## CONTCAR File Reading: ########################
#######################################################################
 
#------------------------------------------
contcar = open(dir_files + '/CONTCAR', "r")
#------------------------------------------

VTemp = contcar.readline().split()
VTemp = contcar.readline().split()

Parametro = float(VTemp[0])                                 # Reading the System Lattice Parameter.

A1 = contcar.readline().split()
A1x = float(A1[0]); A1y = float(A1[1]); A1z = float(A1[2])  # Reading the coordinates (X, Y and Z) of the primitive vector (A1) of the unit cell in real space.

A2 = contcar.readline().split()
A2x = float(A2[0]); A2y = float(A2[1]); A2z = float(A2[2])  # Reading the coordinates (X, Y and Z) of the primitive vector (A2) of the unit cell in real space.

A3 = contcar.readline().split()
A3x = float(A3[0]); A3y = float(A3[1]); A3z = float(A3[2])  # Reading the coordinates (X, Y and Z) of the primitive vector (A3) of the unit cell in real space.

#--------------
contcar.close()
#--------------

#-----------------------------------------------------------------------
# Obtaining the labels of the ions present in the CONTCAR file ---------
#-----------------------------------------------------------------------

#------------------------------------------
contcar = open(dir_files + '/CONTCAR', "r")
#------------------------------------------

for i in range(6):
    VTemp = contcar.readline().split() 
types = len(VTemp)                                                     # Obtaining the number of different types of ions that make up the lattice.

#----------------------------------------------

label = [0]*(types+1)
ion_label = [0]*(ni+1)
rotulo = [0]*(ni+1)
rotulo_temp = [0]*(ni+1)

#----------------------------------------------

for i in range (1,(types+1)):
    label[i] = VTemp[(i-1)]                                            # Obtaining the labels/abbreviations that label each type of ion in the lattice.

VTemp = contcar.readline().split()                                    

for i in range (1,(types+1)):            
    ion_label[i] = int(VTemp[(i-1)])                                   # Obtaining the number of ions corresponding to each label/abbreviation.

#----------------------------------------------

contador = 0

for i in range (1,(types+1)):
    number = ion_label[i]
    for j in range (1,(number+1)):
        contador += 1
        rotulo[contador] = label[i]

#--------------
contcar.close()
#--------------

#------------------------------------------------------------------------
#---- Estimation of the correct value of the Network Parameter as the ---
#------ smallest value between the modulus of vectors A1, A2 and A3 -----
#------------------------------------------------------------------------

if (param_estim == 2):

   A1x = A1x*Parametro; A1y = A1y*Parametro; A1z = A1z*Parametro
   A2x = A2x*Parametro; A2y = A2y*Parametro; A2z = A2z*Parametro
   A3x = A3x*Parametro; A3y = A3y*Parametro; A3z = A3z*Parametro

   Parametro_1 = ((A1x*A1x) + (A1y*A1y) + (A1z*A1z))**0.5
   Parametro = Parametro_1

   Parametro_2 = ((A2x*A2x) + (A2y*A2y) + (A2z*A2z))**0.5
   if (Parametro_2 < Parametro):
      Parametro = Parametro_2

   Parametro_3 = ((A3x*A3x) + (A3y*A3y) + (A3z*A3z))**0.5
   if (Parametro_3 < Parametro):
      Parametro = Parametro_3

   A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
   A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
   A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro

#-----------------------------------------------------------------------

inform.write(" \n")
inform.write("***************************************************** \n")
inform.write("Primitive Vectors of the Crystalline Lattice: ******* \n")
inform.write(f'Param. = {Parametro} Angs.       \n')
inform.write(f'A1 = Param.({A1x}, {A1y}, {A1z}) \n')
inform.write(f'A2 = Param.({A2x}, {A2y}, {A2z}) \n')
inform.write(f'A3 = Param.({A3x}, {A3y}, {A3z}) \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#-----------------------------------------------------------------------

ss1 = A1x*((A2y*A3z) - (A2z*A3y))
ss2 = A1y*((A2z*A3x) - (A2x*A3z))
ss3 = A1z*((A2x*A3y) - (A2y*A3x))
ss =  ss1 + ss2 + ss3                                        # I just divide this sum into three parts, since it is very long, and it exceeded the length of the line.

B1x = ((A2y*A3z) - (A2z*A3y))/ss                             # To understand these operations on the X, Y and Z components of the primitive vectors of the crystalline 
B1y = ((A2z*A3x) - (A2x*A3z))/ss                             # lattice (A1, A2 and A3), you must perform the standard operation of building the primitive vectors of 
B1z = ((A2x*A3y) - (A2y*A3x))/ss                             # the reciprocal lattice based on the primitive vectors of the lattice crystal clear. Such an operation 
B2x = ((A3y*A1z) - (A3z*A1y))/ss                             # is available in any solid-state book.
B2y = ((A3z*A1x) - (A3x*A1z))/ss
B2z = ((A3x*A1y) - (A3y*A1x))/ss
B3x = ((A1y*A2z) - (A1z*A2y))/ss
B3y = ((A1z*A2x) - (A1x*A2z))/ss
B3z = ((A1x*A2y) - (A1y*A2x))/ss

#-----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("Primitive Vectors of the Reciprocal Lattice: ******** \n")
inform.write(f'Param. = {Parametro} Angs.           \n')
inform.write(f'B1 = 2pi/Param.({B1x}, {B1y}, {B1z}) \n')
inform.write(f'B2 = 2pi/Param.({B2x}, {B2y}, {B2z}) \n')
inform.write(f'B3 = 2pi/Param.({B3x}, {B3y}, {B3z}) \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#-------------
inform.close()
#-------------
