
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------
# Verificando se a pasta "Potencial" existe, se não existe ela é criada
#----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Potencial'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Potencial')
#-------------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')
#------------------------------------------------

print ("##############################################################")
print ("############## Plot do Potencial Eletrostatico: ##############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Dica: Para gerar um Plot 3D do Potencial Eletrostaico    ##")
print ("##       projetado sobre a rede cristalina, abra o arquivo  ##")
print ("##       LOCPOT pelo programa VESTA                         ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

#======================================================================
# Verificando a presenca do arquivo LOCPOT ============================
#======================================================================

try:
    f = open(dir_files + '/LOCPOT')
    f.close()
except:
    print('-----------------------------------------------------------------------------------')
    print('Arquivo LOCPOT ausente no diretorio, insira o arquivo e aperte ENTER para continuar')
    print('-----------------------------------------------------------------------------------')
    confirmacao = input (" "); confirmacao = str(confirmacao)

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

if (escolha == -1):
   print ("##############################################################")
   print ("Escolha a dimensao do eixo-x do Plot: ========================")
   print ("Utilize 1 para Angs. =========================================")
   print ("Utilize 2 para nm. ===========================================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

   print ("##############################################################")
   print ("Deseja destacar a coordenada dos ions no Plot? ===============")
   print ("[0] Nao ======================================================")
   print ("[1] Sim (Padrao) =============================================")
   print ("##############################################################") 
   destaque = input (" "); destaque = int(destaque)
   print (" ")   

if (escolha == 1):
   Dimensao = 1
   destaque = 1

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo LOCPOT ---------------------------
#----------------------------------------------------------------------

print (".........................................................")
print ("................ Lendo o arquivo LOCPOT: ................")
print ("................... Espere um momento ...................")
print (".........................................................")
print (" ")

#----------------------------------------
locpot = open(dir_files + '/LOCPOT', 'r')
#----------------------------------------

for i in range (8): VTemp = locpot.readline()

# Resultado extraido do arquivo PROCAR (_procar.py)
Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

#--------------------------------------------------------------------------

for i in range (ni):
    VTemp = locpot.readline().split()
    #---------------------------------------------------------------
    m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
    #--------------------------------------------------------------
    ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
    ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
    ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
VTemp = locpot.readline()
VTemp = locpot.readline().split()

Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)
coord = [0]*3

passo1 = (GRID/5)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 5 - ((passo1*5) -GRID)

for i in range (passo1):

    VTemp = locpot.readline()
    #-----------------------------------------------------
    for k in range(10):
        VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
        VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
    VTemp = VTemp.split()    
    #----------------------------------------------------- 

    if (i < (passo1-1)):
       for j in range(5): V_local[((i)*5) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*5) + j] = float(VTemp[j])

#-------------
locpot.close()
#-------------
  
#--------------------------------------------------------------------------

fator_x = max(Ax) - min(Ax)
fator_y = max(Ay) - min(Ay)
fator_z = max(Az) - min(Az)

escala_x = 1.0/float(GRID/Grid_x); Vx = [0]*(Grid_x); X = [0]*(Grid_x)
escala_y = 1.0/float(GRID/Grid_y); Vy = [0]*(Grid_y); Y = [0]*(Grid_y)
escala_z = 1.0/float(GRID/Grid_z); Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

#----------------------------------------------------------------------------
# Analisando os dados - Obtendo o valor médio do Potencial 3D em cada direção
#----------------------------------------------------------------------------

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#======================================================================
#======================================================================
# Plot 2D do Potencial médio em uma dada direção (Grace) ==============
#====================================================================== 
#======================================================================   
execute_python_file(filename = 'plot/Grace/plot_potencial.py')

#======================================================================
#======================================================================
# Plot 2D do Potencial médio em uma dada direção (Matplotlib) =========
#====================================================================== 
#======================================================================  

#======================================================================
# Gravando dados para o Plot do Potencial =============================
#======================================================================     

#---------------------------------------------------------------------
potencial = open(dir_files + '/output/Potencial/Potencial_X.dat', "w")
#---------------------------------------------------------------------

for i in range (Grid_x):
    potencial.write(f'{X[i]} {Vx[i]} \n')
potencial.close()

#---------------------------------------------------------------------
potencial = open(dir_files + '/output/Potencial/Potencial_Y.dat', "w")
#---------------------------------------------------------------------

for i in range (Grid_y):
    potencial.write(f'{Y[i]} {Vy[i]} \n')
potencial.close()

#---------------------------------------------------------------------
potencial = open(dir_files + '/output/Potencial/Potencial_Z.dat', "w")
#---------------------------------------------------------------------

for i in range (Grid_z):
    potencial.write(f'{Z[i]} {Vz[i]} \n')
potencial.close()

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Potencial.py para o diretório de output -----------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Potencial.py já se encontra no diretorio de output
try: f = open(dir_files + '/output/Potencial/Potencial.py'); f.close(); os.remove(dir_files + '/output/Potencial/Potencial.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_potencial.py'
destination = dir_files + '/output/Potencial/Potencial.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Potencial.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/Potencial/Potencial.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# VASProcar versão {version} - Python tools for VASP                  \n')
linha += 1; lines.insert(linha, f'# {url_1}                                                             \n')
linha += 1; lines.insert(linha, f'# {url_2}                                                             \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# authors:                                                             \n')
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
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'ni = {ni}  #  Numero de ions da rede \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] em Angstron; [2] em nm \n')
linha += 1; lines.insert(linha, f'destaque = {destaque}  #  Escolha quanto a destacar a coordenada dos ions, onde: [0] NÃO e [1] SIM \n')
linha += 1; lines.insert(linha, f'ion_x = {ion_x}  #  Coordenadas dos ions a serem destacadas no eixo-x \n')
linha += 1; lines.insert(linha, f'ion_y = {ion_y}  #  Coordenadas dos ions a serem destacadas no eixo-y \n')
linha += 1; lines.insert(linha, f'ion_z = {ion_z}  #  Coordenadas dos ions a serem destacadas no eixo-z \n')
linha += 1; lines.insert(linha, f'fator_x = {fator_x}; fator_y = {fator_y}; fator_z = {fator_z}  #  Variação das coordenadas X,Y,Z sofrida pelos vetores da rede \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Potencial/Potencial.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------
exec(open(dir_files + '/output/Potencial/Potencial.py').read())
#--------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
