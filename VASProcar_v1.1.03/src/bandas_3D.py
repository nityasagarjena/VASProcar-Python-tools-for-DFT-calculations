
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------------
# Verificando se a pasta "Bandas_3D" existe, se não existir ela sera criada --
#-----------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Bandas_3D'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Bandas_3D')
#-------------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')
#-----------------------------------------------

#======================================================================
# Analisando a variação das coordenadas dos pontos-k ==================
#======================================================================
execute_python_file(filename = '_var_kpoints.py')
#-----------------------------------------------

soma_1 = dk[0] + dk[1] + dk[2]
soma_2 = dk[3] + dk[4] + dk[5]

if (soma_1 != 2 and soma_2 != 2):
   print("===========================================================")
   print("!!! ERROR !!!                                              ")
   print("===========================================================")
   print("O calculo efetuado nao corresponde a um plano 2D na Zona de")
   print("Brillouin: Plano kikj com i,j = x,y,z  or  i,j = 1,2,3     ")
   print("Dica: -----------------------------------------------------")
   print("Para gerar o arquivo KPOINTS correto, utilize a opcao [888]")
   print("===========================================================")
   confirmacao = input (" ")
   exit()

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("####################### Plot Banda 3D: #######################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   print ("##############################################################")
   print ("Quanto a energia dos estados, o que vc deseja? ===============")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")

print ("##############################################################")
print ("Escolha o intervalo de Bandas a serem Plotadas: ============= ")
print ("Digite como nos exemplos abaixo ============================= ")
print ("--------------------------------------------------------------")
print ("Banda_inicial Banda_final: 5 15                               ")
print ("Banda_inicial Banda_final: 7 7                                ")
print ("##############################################################") 
print (" ")
Band_i, Band_f = input ("Banda_inicial Banda_final: ").split()
Band_i = int(Band_i)
Band_f = int(Band_f)
print (" ")

#-----------------------------------------------------------------------------

if (soma_1 == 2 or soma_2 == 2):
   #----------------------------------   
   if (soma_2 == 2 and escolha == -1):
      print ("##############################################################") 
      print ("## Escolha a dimensao dos eixos-k no Plot 3D: ============= ##")
      print ("##############################################################")
      print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
      print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
      print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")  
   #----------------------------------
   if (soma_1 == 2 and soma_2 == 2 and escolha == -1):    
      print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")    
   #----------------------------------
   if (soma_2 == 2 and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != 2):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != 2 and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == 2 and soma_2 == 2 and escolha == 1):
      Dimensao = 4
   #----------------------------------   
     
   if (Dimensao < 4):
      if (dk[3] == 1 and dk[4] == 1): Plano_k = 1  #  Plano kxky
      if (dk[3] == 1 and dk[5] == 1): Plano_k = 2  #  Plano kxkz
      if (dk[4] == 1 and dk[5] == 1): Plano_k = 3  #  Plano kykz
   
   if (Dimensao == 4):
      if (dk[0] == 1 and dk[1] == 1): Plano_k = 1  #  Plano k1k2
      if (dk[0] == 1 and dk[2] == 1): Plano_k = 2  #  Plano k1k3
      if (dk[1] == 1 and dk[2] == 1): Plano_k = 3  #  Plano k2k3   

#-----------------------------------------------------------------------------
   
if (escolha == -1):
   print ("##############################################################") 
   print ("## Escolha o pacote para pre-visualizar o Plot 3D: ======== ##")
   print ("##############################################################")
   print ("## [1] Plotly (Visualizacao mais leve) ==================== ##")
   print ("## [2] Matplotlib ========================================= ##")
   print ("##############################################################") 
   pacote = input (" "); pacote = int(pacote)
   if (pacote == 2):
      n_d = 101
   print (" ")

   print ("##############################################################")
   print ("## Como prefere que seja o Plot 3D? ======================= ##")
   print ("##############################################################")
   print ("## [0] Pontos (Dados brutos) ============================== ##")
   if (pacote == 1): print ("## [1] Superficie (Interpolacao) ========================== ##")
   if (pacote == 2): print ("## [1] Superficie (Dados brutos + Triangularizacao) ======= ##")
   print ("## [2] Pontos + Superficie ================================ ##")  
   print ("##############################################################") 
   tipo_plot = input (" "); tipo_plot = int(tipo_plot)
   print (" ")

   if (pacote == 1 and tipo_plot > 0):
      print ("##############################################################")
      print ("Qual a dimensao-D (DxD) do GRID de interpolacao? =============")
      print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")     

if (escolha == 1):
   esc_fermi = 1
   pacote = 1
   tipo_plot = 1
   n_d = 101

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0    

#======================================================================
# Extraindo os resultados do(s) arquivo(s) PROCAR =====================
#======================================================================
execute_python_file(filename = '_procar.py')
#------------------------------------------   

#----------------------------------------------------------------------
Band_antes   = (Band_i - 1)       # Bandas que nao serao plotadas.
Band_depois  = (Band_f + 1)       # Bandas que nao serao plotadas.
#----------------------------------------------------------------------

#======================================================================
# Gravando dados para o Plot 3D da Estrutura de Bandas ================
#======================================================================     

#-------------------------------------------------------------------
bandas_3D = open(dir_files + '/output/Bandas_3D/Bandas_3D.dat', 'w')
#-------------------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           bandas_3D.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} ')   
        if (Dimensao == 4):
           bandas_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} ')
        for Band_n in range (Band_i,(Band_f+1)):
            bandas_3D.write(f'{Energia[j][point_k][Band_n]} ')
        bandas_3D.write("\n")
               
#----------------
bandas_3D.close()
#----------------

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Copiando os codigos Bandas_3D_matplotlib.py e Bandas_3D_plotly.py para o diretório de saida --
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# Teste para saber se o arquivo Bandas_3D_plotly.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py'); f.close(); os.remove(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py')
except: 0 == 0

# Teste para saber se o arquivo Bandas_3D_matplotlib.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py'); f.close(); os.remove(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_bandas_3D_plotly.py'
destination = dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py'
shutil.copyfile(source, destination)

source = main_dir + '/plot/plot_bandas_3D_matplotlib.py'
destination = dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Inserindo parâmetros para que os códigos de Plot possam ser executados isoladamente ----------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

for i in range (2):

    if (i == 0): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py', 'r')
    if (i == 1): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py', 'r')
    lines = file.readlines()
    file.close()

    if (i == 0): linha = 8
    if (i == 1): linha = 11

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
    linha += 1; lines.insert(linha, f'tipo_plot = {tipo_plot}  # [0] Plotado em pontos; [1] Plotado em superficie; [2] pontos + superficie \n')   
    linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
    linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}  #  [1] kxky ou k1k2; [2] kxkz ou k1k3; [3] kykz ou k2k3  \n')
    linha += 1; lines.insert(linha, f'Band_i = {Band_i}  #  Banda inicial a ser plotada \n')
    linha += 1; lines.insert(linha, f'Band_f = {Band_f}  #  Banda final a ser plotada \n')
    linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
    linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
    if (i == 0):
       linha += 1
       lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')      
    if (i == 1):
       linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
    linha += 1; lines.insert(linha, '\n')
    linha += 1; lines.insert(linha, '#===================================================================== \n')

    if (i == 0): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py', 'w')
    if (i == 1): file = open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py', 'w')
    file.writelines(lines)
    file.close()

#----------------------------------------------------------------------------
if (pacote == 1):
   exec(open(dir_files + '/output/Bandas_3D/Bandas_3D_plotly.py').read())
if (pacote == 2):
   exec(open(dir_files + '/output/Bandas_3D/Bandas_3D_matplotlib.py').read())
#----------------------------------------------------------------------------
   
#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
