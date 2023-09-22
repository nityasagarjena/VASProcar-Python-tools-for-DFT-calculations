# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())
   
#-----------------------------------------------------------------------
# Check whether the 'BSE' folder exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/BSE'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/BSE')
#-------------------------------------

print ("##############################################################")
print ("################## Dieletric function plot: ##################")
print ("##############################################################")
print (" ")

#======================================================================
# Check if vasprun.xml exists =========================================
#======================================================================

try:
    f = open(dir_files + '/vasprun.xml')
    f.close()
except:
    print ("--------------------------------------------------------------")
    print ("Missing the file 'vasprun.xml' in the current directory ------")
    print ("Please, fix it! and press ENTER to continue ------------------")
    print ("--------------------------------------------------------------")
    confirmacao = input (" "); confirmacao = str(confirmacao)   

#======================================================================
# Get the input from user =============================================
#======================================================================

if (escolha == -1):
   
   print ("##############################################################")
   print ("Would you like to choose the plot energy range? ==============")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################") 
   esc_energ = input (" "); esc_energ = int(esc_energ)
   print (" ")
 
   if (esc_energ == 1):
      print ("##############################################################")
      print ("Inform the energy range to be considered:  ===================")
      print ("Examples:                                                     ")
      print ("--------------------------------------------------------------")
      print ("Initial_Energy  Final_Energy: -5.0 3.5                        ")
      print ("Initial_Energy  Final_Energy:  1.0 9.8                        ") 
      print ("##############################################################") 
      print (" ")
      x_inicial, x_final = input ("Initial_Energy  Final_Energy: ").split()
      x_inicial = float(x_inicial)
      x_final   = float(x_final)
      print (" ") 
   
print ("##############################################################")
print ("Inform the obtained Fermi energy =============================")
print ("##############################################################") 
Efermi = input (" "); Efermi = float(Efermi)
print (" ")

if (escolha == -1):
   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")  

if (escolha == 1):
   esc_fermi = 1
   esc_energ = 0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------
# Obtaining the results from vasprun.xml ------------------------------
#----------------------------------------------------------------------

print (".........................................................")
print ("................. Reagind vasprun.xml ...................")
print ("................ please, wait a moment ..................")
print (".........................................................")

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

passo = -1

palavra = '</set>'
for line in vasprun:
    passo += 1
    if palavra in line: 
       break

#--------------
vasprun.close()
#--------------

#==============================================

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

energ = [0.0]*passo
X_i   = [0.0]*passo;  X_r  = [0.0]*passo
Y_i   = [0.0]*passo;  Y_r  = [0.0]*passo
Z_i   = [0.0]*passo;  Z_r  = [0.0]*passo
XY_i  = [0.0]*passo;  XY_r = [0.0]*passo
YZ_i  = [0.0]*passo;  YZ_r = [0.0]*passo
ZX_i  = [0.0]*passo;  ZX_r = [0.0]*passo
media_i  = [0.0]*passo;  media_r  = [0.0]*passo
modulo_i = [0.0]*passo;  modulo_r = [0.0]*passo

#----------------------------------------------

for i in range(passo):
    VTemp = vasprun.readline().split()
    energ[i] = float(VTemp[1])
    X_i[i]   = float(VTemp[2])
    Y_i[i]   = float(VTemp[3])
    Z_i[i]   = float(VTemp[4])
    media_i[i]  = (X_i[i] + Y_i[i] + Z_i[i])/3
    modulo_i[i] = ((X_i[i]**2) + (Y_i[i]**2) + (Z_i[i]**2))**0.5
    # XY_i[i]  = float(VTemp[5])
    # YZ_i[i]  = float(VTemp[6])
    # ZX_i[i]  = float(VTemp[7])

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

for i in range(passo):
    VTemp = vasprun.readline().split()
    X_r[i]   = float(VTemp[2])
    Y_r[i]   = float(VTemp[3])
    Z_r[i]   = float(VTemp[4])
    media_r[i]  = (X_r[i] + Y_r[i] + Z_r[i])/3
    modulo_r[i] = ((X_r[i]**2) + (Y_r[i]**2) + (Z_r[i]**2))**0.5
    # XY_r[i]  = float(VTemp[5])
    # YZ_r[i]  = float(VTemp[6])
    # ZX_r[i]  = float(VTemp[7])

#--------------
vasprun.close()
#--------------

#======================================================================
# Saving data to plot the Dieletric function ==========================
#======================================================================     

#-------------------------------------------------
BSE = open(dir_files + '/output/BSE/BSE.dat', 'w')
#-------------------------------------------------

for i in range (passo):
    BSE.write(f'{energ[i]}')
    BSE.write(f' {modulo_i[i]} {media_i[i]}')
    BSE.write(f' {X_i[i]} {Y_i[i]} {Z_i[i]}')
    # BSE.write(f' {XY_i[i]} {YZ_i[i]} {ZX_i[i]}')
    BSE.write(f' {media_r[i]} {modulo_r[i]}')
    BSE.write(f' {X_r[i]} {Y_r[i]} {Z_r[i]}')
    # BSE.write(f' {XY_r[i]} {YZ_r[i]} {ZX_r[i]}')
    BSE.write(f' \n')
    
#----------
BSE.close()
#----------

if (esc_energ == 0):
   x_inicial = min(energ)
   x_final   = max(energ)

#=================================================================================
#=================================================================================
# Dieletric function Plot using (GRACE) ==========================================
#=================================================================================
#=================================================================================

if (save_agr == 1):

   print(" ")
   print ("========== Plotting the Dielectric Function (Grace): ==========")

   execute_python_file(filename = 'plot/Grace/plot_dielectric_function.py')

   print ("Dielectric Function Plot (.agr file) completed ----------------")

#=================================================================================
#=================================================================================
# Dieletric function Plot using (Matplotlib) =====================================
#================================================================================= 
#=================================================================================     

#---------------------------------------------------------------------------------
# Copy Dielectric_Function.py to the output folder directory  --------------------
#---------------------------------------------------------------------------------

try: f = open(dir_files + '/output/BSE/Dielectric_Function.py'); f.close(); os.remove(dir_files + '/output/BSE/Dielectric_Function.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_dielectric_function.py'
destination = dir_files + '/output/BSE/Dielectric_Function.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Entering parameters that allow the code to run separately ------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'r')
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
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout file \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'esc_energ = {esc_energ}  #  Would you like to perform an energy range analysis: [0] No e [1] Yes \n')
linha += 1; lines.insert(linha, f'x_inicial = {x_inicial}; x_final = {x_final}  #  Initial and final energy (based on the energy range chosen in the last option) \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NOT e [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/BSE/Dielectric_Function.py').read())
#---------------------------------------------------------------------

#=======================================================================

print(" ")
print("================================================================")
print("= Edit the Dielectric Function Plot through the ================")
print("= Dielectric_Function.py or .agr (via Grace) files generated ===")
print("= in the output/BSE folder =====================================")   
print("================================================================")

#--------------------------------------------------------------------
print(" ")
print("======================= Completed ==========================")
#--------------------------------------------------------------------  

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
