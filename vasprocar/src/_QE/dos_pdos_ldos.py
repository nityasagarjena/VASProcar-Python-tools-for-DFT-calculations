# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'DOS' exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/DOS'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/DOS')
#-------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("################### Densidade de Estados: ####################")
print ("##############################################################") 
print (" ")

if (escolha == -1):

   print ("##############################################################") 
   print ("Deseja alterar o padrao de cores da DOS|lDOS|pDOS?            ")
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
      print ("DOS_total|lDOS:  7 13  (Grey, Maroon)                         ")
      print ("--------------------------------------------------------------")  
      print ("pDOS S|P|D:  4 2 3  (Blue, Red, Green)                        ")
      print ("--------------------------------------------------------------")      
      print ("pDOS Px|Py|Pz:  4 2 3  (Blue, Red, Green)                     ")
      print ("--------------------------------------------------------------") 
      print ("pDOS Dxy|Dyz|Dz2|Dxz|Dx2: 4 2 3 10 9                          ")
      print ("(Blue, Red, Green, Magenta, Cyan)                             ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Digite em sequencia as cores da DOS_total e da lDOS:          ")
      cor_orb = input ("Cores_DOS|lDOS: ")
      #---------------------
      tcor = cor_orb.split()
      c_DOS = int(tcor[0]); c_lDOS = int(tcor[1])
      #---------------------
      print (" ")

      print ("==============================================================") 
      print ("Digite em sequencia as cores das pdOS S|P|D:                  ")
      cor_orb = input ("Cores_pdOS_S|P|D: ")
      #---------------------
      tcor = cor_orb.split()
      c_S = int(tcor[0]); c_P = int(tcor[1]); c_D = int(tcor[2])
      #---------------------
      print (" ")
      
      if (lorbit >= 11):
         print ("==============================================================") 
         print ("Digite em sequencia as cores das pdOS Px|Py|Pz:               ")
         cor_orb = input ("Cores_pdOS_Px|Py|Pz: ")
         #---------------------
         tcor = cor_orb.split()
         c_Px = int(tcor[0]); c_Py = int(tcor[1]); c_Pz = int(tcor[2])
         #---------------------
         print (" ")
         
         print ("==============================================================") 
         print ("Digite em sequencia as cores das pDOS Dxy|Dyz|Dz2|Dxz|Dx2:    ")
         cor_orb = input ("Cores_pDOS_Dxy|Dyz|Dz2|Dxz|Dx2: ")
         #---------------------
         tcor = cor_orb.split()
         c_Dxy = int(tcor[0]); c_Dyz = int(tcor[1]); c_Dz2 = int(tcor[2]); c_Dxz = int(tcor[3]); c_Dx2 = int(tcor[4])
         #---------------------
         print (" ") 

   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")    

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

   if (esc == 1):
      
      #-------------------------
      sim_nao = ["nao"]*(ni + 1)
      #-------------------------

      print ("##############################################################")
      print ("Escolha os intervalos_de_ions a serem analisados: =========== ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("A ordem em que os ions são adicionados, nao altera o resultado")
      print ("--------------------------------------------------------------")
      print ("intervalos_de_ions: 1:5 7:7 11:11 15:27                       ")          
      print ("intervalos_de_ions: 7:49 50:53                                ")
      print ("intervalos_de_ions: 3:3                                       ")
      print ("##############################################################")
      ion_range = input ("intervalo_de_ions: ")
      print (" ")
      #--------------------------------------------------
      selected_ions = ion_range.replace(':', ' ').split()
      loop = int(len(selected_ions)/2)
      #--------------------------------------------------
      
      for i in range (1,(loop+1)):
          #----------------------------------------
          loop_i = int(selected_ions[(i-1)*2])
          loop_f = int(selected_ions[((i-1)*2) +1])
          #----------------------------------------------------------------------
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
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

if (escolha == 1):
   esc_fermi = 1  
   esc = 0 

#----------------------------------------------------------------------
# Obtenção dos nomes dos arquivos que contem a DOS, lDOs e pDOs -------
#----------------------------------------------------------------------

#--------------------------------------------
projwfc = open(dir_files + '/projwfc.in', "r")
#--------------------------------------------

for i in range(1000):
    VTemp = projwfc.readline()
    VTemp = VTemp.replace('=', ' = ')
    VTemp = VTemp.replace(',', ' , ')
    VTemp = VTemp.replace("'", "")
    VTemp = VTemp.split()
    if (len(VTemp) > 0 and VTemp[0] == 'filpdos'):
       filpdos = VTemp[2] 

#--------------
projwfc.close()
#--------------

#----------------------------------------------------------------------

#---------------------------------------------
projwfc = open(dir_files + '/projwfc.out', "r")
#---------------------------------------------

palavra = 'Problem'       
                           
for line in projwfc:   
    if palavra in line: 
       break

VTemp = projwfc.readline().split()
n_wfc = int(VTemp[2])

name_file = ['a']*(n_wfc+1)

for i in range(9):
    VTemp = projwfc.readline()

for i in range(1,(n_wfc+1)):
    #---------------------------------
    VTemp = projwfc.readline()
    VTemp = VTemp.replace('#', ' # ')
    VTemp = VTemp.replace('=', ' = ')
    VTemp = VTemp.replace(':', ' : ')
    VTemp = VTemp.replace('(', ' ( ')
    VTemp = VTemp.replace(')', ' ) ')    
    VTemp = VTemp.split()
    #----------------------------------
    n_ion = str(VTemp[5])
    r_ion = str(VTemp[7])
    wfc   = str(VTemp[11])
    n_l   = int(VTemp[15])
    if (SO == 2):  n_j = str(VTemp[18])
    #----------------------------------
    if (n_l == 0): n_l = 's'
    if (n_l == 1): n_l = 'p'
    if (n_l == 2): n_l = 'd'
    #----------------------------------
    
    if (SO == 1):
       name_file[i] = filpdos + '.pdos_atm#' + n_ion + '(' + r_ion + ')_wfc#' + wfc + '(' + n_l + ')'
          
    if (SO == 2):
       name_file[i] = filpdos + '.pdos_atm#' + n_ion + '(' + r_ion + ')_wfc#' + wfc + '(' + n_l + '_j' + n_j + ')'

#--------------
projwfc.close()
#--------------

#----------------------------------------------------------------------

new_name = []

for i in range(1,(n_wfc+1)):
    if (i == 1):
       new_name.append(name_file[i])
    if (i != 1):
       if (name_file[i] != name_file[i-1]):
          new_name.append(name_file[i])

ion = [0]*(len(new_name) +1)
orb = [0]*(len(new_name) +1)

#----------------------------------------------------------------------

print ("Arquivos identificados =======================================")

for i in range(1,(len(new_name)+1)):
    name = new_name[i-1]
    name = name.replace('#', ' # ')
    name = name.replace('(', ' ( ')  
    name = name.replace(')', ' ) ') 
    name = name.replace('_', ' _ ')
    name = name.split()
    ion[i] = int(name[4])
    orb[i] = str(name[13])
    print (f'{new_name[i-1]}:  ion_{ion[i]} - orbital_{orb[i]}')

print ("==============================================================")

#----------------------------------------------------------------------
# Verificando a presença ou não dos arquivos acima listados -----------
#----------------------------------------------------------------------

n_file = 0

for i in range(1,(len(new_name)+1)):
    name = new_name[i-1]
  
    try:
        f = open(dir_files + '/' + name)
        f.close()
        n_file = 1
    except:
        print('')
        print(f'... Arquivo {name} ausente ...')

if (n_file == 0):   
   print('')
   print('')
   print('---------------------------------------------------------------------------')
   print('Apos inserir os arquivos ausentes no diretorio, aperte ENTER para continuar')
   print('---------------------------------------------------------------------------')
   confirmacao = input (" "); confirmacao = str(confirmacao)

print ("")
print ("Analisando os arquivos ... ===================================")
print ("")

#----------------------------------------------------------------------
# Obtendo o numero de valores de energia (NEDOS) presente na DOS ------
#----------------------------------------------------------------------

#--------------------------------------------------------
dos_files = open(dir_files + '/' + str(new_name[0]), "r")
#--------------------------------------------------------

VTemp = dos_files.readline().split()

if (VTemp[1] == 'ik'):
   kresolveddos = 'True'
   passo = nk
if (VTemp[1] != 'ik'):
   kresolveddos = 'False'
   passo = 1

energia = []
energia.append(-1000.0)
number = 0
                           
while number < 1:
      VTemp = dos_files.readline().split()
      if (len(VTemp) == 0):
         number += 1
      if (len(VTemp) > 0):
         if (kresolveddos == 'True'): 
            energia.append(float(VTemp[1]))
         if (kresolveddos == 'False'): 
            energia.append(float(VTemp[0]))
            
energia[0] = energia[1]
NEDOS = len(energia) -1
E_min = min(energia)
E_max = max(energia)

#----------------
dos_files.close()
#----------------

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------   

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

dos_tot  = [0]*(NEDOS+1)  # DOS Total
ldos     = [0]*(NEDOS+1)  # DOS Local
lpdos    = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]  # DOS Local e Projetada
dos_data = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]  # Conjunto de dados da DOS, lDOS e pDOS

pdos_S_tot = [0]*(NEDOS+1)  # pdos_S Total
pdos_P_tot = [0]*(NEDOS+1)  # pdos_P Total
pdos_D_tot = [0]*(NEDOS+1)  # pdos_D Total
lpdos_S    = [0]*(NEDOS+1)  # Local pdos_S
lpdos_P    = [0]*(NEDOS+1)  # Local pdos_P
lpdos_D    = [0]*(NEDOS+1)  # Local pdos_D

lpdos_tot = [[0]*(NEDOS+1) for i in range(n_orb+1)]  # Local pdos Total

y_inicial = E_min
y_final   = E_max

x_inicial = +1000.0
x_final   = -1000.0

#----------------------------------------------------------------------
# Extraindo os resultados dos arquivos DOS_files ----------------------
#----------------------------------------------------------------------

for i in range(1,(len(new_name)+1)):

    t_ion = ion[i]

    if (orb[i] == 's'): t_orb = 1
    if (orb[i] == 'p'): t_orb = 2
    if (orb[i] == 'd'): t_orb = 3
           
    #----------------------------------------------------------
    dos_files = open(dir_files + '/' + str(new_name[i-1]), "r")
    #----------------------------------------------------------

    VTemp = dos_files.readline()

    for point_k in range (passo):
        for j in range (NEDOS+1):
            VTemp = dos_files.readline().split()
            if (len(VTemp) > 0):
               if (kresolveddos == 'True'): 
                  dos_data[t_orb][t_ion][j] = dos_data[t_orb][t_ion][j] + float(VTemp[2])
               if (kresolveddos == 'False'): 
                  dos_data[t_orb][t_ion][j] = dos_data[t_orb][t_ion][j] + float(VTemp[1])
                  
    #----------------
    dos_files.close()
    #----------------

    print (f'Processado {i}/{len(new_name)} arquivos ...')

#----------------------------------------------------------------------

for i in range (1,(ni+1)):
    if (esc == 1): temp_sn = sim_nao[i]
    #----------------------------
    for j in range (1,(NEDOS+1)):
        for k in range(1,(n_orb+1)):
            if (esc == 0 or (esc == 1 and temp_sn == "sim")):
               lpdos[k][i][j] = dos_data[k][i][j]
               
               lpdos_tot[k][j] = lpdos_tot[k][j] + lpdos[k][i][j]
               ldos[j] = ldos[j] + lpdos[k][i][j]

               if (k == 1):
                  lpdos_S[j] = lpdos_S[j] + lpdos[k][i][j]
               #------------------------------------------   
               if (lorbit == 10 and k == 2):
                  lpdos_P[j] = lpdos_P[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit == 10 and k == 3):
                  lpdos_D[j] = lpdos_D[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
                  lpdos_P[j] = lpdos_P[j] + lpdos[k][i][j]
               #------------------------------------------                   
               if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
                  lpdos_D[j] = lpdos_D[j] + lpdos[k][i][j]           
            
            dos_tot[j] = dos_tot[j] + dos_data[k][i][j]                     

            if (k == 1):
               pdos_S_tot[j] = pdos_S_tot[j] + dos_data[k][i][j]
            #---------------------------------------------------                
            if (lorbit == 10 and k == 2):
               pdos_P_tot[j] = pdos_P_tot[j] + dos_data[k][i][j]
            #---------------------------------------------------                
            if (lorbit == 10 and k == 3):
               pdos_D_tot[j] = pdos_D_tot[j] + dos_data[k][i][j]
            #---------------------------------------------------                
            if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
               pdos_P_tot[j] = pdos_P_tot[j] + dos_data[k][i][j]
            #---------------------------------------------------                
            if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
               pdos_D_tot[j] = pdos_D_tot[j] + dos_data[k][i][j]

    if (dos_tot[k] <= x_inicial): x_inicial = dos_tot[k]
    if (dos_tot[k] >= x_final):   x_final   = dos_tot[k] 

#======================================================================
# Gravando as informações para o Plot da DOS, pDOS e lDOS =============
#======================================================================

#---------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.dat', 'w')
#---------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #-------------
    if (esc == 0):
       dos_pdos_ldos.write(f'{energia[k]} {dos_tot[k]} 0.0')
       dos_pdos_ldos.write(f' {pdos_S_tot[k]} 0.0 {pdos_P_tot[k]} 0.0 {pdos_D_tot[k]} 0.0')
    if (esc == 1):
       dos_pdos_ldos.write(f'{energia[k]} {dos_tot[k]} {ldos[k]}')
       dos_pdos_ldos.write(f' {pdos_S_tot[k]} {lpdos_S[k]} {pdos_P_tot[k]} {lpdos_P[k]} {pdos_D_tot[k]} {lpdos_D[k]}')
    if (lorbit > 10):
       dos_pdos_ldos.write(f' {lpdos_tot[4][k]} {lpdos_tot[2][k]} {lpdos_tot[3][k]}')
       dos_pdos_ldos.write(f' {lpdos_tot[5][k]} {lpdos_tot[6][k]} {lpdos_tot[7][k]} {lpdos_tot[8][k]} {lpdos_tot[9][k]}')
    dos_pdos_ldos.write(f' \n')      

#--------------------
dos_pdos_ldos.close()
#--------------------

#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (GRACE) ===============================================
#==================================================================================== 
#====================================================================================

if (save_agr == 1):

   print(" ")
   print ("============= Plotando a DOS, pDOS, lDOS (Grace): =============")
   
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos.py')

   print ("Plot da DOS, pDOS, lDOS via Grace (arquivos .agr) concluido ---")

#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (Matplotlib) ==========================================
#==================================================================================== 
#====================================================================================

#------------------------------------------------------------------------
# Copy DOS_pDOS_lDOS.py to the output folder directory ------------------
#------------------------------------------------------------------------

try: f = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py'); f.close(); os.remove(dir_files + '/output/DOS/DOS_pDOS_lDOS.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_dos_pdos_ldos.py'
destination = dir_files + '/output/DOS/DOS_pDOS_lDOS.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'r')
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
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; x_inicial = {x_inicial}; x_final = {x_final}; energ_min = {y_inicial}; energ_max = {y_final}; lorbit = {lorbit}; esc = {esc} \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout file \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                       
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#======================================================================== \n')
linha += 1; lines.insert(linha, '# Codigo de cores:                                                        \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Cores aplicadas a DOS|lDOS|pDOS:                                        \n')
linha += 1; lines.insert(linha, f'c_DOS = {c_DOS}; c_lDOS = {c_lDOS}; c_S = {c_S}; c_P = {c_P}; c_D = {c_D} \n')
if (lorbit >= 11):
   linha += 1; lines.insert(linha, f'c_Px = {c_Px}; c_Py = {c_Py}; c_Pz = {c_Pz} \n')
   linha += 1; lines.insert(linha, f'c_Dxy = {c_Dxy}; c_Dyz = {c_Dyz}; c_Dz2 = {c_Dz2}; c_Dxz = {c_Dxz}; c_Dx2 = {c_Dx2} \n')    
linha += 1; lines.insert(linha, '#======================================================================== \n')

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py').read())
#---------------------------------------------------------------

#=======================================================================

print(" ")
print("================================================================")
print("= Edite o Plot da DOS por meio dos arquivos DOS_pDOS_lDOS.py ou ")
print("= .agr (via Grace) gerados na pasta output/DOS =================")   
print("================================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
