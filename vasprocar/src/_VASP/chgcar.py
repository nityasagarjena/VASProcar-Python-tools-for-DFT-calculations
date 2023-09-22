# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())
   
#-----------------------------------------------------------------------
# Check whether the 'Charge' folder exists -----------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Charge'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Charge')
#----------------------------------------

print ("##############################################################")
print ("######### Charge Density / Charge Transfer - 2D Plot #########")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Hint: To generate a 3D Plot of the Charge over the ----- ##")
print ("##       crystal lattice, open the file CHGCAR in the VESTA ##")
print ("##       program ------------------------------------------ ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("What do you want to analyze? =================================")
print ("[0] Total Charge Density - x,y,z Directions  (2D Plot) =======")
print ("[1] Charge Transfer - x,y,z directions (2D Plot) =============")
print ("--------------------------------------------------------------")
print ("Only for Spin-Polarized calculation (LNONCOLLINEAR = .TRUE.)  ")
print ("[2] Magnetisation Density (2D Plot) ==========================")
print ("--------------------------------------------------------------")
print ("Only for Non-collinear Calculation (LNONCOLLINEAR = .TRUE.)   ")
print ("[3] Magnetisation Density - x direction (2D Plot) ============")
print ("[4] Magnetisation Density - y direction (2D Plot) ============")
print ("[5] Magnetisation Density - z direction (2D Plot) ============")
print ("##############################################################")
plot_type = input (" "); plot_type = int(plot_type)
print (" ")

if (plot_type != 1):
   nfiles = 1

if (plot_type == 1):

   print ("##############################################################")
   print ("How many CHGCAR files do you want to analyze:                 ")
   print ("##############################################################") 
   nfiles = input (" "); nfiles = int(nfiles)
   print (" ")

   #----------------------------------------------------------------------
   new_chgcar = open(dir_files + '/' + 'CHGCAR_Charge_Transfer.vasp', 'w')
   #----------------------------------------------------------------------

names = [0]*nfiles

for i in range(nfiles):
    if (i == 0):
       print ("##############################################################")
       print ("Enter the name of the main CHGCAR file:                       ")
       print ("##############################################################") 
       names[i] = input (" "); names[i] = str(names[i])
       print (" ")
    if (i != 0):
       print ("##############################################################")
       print ("Enter the name of the CHGCAR file to be subtracted:           ")
       print ("##############################################################") 
       names[i] = input (" "); names[i] = str(names[i])
       print (" ")

if (plot_type == 1):
   print ("==============================================================")
   print ("Calculation to be performed:                                  ")
   print ("--------------------------------------------------------------") 
   for i in range(nfiles):
       if (i == 0):
          print (f'+ ({names[i]})')
       if (i != 0):
          print (f'- ({names[i]}) ')
   print ("==============================================================")
   print (" ")

if (escolha == -1): 
   print ("##############################################################")
   print ("Choose the Plot's x-axis (abscissa) dimension: ===============")
   print ("[1] to Angs. (Default) =======================================")
   print ("[2] to nm. ===================================================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

   """
   print ("##############################################################")
   print ("Do you want to highlight the coordinate of the ions? =========")
   print ("[0] NOT ======================================================")
   print ("[1] YES (Default) ============================================")
   print ("##############################################################") 
   destaque = input (" "); destaque = int(destaque)
   print (" ")   
   """
   destaque = 0

if (escolha == 1):
   Dimensao = 1
   destaque = 0

#----------------------------------------------------------------------
# Obtaining the results from the files CHGCAR -------------------------
#----------------------------------------------------------------------

for m in range(nfiles):

    if (m == 0): fator = +1
    if (m != 0): fator = -1

    name = str(names[m])
    print (".........................................................")
    print (f'Readind {name} ')
    print ("please, wait a moment ...................................")
    print (".........................................................")
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

    #-----------------------------------------
    chgcar = open(dir_files + '/' + name, 'r')
    #-----------------------------------------

    VTemp = chgcar.readline()  
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    Parametro = float(VTemp)

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    VTemp = VTemp.split()
    A1x = float(VTemp[0]); A1y = float(VTemp[1]); A1z = float(VTemp[2])

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 
    
    VTemp = VTemp.split()
    A2x = float(VTemp[0]); A2y = float(VTemp[1]); A2z = float(VTemp[2])

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    VTemp = VTemp.split()
    A3x = float(VTemp[0]); A3y = float(VTemp[1]); A3z = float(VTemp[2])

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 
   
    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    VTemp = VTemp.split()

    ni = 0
    passo = len(VTemp)
    for i in range(passo):
        ni = ni + int(VTemp[i])

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
    Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
    Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

    ion_x = [0]*(ni)
    ion_y = [0]*(ni)
    ion_z = [0]*(ni)

    for i in range (ni):
        VTemp = chgcar.readline()
        if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 
        VTemp = VTemp.split()
        #---------------------------------------------------------------
        m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
        #---------------------------------------------------------------
        ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
        ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
        ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    VTemp = chgcar.readline()
    if (plot_type == 1 and m == 0): new_chgcar.write(f'{VTemp}') 

    palavra = str(VTemp)

    VTemp = VTemp.split()

    Grid_x = int(VTemp[0])
    Grid_y = int(VTemp[1])
    Grid_z = int(VTemp[2])
    GRID = Grid_x*Grid_y*Grid_z
    
    V_local = [0]*(GRID)
    if (plot_type == 1 and m == 0): new_V_local = [0]*(GRID)

    if (m == 0):
       Vx = [0.0]*(Grid_x)
       Vy = [0.0]*(Grid_y)
       Vz = [0.0]*(Grid_z)

    passo1 = (GRID/5)
    resto = passo1 - int(passo1)
    if (resto == 0): passo1 = int(passo1)
    if (resto != 0): passo1 = int(passo1) + 1

    passo2 = 5 - ((passo1*5) -GRID)

    #---------------------------------------------------------
    if (plot_type < 2):  passo = 0
    if (plot_type == 2): passo = 1
    if (plot_type > 2):  passo = plot_type -2

    for i in range(passo):
        for line in chgcar:   
            if palavra in line: 
               break    
    #---------------------------------------------------------

    for i in range (passo1):

        VTemp = chgcar.readline()
        #-----------------------------------------------------
        for k in range(10):
            VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
            VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
        VTemp = VTemp.split()    
        #----------------------------------------------------- 

        if (i < (passo1-1)):
           for j in range(5):
               V_local[((i)*5) + j] = float(VTemp[j])
           if (plot_type == 1):
              for j in range(5):
                  new_V_local[((i)*5) + j] = new_V_local[((i)*5) + j] + V_local[((i)*5) + j]*fator
        if (i == (passo1-1)):
           for j in range(passo2):
               V_local[((i)*5) + j] = float(VTemp[j])
           if (plot_type == 1):
              for j in range(passo2):
                  new_V_local[((i)*5) + j] = new_V_local[((i)*5) + j] + V_local[((i)*5) + j]*fator

    #-------------
    chgcar.close()
    #-------------
  
    #-------------------------------------------------------------------------------------

    fator_x = max(Ax) - min(Ax)
    fator_y = max(Ay) - min(Ay)
    fator_z = max(Az) - min(Az)

    """
    escala_x = 1.0/float(GRID/Grid_x); X = [0]*(Grid_x)
    escala_y = 1.0/float(GRID/Grid_y); Y = [0]*(Grid_y)
    escala_z = 1.0/float(GRID/Grid_z); Z = [0]*(Grid_z)
    """

    escala_x = 1.0/float(GRID); X = [0]*(Grid_x)
    escala_y = 1.0/float(GRID); Y = [0]*(Grid_y)
    escala_z = 1.0/float(GRID); Z = [0]*(Grid_z)
    
    #----------------------------------------------------------------------------
    # Analyzing the data: Obtaining the average Charge value in a given direction
    #----------------------------------------------------------------------------

    for i in range (Grid_x):
        for j in range (Grid_y):  
            for k in range (Grid_z):                          
                indice = i + (j + k*Grid_y)*Grid_x
                Vx[i] = Vx[i] + V_local[indice]*escala_x*fator
                Vy[j] = Vy[j] + V_local[indice]*escala_y*fator
                Vz[k] = Vz[k] + V_local[indice]*escala_z*fator

if (plot_type == 1): 

   for i in range (passo1):

       if (i < (passo1-1)):
          for j in range(5):
              new_chgcar.write(f'{new_V_local[((i)*5) + j]} ')
       if (i == (passo1-1)):
          for j in range(passo2):
              new_chgcar.write(f'{new_V_local[((i)*5) + j]} ')
       new_chgcar.write(f' \n')
   new_chgcar.close()

#=======================================================================
# Saving data to plot the Charge =======================================
#=======================================================================            

#---------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Charge/Charge_X.dat', "w")
#---------------------------------------------------------------------------------

for i in range (Grid_x):
    X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x     
    densidade.write(f'{X[i]} {Vx[i]} \n')
densidade.close()

#---------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Charge/Charge_Y.dat', "w")
#---------------------------------------------------------------------------------

for i in range (Grid_y):
    Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y    
    densidade.write(f'{Y[i]} {Vy[i]} \n')
densidade.close()

#---------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Charge/Charge_Z.dat', "w")
#---------------------------------------------------------------------------------

for i in range (Grid_z):
    Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z     
    densidade.write(f'{Z[i]} {Vz[i]} \n')
densidade.close()

#=================================================================================
#=================================================================================
# Charge - 2D Plot using (GRACE) =================================================
#================================================================================= 
#=================================================================================  

if (save_agr == 1):

   print(" ")
   print ("=================== Plotting Charge (Grace) ===================")

   execute_python_file(filename = 'plot/Grace/plot_chgcar.py')

   print ("Charge Plot via Grace (.agr file) completed")

#=================================================================================
#=================================================================================
# Charge - 2D Plot using (Matplotlib) ============================================
#================================================================================= 
#=================================================================================  

#---------------------------------------------------------------------------------
# Copy Charge.py to the output folder directory ----------------------------------
#---------------------------------------------------------------------------------

try: f = open(dir_files + '/output/Charge/Charge.py'); f.close(); os.remove(dir_files + '/output/Charge/Charge.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_chgcar.py'
destination = dir_files + '/output/Charge/Charge.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Entering parameters that allow the code to run separately ------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/Charge/Charge.py', 'r')
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
linha += 1; lines.insert(linha, f'ni = {ni}   # Total Num. of ions \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}   # [1] Angstron; [2] nm \n')
linha += 1; lines.insert(linha, f'destaque = {destaque}   # Choose how much to highlight the coordinate of the ions, where: [0] NO and [1] YES \n')
linha += 1; lines.insert(linha, f'plot_type = {plot_type}   # Plot type: [0] Charge Density, [1] Charge Transfer \n')
"""
linha += 1; lines.insert(linha, f'ion_x = {ion_x}   # Coordinates of ions to be highlighted on the x-axis \n')
linha += 1; lines.insert(linha, f'ion_y = {ion_y}   # Coordinates of ions to be highlighted on the y-axis \n')
linha += 1; lines.insert(linha, f'ion_z = {ion_z}   # Coordinates of ions to be highlighted on the z-axis \n')
"""
linha += 1; lines.insert(linha, f'fator_x = {fator_x}; fator_y = {fator_y}; fator_z = {fator_z}   # Variation of the X,Y,Z coordinates suffered by the lattice vectors \n')
 
if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}   # Plotting output format, where [0] = NOT and [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Charge/Charge.py', 'w')
file.writelines(lines)
file.close()

#-----------------------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Charge/Charge.py').read())
#-----------------------------------------------------------------------------

#=======================================================================

print(" ")
print("==============================================================")
print("= Edit the Charge Plot through the Charge.py or .agr files ===")
print("= (via Grace) generated in the folder output/Charge ==========")   
print("==============================================================")
   
#--------------------------------------------------------------------
print(" ")
print("======================= Completed ==========================")
#--------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
