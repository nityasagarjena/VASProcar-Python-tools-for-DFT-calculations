# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Psi' exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Psi'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Psi')
#-------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

ion_orb = [[[0]*(n_orb+1) for i in range(ni+1)] for j in range(6+1)]  #  ion_orb[n_psi][ni][n_orb]
label_psi = ['null']*(6)
esc_ions = 0

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("################## Projecao dos estados Psi ##################")
print ("##############################################################") 
print (" ")

print ("##############################################################")
print ("Para definir um estado_Psi, voce deve informar um determinado ")
print ("intervalo_de_ions, e tambem informar quais orbitais devem ser ")
print ("incluidos neste respectivo intervalo.                         ")
print ("==============================================================")
print ("Para um dado estado_Psi, voce pode informar quantos intervalos")
print ("de ions achar necessario.                                     ")
print ("==============================================================")
print ("Os ions e orbitais podem ser adicionados em qualquer ordem.   ")
print ("==============================================================")
print ("Use a nomenclatura abaixo para designar os Orbitais:          ")
if (n_orb == 3):  print ("s p d")
if (n_orb == 4):  print ("s p d f")
if (n_orb == 9):  print ("s p d px py pz dxy dyz dz2 dxz dx2")
if (n_orb == 16): print ("s p d f px py pz dxy dyz dz2 dxz dx2 fyx2 fxyz fyz2 fzz2 fxz2 fzx2 fxx2")
print ("==============================================================")
print ("Para um mesmo intervalo de ions, separe os orbitais usando +  ")
print ("==============================================================")
print ("Exemplos:                                                     ")
if (lorbit == 10):
   if (n_orb == 3): print ("intervalos_de_ions orbitais  3:3 s+p+d       ")
   if (n_orb == 4): print ("intervalos_de_ions orbitais  3:3 s+p+d+f     ")
   print ("intervalos_de_ions orbitais  5:14 s+p 15:36 s+d               ")
   print ("intervalos_de_ions orbitais  14:49 s 50:51 p 52* d            ")
if (n_orb >= 9):
   print ("intervalos_de_ions orbitais  15:27 s+pz 28:36 px+py 37* d     ")  
   print ("intervalos_de_ions orbitais  35:78 s+pz+dxz+dx2               ")
   print ("intervalos_de_ions orbitais  9* s+p+d 10:14 pz 15* px+py      ")
   print ("##############################################################")
print(" ")

print ("##############################################################")
print ("Quantos estados Psi deseja analisar? =========================")
print (" ========= (Sao permitidos no maximo 6 estados Psi) ========= ")
print ("##############################################################")
n_psi = input (" "); n_psi = int(n_psi)
print(" ")

if (n_psi <= 0): n_psi = 1
if (n_psi > 6):  n_psi = 6

for i in range(1,(n_psi+1)):
    
    print ("==============================================================")
    print (f'Digite o rotulo do estado_Psi {i}: =============================')
    print ("==============================================================")
    label_psi[i-1] = input ("rotulo: "); label_psi[i-1] = str(label_psi[i-1])
    print(" ")

    print ("==============================================================")
    print (f'Informe os intervalos_de_ions e orbitais do estado_psi_{i} =====')
    print (" ")
    psi_io = input ("intervalos_de_ions orbitais  ").replace(':', ' ').replace('-', ' ').replace('*', ' *').split( )
    print (" ")

    loop = int(len(psi_io)/3)

    for j in range(1,(loop+1)):

        #------------------------------------------
        loop_i = int(psi_io[((j-1)*3)])
        if (psi_io[((j-1)*3) +1] == "*"):
           psi_io[((j-1)*3) +1] = psi_io[((j-1)*3)]
        loop_f = int(psi_io[((j-1)*3) +1])
        #----------------------------------------------------------------------------------------
        if ((loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
           print (" ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print ("   ERRO: Os valores de ions informados estao incorretos   ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           confirmacao = input (" ")
           exit()

        psi_o = psi_io[((j-1)*3) +2].split('+')
        loop_o = len(psi_o)
             
        for p in range(loop_i,(loop_f+1)):
            for t in range(loop_o):
                #------------------------------------------  
                if (n_orb <= 4):                   
                   if (psi_o[t] == 's' or psi_o[t] == 'S'):
                      ion_orb[i][p][1] = 1                    
                   if (psi_o[t] == 'p' or psi_o[t] == 'P'):
                      ion_orb[i][p][2] = 1                      
                   if (psi_o[t] == 'd' or psi_o[t] == 'D'):
                      ion_orb[i][p][3] = 1
                #------------------------------------------ 
                if (n_orb == 4 and DFT == '_VASP/'):
                   if (psi_o[t] == 'f' or psi_o[t] == 'F'):
                      ion_orb[i][p][4] = 1
                #------------------------------------------     
                if (n_orb >= 9):                   
                   if (psi_o[t] == 's' or psi_o[t] == 'S'):
                      ion_orb[i][p][1] = 1                      
                   if (psi_o[t] == 'p' or psi_o[t] == 'P'):
                      ion_orb[i][p][2] = 1; ion_orb[i][p][3] = 1; ion_orb[i][p][4] = 1                      
                   if (psi_o[t] == 'd' or psi_o[t] == 'D'):
                      ion_orb[i][p][5] = 1; ion_orb[i][p][6] = 1; ion_orb[i][p][7] = 1; ion_orb[i][p][8] = 1; ion_orb[i][p][9] = 1                       
                   if (psi_o[t] == 'py' or psi_o[t] == 'Py' or psi_o[t] == 'PY'):
                      if (DFT == '_VASP/'): ion_orb[i][p][2] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][4] = 1
                   if (psi_o[t] == 'pz' or psi_o[t] == 'Pz' or psi_o[t] == 'PZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][3] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][2] = 1
                   if (psi_o[t] == 'px' or psi_o[t] == 'Px' or psi_o[t] == 'PX'):
                      if (DFT == '_VASP/'): ion_orb[i][p][4] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][3] = 1 
                   if (psi_o[t] == 'dxy' or psi_o[t] == 'Dxy' or psi_o[t] == 'DXY'):
                      if (DFT == '_VASP/'): ion_orb[i][p][5] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][9] = 1 
                   if (psi_o[t] == 'dyz' or psi_o[t] == 'Dyz' or psi_o[t] == 'DYZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][6] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][7] = 1 
                   if (psi_o[t] == 'dz2' or psi_o[t] == 'Dz2' or psi_o[t] == 'DZ2'):
                      if (DFT == '_VASP/'): ion_orb[i][p][7] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][5] = 1 
                   if (psi_o[t] == 'dxz' or psi_o[t] == 'Dxz' or psi_o[t] == 'DXZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][8] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][6] = 1 
                   if (psi_o[t] == 'dx2' or psi_o[t] == 'Dx2' or psi_o[t] == 'DX2' or psi_o[t] == 'dx2-y2' or psi_o[t] == 'Dx2-y2' or psi_o[t] == 'DX2-Y2'):
                      if (DFT == '_VASP/'): ion_orb[i][p][9] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][8] = 1 
                #-----------------------------------------------
                if (n_orb == 16 and DFT == '_VASP/'): 
                   if (psi_o[t] == 'f' or psi_o[t] == 'F'):
                      ion_orb[i][p][10] = 1; ion_orb[i][p][11] = 1; ion_orb[i][p][12] = 1; ion_orb[i][p][13] = 1
                      ion_orb[i][p][14] = 1; ion_orb[i][p][15] = 1; ion_orb[i][p][16] = 1                     
                   if (psi_o[t] == 'fyx2' or psi_o[t] == 'Fyx2' or psi_o[t] == 'FYX2'): ion_orb[i][p][10] = 1
                   if (psi_o[t] == 'fxyz' or psi_o[t] == 'Fxyz' or psi_o[t] == 'FXYZ'): ion_orb[i][p][11] = 1
                   if (psi_o[t] == 'fyz2' or psi_o[t] == 'Fyz2' or psi_o[t] == 'FYZ2'): ion_orb[i][p][12] = 1
                   if (psi_o[t] == 'fzz2' or psi_o[t] == 'Fzz2' or psi_o[t] == 'FZZ2'): ion_orb[i][p][13] = 1
                   if (psi_o[t] == 'fxz2' or psi_o[t] == 'Fxz2' or psi_o[t] == 'FXZ2'): ion_orb[i][p][14] = 1
                   if (psi_o[t] == 'fzx2' or psi_o[t] == 'Fzx2' or psi_o[t] == 'FZX2'): ion_orb[i][p][15] = 1
                   if (psi_o[t] == 'fxx2' or psi_o[t] == 'Fxx2' or psi_o[t] == 'FXX2'): ion_orb[i][p][16] = 1

temp = [0.0]*(n_orb)

#==========================================================================


if (ni <= 10):

   print ("##############################################################")
   print ("Confira os estados informados antes de prosseguir:            ")
   print ("Onde [0] = NAO e [1] = SIM                                    ")
   print ("##############################################################")

   for i in range(1,(n_psi+1)):
       print (" ")
       print ("------------")
       print (f'Estado Psi {i}')
       print ("------------")
       for j in range(1,(ni+1)):
           for k in range (1,(n_orb+1)):
               temp[k-1] = ion_orb[i][j][k]

           if (n_orb == 3):
              print (f'ion {j} ({rotulo[j]}): orbitais S[{temp[0]}] P[{temp[1]}] D[{temp[2]}]')
           if (n_orb == 4):
              print (f'ion {j} ({rotulo[j]}): orbitais S[{temp[0]}] P[{temp[1]}] D[{temp[2]} F[{temp[3]}]')
           if (n_orb == 9):
              print (f'ion {j} ({rotulo[j]}): orbitais S[{temp[0]}] Px[{temp[3]}] Py[{temp[1]}] Pz[{temp[2]}] Dxy[{temp[4]}] Dyz[{temp[5]}] Dz2[{temp[6]}] Dxz[{temp[7]}] Dx2[{temp[8]}]')   
           if (n_orb == 16):
              print ("========================== Em Edicao ==========================")         

   print (" ")
   print ("##############################################################")
   print ("Atencao: Caso esteja tudo certo com os estados Psi informados ")
   print ("         aperte [ENTER] para continuar.                       ")
   print ("##############################################################")
   confirmacao = input (" ")

# Demais parâmetros de input ==========================================

if (escolha == -1):

   print ("##############################################################") 
   print ("Deseja alterar o padrao de cores das projecoes dos Estados Psi")
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
      print ("Cor dos Estados Psi 1|2|3|4|5|6:  4 2 3 10 9 5                ")
      print ("(Blue, Red, Green, Magenta, Cyan, Yellow)                     ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Digite em sequencia as cores dos Estados Psi que vc definiu:  ")
      cor_psi = input ("Cores_dos_Estados_Psi: ")
      #---------------------
      tcor = cor_psi.split()
      #-------------------------
      for i in range(len(tcor)):         
          if (i == 0): c_Psi1 = int(tcor[0])
          if (i == 1): c_Psi2 = int(tcor[1])
          if (i == 2): c_Psi3 = int(tcor[2])
          if (i == 3): c_Psi4 = int(tcor[3])
          if (i == 4): c_Psi5 = int(tcor[4])
          if (i == 5): c_Psi6 = int(tcor[5])
      #-------------------------------------
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
      print ("intervalos_de_bandas  7* 9* 11* 13* 16:21                     ")
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
   print ("Deseja ignorar contribuicoes abaixo de um determinado valor?  ")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################")
   esc_ignorar = input (" "); esc_ignorar = int(esc_ignorar)
   print (" ")
   
   if (esc_ignorar == 0 or esc_ignorar != 1):
      contrib_min = 0.0 
   if (esc_ignorar == 1):
      print ("##############################################################") 
      print ("Digite o valor minimo de contribuição a ser plotado ==========")
      print ("Observacao: Digite um valor entre 0.0 e 1.0 ==================")
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
   dest_k = 1
   Dimensao = 1
   l_symmetry = 0
   peso_total = 1.0
   contrib_min = 0.0
   transp = 1.0

#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
read_psi = 1
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

try: f = open(dir_files + '/output/Psi/Bandas.dat'); f.close(); os.remove(dir_files + '/output/Psi/Bandas.dat')
except: 0 == 0
  
source = dir_files + '/output/Bandas.dat'
destination = dir_files + '/output/Psi/Bandas.dat'
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
   print ("================ Plotando as Projecoes (Grace) ================")

   execute_python_file(filename = 'plot/Grace/plot_projecao_psi.py')

   print ("Plot das projecoes via Grace (arquivos .agr) concluido --------")
    
#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Psi.py to the output folder directory --------------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Psi/Psi.py'); f.close(); os.remove(dir_files + '/output/Psi/Psi.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_psi.py'
destination = dir_files + '/output/Psi/Psi.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Psi/Psi.py', 'r')
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
linha += 1; lines.insert(linha, f'n_psi = {n_psi}          #  Numero de estados Psi \n')
linha += 1; lines.insert(linha, f'label_psi = {label_psi}  #  Rotulos dos estados Psi \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}    #  Total Num. of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk = {nk}                #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}                #  Total Num. of bands \n')
linha += 1; lines.insert(linha, f'n_orb = {n_orb}          #  Num. of Orbitals \n')
linha += 1; lines.insert(linha, f'bands_range = "{bands_range}"  # Bandas a serem plotadas/Analisadas \n')
linha += 1; lines.insert(linha, f'E_min = {E_min}          #  Lower energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'E_max = {E_max}          #  Higher energy value of the bands in the plot (in relation to the Fermi level) \n')
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
linha += 1; lines.insert(linha, '# Cores aplicadas aos Estados Psi:                                        \n')
linha += 1; lines.insert(linha, f'c_Psi1 = {c_Psi1}; c_Psi2 = {c_Psi2}; c_Psi3 = {c_Psi3}; c_Psi4 = {c_Psi4}; c_Psi5 = {c_Psi5}; c_Psi6 = {c_Psi6} \n') 
linha += 1; lines.insert(linha, '#======================================================================== \n')

file = open(dir_files + '/output/Psi/Psi.py', 'w')
file.writelines(lines)
file.close()

#-----------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Psi/Psi.py').read())
#-----------------------------------------------------

#=======================================================================

print(" ")
print("=============================================================")
print("= Edite o Plot das projecoes por meio dos seguintes arquivos ")
print("= Psi.py ou .agr (via Grace) gerados na pasta output/Psi ====")   
print("=============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
