# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

##############################################################################
# Analisando os arquivos scf.out, nscf.in, nscf.out, bands.in e filband_file #
###################### Buscando informacoes do Sistema #######################
##############################################################################

# -----------------------------------------------------------------------------
# Verificando a presença dos arquivos scf.out, nscf.in, nscf.out e bands.in ---
# -----------------------------------------------------------------------------

n_scf_o = 0

try:
    f = open(dir_files + '/scf.out')
    f.close()
    n_scf_o = 1
except:
    print('')
    print('... Arquivo scf.out ausente ...')

#-----------------------------------

n_nscf_i = 0

try:
    f = open(dir_files + '/nscf.in')
    f.close()
    n_nscf_i = 1
except:
    print('')
    print('... Arquivo nscf.in ausente ...')

#-----------------------------------

n_nscf_o = 0

try:
    f = open(dir_files + '/nscf.out')
    f.close()
    n_nscf_o = 1
except:
    print('')
    print('... Arquivo nscf.out ausente ...')

#-----------------------------------

n_bands_i = 0

try:
    f = open(dir_files + '/bands.in')
    f.close()
    n_bands_i = 1
except:
    print('')
    print('... Arquivo bands.in ausente ...')

#-----------------------------------
    
"""
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
   print('... Arquivo PROCAR ausente ...')

#-----------------------------------
"""

#-----------------------------------------------------------------------------------
# Control parameters for reading orbitals and spin components in the PROCAR file ---
#-----------------------------------------------------------------------------------
read_orb  = 0
read_spin = 0
read_reg  = 0
read_psi  = 0

if (n_scf_o == 0 or n_nscf_i == 0 or n_nscf_o == 0 or n_bands_i == 0):   
   print('')
   print('')
   print('---------------------------------------------------------------------------')
   print('Apos inserir os arquivos ausentes no diretorio, aperte ENTER para continuar')
   print('---------------------------------------------------------------------------')
   confirmacao = input (" "); confirmacao = str(confirmacao)

"""   
# ----------------------------------------------------------------------
# Verificando a presença e o nº de arquivos PROCAR a serem lidos: ------
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
"""

#-----------------------------------------------------------------------------------------------
# Parametros de controle para a leitura dos orbitais e componentes de spin no arquivo PROCAR ---
#-----------------------------------------------------------------------------------------------
read_orb  = 0
read_spin = 0

# Valor padrão de algumas tags ========================================
energ_tot_all_electron = 0.0
energ_tot = 0.0
Efermi = -1000.0
n_procar = 1  # ???????????????????????????????????????????????????????
lorbit = 10   # ???????????????????????????????????????????????????????
n_orb = 3     # Número de Orbitais ????????????????????????????????????
ispin = 1
SO = 1
LNC = 1

#======================================================================

#------------------------------------------
scf_out = open(dir_files + '/scf.out', "r")
#------------------------------------------

for i in range(20000):
    #---------------------------------
    VTemp = scf_out.readline().split()
    #---------------------------------
                          
    if (len(VTemp) == 6 and (VTemp[1] == 'Fermi' and VTemp[2] == 'energy')):
       Efermi = float(VTemp[4])     # Energia de Fermi do sistema

    if (len(VTemp) == 6 and (VTemp[1] == 'total' and VTemp[2] == 'energy')):
       energ_tot = float(VTemp[4])     # Energia total do sistema

    if (len(VTemp) == 6 and (VTemp[1] == 'all-electron' and VTemp[2] == 'energy')):
       energ_tot_all_electron = float(VTemp[4])     # Energia total de todos os elétrons do sistema

#--------------
scf_out.close()
#--------------

#======================================================================

#------------------------------------------
nscf_in = open(dir_files + '/nscf.in', "r")
#------------------------------------------

for i in range(10000):
    #----------------------------------------------------------------------------------
    VTemp = nscf_in.readline().replace('=', ' = ').replace(',', ' , ').replace("'", "")
    VTemp = VTemp.split()
    #--------------------
                          
    # if (len(VTemp) > 0 and VTemp[0] == 'nat'):
    #    ni = int(VTemp[2])     # Numero de ions da rede
                          
    # if (len(VTemp) > 0 and VTemp[0] == 'ntyp'):
    #    types = int(VTemp[2])  # Numero de diferentes tipos de ions da rede
                          
    if (len(VTemp) > 0 and VTemp[0] == 'nspin'):
       ispin = int(VTemp[2])  # Variavel que determina se o calculo é spin polarizado ou não
                          
    if (len(VTemp) > 0 and VTemp[0] == 'lspinorb'):
       VTemp[2] = VTemp[2].replace('.', '')
       if (VTemp[2][0] == 't' or VTemp[2][0] == 'T'):
          SO = 2              # Variavel que informa se o cálculo possui acoplamento spin-orbita ou não
          LNC = 2

#--------------
nscf_in.close()
#--------------

#======================================================================

#--------------------------------------------
nscf_out = open(dir_files + '/nscf.out', "r")
#--------------------------------------------
                                
for line in nscf_out:   
    if 'unit-cell' in line: 
       break

VTemp = nscf_out.readline().split()
ni = int(VTemp[4])            # Numero de ions da rede

VTemp = nscf_out.readline().split()
types = int(VTemp[5])         # Numero de diferentes tipos de ions da rede

VTemp = nscf_out.readline().split()
n_eletrons = float(VTemp[4])  # Numero de elétrons

VTemp = nscf_out.readline().split()
nb = int(VTemp[4])            # Numero de bandas
nb = nb*ispin # ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

#----------------------------------------------------------------------

test = 'null'

while (test != 'celldm(1)='):    
      VTemp = nscf_out.readline().split()
      if (len(VTemp) == 6):
         test = str(VTemp[0]) 

cell_1 = float(VTemp[1]); cell_2 = float(VTemp[3]); cell_3 = float(VTemp[5]) 

VTemp = nscf_out.readline().split()
cell_4 = float(VTemp[1]); cell_5 = float(VTemp[3]); cell_6 = float(VTemp[5])

Parametro = cell_1

VTemp = nscf_out.readline()
VTemp = nscf_out.readline()

A1 = nscf_out.readline().split()
A1x = float(A1[3]); A1y = float(A1[4]); A1z = float(A1[5])  # Leitura das coordenadas (X, Y, Z) do vetor primitivo (A1) da celula unitaria no espaco real

A2 = nscf_out.readline().split()
A2x = float(A2[3]); A2y = float(A2[4]); A2z = float(A2[5])  # Leitura das coordenadas (X, Y, Z) do vetor primitivo (A2) da celula unitaria no espaco real

A3 = nscf_out.readline().split()
A3x = float(A3[3]); A3y = float(A3[4]); A3z = float(A3[5])  # Leitura das coordenadas (X, Y, Z) do vetor primitivo (A3) da celula unitaria no espaco real

#----------------------------------------------------------------------

VTemp = nscf_out.readline()
VTemp = nscf_out.readline()

B1  = nscf_out.readline().split()
B1x = float(B1[3]); B1y = float(B1[4]); B1z = float(B1[5])  # Leitura das coordenadas (Kx, Ky, Kz) do vetor primitivo (B1) da 1º Zona de Brillouin no espaço recíproco

B2  = nscf_out.readline().split()
B2x = float(B2[3]); B2y = float(B2[4]); B2z = float(B2[5])  # Leitura das coordenadas (Kx, Ky, Kz) do vetor primitivo (B2) da 1º Zona de Brillouin no espaço recíproco

B3  = nscf_out.readline().split()
B3x = float(B3[3]); B3y = float(B3[4]); B3z = float(B3[5])  # Leitura das coordenadas (Kx, Ky, Kz) do vetor primitivo (B3) da 1º Zona de Brillouin no espaço recíproco

#----------------------------------------------------------------------  
                          
for line in nscf_out:   
    if 'site' in line: 
       break 

rotulo = [0]*(ni+1)
rotulo_temp = [0]*(ni+1)                              

for i in range(1,(ni+1)):
    VTemp = nscf_out.readline().split()
    rotulo[i] = VTemp[1]  # Obtenção dos rótulos para cada ion da rede

#----------------------------------------------------------------------  

test = 'null'

while (test == 'number'):
      #----------------------------------------------
      VTemp = nscf_out.readline().replace('=', ' = ')
      VTemp = VTemp.split()
      #--------------------
      if (len(VTemp) > 6):
         test = str(VTemp[0])
         nk = int(VTemp[5])

#---------------
nscf_out.close()
#---------------

#======================================================================

#-----------------------------------------
bands = open(dir_files + '/bands.in', "r")
#-----------------------------------------

test1 = 'null'
test2 = 'null'

while (test1 != 'prefix' or test2 != 'filband'): 
      #--------------------------------
      VTemp = bands.readline()
      VTemp = VTemp.replace('=', ' = ')
      VTemp = VTemp.replace(',', ' , ')
      VTemp = VTemp.replace("'", "")
      VTemp = VTemp.split()
      #--------------------------------------------
      if (len(VTemp) > 0 and VTemp[0] == 'prefix'):
         prefix = str(VTemp[2])
         test1 = VTemp[0]
      #---------------------------------------------
      if (len(VTemp) > 0 and VTemp[0] == 'filband'):
         filband = str(VTemp[2])
         test2 = VTemp[0]

#------------
bands.close()
#------------

#----------------------------------------------

try:
    f = open(dir_files + '/' + filband)
    f.close()
except:
    print('')
    print(f'... Arquivo {filband} ausente ...')
    print('')
    print('------------------------------------------------------------------')
    print('Apos inserir os arquivos no diretorio, aperte ENTER para continuar')
    print('------------------------------------------------------------------')
    confirmacao = input (" "); confirmacao = str(confirmacao)
   
#----------------------------------------------

#-------------------------------------------
bands = open(dir_files + '/' + filband, "r")
#-------------------------------------------

#--------------------------------
VTemp = bands.readline()
VTemp = VTemp.replace('=', ' = ')
VTemp = VTemp.replace(',', ' , ')
VTemp = VTemp.replace('/', ' / ')
VTemp = VTemp.split()
#--------------------------------

nb = int(VTemp[3])  # Numero de bandas
nb = nb*ispin       # ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
nk = int(VTemp[7])  # Numero de pontos-k 

#------------
bands.close()
#------------

#======================================================================

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

inform.write("------------------------------------------------------ \n")

if (SO == 1):
   inform.write("LSORBIT = .FALSE. (Calculo sem acoplamento SO) \n")
if (SO == 2):
   inform.write("LSORBIT = .TRUE. (Calculo com acoplamento SO) \n")

inform.write("------------------------------------------------------ \n")

# if (n_procar == 1): inform.write(f'nº Pontos-k = {nk};  nº Bandas = {nb} \n')
# if (n_procar > 1):  inform.write(f'nº Pontos-k = {nk*n_procar} (nº PROCARs = {n_procar});  nº Bandas = {nb} \n')   

inform.write(f'nº Pontos-k = {nk};  nº Bandas = {nb} \n')
inform.write(f'nº ions = {ni};  nº eletrons = {n_eletrons} \n')

inform.write("----------------------------------------------------- \n")
inform.write(f'ISPIN = {ispin} ')
if (ispin == 1): inform.write("(sem polarizacao de spin) \n")
if (ispin == 4): inform.write("(com polarizacao de spin) \n")
inform.write("----------------------------------------------------- \n")

if (Efermi != -1000.0):
   inform.write(f'Energia de fermi = {Efermi} eV \n')
   inform.write("----------------------------------------------------- \n")

#------------------------------------------------------------------------------
# inform.write(f'Ultima Banda ocupada = {n1_valencia} \n')
# inform.write(f'Primeira Banda vazia = {n1_conducao} \n')
# if (kp1 == kp2):
#    inform.write(f'GAP (direto) = {GAP:.4f} eV  -  Kpoint {kp1} \n')
# if (kp1 != kp2):
# inform.write(f'GAP (indireto) = {GAP:.4f} eV  //  Kpoints {kp1} e {kp2} \n')
# inform.write("---------------------------------------------------- \n")
#------------------------------------------------------------------------------

if (energ_tot_all_electron != 0.0):
   inform.write(f'total all-electron energy = {(energ_tot_all_electron/13.605684958731):.6f} eV ({(energ_tot_all_electron):.6f} Ry) \n')
if (energ_tot != 0.0):
   inform.write(f'total energy = {(energ_tot/13.605684958731):.6f} eV  ({(energ_tot):.6f} Ry) \n')
inform.write("----------------------------------------------------- \n")

# inform.write(" \n")
# inform.write("################# Magnetizacao: ##################### \n")
# inform.write(f'Eixo X:  total = {mag_tot_x:.4f} \n')
# inform.write(f'Eixo Y:  total = {mag_tot_y:.4f} \n')
# inform.write(f'Eixo Z:  total = {mag_tot_z:.4f} \n')
# inform.write("##################################################### \n")

#-----------------------------------------------------------------------

inform.write(" \n")
inform.write("***************************************************** \n")
inform.write("Vetores Primitivos da Rede Cristalina *************** \n")
inform.write(f'A1 = Param.({(A1x):12.9f}, {(A1y):12.9f}, {(A1z):12.9f}) \n')
inform.write(f'A2 = Param.({(A2x):12.9f}, {(A2y):12.9f}, {(A2z):12.9f}) \n')
inform.write(f'A3 = Param.({(A3x):12.9f}, {(A3y):12.9f}, {(A3z):12.9f}) \n')
inform.write(f'Param. = {(Parametro/1.8897259886):.6f} Angs.  ({Parametro} Bohr|a.u.) \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#-----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("Vetores Primitivos da Rede Reciproca **************** \n")
inform.write(f'B1 = 2pi/Param.({(B1x):11.8f}, {(B1y):11.8f}, {(B1z):11.8f}) \n')
inform.write(f'B2 = 2pi/Param.({(B2x):11.8f}, {(B2y):11.8f}, {(B2z):11.8f}) \n')
inform.write(f'B3 = 2pi/Param.({(B3x):11.8f}, {(B3y):11.8f}, {(B3z):11.8f}) \n')
inform.write(f'Param. = {(Parametro/1.8897259886):.6f} Angs.  ({Parametro} Bohr|a.u.) \n')
inform.write("***************************************************** \n")
inform.write(" \n")


#-----------------------------------------------------------------------

#-------------
inform.close()
#-------------

""" 
if (ispin == 1):
    
   #-----------------------------------------------------------------------
   # Verificando de quais bandas correspondem as bandas de valencia e -----
   # conducao, bem como do respectivo GAP de energia ----------------------
   # ----------------------------------------------------------------------
   # Esta verificacao somente faz sentido para calculos realizados em um --
   # unico passo (n_procar = 1), visto que o arquivo OUTCAR analisado ----- 
   # pode ou nao conter a regiao de menor GAP do sistema ------------------
   # ----------------------------------------------------------------------
   # Esta verificacao tambem nao faz sentido para sistemas metalicos ------
   #-----------------------------------------------------------------------

   VTemp = outcar.readline(); VTemp = outcar.readline()

   menor_n2 = -1000.0
   maior_n2 = +1000.0
   number = 0

   for i in range(nk):
       number += 1
    
       VTemp = outcar.readline()
       VTemp = outcar.readline()
       for j in range(nb):
           VTemp = outcar.readline().split()
           n1 = int(VTemp[0])
           n2 = float(VTemp[1])
           n3 = float(VTemp[2])
           if (n3 > 0.0):
              if (n2 > menor_n2):
                 menor_n2 = n2
                 n1_valencia = n1
                 kp1 = number
           if (n3 == 0.0):
              if (n2 < maior_n2):
                 maior_n2 = n2
                 n1_conducao = n1
                 kp2 = number
           GAP = (maior_n2 - menor_n2)
       VTemp = outcar.readline() 

   if (n_procar == 1):
      inform.write(f'Ultima Banda ocupada = {n1_valencia} \n')
      inform.write(f'Primeira Banda vazia = {n1_conducao} \n')

      if (kp1 == kp2):
         inform.write(f'GAP (direto) = {GAP:.4f} eV  -  Kpoint {kp1} \n')
      if (kp1 != kp2):
         inform.write(f'GAP (indireto) = {GAP:.4f} eV  //  Kpoints {kp1} e {kp2} \n')

      inform.write("---------------------------------------------------- \n")

#=======================================================================

if (ispin == 1):

   #-----------------------------------------------------------------------
   # Buscando os valores de Magnetizacao: ---------------------------------
   #-----------------------------------------------------------------------

   if (SO == 2):
      temp_xk = 4 + ni

   #------------------------- Magentizacao (X): ---------------------------

      palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
      number = 0 

      for line in outcar:
          number += 1
     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()

      VTemp = outcar.readline().split()
      mag_s_x = float(VTemp[1])
      mag_p_x = float(VTemp[2])
      mag_d_x = float(VTemp[3])
      mag_tot_x = float(VTemp[4])

   #------------------------- Magentizacao (y): ---------------------------

      palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
      number = 0 

      for line in outcar:
          number += 1
     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()

      VTemp = outcar.readline().split()
      mag_s_y = float(VTemp[1])
      mag_p_y = float(VTemp[2])
      mag_d_y = float(VTemp[3])
      mag_tot_y = float(VTemp[4])

   #------------------------- Magentizacao (z): ---------------------------

      palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
      number = 0 

      for line in outcar:
          number += 1
     
          if palavra in line: 
             break

      for i in range(temp_xk):
          VTemp = outcar.readline()

      VTemp = outcar.readline().split()
      mag_s_z = float(VTemp[1])
      mag_p_z = float(VTemp[2])
      mag_d_z = float(VTemp[3])
      mag_tot_z = float(VTemp[4])
   
   #-----------------------------------------------------------------------

      inform.write(" \n")
      inform.write("################# Magnetizacao: ##################### \n")
      inform.write(f'Eixo X:  total = {mag_tot_x:.4f} \n')
      inform.write(f'Eixo Y:  total = {mag_tot_y:.4f} \n')
      inform.write(f'Eixo Z:  total = {mag_tot_z:.4f} \n')
      inform.write("##################################################### \n")

#-------------
outcar.close()
#-------------
"""
