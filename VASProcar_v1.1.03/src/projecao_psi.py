
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------
# Verificando se a pasta "Psi" existe, se não existe ela é criada
#----------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Psi'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Psi')
#-------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

ion_orb = [[[0]*(n_orb+1) for i in range(ni+1)] for j in range(5+1)]  #  ion_orb[n_psi][ni][n_orb]

psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  psi[n_psi][n_procar][nk][nb]          
est_psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  est_psi[n_psi][n_procar][nk][nb]
estado_psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  estado_psi[n_psi][n_procar][nk][nb]
total = [[[0.0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]  #  total[n_procar][nk][nb] 

l_psi = ['null']*(5+1)
dpi = 2*3.1415926535897932384626433832795

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Projecao dos estados Psi ##################")
print ("##############################################################") 
print (" ")

print ("##############################################################")
print ("Para definir um estado_Psi, voce deve informar um determinado ")
print ("intervalo_de_ions, e tambem informar quais orbitais devem ser ")
print ("incluidos neste respectivo intervalo.                         ")
print ("==============================================================")
print ("Para um dado estado_Psi, voce pode informar quantos intervalos")
print ("de ions achar necessario.                                     ")
print ("==============================================================")
print ("Use a nomenclatura abaixo para designar os Orbitais:          ")
if (lorbit == 10):
   print ("s p d                                                         ")
if (lorbit >= 11):
   print ("s p d px py pz dxy dyz dz2 dxz dx2                            ")
print ("==============================================================")
print ("Exemplos:                                                     ")
if (lorbit == 10):
   print ("ion_inicial ion_final orbitais: 3  3  S P D                    ")
   print ("ion_inicial ion_final orbitais: 5  14 S P                      ")
   print ("ion_inicial ion_final orbitais: 14 49 S                      ")
if (lorbit >= 11):
   print ("ion_inicial ion_final orbitais: 15 27 S Px Py Pz Dxy          ")  
   print ("ion_inicial ion_final orbitais: 35 78 S Pz Dxy Dyz Dz2 Dxz Dx2")
   print ("ion_inicial ion_final orbitais: 9  9  S P D                   ")
   print ("##############################################################")
print(" ")

print ("##############################################################")
print ("Quantos estados Psi deseja analisar? =========================")
print (" ========= (Sao permitidos no maximo 5 estados Psi) ========= ")
print ("##############################################################")
n_psi = input (" "); n_psi = int(n_psi)
print(" ")

if (n_psi <= 0): n_psi = 1
if (n_psi > 5):  n_psi = 5

for i in range(1,(n_psi+1)):
    print ("==============================================================")
    print (f'Digite o rotulo do estado_Psi {i}: =============================')
    print ("==============================================================")
    l_psi[i] = input ("rotulo: "); l_psi[i] = str(l_psi[i])
    print(" ")

    print ("==============================================================")
    print (f'Quantos intervalos_de_ions deseja fornecer ao estado_psi {i}? ==')
    print ("==============================================================")   
    loop = input (" "); loop = int(loop)
    print (" ")

    for j in range (1,(loop+1)):
        #--------------------------------------------------------------------------
        print ("==============================================================")
        print (f'Informe o intervalo_{j} de ions e orbitais do estado_psi_{i} ===')
        print (" ")
        psi_io = input ("ion_inicial ion_final orbitais: ").split()
        print (" ")
        #----------------------
        loop_i = int(psi_io[0])
        loop_f = int(psi_io[1])
        #----------------------
        if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
           print (" ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print ("   ERRO: Os valores de ions informados estao incorretos   ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           confirmacao = input (" ")
           exit()
           
        #----------------------   
        loop_o = len(psi_io) -2
        #----------------------
        
        for p in range(loop_i,(loop_f+1)):
            for t in range(1,(loop_o+1)):
                #------------------------
                if (lorbit == 10):                   
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'): ion_orb[i][p][1] = 1                    
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'): ion_orb[i][p][2] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'): ion_orb[i][p][3] = 1
                #------------------------      
                if (lorbit >= 11):                   
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'): ion_orb[i][p][1] = 1                      
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'): ion_orb[i][p][2] = 1; ion_orb[i][p][3] = 1; ion_orb[i][p][4] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'): ion_orb[i][p][5] = 1; ion_orb[i][p][6] = 1; ion_orb[i][p][7] = 1; ion_orb[i][p][8] = 1; ion_orb[i][p][9] = 1                                          
                   if (psi_io[t+1] == 'py' or psi_io[t+1] == 'Py' or psi_io[t+1] == 'PY'): ion_orb[i][p][2] = 1                      
                   if (psi_io[t+1] == 'pz' or psi_io[t+1] == 'Pz' or psi_io[t+1] == 'PZ'): ion_orb[i][p][3] = 1
                   if (psi_io[t+1] == 'px' or psi_io[t+1] == 'Px' or psi_io[t+1] == 'PX'): ion_orb[i][p][4] = 1                    
                   if (psi_io[t+1] == 'dxy' or psi_io[t+1] == 'Dxy' or psi_io[t+1] == 'DXY'): ion_orb[i][p][5] = 1                      
                   if (psi_io[t+1] == 'dyz' or psi_io[t+1] == 'Dyz' or psi_io[t+1] == 'DYZ'): ion_orb[i][p][6] = 1                      
                   if (psi_io[t+1] == 'dz2' or psi_io[t+1] == 'Dz2' or psi_io[t+1] == 'DZ2'): ion_orb[i][p][7] = 1                      
                   if (psi_io[t+1] == 'dxz' or psi_io[t+1] == 'Dxz' or psi_io[t+1] == 'DXZ'): ion_orb[i][p][8] = 1                      
                   if (psi_io[t+1] == 'dx2' or psi_io[t+1] == 'Dx2' or psi_io[t+1] == 'DX2'): ion_orb[i][p][9] = 1 

temp = [0.0]*(n_orb)

print ("##############################################################")
print ("Confira os estados informados antes de prosseguir:            ")
print ("Onde [0] = NAO e [1] = SIM                                    ")
print ("##############################################################")

for i in range(1,(n_psi+1)):
    print (" ")
    print ("------------")
    print (f'Estado Psi {i}')
    print ("------------")
    for j in range(1,(ni+1)):
        for k in range (1,(n_orb+1)):
            temp[k-1] = ion_orb[i][j][k]
        if (lorbit == 10):
           print (f'ion {j} ({rotulo[j]}): orbitais S[{temp[0]}] P[{temp[1]}] D[{temp[2]}]')
        if (lorbit >= 11):
           print (f'ion {j} ({rotulo[j]}): orbitais S[{temp[0]}] Px[{temp[3]}] Py[{temp[1]}] Pz[{temp[2]}] Dxy[{temp[4]}] Dyz[{temp[5]}] Dz2[{temp[6]}] Dxz[{temp[7]}] Dx2[{temp[8]}]')   
          
print (" ")
print ("##############################################################")
print ("Atencao: Caso esteja tudo certo com os estados Psi informados ")
print ("         aperte [ENTER] para continuar.                       ")
print ("##############################################################")
confirmacao = input (" ")

# Demais parâmetros de input ==========================================

if (escolha == -1):

   print ("##############################################################")
   print ("Quanto a energia dos estados, o que vc deseja? ===============")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")   

   print ("##############################################################")
   print ("Quanto aos pontos-k de interesse, o que vc deseja? ===========")
   print ("[0] Nao destacar nem rotular nenhum ponto-k ==================")
   print ("[1] Destacar automaticamente os pontos-k informados no KPOINTS")
   print ("[2] Destacar e rotular os pontos-k a sua escolha =============")
   print ("##############################################################") 
   dest_k = input (" "); dest_k = int(dest_k)
   print (" ")

   if (dest_k == 2):
      print ("##############################################################")
      print ("Observacao: O arquivo label.txt sera gerado apos a leitura do ")
      print ("            arquivo PROCAR                                    ")
      print ("##############################################################") 
      print (" ")

      Dimensao = 1

   if (dest_k != 2):   
      print ("##############################################################")
      print ("Escolha a dimensao do eixo-k: ================================")
      print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
      print ("Utilize 2 para k em unidades de 1/Angs. ======================")
      print ("Utilize 3 para k em unidades de 1/nm. ========================")
      print ("##############################################################")
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia a ser aplicado nas projecoes: ")
   print ("Esta opcao e util para verificar a sobreposicao de orbitais.  ")   
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("==============================================================")
   print ("Dica: Quanto maior for a densidade de pontos-k, menor deve ser")
   print ("      o valor de transparencia utilizado, comece por 0.1 ==== ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")   

if (escolha == 1):
   esc_fermi = 1
   dest_k = 1
   Dimensao = 1
   peso_total = 1.0
   transp = 1.0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0    

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
read_orb = 1
execute_python_file(filename = '_procar.py')

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------         
   
# color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
# color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
# color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb] 

#======================================================================
# Calculo do peso (% de contribuição) de cada estado PSi ==============
#======================================================================

for wp in range(1, (n_procar+1)):
    for k in range(1,(nk+1)):                                  
        for b in range (1,(nb+1)):
            for i in range (1,(ni+1)):                                       
                for o in range(1,(n_orb+1)):
                    total[wp][k][b] = total[wp][k][b] + orb[wp][o][k][b][i]
                    #------------------------------------------------------
                    for p in range(1,(n_psi+1)):
                        if (ion_orb[p][i][o] == 1):
                           psi[p][wp][k][b] = psi[p][wp][k][b] + orb[wp][o][k][b][i]                
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------  
            for p in range (1,(n_psi+1)):
                if (total[wp][k][b] != 0.0):
                   psi[p][wp][k][b] = ( psi[p][wp][k][b]/total[wp][k][b] )*peso_total                 
        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------

#======================================================================
# Obtendo o nº pontos-k a serem destacados bem como os seus rótulos ===
#======================================================================
execute_python_file(filename = '_label.py')

#======================================================================
#======================================================================
# Plot das Projeções dos estados Psi (Grace) ==========================
#====================================================================== 
#======================================================================
execute_python_file(filename = 'plot/Grace/plot_projecao_psi.py')
    
#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#-------------------------------------------------------
bandas = open(dir_files + '/output/Psi/Bandas.dat', 'w')
#-------------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------        

# Gravando a informação de cada estado Psi para o Plot das Projeções ==

#-------------------------------------------------
psi = open(dir_files + '/output/Psi/Psi.dat', 'w')
#-------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            psi.write(f'{xx[i][j]} {Energia[i][j][k]}')
            psi.write(f' {estado_psi[1][i][j][k]} {estado_psi[2][i][j][k]} {estado_psi[3][i][j][k]} {estado_psi[4][i][j][k]} {estado_psi[5][i][j][k]}')         
            psi.write(f' \n')
                
#----------
psi.close()
#----------

# Obtendo e gravando as cores no padrão RGB que designam cada orbital bem como cada combinação de orbitais para o Plot das Projeções ===:

#-------------------------------------------------------------
color_rgb = open(dir_files + '/output/Psi/color_rgb.dat', 'w')
#-------------------------------------------------------------

number = -1
           
for Band_n in range (1, (nb+1)):
    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):       
           number += 1
           
           #---------------------------------------------------------------------------------------------------------------------------------------------         
           # Notação do Matplotlib para o padrão RGB de cores: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------
           # c_red = [1, 0, 0]; c_green = [0, 1, 0]; c_blue = [0, 0, 1]; c_magenta = [1, 0, 1]; c_rosybrown = [0.737254902, 0.560784313, 0.560784313] ---           
           #---------------------------------------------------------------------------------------------------------------------------------------------

           #-----------------------------------------------------------------------------
           # Psi_1 = blue; Psi_2 = red; Psi_3 = green; Psi_4 = magenta; Psi_5 = rosybrown
           #-----------------------------------------------------------------------------               
           c_red    =  est_psi[2][wp][point_k][Band_n] + 0.737254902*(est_psi[5][wp][point_k][Band_n]) + est_psi[4][wp][point_k][Band_n]
           c_green  =  est_psi[3][wp][point_k][Band_n] + 0.560784313*(est_psi[5][wp][point_k][Band_n])
           c_blue   =  est_psi[1][wp][point_k][Band_n] + 0.560784313*(est_psi[5][wp][point_k][Band_n]) + est_psi[4][wp][point_k][Band_n]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #-------------------------------------------------
           color_rgb.write(f' {c_red} {c_green} {c_blue} \n')         

#----------------
color_rgb.close()
#----------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Psi.py para o diretório de saida ------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Psi.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Psi/Psi.py'); f.close(); os.remove(dir_files + '/output/Psi/Psi.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_psi.py'
destination = dir_files + '/output/Psi/Psi.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Psi.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

file = open(dir_files + '/output/Psi/Psi.py', 'r')
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
linha += 1; lines.insert(linha, f'n_psi = {n_psi}  #  Numero de estados Psi \n')
linha += 1; lines.insert(linha, f'l_psi = {l_psi}  #  Rotulos dos estados Psi \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}  #  Numero de arquivos PROCAR a serem lidos \n')
linha += 1; lines.insert(linha, f'nk  = {nk}  #  Numero de pontos-k do calculo \n')
linha += 1; lines.insert(linha, f'nb = {nb}  #  Numero de bandas do calculo \n')
linha += 1; lines.insert(linha, f'energ_min = {energ_min}  #  Menor valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'energ_max = {energ_max}  #  Maior valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'lorbit = {lorbit}  #  Valor da variavel lorbit adotada no calculo \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao plot das projecoes \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}  #  [0] Nao destacar nem rotular nenhum ponto-k; [1] Destacar automaticamente os pontos-k informados no KPOINTS; [2] Destacar e rotular os pontos-k a sua escolha \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}  #  Coordenadas dos pontos-k de interesse a serem destacados no plot da projeção \n')

if (dest_k == 2): 
   for i in range(contador2):
       for j in range(34):
           if (label_pk[i] == '#' + str(j+1)):
              label_pk[i] = r_matplot[j]    
   linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  Rotulos dos pontos-k de interesse a serem destacados no plot da projeção \n')

linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Psi/Psi.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------
exec(open(dir_files + '/output/Psi/Psi.py').read())
#--------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
