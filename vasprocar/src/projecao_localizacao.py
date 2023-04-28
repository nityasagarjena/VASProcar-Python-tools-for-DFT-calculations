# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Localizacao' exists ------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Localizacao'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Localizacao')
#---------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

ion_orb = [[[0]*(n_orb+1) for i in range(ni+1)] for j in range(6+1)]  #  ion_orb[reg][ni][n_orb]
label_reg = ['null']*(6)
esc_ions = 0

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("############ Projection of the REGIONS (Location) ############")
print ("##############################################################") 
print (" ")

print ("##############################################################")
print ("To define a REGION to be projected in the band structure, you ")
print ("must inform the ions that belong to this region through       ")
print ("ion_intervals.                                                ")
print ("==============================================================")
print ("For a given REGION, you can inform how many ions_intervals you")
print ("deem necessary.                                               ")
print ("==============================================================")
print ("Ions can be added in any order.                               ")
print ("==============================================================")
print ("Examples:                                                     ")
print ("ions_intervals  15:27 28:36 37*                               ")  
print ("ions_intervals  35:78                                         ")
print ("ions_intervals  9* 10:14 15*                                  ")
print ("##############################################################")
print(" ")

print ("##############################################################")
print ("How many REGIONS do you want to analyze? =====================")
print ("============ (A maximum of 6 REGIONS are allowed) ============")
print ("##############################################################")
n_reg = input (" "); n_reg = int(n_reg)
print(" ")

if (n_reg <= 0): n_reg = 1
if (n_reg > 6):  n_reg = 6

for i in range(1,(n_reg+1)):
    
    print ("==============================================================")
    print (f'Enter the REGION_{i} label: ====================================')
    print ("==============================================================")
    label_reg[i-1] = input ("rotulo: "); label_reg[i-1] = str(label_reg[i-1])
    print(" ")

    print ("==============================================================")
    print (f'Inform the ions_intervals of REGIAO_{i} ========================')
    print (" ")
    reg_ion = input ("ions_intervals  ").replace(':', ' ').replace('-', ' ').replace('*', ' *').split( )
    print (" ")

    loop = int(len(reg_ion)/2)

    for j in range(1,(loop+1)):

        #------------------------------------------
        loop_i = int(reg_ion[(j-1)*2])
        if (reg_ion[((j-1)*2) +1] == "*"):
           reg_ion[((j-1)*2) +1] = reg_ion[(j-1)*2]
        loop_f = int(reg_ion[((j-1)*2) +1])
        #----------------------------------------------------------------------------------------
        if ((loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
           print (" ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print ("ERROR: The informed ion values are incorrect %%%%%%%%%%%%%")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           confirmation = input (" ")
           exit()
           
        for p in range(loop_i,(loop_f+1)):
            for m in range (1,(n_orb+1)):                   
                ion_orb[i][p][m] = 1                    
 
# Other input parameters =================================================

if (escolha == -1):

   print ("##################################################################") 
   print ("Do you want to change the color pattern of the REGIONS projections")
   print ("[0] NO                                                            ")
   print ("[1] YES                                                           ")
   print ("##################################################################") 
   esc_color = input (" "); esc_color = int(esc_color)
   print (" ")  

   if (esc_color == 1):
      print ("##############################################################")
      print ("Color code:                                                   ")
      print ("0  White   | 1  Black | 2  Red    | 3  Green  | 4  Blue       ")
      print ("5  Yellow  | 6  Borwn | 7  Grey   | 8  Violet | 9  Cyan       ")
      print ("10 Magenta |11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa   ")
      print ("15 Dark_Green                                                 ")
      print ("##############################################################")       
      print ("VASProcar color pattern:                                      ")
      print ("                                                              ")
      print ("Color_of_REGIONS 1|2|3|4|5|6:  4 2 3 10 9 5                   ")
      print ("(Blue, Red, Green, Magenta, Cyan, Yellow)                     ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Type in sequence the colors of the REGIONS that you defined:  ")
      cor_reg = input ("Color_of_REGIONS: ")
      #---------------------
      tcor = cor_reg.split()
      #-------------------------
      for i in range(len(tcor)):         
          if (i == 0): c_Reg1 = int(tcor[0])
          if (i == 1): c_Reg2 = int(tcor[1])
          if (i == 2): c_Reg3 = int(tcor[2])
          if (i == 3): c_Reg4 = int(tcor[3])
          if (i == 4): c_Reg5 = int(tcor[4])
          if (i == 5): c_Reg6 = int(tcor[5])
      #-------------------------------------
      print (" ") 

   print ("##############################################################")
   print ("Regarding the Plot of Bands, choose ==========================")
   print ("[0] Plot/Analyze all bands ===================================")
   print ("[1] Plot/Analyze selected bands ==============================")
   print ("##############################################################")
   esc_bands = input (" "); esc_bands = int(esc_bands)
   print(" ")

   if (esc_bands == 0):
      bands_range = '1:' + str(nb)

   if (esc_bands == 1):     
      print ("##############################################################")
      print ("Select the bands to be analyzed using intervals:              ")
      print ("Type as in the examples below =============================== ")
      print ("------------------------------------------------------------- ")
      print ("Bands can be added in any order ----------------------------- ")
      print ("------------------------------------------------------------- ")
      print ("bands_intervals  35:42                                        ")          
      print ("bands_intervals  1:15 27:69 18:19 76*                         ")
      print ("bands_intervals  7* 9* 11* 13* 16:21                          ")
      print ("##############################################################")
      bands_range = input ("bands_intervals  ")
      print (" ")
      #------------------------------------------------------------------------------------------
      selected_bands = bands_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
      loop = int(len(selected_bands)/2)
      #------------------------------------------------------------------------------------------
      
      for i in range (1,(loop+1)):
          #--------------------------------------------------------
          loop_i = int(selected_bands[(i-1)*2])
          if (selected_bands[((i-1)*2) +1] == "*"):
             selected_bands[((i-1)*2) +1] = selected_bands[(i-1)*2]
          loop_f = int(selected_bands[((i-1)*2) +1])
          #----------------------------------------------------------------------------------------
          if ((loop_i > nb) or (loop_f > nb) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("ERROR: The values of the informed bands are incorrect %%%%")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmacao = input (" ")
             exit()

   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")   

   print ("##############################################################") 
   print ("Do you want to modify the energy range to be plotted? ========")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################")
   esc_range_E = input (" "); esc_range_E = int(esc_range_E)
   print (" ")

   if (esc_range_E == 1):
      print ("##############################################################") 
      print ("Enter the energy range to be plotted: ========================")
      print ("Note: Enter the lowest and highest energy value to be plotted ")
      print ("            in relation to the Fermi Level                    ")
      print ("Examples:                                                     ")
      print ("--------------------------------------------------------------")
      print ("E_min E_max: -3.0 15.0                                        ")
      print ("E_min E_max: -5.1 5.0                                         ")
      print ("##############################################################")      
      range_E = input ("E_min E_max:  ")
      print (" ")
      #--------------------------------------------------
      selected_energ = range_E.replace('-', ' -').replace('+', ' +').replace(':', ' ').split()
      E_min = float(selected_energ[0])
      E_max = float(selected_energ[1])

   print ("##############################################################") 
   print ("Do you want to ignore contributions below a certain amount?   ")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################")
   esc_ignorar = input (" "); esc_ignorar = int(esc_ignorar)
   print (" ")
   
   if (esc_ignorar == 0 or esc_ignorar != 1):
      contrib_min = 0.0 
   if (esc_ignorar == 1):
      print ("##############################################################") 
      print ("Enter the minimum contribution amount to be plotted ==========")
      print ("Note: Enter a value between 0.0 and 1.0 ======================")
      print ("##############################################################")
      contrib_min = input (" "); contrib_min = float(contrib_min)
      print (" ")

   print ("##############################################################")
   print ("Would you like to label the k-points?                         ")
   print ("[0] DO NOT label the k-points  ===============================")
   print ("[1] highlight k-points present in KPOINTS file ===============")
   print ("[2] Customize: highlight and Label k-points   ================")
   print ("##############################################################") 
   dest_k = input (" "); dest_k = int(dest_k)
   print (" ")

   if (DFT == '_QE/' and dest_k == 2):
      print ("##############################################################")
      print ("Do you want to insert symmetries as k-point label?            ")
      print ("[0] NOT                                                       ")
      print ("[1] YES                                                       ")
      print ("##############################################################") 
      l_symmetry = input (" "); l_symmetry = int(l_symmetry)
      print (" ") 

   if (dest_k == 2):
      print ("##############################################################")
      print ("label.TXT file should be found inside the 'output' folder ====")
      print ("after reading the PROCAR file ================================")
      print ("##############################################################") 
      print (" ")

      Dimensao = 1

   if (dest_k != 2):   
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] 2pi/Param. (Param. in Angs.) =============================")
      print ("[2] 1/Angs. ==================================================")
      print ("[3] 1/nm.   ==================================================")
      print ("##############################################################")
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print(" ")

   print ("##############################################################")
   print ("Enter the weight/size of the spheres in the projection: ======")
   print ("Enter a value between 0.0 and 1.0 ============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("Enter the transparency value to apply to the projections:     ")
   print ("This option is useful for checking the overlap of orbitals.   ")   
   print ("Enter a value between 0.0 and 1.0 ============================")
   print ("==============================================================")
   print ("Hint: The higher the k-point density, the lower the ==========")
   print ("      transparency value used, start with 0.5 ================")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")   

if (escolha == 1):
   bands_range = '1:' + str(nb)
   esc_fermi = 1
   esc_range_E = 0
   dest_k = 1
   Dimensao = 1
   l_symmetry = 0
   peso_total = 1.0
   transp = 1.0
   contrib_min = 0.0

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
read_reg = 1
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------
if (esc_fermi == 0):
   dE_fermi = 0.0
   dest_fermi = Efermi

if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1)
   dest_fermi = 0.0

if (esc_range_E == 0):
   E_min = energ_min - Efermi
   E_max = energ_max - Efermi
#----------------------------

#======================================================================
# Getting k-points / labels ===========================================
#======================================================================
execute_python_file(filename = DFT + '_label.py')

#======================================================================
# Copy Bandas.dat to the output folder directory ======================
#======================================================================

try: f = open(dir_files + '/output/Localizacao/Bandas.dat'); f.close(); os.remove(dir_files + '/output/Localizacao/Bandas.dat')
except: 0 == 0
  
source = dir_files + '/output/Bandas.dat'
destination = dir_files + '/output/Localizacao/Bandas.dat'
shutil.copyfile(source, destination)

os.remove(dir_files + '/output/Bandas.dat')

os.remove(dir_files + '/output/Orbitais.dat')

#========================================================================
#========================================================================
# Projections Plot using (GRACE) ========================================
#======================================================================== 
#========================================================================

if (save_agr == 1):
    
   print(" ")
   print ("============== Plotting the Projections (Grace): ==============")

   execute_python_file(filename = 'plot/Grace/plot_projecao_localizacao.py')

   print ("Plot of projections via Grace (.agr files) completed ----------")
    
#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Localizacao.py to the output folder directory ------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Localizacao/Localizacao.py'); f.close(); os.remove(dir_files + '/output/Localizacao/Localizacao.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_localizacao.py'
destination = dir_files + '/output/Localizacao/Localizacao.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# {VASProcar_name} Copyright (C) 2023 \n')
linha += 1; lines.insert(linha, f'# GNU GPL-3.0 license \n')
linha += 1; lines.insert(linha, f'# {url_1} \n')
linha += 1; lines.insert(linha, f'# {url_2} \n')
linha += 1; lines.insert(linha, f'# {url_3} \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# Authors:                                                             \n')
linha += 1; lines.insert(linha, '# ==================================================================== \n')
linha += 1; lines.insert(linha, '# Augusto de Lelis Araujo                                              \n')
linha += 1; lines.insert(linha, '# [2022-2023] CNPEM|Ilum|LNNano (Campinas-SP/Brazil)                   \n')
linha += 1; lines.insert(linha, '# [2007-2022] Federal University of Uberlandia (Uberlândia-MG/Brazil)  \n')
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
linha += 1; lines.insert(linha, f'n_reg = {n_reg}          #  Number of REGIONS \n')
linha += 1; lines.insert(linha, f'label_reg = {label_reg}  #  REGIONS labels \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}    #  Total Number of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk = {nk}                #  Total Number of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}                #  Total Number of bands \n')
linha += 1; lines.insert(linha, f'n_orb = {n_orb}          #   Number of Orbitals \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}"  # Bands to be Plotted/Analyzed \n')
linha += 1; lines.insert(linha, f'E_min = {E_min}          #  Lower energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'E_max = {E_max}          #  Higher energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'lorbit = {lorbit}        #  Value of the lorbit variable adopted in the calculation \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}    #  [1] (kx,ky,kz) in 2pi/Param.; [2] (kx,ky,kz) in 1/Angs.; [3] (kx,ky,kz) in 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'peso_total = {peso_total}  #  weight/size of spheres in the projections plot \n')
linha += 1; lines.insert(linha, f'transp = {transp}          #  Transparency applied to the plot of projections \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}          #  [0] DO NOT label the k-points; [1] highlight k-points present in KPOINTS file; [2] Customize: highlight and Label k-points \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}        #  K-points coordinates to be highlighted in the band structure \n')

if (dest_k != 2):
   label_pk = ['null']*len(dest_pk) 
#-------------------------------------------------------------------------------
if (dest_k == 2): 
   for i in range(contador2):
       for j in range(34):
           if (label_pk[i] == '#' + str(j+1)):
              label_pk[i] = r_matplot[j]    
       if (DFT == '_QE/' and l_symmetry == 1):
          label_pk[i] = label_pk[i] + '$_{(' + symmetry_pk[i] + ')}$' 
#------------------------------------------------------------------------------
linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  K-points label \n')
#------------------------------------------------------------------------------

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, where [0] = NOT and [1] = YES \n')                          
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#======================================================================== \n')
linha += 1; lines.insert(linha, '# color code     :                                                        \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Colors applied to REGIONS:                                              \n')
linha += 1; lines.insert(linha, f'c_Reg1 = {c_Reg1}; c_Reg2 = {c_Reg2}; c_Reg3 = {c_Reg3}; c_Reg4 = {c_Reg4}; c_Reg5 = {c_Reg5}; c_Reg6 = {c_Reg6} \n') 
linha += 1; lines.insert(linha, '#======================================================================== \n')

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Localizacao/Localizacao.py').read())
#---------------------------------------------------------------------

#=======================================================================

print(" ")
print("=============================================================")
print("= Edit the Plot of the projections using the following ======")
print("= Localizacao.py or .agr files generated in the =============") 
print("= output/Localizacao folder =================================")
print("=============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Completed =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
