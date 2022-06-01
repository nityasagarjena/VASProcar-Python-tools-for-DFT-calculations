
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------------------
# Verificando se a pasta "Fermi_Surface" existe, se não existir ela sera criada ---
#----------------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Fermi_Surface'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Fermi_Surface')
#-----------------------------------------------

#-------------------------------------------------------------------------------
# Verificando se a subpasta "figures" existe, se não existir ela sera criada ---
#-------------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Fermi_Surface/figures'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Fermi_Surface/figures')
#-------------------------------------------------------    

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')

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
print ("################ Plot da Superficie de Fermi: ################")
print ("##############################################################")
print (" ")

if (escolha == -1):
  
   print ("##############################################################")
   print ("Com relacao as bandas o que deseja analisar? =================")
   print ("[0] Plotar todas as bandas na Superficie de Fermi ============")
   print ("[1] Plotar um intervalo selecionado de bandas na Sup. de Fermi")
   print ("##############################################################")
   esc_band = input (" "); esc_band = int(esc_band)
   print (" ")

   if (esc_band == 1):
      print ("##############################################################")
      print ("Escolha o intervalo de Bandas a serem analisadas: =========== ")
      print ("Digite como no exemplo abaixo =============================== ")
      print ("--------------------------------------------------------------")
      print ("Banda_inicial Banda_final: 5  27                              ")
      print ("Banda_inicial Banda_final: 13 49                              ")
      print ("Banda_inicial Banda_final: 7  7                               ")      
      print ("##############################################################") 
      print (" ")
      Band_i, Band_f = input ("Banda_inicial Banda_final: ").split()
      Band_i = int(Band_i)
      Band_f = int(Band_f)
      print (" ") 

   print ("##############################################################")
   print ("Quanto a energia dos estados, o que vc deseja? ===============")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ") 

print ("##############################################################")
print ("Qual o numero de Energias que deseja analisar? ===============")
print ("##############################################################")
n_energ = input (" "); n_energ = int(n_energ)
print(" ")

if (n_energ <= 0):
   n_energ = 1

print ("##############################################################")
print ("Com relacao aos valores de energias: =========================")
print ("[0] Devem ser obtidas automaticamente pelo codigo ============")
print ("[1] Devem varrer um determinado range de energia =============")
print ("[2] Desejo especificar cada valor de energia manualmente =====")   
print ("##############################################################")
esc_energ = input (" "); esc_energ = int(esc_energ)
print(" ")

if (esc_energ == 1):
   print ("##############################################################")
   print ("Escolha o intervalo de Energia a ser analisado: ============= ")
   print ("Digite como nos exemplos abaixo ============================= ")
   print ("--------------------------------------------------------------")
   print ("Energ_inicial Energ_final: -4.5 6.9                           ")
   print ("Energ_inicial Energ_final:  0.0 5.5                           ")
   print ("##############################################################") 
   print (" ")
   energ_i, energ_f = input ("Energ_inicial Energ_final: ").split()
   energ_i = float(energ_i)
   energ_f = float(energ_f)
   print (" ")

if (esc_energ == 2):
   #----------------
   E = [0.0]*n_energ
   #----------------
   print ("##############################################################")
   print ("Digite os valores de Energia como nos exemplos abaixo ======= ")
   print ("--------------------------------------------------------------")
   print ("Energias: -4.5 -2.0 -1.0  0.0  1.0  3.0 5.0                   ")
   print ("Energias:  0.2  0.5  0.78 1.23 9.97                           ")
   print ("--------------------------------------------------------------")
   print ("!!! Observacao importante !!! =============================== ")
   print ("Sempre digite os valores de energia em ordem crescente ====== ")
   print ("##############################################################") 
   print (" ")
   E = input ("Energias: ").split()
   for i in range(n_energ):
       E[i] = float(E[i])
   print (" ")

#-----------------------------------------------------------------------------

if (soma_1 == 2 or soma_2 == 2):
   #----------------------------------   
   if (soma_2 == 2 and escolha == -1):
      print ("##############################################################") 
      print ("## Escolha a dimensao dos eixos-k no Plot: ================ ##")
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

print ("##############################################################")
print ("Deseja compilar um video apartir das figuras geradas? ========")
print ("[0] NAO ======================================================")
print ("[1] SIM ======================================================")
print ("==============================================================")
print ("Observacao: Nao serao geradas imagens em .pdf ou .eps ========")
print ("##############################################################")
video = input (" "); video = int(video)
print (" ")

if (video == 1):
   #-----------------------------------------------------------------------
   print ("##############################################################")
   print ("Quantas figuras deseja que aparecam por segundo no video? ====")
   print ("Dica 1: ======================================================")
   print ("Escolha entre 1 e 8 figuras ==================================")
   print ("Dica 2: ======================================================")
   print ("Quanto maior for o numero de imagens geradas e maior o numero ")
   print ("de imagens por segundo, maior sera a fluidez do video         ")
   print ("##############################################################")
   n_fig = input (" "); n_fig = int(n_fig)  
   print (" ")
   #-------------------------
   if (n_fig <= 0): n_fig = 1
   #-------------------------
   save_png = 1
   save_pdf = 0
   save_eps = 0

if (escolha == -1):
   print ("##############################################################")
   print ("Qual a dimensao-D (DxD) do GRID de interpolacao? =============")
   print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)  
   print (" ")   

if (escolha == 1):
   esc_fermi = 1
   esc_band = 0
   n_d = 101

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)

if (esc_band == 0):
   Band_i = 1
   Band_f = nb

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = '_procar.py')

#======================================================================
# Gravando dados para o Plot da Superficie de Fermi ===================
#======================================================================     

#------------------------------------------------------------------------
sfermi = open(dir_files + '/output/Fermi_Surface/Fermi_Surface.dat', "w")
#------------------------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           sfermi.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} ')   
        if (Dimensao == 4):
           sfermi.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} ')
        for Band_n in range (1,(nb+1)):
           sfermi.write(f'{Energia[j][point_k][Band_n]} ')
        sfermi.write("\n")
               
#-------------
sfermi.close()
#-------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Fermi_Surface.py para o diretório de saida --------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Fermi_Surface.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Fermi_Surface/Fermi_Surface.py'); f.close(); os.remove(dir_files + '/output/Fermi_Surface/Fermi_Surface.py')
except: 0 == 0
 
source = main_dir + '/plot/plot_fermi_surface.py'
destination = dir_files + '/output/Fermi_Surface/Fermi_Surface.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código de Plot possam ser executados isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Fermi_Surface/Fermi_Surface.py', 'r')
lines = file.readlines()
file.close()

linha = 11

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
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}  #  [1] kxky ou k1k2; [2] kxkz ou k1k3; [3] kykz ou k2k3  \n')
linha += 1; lines.insert(linha, f'ispin = {ispin}  #  [1] Calculo sem polarização de Spin; [2] Calculo com polarização de Spin \n')
linha += 1; lines.insert(linha, f'Band_i = {Band_i}  #  Banda inicial a ser introduzida no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'Band_f = {Band_f}  #  Banda final a ser introduzida no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'esc_energ = {esc_energ}  #  Forma de obtenção das energias: Onde [0] é automatico; [1] range de energia e [2] informado manualmente \n')
linha += 1; lines.insert(linha, f'n_energ = {n_energ}  #  Numero de energias a serem utilizadas no plot das Superficies de Fermi \n')
#--------------------------------
if (esc_energ == 1):
   linha += 1; lines.insert(linha, f'energ_i = {energ_i}; energ_f = {energ_f}  #  Energia inicial e final do Range de energia no plot das Superficies de Fermi \n')
if (esc_energ == 2):
   linha += 1; lines.insert(linha, f'E = {E}  #  Valores de energia especificadas manualmente no plot das Superficies de Fermi \n')
if (esc_energ < 2):
   linha += 1; lines.insert(linha, f'E = [0.0, 0.0, 0.0, 0.0, 0.0]  #  Valores das Curvas de Nivel especificados manualmente \n')
#--------------------------------
linha += 1; lines.insert(linha, f'video = {video}  #  Escolha se um video deve ser gerado ou nao, onde [0] = NAO e [1] = SIM \n')
if (video == 1):
   linha += 1; lines.insert(linha, f'n_fig = {n_fig}  #  Numero de figuras que aparecem no video por segundo \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Fermi_Surface/Fermi_Surface.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------------------
exec(open(dir_files + '/output/Fermi_Surface/Fermi_Surface.py').read())
#----------------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
