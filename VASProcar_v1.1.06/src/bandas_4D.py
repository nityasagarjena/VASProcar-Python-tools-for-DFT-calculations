
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------
# Check if "Plot_4D" folder exists ------------------------------------
#----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Plot_4D'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Plot_4D')
#-----------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Analyzing the variation of the coordinates of the K-points ==========
#======================================================================
execute_python_file(filename = DFT + '_var_kpoints.py')

soma_1 = dk[0] + dk[1] + dk[2]
soma_2 = dk[3] + dk[4] + dk[5]

if (soma_1 != 3 and soma_2 != 3):
   print ("============================================================")
   print ("!!! ERROR !!!                                               ")
   print ("============================================================")
   print ("The calculation performed does not correspond to a GRID 3D  ")
   print ("in the BZ (GRID kxkykz or k1k2k3)                           ")
   print ("------------------------------------------------------------")
   print ("Please, use the option [888] to get the correct KPOINTS file")
   print ("============================================================")
   confirmacao = input (" ")
   exit()

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("###################### ISOSURFACE PLOT: ######################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")

print ("##############################################################")
print ("What to do? ==================================================")
print ("[1] 3D energy dispersion of a specific band  =================")
print ("[2] Energy gap between two selected bands ====================")
print ("##############################################################") 
esc = input (" "); esc = int(esc)
print (" ")

if (esc == 1):
   print ("##############################################################")
   print ("Choose the band to be analyzed: ==============================")
   print ("##############################################################")
   Band = input (" "); Band = int(Band)
   print (" ")
   
   Band_1 = 0; Band_2 = 0

if (esc == 2):
   print ("##############################################################")
   print ("Inform the Band interval to be plotted: ===================== ")
   print ("--------------------------------------------------------------")
   print ("Examples:                                                     ")
   print ("Band_1 Band_2: 5 15                                           ")
   print ("Band_1 Band_2: 7 7                                            ")
   print ("--------------------------------------------------------------")
   print ("##############################################################") 
   print (" ")
   Band_1, Band_2 = input ("Banda_1 Banda_2: ").split()
   Band_1 = int(Band_1)
   Band_2 = int(Band_2)
   print (" ")
      
   Band = 0

#-----------------------------------------------------------------------------   

if (soma_1 == 3 or soma_2 == 3):
   #----------------------------------   
   if (soma_2 == 3 and escolha == -1):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) ==================")
      print ("[2] (kx,ky,kz) 1/Angs. =======================================")
      print ("[3] (kx,ky,kz) 1/nm.   =======================================")     
   #----------------------------------
   if (soma_1 == 3 and soma_2 == 3 and escolha == -1):    
      print ("[4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ===")  
   #----------------------------------
   if (soma_2 == 3 and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != 3):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != 3 and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == 3 and soma_2 == 3 and escolha == 1):
      Dimensao = 4

#-----------------------------------------------------------------------------       

if (escolha == -1):
   
   print ("##############################################################")
   print ("How many isosurfaces would you like to plot? =================")
   print ("Hint: use 15 (unless more precision is required) =============") # ???????????????????????????????????????????????????????
   print ("##############################################################") 
   n_iso = input (" "); n_iso = int(n_iso)
   print (" ")

   print ("##############################################################")
   print ("Choose the K-mesh grid (DxDxD) to be interpolated: ===========")
   print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
   print ("       used as a reference you are free to increase/decrease  ")
   print ("       the number of kpoints to be interpolated               ")
   print ("Hint:  use 31 (unless more precision is required)             ") # ???????????????????????????????????????????????????????
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)
   print (" ")   

if (escolha == 1):
   esc_fermi = 1 
   Dimensao = 4
   n_iso = 15
   n_d = 31

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------
# Obtaining the results from DFT outpout files ------------------------
#----------------------------------------------------------------------
execute_python_file(filename = DFT + '_nscf.py')

#======================================================================
# Saving data to plot the bands =======================================
#====================================================================== 

#------------------------------------------------------------
plot4D = open(dir_files + '/output/Plot_4D/Plot_4d.dat', 'w')
#------------------------------------------------------------

for i in range (1,(n_procar+1)):
    for j in range (1,(nk+1)):
        if (Dimensao < 4):
           x = kx[i][j]
           y = ky[i][j]
           z = kz[i][j]          
        if (Dimensao == 4):
           x = kb1[i][j]
           y = kb2[i][j]
           z = kb3[i][j]
        if (esc == 1):    
           e = Energia[i][j][Band]
        if (esc == 2):    
           e = (Energia[i][j][Band_2] - Energia[i][j][Band_1])
           e = (e**2)**0.5 
        plot4D .write(f'{x} {y} {z} {e} \n')

#--------------
plot4D .close()
#--------------

#----------------------------------------------------------------------
# Copy Plot_4D.py to the output folder directory  ---------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Plot_4D/Plot_4D.py'); f.close(); os.remove(dir_files + '/output/Plot_4D/Plot_4D.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_bandas_4D_plotly.py'
destination = dir_files + '/output/Plot_4D/Plot_4D.py'
shutil.copyfile(source, destination)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Allowing the Plot to be executed separatedly -----------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'r')
lines = file.readlines()
file.close()

linha = 8

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
linha += 1; lines.insert(linha, f'n_iso = {n_iso}    # Número of isosurfaces \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}        # Interpolation grid (DxDxD) \n')
linha += 1; lines.insert(linha, f'Band = {Band}      # The chosen band \n')
linha += 1; lines.insert(linha, f'Band_1 = {Band_1}  # 1nd band of the intervale \n')
linha += 1; lines.insert(linha, f'Band_2 = {Band_2}  # 2nd band of the intervale \n')
if (esc == 1):
   linha += 1; lines.insert(linha, f'Efermi = {Efermi}        # Fermi energy from DFT outpout files \n')
   linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  # Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}      # [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'esc = {esc}                 # Choose how much energy of the states (do not modify) \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------
exec(open(dir_files + '/output/Plot_4D/Plot_4D.py').read())
#----------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
