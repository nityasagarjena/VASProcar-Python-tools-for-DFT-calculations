# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Orbitais' exists ---------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Orbitais'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Orbitais')
#------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Get the input from user =============================================
#======================================================================

if (n_orb == 3):
   print ("############################")
   print ("Projecao dos Orbitais: S|P|D")
   print ("############################")

if (n_orb == 4):
   print ("##############################") 
   print ("Projecao dos Orbitais: S|P|D|F")
   print ("##############################") 

if (n_orb >= 9):
   print ("###############################################################") 
   print ("Projecao dos Orbitais: S, P (Px|Py|Pz), D (Dxy|Dyz|Dz2|Dxz|Dx2)")
   if(n_orb == 16):
     print ("                       F (Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2)")
   print ("###############################################################") 
print(" ") 

if (escolha == -1):

   print ("##############################################################") 
   print ("Deseja alterar o padrao de cores das projecoes dos Orbitais?  ")
   print ("[0] NAO                                                       ")
   print ("[1] SIM                                                       ")
   print ("##############################################################") 
   esc_color = input (" "); esc_color = int(esc_color)
   print (" ")  

   if (esc_color == 1):

      print ("##############################################################")
      print ("Codigo de cores:                                              ")
      print ("0  White   | 1  Black | 2  Red    | 3  Green  | 4  Blue       ")
      print ("5  Yellow  | 6  Borwn | 7  Grey   | 8  Violet | 9  Cyan       ")
      print ("10 Magenta |11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa   ")
      print ("15 Dark_Green                                                 ")
      print ("##############################################################")       
      print ("Padrao de cores do VASProcar:                                 ")
      print ("                                                              ")
      print ("Orbitais S|P|D|F:  4 2 3 10 (Blue, Red, Green, Magenta)       ")
      print ("--------------------------------------------------------------")      
      print ("Orbitais Px|Py|Pz: 4 2 3    (Blue, Red, Green)                ")
      print ("--------------------------------------------------------------") 
      print ("Orbitais Dxy|Dyz|Dz2|Dxz|Dx2: 4 2 3 10 9                      ")
      print ("(Blue, Red, Green, Magenta, Cyan)                             ")
      print ("--------------------------------------------------------------")
      if (n_orb == 16): 
         print ("Orbitais Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2: 4 2 3 10 9 5 11  ")
         print ("(Blue, Red, Green, Magenta, Cyan, Yellow, Orange)             ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Digite em sequencia as cores dos orbitais S|P|D|F:            ")
      cor_orb = input ("Cores_dos_Orbitais: ")
      #---------------------
      tcor = cor_orb.split()
      c_S = int(tcor[0]); c_P = int(tcor[1]); c_D = int(tcor[2]); c_F = int(tcor[3])
      #---------------------
      print (" ")
      
      if (n_orb >= 9):

         print ("==============================================================") 
         print ("Digite em sequencia as cores dos orbitais Px|Py|Pz:           ")
         cor_orb = input ("Cores_dos_Orbitais: ")
         #---------------------
         tcor = cor_orb.split()
         c_Px = int(tcor[0]); c_Py = int(tcor[1]); c_Pz = int(tcor[2])
         #---------------------
         print (" ")
         
         print ("==============================================================") 
         print ("Digite em sequencia as cores dos orbitais Dxy|Dyz|Dz2|Dxz|Dx2:")
         cor_orb = input ("Cores_dos_Orbitais: ")
         #---------------------
         tcor = cor_orb.split()
         c_Dxy = int(tcor[0]); c_Dyz = int(tcor[1]); c_Dz2 = int(tcor[2]); c_Dxz = int(tcor[3]); c_Dx2 = int(tcor[4])
         #---------------------
         print (" ")

         if (n_orb == 16):
            print ("=============================================================================") 
            print ("Digite em sequencia as cores dos orbitais Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2:")
            cor_orb = input ("Cores_dos_Orbitais: ")
            #---------------------
            tcor = cor_orb.split()
            c_Fyx2 = int(tcor[0]); c_Fxyz = int(tcor[1]); c_Fyz2 = int(tcor[2]); c_Fzz2 = int(tcor[3])
            c_Fxz2 = int(tcor[4]); c_Fzx2 = int(tcor[5]); c_Fxx2 = int(tcor[6])
            #---------------------
            print (" ")

   print ("##############################################################")
   print ("Com relacao ao Plot das Bandas, escolha ======================")
   print ("[0] Plotar/Analisar todas as bandas ==========================")
   print ("[1] Plotar/Analisar bandas selecionadas ======================")
   print ("##############################################################")
   esc_bands = input (" "); esc_bands = int(esc_bands)
   print(" ")

   if (esc_bands == 0):
      bands_range = '1:' + str(nb)

   if (esc_bands == 1):     
      print ("##############################################################")
      print ("Selecione por meio de intervalos as bandas a serem analisadas:")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("------------------------------------------------------------- ")
      print ("A bandas podem ser adicionadas em qualquer ordem ------------ ")
      print ("------------------------------------------------------------- ")
      print ("intervalos_de_bandas  35:42                                   ")          
      print ("intervalos_de_bandas  1:15 27:69 18:19 76*                    ")
      print ("intervalos_de_bandas  7* 9* 11* 13* 14-15                     ")
      print ("##############################################################")
      bands_range = input ("intervalos_de_bandas  ")
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
             print ("ERRO: Os valores das bandas informadas estao incorretos %%")
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
   print ("O que vc deseja Analisar? ====================================")
   print ("[0] Analisar todos os ions da rede ===========================")
   print ("[1] Analisar ions selecionados ===============================")
   print ("##############################################################")
   esc_ions = input (" "); esc_ions = int(esc_ions)
   print(" ")

   if (esc_ions == 1):
      
      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  #  Inicialização do vetor sim_nao
      #-------------------------

      print ("##############################################################")
      print ("Escolha os intervalos_de_ions a serem analisados: =========== ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("A ordem em que os ions são adicionados, nao altera o resultado")
      print ("--------------------------------------------------------------")
      print ("intervalos_de_ions  1:5 3:9 11* 15:27                         ")          
      print ("intervalos_de_ions  7:49 50:53                                ")
      print ("intervalos_de_ions  1* 3* 6:9                                 ")
      print ("##############################################################")
      ion_range = input ("intervalo_de_ions  ")
      print (" ")
      #---------------------------------------------------------------------------------------
      selected_ions = ion_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
      loop = int(len(selected_ions)/2)
      #---------------------------------------------------------------------------------------
      
      for i in range (1,(loop+1)):
          #------------------------------------------------------
          loop_i = int(selected_ions[(i-1)*2])
          if (selected_ions[((i-1)*2) +1] == "*"):
             selected_ions[((i-1)*2) +1] = selected_ions[(i-1)*2]
          loop_f = int(selected_ions[((i-1)*2) +1])
          #----------------------------------------------------------------------------------------
          if ((loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmacao = input (" ")
             exit()
          #----------------------------------------------------------------------           
          for j in range(loop_i, (loop_f + 1)):
              sim_nao[j] = "sim"    

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
      print ("Deseja inserir as simetrias como rotulo dos pontos-k?         ")
      print ("[0] NAO                                                       ")
      print ("[1] SIM                                                       ")
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
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia a ser aplicado nas projecoes: ")
   print ("Esta opcao e util para verificar a sobreposicao de orbitais.  ")   
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("==============================================================")
   print ("Dica: Quanto maior for a densidade de pontos-k, menor deve ser")
   print ("      o valor de transparencia utilizado, comece por 0.1 =====")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")         

if (escolha == 1):
   bands_range = '1:' + str(nb)
   esc_fermi = 1
   esc_range_E = 0  
   esc_ions = 0
   dest_k = 1
   Dimensao = 1
   l_symmetry = 0
   peso_total = 1.0
   transp = 1.0

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
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
# Copy Bandas.dat and Orbitais.dat to the output folder directory =====
#======================================================================

try: f = open(dir_files + '/output/Orbitais/Bandas.dat'); f.close(); os.remove(dir_files + '/output/Orbitais/Bandas.dat')
except: 0 == 0
  
source = dir_files + '/output/Bandas.dat'
destination = dir_files + '/output/Orbitais/Bandas.dat'
shutil.copyfile(source, destination)

os.remove(dir_files + '/output/Bandas.dat')

#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Orbitais/Orbitais.dat'); f.close(); os.remove(dir_files + '/output/Orbitais/Orbitais.dat')
except: 0 == 0
  
source = dir_files + '/output/Orbitais.dat'
destination = dir_files + '/output/Orbitais/Orbitais.dat'
shutil.copyfile(source, destination)

os.remove(dir_files + '/output/Orbitais.dat')

#========================================================================
#========================================================================
# Projections Plot using (GRACE) ========================================
#======================================================================== 
#========================================================================

if (save_agr == 1):
    
   print(" ")
   print ("================ Plotando as Projecoes (Grace) ================")

   execute_python_file(filename = 'plot/Grace/plot_projecao_orbitais.py')

   print ("Plot das projecoes via Grace (arquivos .agr) concluido --------")
  
#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Orbitais.py to the output folder directory ---------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Orbitais/Orbitais.py'); f.close(); os.remove(dir_files + '/output/Orbitais/Orbitais.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_orbitais.py'
destination = dir_files + '/output/Orbitais/Orbitais.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'r')
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
linha += 1; lines.insert(linha, f'n_procar = {n_procar}  #  Total Num. of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk = {nk}              #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}              #  Total Num. of bands \n')
linha += 1; lines.insert(linha, f'n_orb = {n_orb}        #  Num. of Orbitals \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}"  # Bandas a serem plotadas/Analisadas \n')
linha += 1; lines.insert(linha, f'E_min = {E_min}        #  Lower energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'E_max = {E_max}        #  Higher energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'lorbit = {lorbit}        #  Valor da variavel lorbit adotada no calculo \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}    #  [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'peso_total = {peso_total}  #  peso/tamanho das esferas no plot das projecões \n')
linha += 1; lines.insert(linha, f'transp = {transp}          #  Transparencia aplicada ao plot das projecoes \n')
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
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#======================================================================== \n')
linha += 1; lines.insert(linha, '# Codigo de cores:                                                        \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Cores aplicadas aos orbitais:                                           \n')
linha += 1; lines.insert(linha, f'c_S = {c_S}; c_P = {c_P}; c_D = {c_D}; c_F = {c_F} \n')
if (lorbit >= 11):
   linha += 1; lines.insert(linha, f'c_Px = {c_Px}; c_Py = {c_Py}; c_Pz = {c_Pz} \n')
   linha += 1; lines.insert(linha, f'c_Dxy = {c_Dxy}; c_Dyz = {c_Dyz}; c_Dz2 = {c_Dz2}; c_Dxz = {c_Dxz}; c_Dx2 = {c_Dx2} \n')    
   if (n_orb == 16): 
      linha += 1; lines.insert(linha, f'c_Fyx2 = {c_Fyx2}; c_Fxyz = {c_Fxyz}; c_Fyz2 = {c_Fyz2}; c_Fzz2 = {c_Fzz2}; c_Fxz2 = {c_Fxz2}; c_Fzx2 = {c_Fzx2}; c_Fxx2 = {c_Fxx2} \n') 
linha += 1; lines.insert(linha, '#======================================================================== \n')

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Orbitais/Orbitais.py').read())
#---------------------------------------------------------------

#=======================================================================

print(" ")
print("================================================================")
print("= Edite o Plot das projecoes por meio dos arquivos Orbitais.py  ")
print("= ou dos arquivos .agr (Grace) gerados na pasta output/Orbitais ")
print("================================================================")
   
#-----------------------------------------------------------------------
print(" ")
print("-------------------------- Concluido! --------------------------")
#-----------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
