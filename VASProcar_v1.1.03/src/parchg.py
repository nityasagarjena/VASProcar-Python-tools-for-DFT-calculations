
#------------------------------------------------------------------------------------
# Verificando se a pasta "Densidade_Carga_Parcial" existe, se não existe ela é criada
#------------------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Densidade_Carga_Parcial'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Densidade_Carga_Parcial')
#---------------------------------------------------------

print ("##############################################################")
print ("############# Plot da Densidade de Carga Parcial #############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("## Dica: Para gerar um Plot 3D da Densidade de Carga        ##")
print ("##       projetada sobre a rede cristalina, renomei o       ##")
print ("##       arquivo para PARCHG e abra pelo programa VESTA     ##")
print ("## ======================================================== ##")
print ("## Link: http://jp-minerals.org/vesta/en/download.html      ##")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Insira o nome completo do arquivo PARCHG que deseja analisar: ")
print ("##############################################################") 
name = input (" "); name = str(name)
print (" ")

#======================================================================
# Verificando a presenca do arquivo informado =========================
#======================================================================

try:
    f = open(dir_files + '/' + name)
    f.close()
except:
    print('----------------------------------------------------------------------------')
    print('Arquivo ausente no diretorio, insira o arquivo e aperte ENTER para continuar')
    print('----------------------------------------------------------------------------')
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
# Extraindo os resultados do arquivo PARCHG ---------------------------
#----------------------------------------------------------------------

print (".........................................................")
print ("................ Lendo o arquivo PARCHG: ................")
print ("................... Espere um momento ...................")
print (".........................................................")
print (" ")

#-----------------------------------------
parchg = open(dir_files + '/' + name, 'r')
#-----------------------------------------

for i in range (8):
    VTemp = parchg.readline()

# Resultado extraido do arquivo PROCAR (_procar.py)
Ax = [A1x*Parametro, A2x*Parametro, A3x*Parametro]
Ay = [A1y*Parametro, A2y*Parametro, A3y*Parametro]
Az = [A1z*Parametro, A2z*Parametro, A3z*Parametro]

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

for i in range (ni):
    VTemp = parchg.readline().split()
    #---------------------------------------------------------------
    m1 = float(VTemp[0]); m2 = float(VTemp[1]); m3 = float(VTemp[2])
    #--------------------------------------------------------------
    ion_x[i] = ((m1*A1x) + (m2*A2x) + (m3*A3x))*Parametro; ion_x[i] = ion_x[i] - min(Ax)
    ion_y[i] = ((m1*A1y) + (m2*A2y) + (m3*A3y))*Parametro; ion_y[i] = ion_y[i] - min(Ay)
    ion_z[i] = ((m1*A1z) + (m2*A2z) + (m3*A3z))*Parametro; ion_z[i] = ion_z[i] - min(Az)
    
VTemp = parchg.readline()
VTemp = parchg.readline().split()

Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)

passo1 = (GRID/10)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 10 - ((passo1*10) -GRID)

for i in range (passo1):

    VTemp = parchg.readline()
    #-----------------------------------------------------
    for k in range(10):
        VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
        VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
    VTemp = VTemp.split()    
    #----------------------------------------------------- 

    if (i < (passo1-1)):
       for j in range(10): V_local[((i)*10) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*10) + j] = float(VTemp[j])

#-------------
parchg.close()
#-------------
  
#--------------------------------------------------------------------------

fator_x = max(Ax) - min(Ax)
fator_y = max(Ay) - min(Ay)
fator_z = max(Az) - min(Az)

escala_x = 1.0/float(GRID/Grid_x); Vx = [0]*(Grid_x); X = [0]*(Grid_x)
escala_y = 1.0/float(GRID/Grid_y); Vy = [0]*(Grid_y); Y = [0]*(Grid_y)
escala_z = 1.0/float(GRID/Grid_z); Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

#---------------------------------------------------------------------------------------------
# Analisando os dados: Obtendo o valor médio da Densidade de Carga Parcial em uma dada direção
#---------------------------------------------------------------------------------------------

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#=================================================================================
#=================================================================================
# Plot 2D da Densidade de Carga Parcial em uma dada direção (Grace) ==============
#================================================================================= 
#=================================================================================  
execute_python_file(filename = 'plot/Grace/plot_parchg.py')

#=================================================================================
#=================================================================================
# Plot 2D da Densidade de Carga Parcial em uma dada direção (Matplotlib) =========
#================================================================================= 
#=================================================================================  

#======================================================================
# Gravando dados para o Plot da Densidade de Carga Parcial ============
#======================================================================     

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_X.dat', "w")
#-----------------------------------------------------------------------------------

for i in range (Grid_x):
    densidade.write(f'{X[i]} {Vx[i]} \n')
densidade.close()

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_Y.dat', "w")
#-----------------------------------------------------------------------------------

for i in range (Grid_y):
    densidade.write(f'{Y[i]} {Vy[i]} \n')
densidade.close()

#-----------------------------------------------------------------------------------
densidade = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade_Z.dat', "w")
#-----------------------------------------------------------------------------------

for i in range (Grid_z):
    densidade.write(f'{Z[i]} {Vz[i]} \n')
densidade.close()

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Densidade.py para o diretório de output -----------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Densidade.py já se encontra no diretorio de output
try: f = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py'); f.close(); os.remove(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_parchg.py'
destination = dir_files + '/output/Densidade_Carga_Parcial/Densidade.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Densidade.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py', 'r')
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

file = open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------------------------
exec(open(dir_files + '/output/Densidade_Carga_Parcial/Densidade.py').read())
#----------------------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
