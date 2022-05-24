
#######################################################
########## Analisando o arquivo OUTCAR ################
######## Buscando informacoes do Sistema ##############
#######################################################

#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r")
#--------------------------------------------------------
inform = open(dir_files + '/output/informacoes.txt', "w")
#--------------------------------------------------------

#----------------------------------------------------------------------
# Obtenção do nº de pontos-k (nk), bandas (nb) e ions (ni): -----------
#----------------------------------------------------------------------

palavra = 'Dimension'                          # Dimension e uma palavra presente em uma linha anterior as linhas que contem a informacao sobre o número de pontos-k (nk), bandas (nb) e ions (ni).

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
nk = int(VTemp[3])
nb = int(VTemp[14])

VTemp = outcar.readline().split()
ni = int(VTemp[11])

#-----------------------------------------------------------------------
# Verificacao se o calculo foi realizado com ou sem o acoplamento SO: --
#-----------------------------------------------------------------------

palavra = 'ICHARG'                             # ICHARG e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel ISPIN.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
ispin = int(VTemp[2])                          # Leitura do valor associado a variavel ISPIN.

#------------
nb = nb*ispin
#------------
  
#-----------------------------------------------------------------------

palavra = 'LNONCOLLINEAR'                      # LNONCOLLINEAR e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel LSORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lsorbit = VTemp[2]                             # Leitura do valor associado a variavel LSORBIT.

inform.write("---------------------------------------------------- \n")

if (lsorbit == "F"):
   SO = 1
   inform.write("LSORBIT = .FALSE. (Calculo sem acoplamento SO) \n")
if (lsorbit == "T"):
   SO = 2
   inform.write("LSORBIT = .TRUE. (Calculo com acoplamento SO) \n")

#-----------------------------------------------------------------------
# Obtenção do número de eletrons do sistema: ---------------------------
#---------------------------------------------------------------------- 
 
palavra = 'VCA'                                       # VCA e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel NELECT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
n_eletrons = float(VTemp[2])                          # Leitura do valor associado a variavel NELECT.

inform.write("---------------------------------------------------- \n")

if (n_procar == 1):
   inform.write(f'nº Pontos-k = {nk};  nº Bandas = {nb} \n')
if (n_procar > 1):
   inform.write(f'nº Pontos-k = {nk*n_procar} (nº PROCARs = {n_procar});  nº Bandas = {nb} \n')   

inform.write(f'nº ions = {ni};  nº eletrons = {n_eletrons} \n')

#-----------------------------------------------------------------------
# Obtenção do LORBIT utilizado para a geracao do arquivo PROCAR: -------
#-----------------------------------------------------------------------
 
palavra = 'LELF'                                    # LELF e uma palavra presenta em uma linha anterior a linha que contem a informacao sobre a variavel LORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lorbit = int(VTemp[2])                              # Leitura do valor associado a variavel LORBIT.

inform.write("--------------------------------------------------- \n")
inform.write(f'LORBIT = {lorbit};  ISPIN = {ispin} ')
if (ispin == 1): inform.write("(sem polarizacao de spin) \n")
if (ispin == 2): inform.write("(com polarizacao de spin) \n")
inform.write("--------------------------------------------------- \n")

#-------------
outcar.close()
#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r") 
#----------------------------------------

#-----------------------------------------------------------------------
# Busca da Energia de Fermi do sistema: --------------------------------
#-----------------------------------------------------------------------

palavra = 'average'                            # average e uma palavra presente em uma linha um pouco anterior a linha que contem a informacao sobre a variavel E-fermi.
number = 0                                     # number representa qual linha contem a informacao sobre a variavel E-fermi.

for line in outcar:
    number += 1
     
    if palavra in line: 
       break

palavra = 'E-fermi'

for line in outcar:
    number += 1
     
    if palavra in line: 
       break

#-------------
outcar.close()
#----------------------------------------
outcar = open(dir_files + '/OUTCAR', "r") 
#----------------------------------------

for i in range(number):
    VTemp = outcar.readline().split()

Efermi = float(VTemp[2])                              # Leitura do valor associado a variavel E-fermi.

inform.write(f'Energia de fermi = {Efermi} eV \n')
inform.write("--------------------------------------------------- \n")

#==========================================================================

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

#-----------------------------------------------------------------------
# Busca da Energia total do sistema: -----------------------------------
#-----------------------------------------------------------------------

palavra = 'FREE'                               # FREE e uma palavra presente em uma linha que fica quatro linhas anteriores a linha que contem a informacao sobre a variavel (free energy TOTEN).
number = 0                                     # number representa qual linha contem a informacao sobre a variavel (free energy TOTEN).

for line in outcar:
    number += 1
     
    if palavra in line: 
       break

for i in range(3):
    VTemp = outcar.readline()
    
VTemp = outcar.readline().split()
energ_tot = float(VTemp[3])                    # Leitura do valor associado a variavel NELECT.

inform.write(f'free energy TOTEN = {energ_tot} eV \n')
inform.write("--------------------------------------------------- \n")

#==========================================================================

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

#######################################################################
##################### Leitura do Arquivo CONTCAR ######################
#######################################################################
 
#------------------------------------------
contcar = open(dir_files + '/CONTCAR', "r")
#------------------------------------------

VTemp = contcar.readline().split()
VTemp = contcar.readline().split()

Parametro = float(VTemp[0])                                 # Leitura do Parametro de rede do sistema.

A1 = contcar.readline().split()
A1x = float(A1[0]); A1y = float(A1[1]); A1z = float(A1[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A1) da celula unitaria no espaco real.

A2 = contcar.readline().split()
A2x = float(A2[0]); A2y = float(A2[1]); A2z = float(A2[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A2) da celula unitaria no espaco real.

A3 = contcar.readline().split()
A3x = float(A3[0]); A3y = float(A3[1]); A3z = float(A3[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A3) da celula unitaria no espaco real.

#--------------
contcar.close()
#--------------

#-----------------------------------------------------------------------
# Obtenção dos rótulos dos ions presentes no arquivo CONTCAR -----------
#-----------------------------------------------------------------------

#------------------------------------------
contcar = open(dir_files + '/CONTCAR', "r")
#------------------------------------------

for i in range(6):
    VTemp = contcar.readline().split() 
types = len(VTemp)                                                     # Obtenção do número de diferentes tipos de ions que compoem a rede.

#----------------------------------------------

label = [0]*(types+1)
ion_label = [0]*(ni+1)
rotulo = [0]*(ni+1)
rotulo_temp = [0]*(ni+1)

#----------------------------------------------

for i in range (1,(types+1)):
    label[i] = VTemp[(i-1)]                                            # Obtenção dos rótulos/abreviações que rotulam cada tipo de ion da rede.

VTemp = contcar.readline().split()                                    

for i in range (1,(types+1)):            
    ion_label[i] = int(VTemp[(i-1)])                                   # Obtenção do número de ions correspondentes a cada rótulo/abreviação.

#----------------------------------------------

contador = 0

for i in range (1,(types+1)):
    number = ion_label[i]
    for j in range (1,(number+1)):
        contador += 1
        rotulo[contador] = label[i]

#--------------
contcar.close()
#--------------

#-----------------------------------------------------------------------
#---- Estimativa do valor correto do Parametro de Rede como sendo o ----
#---------- menor valor entre o modulo dos vetores A1, A2 e A3 ---------
#-----------------------------------------------------------------------

if (param_estim == 2):

   A1x = A1x*Parametro; A1y = A1y*Parametro; A1z = A1z*Parametro
   A2x = A2x*Parametro; A2y = A2y*Parametro; A2z = A2z*Parametro
   A3x = A3x*Parametro; A3y = A3y*Parametro; A3z = A3z*Parametro

   Parametro_1 = ((A1x*A1x) + (A1y*A1y) + (A1z*A1z))**0.5
   Parametro = Parametro_1

   Parametro_2 = ((A2x*A2x) + (A2y*A2y) + (A2z*A2z))**0.5
   if (Parametro_2 < Parametro):
      Parametro = Parametro_2

   Parametro_3 = ((A3x*A3x) + (A3y*A3y) + (A3z*A3z))**0.5
   if (Parametro_3 < Parametro):
      Parametro = Parametro_3

   A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
   A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
   A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro

#-----------------------------------------------------------------------

inform.write(" \n")
inform.write("***************************************************** \n")
inform.write("***** Vetores Primitivos da Rede Cristalina ********* \n")
inform.write(f'***** A1 = Param.({A1x}, {A1y}, {A1z}) \n')
inform.write(f'***** A2 = Param.({A2x}, {A2y}, {A2z}) \n')
inform.write(f'***** A3 = Param.({A3x}, {A3y}, {A3z}) \n')
inform.write(f'***** Param. = {Parametro} Angs. \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#-----------------------------------------------------------------------

ss1 = A1x*((A2y*A3z) - (A2z*A3y))
ss2 = A1y*((A2z*A3x) - (A2x*A3z))
ss3 = A1z*((A2x*A3y) - (A2y*A3x))
ss =  ss1 + ss2 + ss3                                        # Eu apenas divide esta soma em tres partes, uma vez que ela e muito longa, e ultrapassava a extensao da linha.

B1x = ((A2y*A3z) - (A2z*A3y))/ss                             # Para compreender estas operacoes sobre as componentes X, Y e Z dos vetores primitvos da rede
B1y = ((A2z*A3x) - (A2x*A3z))/ss                             # cristalina (A1, A2 e A3), vc deve executar a operacao padrao de construcao dos vetores
B1z = ((A2x*A3y) - (A2y*A3x))/ss                             # primitivos da rede rec¡proca com base nos vetores primitvos da rede cristalina.
B2x = ((A3y*A1z) - (A3z*A1y))/ss                             # Tal operacao se encontra disponivel em qualquer livro de estado solido.
B2y = ((A3z*A1x) - (A3x*A1z))/ss
B2z = ((A3x*A1y) - (A3y*A1x))/ss
B3x = ((A1y*A2z) - (A1z*A2y))/ss
B3y = ((A1z*A2x) - (A1x*A2z))/ss
B3z = ((A1x*A2y) - (A1y*A2x))/ss

#-----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("***** Vetores Primitivos da Rede Reciproca ********** \n")
inform.write(f'***** B1 = 2pi/Param.({B1x}, {B1y}, {B1z}) \n')
inform.write(f'***** B2 = 2pi/Param.({B2x}, {B2y}, {B2z}) \n')
inform.write(f'***** B3 = 2pi/Param.({B3x}, {B3y}, {B3z}) \n')
inform.write(f'***** Param. = {Parametro} Angs. \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#-------------
inform.close()
#-------------
