# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

#######################################################
############## Analyzing the OUTCAR file ##############
########### Searching for system information ##########
#######################################################

# ---------------------------------------------------------------------
# Checking the presence of CONTCAR, OUTCAR and PROCAR files: ----------
# ---------------------------------------------------------------------

n_contcar = 0

try:
    f = open(dir_files + '/CONTCAR')
    f.close()
    n_contcar = 1
except:
    print('')
    print('... Missing CONTCAR file ...')

#-----------------------------------

n_outcar = 0

try:
    f = open(dir_files + '/OUTCAR')
    f.close()
    n_outcar = 1
except:
    print('')
    print('... Missing OUTCAR file ...')

#-----------------------------------

n_procar = 0

try:
    f = open(dir_files + '/PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

try:
    f = open(dir_files + '/PROCAR.1')
    f.close()
    n_procar = 1
except:
    0 == 0    

if (n_procar == 0):
   print('')
   print('... Missing PROCAR file ...')

#-----------------------------------

if (n_contcar == 0 or n_outcar == 0 or n_procar == 0):   
   print('')
   print('')
   print('---------------------------------------------------------------------------')
   print('After inserting the missing files in the directory, press ENTER to continue')
   print('---------------------------------------------------------------------------')
   confirmacao = input (" "); confirmacao = str(confirmacao)
   
# ----------------------------------------------------------------------
# Checking the presence and number of PROCAR files to be read: ---------
# ----------------------------------------------------------------------

n_procar = 0

try:
    f = open(dir_files + '/PROCAR')
    f.close()
    n_procar = 1
except:
    0 == 0

for i in range(1, 100):
    try:
        f = open(dir_files + '/PROCAR.'+str(i))
        f.close()
        n_procar = i
    except:
        0 == 0

# ----------------------------------------------------------------------
# Checking the amount of orbitals in the PROCAR file: ------------------
# ----------------------------------------------------------------------

if (n_procar == 1):
   procar = open(dir_files + '/PROCAR', "r")
if (n_procar > 1):
   procar = open(dir_files + '/PROCAR.1', "r")

if (n_procar != 0):
   #-----------
   test = 'nao'
   #-----------
   while (test == 'nao'):             
         #------------------------
         VTemp = procar.readline()
         Teste = VTemp.split() 
         #---------------------------------------------
         if (len(Teste) > 0 and Teste[0] == 'ion'):
            test = 'sim'

   VTemp = procar.readline().split()

   #--------------------
   n_orb = len(VTemp) -2
   #--------------------

   procar.close()

#-----------------------------------------------------------------------------------
# Control parameters for reading orbitals and spin components in the PROCAR file ---
#-----------------------------------------------------------------------------------
read_orb  = 0
read_spin = 0
read_reg  = 0
read_psi  = 0

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
   inform.write("LNONCOLLINEAR = .TRUE. (Non-collinear calculation) \n")

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
   inform.write(f'nº k-points = {nk};  nº Bands = {nb} \n')
if (n_procar > 1):
   inform.write(f'nº k-points = {nk*n_procar} (nº PROCAR files = {n_procar});  nº Bands = {nb} \n')   

inform.write(f'nº ions = {ni};  nº electrons = {n_eletrons} \n')

#-----------------------------------------------------------------------
# Obtaining the LORBIT used to generate the PROCAR file: ---------------
#-----------------------------------------------------------------------
 
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

B1x = ((A2y*A3z) - (A2z*A3y))/ss                             # To understand these operations on the X, Y and Z components of the primitive vectors of the lattice, 
B1y = ((A2z*A3x) - (A2x*A3z))/ss                             # you must perform the standard operation of building the primitive vectors of the reciprocal lattice 
B1z = ((A2x*A3y) - (A2y*A3x))/ss                             # based on the primitive vectors of the crystalline lattice. Such an operation is available in any solid-state book.
B2x = ((A3y*A1z) - (A3z*A1y))/ss                             
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
