
#######################################################
########## Analisando o arquivo OUTCAR ################
######## Buscando informacoes do Sistema ##############
#######################################################

# ---------------------------------------------------------------------
# Verificando a presença dos arquivos CONTCAR, OUTCAR e PROCAR: -------
# ---------------------------------------------------------------------

n_contcar = 0

try:
    f = open(dir_files + '/CONTCAR')
    f.close()
    n_contcar = 1
except:
    print('')
    print('... Arquivo CONTCAR ausente ...')

#-----------------------------------

n_outcar = 0

try:
    f = open(dir_files + '/OUTCAR')
    f.close()
    n_outcar = 1
except:
    print('')
    print('... Arquivo OUTCAR ausente ...')

#-----------------------------------

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

if (n_contcar == 0 or n_outcar == 0 or n_procar == 0):   
   print('')
   print('')
   print('---------------------------------------------------------------------------')
   print('Apos inserir os arquivos ausentes no diretorio, aperte ENTER para continuar')
   print('---------------------------------------------------------------------------')
   confirmacao = input (" "); confirmacao = str(confirmacao)
   
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

#-----------------------------------------------------------------------------------------------
# Parametros de controle para a leitura dos orbitais e componentes de spin no arquivo PROCAR ---
#-----------------------------------------------------------------------------------------------
read_orb  = 0
read_spin = 0 

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
