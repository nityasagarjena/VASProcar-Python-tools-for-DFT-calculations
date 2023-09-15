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
      print ("intervalos_de_ions: 1-5 3-9 11-11 15-27                       ")          
      print ("intervalos_de_ions: 7-49 50-53                                ")
      print ("intervalos_de_ions: 3-3                                       ")
      print ("##############################################################")
      ion_range = input ("intervalo_de_ions: ")
      print (" ")
      #--------------------------------------------------
      selected_ions = ion_range.replace('-', ' ').split()
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

#---------------------------------------------
projwfc = open(dir_files + '/projwfc.in', "r")
#---------------------------------------------

filpdos = 'a'
filproj = 'a'

for i in range(1000):
    #----------------------------------------------------------------------------------
    VTemp = projwfc.readline().replace('=', ' = ').replace(',', ' , ').replace("'", "")
    VTemp = VTemp.split()
    #--------------------
    if (len(VTemp) >= 3):
       if (VTemp[0] == 'prefix'):  prefix  = str(VTemp[2])
       if (VTemp[0] == 'filpdos'): filpdos = str(VTemp[2])
       if (VTemp[0] == 'filproj'): filproj = str(VTemp[2])

#--------------
projwfc.close()
#--------------

if (filpdos == 'a'): filpdos = prefix
if (filproj == 'a'): filproj = prefix

#===================================================================

#----------------------------------------------
projwfc = open(dir_files + '/projwfc.out', "r")
#----------------------------------------------

test = 'null' 

while (test != 'Calling'):             
      #---------------------------------
      VTemp = projwfc.readline().split()
      if (len(VTemp) > 0): test = str(VTemp[0])
      #----------------------------------------

for ii in range(4):
    VTemp = projwfc.readline()

test = 'state'

n_wfc = 0

while (test == 'state'):             
      #-------------------------
      VTemp = projwfc.readline().replace(":", " : ").replace("(", " ( ").replace(")", " ) ")
      VTemp = VTemp.split()
      if (len(VTemp) > 0):
         test = str(VTemp[0])
         if (test == 'state'):
            n_wfc += 1
      if (len(VTemp) == 0):
         test = 'null'
      #--------------------

projwfc.close()

#===================================================================

#----------------------------------------------
projwfc = open(dir_files + '/projwfc.out', "r")
#----------------------------------------------

palavra = 'Atomic'       
                         
for line in projwfc:   
    if palavra in line: 
       break

VTemp = projwfc.readline()
VTemp = projwfc.readline()

name_file = ['a']*(n_wfc+1)

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
    n_l   = int(VTemp[18])
    if (SO == 2):  n_j = str(VTemp[15])
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

#----------------------------------------------------------------------
# Obtendo o numero de valores de energia (NEDOS) presente na DOS ------
#----------------------------------------------------------------------

#--------------------------------------------------------
dos_files = open(dir_files + '/' + str(new_name[0]), "r")
#--------------------------------------------------------

VTemp = dos_files.readline()

energia = []
energia.append(-1000.0)
number = 0
                           
while number < 1:
      VTemp = dos_files.readline().split()
      if (len(VTemp) == 0):
         number += 1
      if (len(VTemp) > 0):
         energia.append(float(VTemp[1]))

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

dos     = [0]*(NEDOS+1)  #  dos[NEDOS]
l_dos   = [0]*(NEDOS+1)  #  l_dos[NEDOS]

pdos     = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]   # pdos[9][ni][NEDOS]
pdos_tot = [[0]*(NEDOS+1) for i in range(n_orb+1)]                          # pdos_tot[9][NEDOS]

# pdos[1][ni][NEDOS] = Orbital S    //  pdos_tot[1][ni][NEDOS] = Orbital S total
# pdos[2][ni][NEDOS] = Orbital Py   //  pdos_tot[2][ni][NEDOS] = Orbital Py total
# pdos[3][ni][NEDOS] = Orbital Pz   //  pdos_tot[3][ni][NEDOS] = Orbital Pz total
# pdos[4][ni][NEDOS] = Orbital Px   //  pdos_tot[4][ni][NEDOS] = Orbital Px total
# pdos[5][ni][NEDOS] = Orbital Dxy  //  pdos_tot[5][ni][NEDOS] = Orbital Dxy total
# pdos[6][ni][NEDOS] = Orbital Dyz  //  pdos_tot[6][ni][NEDOS] = Orbital Dyz total
# pdos[7][ni][NEDOS] = Orbital Dz2  //  pdos_tot[7][ni][NEDOS] = Orbital Dz2 total
# pdos[8][ni][NEDOS] = Orbital Dxz  //  pdos_tot[8][ni][NEDOS] = Orbital Dxz total
# pdos[9][ni][NEDOS] = Orbital Dx2  //  pdos_tot[9][ni][NEDOS] = Orbital Dx2 total

pdos_P     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_P[ni][NEDOS]
pdos_D     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_D[ni][NEDOS]
pdos_P_tot = [0]*(NEDOS+1)                          # pdos_P_tot[NEDOS]
pdos_D_tot = [0]*(NEDOS+1)                          # pdos_D_tot[NEDOS]

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

    for point_k in range (1,(nk+1)):
        for j in range (NEDOS+1):
            VTemp = dos_files.readline().split()
            if (len(VTemp) > 0):
               pdos[t_orb][t_ion][j] = float(VTemp[2])

    #----------------
    dos_files.close()
    #----------------

#----------------------------------------------------------------------

for t_ion in range (1,(ni+1)):
    if (esc == 1): temp_sn = sim_nao[t_ion]
    #------------------------
    for j in range (1,(NEDOS+1)):
        for t_orb in range(1,(n_orb+1)):
            if (esc == 0 or (esc == 1 and temp_sn == "sim")):
               #---------------------------------------------------------------------------
               if (t_orb == 2): pdos_P[t_ion][j] = pdos_P[t_ion][j] + pdos[t_orb][t_ion][j]
               if (t_orb == 3): pdos_D[t_ion][j] = pdos_D[t_ion][j] + pdos[t_orb][t_ion][j]           
               #---------------------------------------------------------------------------
               pdos_tot[t_orb][j] = pdos_tot[t_orb][j] + pdos[t_orb][t_ion][j]
               l_dos[j] = l_dos[j] + pdos[t_orb][t_ion][j]
               
            dos[j] = dos[j] + pdos[t_orb][t_ion][j]
            if (dos[j] <= x_inicial): x_inicial = dos[j]
            if (dos[j] >= x_final):   x_final   = dos[j]
            
        pdos_P_tot[j] = pdos_P_tot[j] + pdos_P[t_ion][j]

#======================================================================
# Gravando as informações para o Plot da DOS, pDOS e lDOS =============
#======================================================================

#---------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.dat', 'w')
#---------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #---------------------------------------------------------------------------
    if (esc == 0): dos_pdos_ldos.write(f'{energia[k]} {dos[k]} 0.0')
    if (esc == 1): dos_pdos_ldos.write(f'{energia[k]} {dos[k]} {l_dos[k]}')
    dos_pdos_ldos.write(f' {pdos_tot[1][k]} {pdos_P_tot[k]} {pdos_D_tot[k]}')
    if (lorbit > 10): dos_pdos_ldos.write(f' {pdos_tot[4][k]} {pdos_tot[2][k]} {pdos_tot[3][k]} {pdos_tot[5][k]} {pdos_tot[6][k]} {pdos_tot[7][k]} {pdos_tot[8][k]} {pdos_tot[9][k]}')
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
   execute_python_file(filename = '_QE/dos_plot/Grace/plot_dos_pdos_ldos.py')

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
   
source = main_dir + '_QE/dos_plot/plot_dos_pdos_ldos.py'
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
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                       
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------
exec(open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py').read())
#------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
