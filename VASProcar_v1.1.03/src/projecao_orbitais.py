
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#---------------------------------------------------------------------
# Verificando se a pasta "Orbitais" existe, se não existe ela é criada
#---------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Orbitais'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Orbitais')
#------------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("############### Projecao dos Orbitais (S,P,D): ###############")
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
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

   if (esc == 1):
      
      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  #  Inicialização do vetor sim_nao
      #-------------------------
      
      print ("##############################################################")
      print ("Os ions devem ser selecionados por meio de intervalos ======= ")
      print ("Quantos intervalos de ions vc ira fornecer abaixo? ===========")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)

      print (" ")
      print ("##############################################################")
      print ("Escolha os intervalos de ions a serem analisados: =========== ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("ion_inicial ion_final: 3  3                                   ")
      print ("ion_inicial ion_final: 15 27                                  ")          
      print ("ion_inicial ion_final: 7  49                                  ")
      print ("##############################################################") 
      print (" ")      

      for i in range (1,(loop+1)):

          print (f'{i} intervalo: =================================================')
          print (" ")
          loop_i, loop_f = input ("ion_inicial ion_final: ").split()
          loop_i = int(loop_i)
          loop_f = int(loop_f)
          print (" ")

          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print (" ")
             
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"    

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
   esc = 0
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
   
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = Parcela do Orbital (S, P ou D) referente a cada ion "ni".
#  soma_orb = Soma do Orbital (S, P ou D) sobre todos os ions "ni" selecionados.
#  tot      = Soma sobre todos os orbitais e todos os ions.

color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb]

orbital_S   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_P   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_D   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Px  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Py  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Pz  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dxy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dyz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dz2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dxz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dx2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]

orb_S   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_P   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_D   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Px  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Py  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Pz  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Dxy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Dyz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Dz2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Dxz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orb_Dx2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]

dpi = 2*3.1415926535897932384626433832795

#======================================================================
# Calculo do peso (% de contribuição) de cada orbital =================
#====================================================================== 

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):            
                #------------------------------------------------------                
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------                              
                for orb_n in range(1,(n_orb+1)):
                    total[wp][point_k][Band_n] = total[wp][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]                    
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------  
            for orb_n in range (1, (n_orb+1)):
                if (total[wp][point_k][Band_n] != 0.0):
                   soma_orb[wp][orb_n][point_k][Band_n] = ( soma_orb[wp][orb_n][point_k][Band_n]/total[wp][point_k][Band_n] )*peso_total                   
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
# Plot das Projeções dos Orbitais (Grace) =============================
#====================================================================== 
#======================================================================
execute_python_file(filename = 'plot/Grace/plot_projecao_orbitais.py')
    
#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#------------------------------------------------------------
bandas = open(dir_files + '/output/Orbitais/Bandas.dat', 'w')
#------------------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------

# Gravando a informação de cada orbital para o Plot das Projeções =====

#---------------------------------------------------------------
orbital = open(dir_files + '/output/Orbitais/Orbitais.dat', 'w')
#---------------------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            orbital.write(f'{xx[i][j]} {Energia[i][j][k]}')
            orbital.write(f' {orbital_S[i][j][k]} {orbital_P[i][j][k]} {orbital_D[i][j][k]}')
            if (lorbit > 10):
               orbital.write(f' {orbital_Px[i][j][k]} {orbital_Py[i][j][k]} {orbital_Pz[i][j][k]}')
               orbital.write(f' {orbital_Dxy[i][j][k]} {orbital_Dyz[i][j][k]} {orbital_Dz2[i][j][k]} {orbital_Dxz[i][j][k]} {orbital_Dx2[i][j][k]}')             
            orbital.write(f' \n')
                
#--------------
orbital.close()
#--------------

# Obtendo e gravando as cores no padrão RGB que designam cada orbital bem como cada combinação de orbitais para o Plot das Projeções ===:

#------------------------------------------------------------------
color_rgb = open(dir_files + '/output/Orbitais/color_rgb.dat', 'w')
#------------------------------------------------------------------

number = -1
for Band_n in range (1, (nb+1)):
    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):       
           number += 1
           
           #---------------------------------------------------------------------------------------------------------------------------------------------         
           # Notação do Matplotlib para o padrão RGB de cores: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------
           # c_red = [1, 0, 0]; c_green = [0, 1, 0]; c_blue = [0, 0, 1]; c_rosybrown = [0.737254902, 0.560784313, 0.560784313]; c_magenta = [1, 0, 1] ---           
           #---------------------------------------------------------------------------------------------------------------------------------------------

           #-----------------------------------------
           # orb_S = blue; orb_P = red; orb_D = green 
           #-----------------------------------------          
           c_red   =  orb_P[wp][point_k][Band_n]
           c_green =  orb_D[wp][point_k][Band_n]
           c_blue  =  orb_S[wp][point_k][Band_n]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #---------------------------------------------
           color_rgb.write(f'{c_red} {c_green} {c_blue}')
           
           #--------------------------------------------
           # orb_Px = blue; orb_Py = red; orb_Pz = green 
           #--------------------------------------------          
           if (orb_P[wp][point_k][Band_n] != 0 and lorbit >= 11):
              orb_Px[wp][point_k][Band_n]  =  (orb_Px[wp][point_k][Band_n])/orb_P[wp][point_k][Band_n]
              orb_Py[wp][point_k][Band_n]  =  (orb_Py[wp][point_k][Band_n])/orb_P[wp][point_k][Band_n]
              orb_Pz[wp][point_k][Band_n]  =  (orb_Pz[wp][point_k][Band_n])/orb_P[wp][point_k][Band_n]                        
           #------------------------------------------------------------------------------------------           
           if (lorbit >= 11):
              c_red   =  orb_Py[wp][point_k][Band_n]
              c_green =  orb_Pz[wp][point_k][Band_n]
              c_blue  =  orb_Px[wp][point_k][Band_n]
              #--------------------------------
              if (c_red > 1.0):   c_red   = 1.0
              if (c_green > 1.0): c_green = 1.0
              if (c_blue > 1.0):  c_blue  = 1.0
              #----------------------------------------------              
              color_rgb.write(f' {c_red} {c_green} {c_blue}')
           
           #---------------------------------------------------------------------------------------
           # orb_Dxy = blue; orb_Dyz = red; orb_Dz2 = green; orb_Dxz = rosybrown; orb_Dx2 = magneta 
           #---------------------------------------------------------------------------------------
           if (orb_D[wp][point_k][Band_n] != 0 and lorbit >= 11):
              orb_Dxy[wp][point_k][Band_n]  =  (orb_Dxy[wp][point_k][Band_n])/orb_D[wp][point_k][Band_n]
              orb_Dyz[wp][point_k][Band_n]  =  (orb_Dyz[wp][point_k][Band_n])/orb_D[wp][point_k][Band_n]
              orb_Dz2[wp][point_k][Band_n]  =  (orb_Dz2[wp][point_k][Band_n])/orb_D[wp][point_k][Band_n]
              orb_Dxz[wp][point_k][Band_n]  =  (orb_Dxz[wp][point_k][Band_n])/orb_D[wp][point_k][Band_n]
              orb_Dx2[wp][point_k][Band_n]  =  (orb_Dx2[wp][point_k][Band_n])/orb_D[wp][point_k][Band_n]           
           #--------------------------------------------------------------------------------------------           
           if (lorbit >= 11):
              c_red    =  orb_Dyz[wp][point_k][Band_n] + orb_Dx2[wp][point_k][Band_n] + 0.737254902*(orb_Dxz[wp][point_k][Band_n]) 
              c_green  =  orb_Dz2[wp][point_k][Band_n] + 0.560784313*(orb_Dxz[wp][point_k][Band_n])
              c_blue   =  orb_Dxy[wp][point_k][Band_n] + orb_Dx2[wp][point_k][Band_n] + 0.560784313*(orb_Dxz[wp][point_k][Band_n])
              #--------------------------------
              if (c_red > 1.0):   c_red   = 1.0
              if (c_green > 1.0): c_green = 1.0
              if (c_blue > 1.0):  c_blue  = 1.0
              #----------------------------------------------
              color_rgb.write(f' {c_red} {c_green} {c_blue}')            

           color_rgb.write(f' \n')

#----------------
color_rgb.close()
#----------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Orbitais.py para o diretório de saida -------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Orbitais.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Orbitais/Orbitais.py'); f.close(); os.remove(dir_files + '/output/Orbitais/Orbitais.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_orbitais.py'
destination = dir_files + '/output/Orbitais/Orbitais.py'
shutil.copyfile(source, destination)

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Orbitais.py possa ser executado isoladamente ---
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'r')
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

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------
exec(open(dir_files + '/output/Orbitais/Orbitais.py').read())
#------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
