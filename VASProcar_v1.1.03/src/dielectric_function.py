
#-----------------------------------------------------------------------
# Verificando se a pasta "BSE" existe, se não existe ela é criada -----
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/BSE'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/BSE')
#-------------------------------------

print ("##############################################################")
print ("################# Plot da Funcao Dieletrica: #################")
print ("##############################################################")
print (" ")

#======================================================================
# Verificando a presenca do arquivo vasprun.xml =======================
#======================================================================

try:
    f = open(dir_files + '/vasprun.xml')
    f.close()
except:
    print('----------------------------------------------------------------------------------------')
    print('Arquivo vasprun.xml ausente no diretorio, insira o arquivo e aperte ENTER para continuar')
    print('----------------------------------------------------------------------------------------')
    confirmacao = input (" "); confirmacao = str(confirmacao)   

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

if (escolha == -1):
   
   print ("##############################################################")
   print ("Deseja escolher o range de energia do Plot? ==================")
   print ("[0] NAO                                                       ")
   print ("[1] SIM                                                       ")
   print ("##############################################################") 
   esc_energ = input (" "); esc_energ = int(esc_energ)
   print (" ")
 
   if (esc_energ == 1):
      print ("##############################################################")
      print ("Informe os dois valores de energia do intervalo: =============")
      print ("Digite como nos exemplos abaixo ==============================")
      print ("--------------------------------------------------------------")
      print ("E_inicial E_final: -5.0 3.5                                   ")
      print ("E_inicial E_final:  1.0 9.8                                   ")
      print ("##############################################################") 
      print (" ")
      x_inicial, x_final = input ("E_inicial E_final: ").split()
      x_inicial = float(x_inicial)
      x_final   = float(x_final)
      print (" ") 
   
print ("##############################################################")
print ("Qual o valor da energia de Fermi? ============================")
print ("##############################################################") 
Efermi = input (" "); Efermi = float(Efermi)
print (" ")

if (escolha == -1):
   print ("##############################################################")
   print ("Quanto a energia, o que vc deseja? ===========================")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")  

if (escolha == 1):
   esc_fermi = 1
   esc_energ = 0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo vasprun.xml ----------------------
#----------------------------------------------------------------------

print (".........................................................")
print (".............. Lendo o arquivo vasprun.xml ..............")
print ("................... Espere um momento ...................")
print (".........................................................")

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

passo = -1

palavra = '</set>'
for line in vasprun:
    passo += 1
    if palavra in line: 
       break

#--------------
vasprun.close()
#--------------

#==============================================

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  
for line in vasprun:   
    if palavra in line: 
       break

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

energ = [0.0]*passo
X_i   = [0.0]*passo;  X_r  = [0.0]*passo
Y_i   = [0.0]*passo;  Y_r  = [0.0]*passo
Z_i   = [0.0]*passo;  Z_r  = [0.0]*passo
XY_i  = [0.0]*passo;  XY_r = [0.0]*passo
YZ_i  = [0.0]*passo;  YZ_r = [0.0]*passo
ZX_i  = [0.0]*passo;  ZX_r = [0.0]*passo
media_i  = [0.0]*passo;  media_r  = [0.0]*passo
modulo_i = [0.0]*passo;  modulo_r = [0.0]*passo

#----------------------------------------------

for i in range(passo):
    VTemp = vasprun.readline().split()
    energ[i] = float(VTemp[1])
    X_i[i]   = float(VTemp[2])
    Y_i[i]   = float(VTemp[3])
    Z_i[i]   = float(VTemp[4])
    media_i[i]  = (X_i[i] + Y_i[i] + Z_i[i])/3
    modulo_i[i] = ((X_i[i]**2) + (Y_i[i]**2) + (Z_i[i]**2))**0.5
    # XY_i[i]  = float(VTemp[5])
    # YZ_i[i]  = float(VTemp[6])
    # ZX_i[i]  = float(VTemp[7])

palavra = '<set>'
for line in vasprun:   
    if palavra in line: 
       break

for i in range(passo):
    VTemp = vasprun.readline().split()
    X_r[i]   = float(VTemp[2])
    Y_r[i]   = float(VTemp[3])
    Z_r[i]   = float(VTemp[4])
    media_r[i]  = (X_r[i] + Y_r[i] + Z_r[i])/3
    modulo_r[i] = ((X_r[i]**2) + (Y_r[i]**2) + (Z_r[i]**2))**0.5
    # XY_r[i]  = float(VTemp[5])
    # YZ_r[i]  = float(VTemp[6])
    # ZX_r[i]  = float(VTemp[7])

#--------------
vasprun.close()
#--------------

#======================================================================
# Gravando dados para o Plot da Função Dieletrica: ====================
#======================================================================     

#-------------------------------------------------
BSE = open(dir_files + '/output/BSE/BSE.dat', 'w')
#-------------------------------------------------

for i in range (passo):
    BSE.write(f'{energ[i]}')
    BSE.write(f' {modulo_i[i]} {media_i[i]}')
    BSE.write(f' {X_i[i]} {Y_i[i]} {Z_i[i]}')
    # BSE.write(f' {XY_i[i]} {YZ_i[i]} {ZX_i[i]}')
    BSE.write(f' {media_r[i]} {modulo_r[i]}')
    BSE.write(f' {X_r[i]} {Y_r[i]} {Z_r[i]}')
    # BSE.write(f' {XY_r[i]} {YZ_r[i]} {ZX_r[i]}')
    BSE.write(f' \n')
    
#----------
BSE.close()
#----------

#=================================================================================
#=================================================================================
# Plot da Funcao Dieletrica (Grace) ==============================================
#=================================================================================
#=================================================================================
execute_python_file(filename = 'plot/Grace/plot_dielectric_function.py')

#=================================================================================
#=================================================================================
# Plot 2D da Funcao Dieletrica (BSE) (Matplotlib) ================================
#================================================================================= 
#=================================================================================     

#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Copiando o codigo Dielectric_Function.py para o diretório de output ---
#------------------------------------------------------------------------
#------------------------------------------------------------------------

# Teste para saber se o arquivo Densidade.py já se encontra no diretorio de output
try: f = open(dir_files + '/output/BSE/Dielectric_Function.py'); f.close(); os.remove(dir_files + '/output/BSE/Dielectric_Function.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_dielectric_function.py'
destination = dir_files + '/output/BSE/Dielectric_Function.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Densidade.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'r')
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
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'esc_energ = {esc_energ}  #  Escolha quanto a opção de analisar ou não um determinado range de energia, onde: [0] NAO e [1] SIM \n')
linha += 1; lines.insert(linha, f'x_inicial = {x_inicial}; x_final = {x_final}  #  Valore inicial e final do range de energia, vinculada a opção acima \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/BSE/Dielectric_Function.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------
exec(open(dir_files + '/output/BSE/Dielectric_Function.py').read())
#------------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
