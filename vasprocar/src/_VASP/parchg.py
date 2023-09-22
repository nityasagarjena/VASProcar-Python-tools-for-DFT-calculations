# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())
   
#-----------------------------------------------------------------------
# Check whether the 'Densidade_Carga_Parcial' folder exists ------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Densidade_Carga_Parcial'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Densidade_Carga_Parcial')
#---------------------------------------------------------

print ("##############################################################")
print ("################ Partial Charge Density Plot: ################")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Hint: To generate a 3D Plot of the Projected Charge      ##")
print ("##       Density over the crystal lattice, rename the file  ##")
print ("##       to PARCHG and open it in the VESTA program         ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Enter the full name of the PARCHG file you want to analyze:   ")
print ("##############################################################") 
name = input (" "); name = str(name)
print (" ")

#======================================================================
# Check if file exists ================================================
#======================================================================

try:
    f = open(dir_files + '/' + name)
    f.close()
except:
    print ("--------------------------------------------------------------")
    print (f'Missing the file {name} in the current directory ')
    print ("Please, fix it! and press ENTER to continue ")
    print ("--------------------------------------------------------------")
    confirmacao = input (" "); confirmacao = str(confirmacao)

#======================================================================
# Get the input from user =============================================
#======================================================================

if (escolha == -1): 
   print ("##############################################################")
   print ("Choose the Plot's x-axis (abscissa) dimension: ===============")
   print ("[1] to Angs. (Default) =======================================")
   print ("[2] to nm. ===================================================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

   print ("##############################################################")
   print ("Do you want to highlight the coordinate of the ions? =========")
   print ("[0] NOT ======================================================")
   print ("[1] YES (Default) ============================================")
   print ("##############################################################") 
   destaque = input (" "); destaque = int(destaque)
   print (" ")   

if (escolha == 1):
   Dimensao = 1
   destaque = 1

#----------------------------------------------------------------------
# Obtaining the results from type PARCHG ------------------------------
#----------------------------------------------------------------------

print (".........................................................")
print (f'................. Readind {name} ')
print ("................ please, wait a moment ")
print (".........................................................")
print (" ")

#-----------------------------------------
parchg = open(dir_files + '/' + name, 'r')
#-----------------------------------------

for i in range (8):
    VTemp = parchg.readline()

Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

for i in range (ni):
    VTemp = parchg.readline().split()
    #---------------------------------------------------------------
    m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
    #--------------------------------------------------------------
    ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
    ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
    ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
VTemp = parchg.readline()
VTemp = parchg.readline().split()

Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)

passo1 = (GRID/10)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 10 - ((passo1*10) -GRID)

for i in range (passo1):

    VTemp = parchg.readline()
    #-----------------------------------------------------
    for k in range(10):
        VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
        VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
    VTemp = VTemp.split()    
    #----------------------------------------------------- 

    if (i < (passo1-1)):
       for j in range(10): V_local[((i)*10) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*10) + j] = float(VTemp[j])

#-------------
parchg.close()
#-------------
  
#--------------------------------------------------------------------------

fator_x = max(Ax) - min(Ax)
fator_y = max(Ay) - min(Ay)
fator_z = max(Az) - min(Az)

escala_x = 1.0/float(GRID/Grid_x); Vx = [0]*(Grid_x); X = [0]*(Grid_x)
escala_y = 1.0/float(GRID/Grid_y); Vy = [0]*(Grid_y); Y = [0]*(Grid_y)
escala_z = 1.0/float(GRID/Grid_z); Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

#--------------------------------------------------------------------------------------------
# Analyzing the data: Obtaining the average Partial Charge Density value in a given direction
#--------------------------------------------------------------------------------------------

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#======================================================================
# Saving data to plot the Partial Charge Density ======================
#======================================================================             

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_X.dat', "w")
#-----------------------------------------------------------------------------------
for i in range (Grid_x):
    X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
    densidade.write(f'{X[i]} {Vx[i]} \n')
densidade.close()

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_Y.dat', "w")
#-----------------------------------------------------------------------------------
for i in range (Grid_y):
    Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
    densidade.write(f'{Y[i]} {Vy[i]} \n')
densidade.close()

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_Z.dat', "w")
#-----------------------------------------------------------------------------------
for i in range (Grid_z):
    Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
    densidade.write(f'{Z[i]} {Vz[i]} \n')
densidade.close()

#=================================================================================
#=================================================================================
# Partial Charge Density 2D Plot using (GRACE) ===================================
#================================================================================= 
#=================================================================================  

if (save_agr == 1):

   print(" ")
   print ("=========== Plotting Partial Charge Density (Grace) ===========")

   execute_python_file(filename = 'plot/Grace/plot_parchg.py')

   print ("Partial Charge Density Plot via Grace (.agr file) completed")

#=================================================================================
#=================================================================================
# Partial Charge Density 2D Plot using (Matplotlib) ==============================
#================================================================================= 
#=================================================================================  

#---------------------------------------------------------------------------------
# Copy Densidade.py to the output folder directory  ------------------------------
#---------------------------------------------------------------------------------

try: f = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py'); f.close(); os.remove(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_parchg.py'
destination = dir_files + '/output/Densidade_Carga_Parcial/Densidade.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Entering parameters that allow the code to run separately ------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# {VASProcar_name} \n')
linha += 1; lines.insert(linha, f'# {url_1} \n')
linha += 1; lines.insert(linha, f'# {url_2} \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# Authors:                                                             \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Augusto de Lelis Araujo                                              \n')
linha += 1; lines.insert(linha, '# Federal University of Uberlandia (Uberlândia/MG - Brazil)            \n')
linha += 1; lines.insert(linha, '# e-mail: augusto-lelis@outlook.com                                    \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Renan da Paixao Maciel                                               \n')
linha += 1; lines.insert(linha, '# Uppsala University (Uppsala/Sweden)                                  \n')
linha += 1; lines.insert(linha, '# e-mail: renan.maciel@physics.uu.se                                   \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '\n')

linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# These are the parameters that allows the code to run separatedly === \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'ni = {ni}  #  Total Num. of ions \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] Angstron; [2] nm \n')
linha += 1; lines.insert(linha, f'destaque = {destaque}  #  Choose how much to highlight the coordinate of the ions, where: [0] NO and [1] YES \n')
linha += 1; lines.insert(linha, f'ion_x = {ion_x}  #  Coordinates of ions to be highlighted on the x-axis \n')
linha += 1; lines.insert(linha, f'ion_y = {ion_y}  #  Coordinates of ions to be highlighted on the y-axis \n')
linha += 1; lines.insert(linha, f'ion_z = {ion_z}  #  Coordinates of ions to be highlighted on the z-axis \n')
linha += 1; lines.insert(linha, f'fator_x = {fator_x}; fator_y = {fator_y}; fator_z = {fator_z}  #  Variation of the X,Y,Z coordinates suffered by the lattice vectors \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NOT and [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py', 'w')
file.writelines(lines)
file.close()

#-------------------------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py').read())
#-------------------------------------------------------------------------------

#=======================================================================

print(" ")
print("==============================================================")
print("= Edit the Density Plot through the Densidade.py or .agr files")
print("= (via Grace) generated in the folder ========================")   
print("= output/Densidade_Carga_Parcial =============================")
print("==============================================================")
   
#--------------------------------------------------------------------
print(" ")
print("======================= Completed ==========================")
#--------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
