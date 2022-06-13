
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------------
# Verificando se a pasta "Localizacao" existe, se não existe ela é criada ---
#----------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Localizacao'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Localizacao')
#---------------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

ABC = [0]*(ni+1)            # Inicilização do vetor ABC
rotulo_A = 'null'; rotulo_B = 'null'; rotulo_C = 'null'; rotulo_D = 'null'; rotulo_E = 'null'

for i in range (1,(ni+1)):  # Por padrão todos os ions pertencem a Região E
    ABC[i] = 'X'

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Localizacao dos Estados: ##################")
print ("##############################################################") 
print (" ")

print ("##############################################################")
print ("Para definir uma dada REGIAO da rede cristalina, voce deve    ")
print ("informar os ions que pertencem a esta REGIAO, por meio de     ")
print ("intervalos_de_ions.                                           ")
print ("==============================================================")
print ("Para uma dada REGIAO, voce pode informar quantos intervalos_de")
print ("_ions achar necessario.                                       ")
print ("==============================================================")
print ("A ordem em que os ions são adicionados, nao altera o resultado")
print ("==============================================================")
print ("intervalos_de_ions: 1-5 3-9 11-11 15-27                       ")          
print ("intervalos_de_ions: 7-49 50-53                                ")
print ("intervalos_de_ions: 3-3                                       ")
print ("##############################################################")
print(" ")

print ("##############################################################")
print ("Qual o numero de diferentes REGIOES da rede a ser analisada?  ")
print ("============ (Sao permitido no maximo 5 REGIOES) ===========  ")
print ("##############################################################")
n_reg = input (" "); n_reg = int(n_reg)
print(" ")

if (n_reg <= 0): n_reg = 1
if (n_reg > 5):  n_reg = 5

print ("##############################################################")
print ("Escolha os intervalos_de_ions correspondentes a cada REGIAO:  ")
print ("Digite como nos exemplos abaixo ============================= ")
print ("--------------------------------------------------------------")
print ("A ordem em que os ions são adicionados, nao altera o resultado")
print ("--------------------------------------------------------------")
print ("rotulo intervalos_de_ions:  superficie 1-5 3-9 11-11 15-27    ")          
print ("rotulo intervalos_de_ions:  bulk 7-49 50-53                   ")
print ("rotulo intervalos_de_ions:  borda 3-3                         ")
print ("##############################################################")
print(" ")

for i in range(1,(n_reg+1)):

    print ("==============================================================")
    print (f'Digite o rotulo e o intervalor_de_ions da REGIAO_{i}: ==========')
    print ("==============================================================")
    ion_range = input ("rotulo intervalo_de_ions: ")
    print (" ")
    #--------------------------------------------------
    selected_ions = ion_range.replace('-', ' ').split()
    loop = int((len(selected_ions) -1)/2)
    #--------------------------------------------------

    rotulo = str(selected_ions[0])
    
    if (i == 1):
       loop_cha = "A"; rotulo_A = rotulo
    if (i == 2):
       loop_cha = "B"; rotulo_B = rotulo
    if (i == 3):
       loop_cha = "C"; rotulo_C = rotulo
    if (i == 4):
       loop_cha = "D"; rotulo_D = rotulo
    if (i == 5):
       loop_cha = "E"; rotulo_E = rotulo
      
    for j in range (1,(loop+1)):
        #----------------------------------------
        loop_i = int(selected_ions[((j-1)*2) +1])
        loop_f = int(selected_ions[((j-1)*2) +2])
        #----------------------------------------------------------------------
        if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
           print (" ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print ("   ERRO: Os valores de ions informados estao incorretos   ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           confirmacao = input (" ")
           exit()
        #----------------------------------------------------------------------           
        for k in range (loop_i, (loop_f+1)):
            ABC[k] = loop_cha 

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
   print ("Esta opcao e util para verificar a sobreposicao de regioes.   ")   
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
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

Prop = [[[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]   # Prop[5][wp][nk][nb]
# Prop[1][wp][nk][nb] = Proporção de contribuição da Região_1 (A)
# Prop[2][wp][nk][nb] = Proporção de contribuição da Região_2 (B)
# Prop[3][wp][nk][nb] = Proporção de contribuição da Região_3 (C)
# Prop[4][wp][nk][nb] = Proporção de contribuição da Região_4 (D)
# Prop[5][wp][nk][nb] = Proporção de contribuição da Região_5 (E)
   
atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*(4+1)

num_A = 0
num_B = 0
num_C = 0
num_D = 0
num_E = 0

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

#-----------------------------------------------------------------------------------
contribuicao = open(dir_files + '/output/Localizacao/Contribuicao_Regioes.txt', 'w')
#-----------------------------------------------------------------------------------

for wp in range(1, (n_procar+1)):    
      
    if (n_procar > 1):
       contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contribuicao.write(f'PROCAR {wp} \n')
       contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contribuicao.write(" \n")
      
    ###################################################################
    ###################### Loop dos Pontos_k ##########################
    ###################################################################

    for point_k in range(1, (nk+1)):                                  
        
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(f'Ponto-k {point_k}: Coord. Diretas ({kb1[wp][point_k]}, {kb2[wp][point_k]}, {kb3[wp][point_k]}) \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(" \n")      

        ###############################################################
        ################### Loop dos Bandas ###########################
        ###############################################################

        for Band_n in range (1, (nb+1)):

            contribuicao.write("================================================================= \n")
            contribuicao.write(f'Banda {Band_n} \n')
            contribuicao.write("================================================================= \n")          

            orb_total = 0.0
            Regiao_A = 0.0
            Regiao_B = 0.0
            Regiao_C = 0.0
            Regiao_D = 0.0
            Regiao_E = 0.0
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            Soma_D = 0.0
            Soma_E = 0.0
            
            ###########################################################
            ################ Loop dos ions ############################
            ###########################################################

            for ion_n in range (1, (ni+1)):
               
                #----------------------
                atomo[ion_n] = ion_n
                temp_sm = ABC[ion_n]
                Reg[ion_n] = ABC[ion_n]
                #----------------------

                if (temp_sm == "A"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_A          =  Soma_A     +  Contrib[ion_n]
                   Regiao_A        =  Regiao_A   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]  
                  
                if (temp_sm == "B"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_B          =  Soma_B     +  Contrib[ion_n]
                   Regiao_B        =  Regiao_B   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]  

                if (temp_sm == "C"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_C          =  Soma_C     +  Contrib[ion_n]
                   Regiao_C        =  Regiao_C   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]                 

                if (temp_sm == "D"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_D          =  Soma_D     +  Contrib[ion_n]
                   Regiao_D        =  Regiao_D   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n] 

                if (temp_sm == "E"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_E          =  Soma_E     +  Contrib[ion_n]
                   Regiao_E        =  Regiao_E   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n] 

            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------

            if (Regiao_A != 0.0): num_A = 1
            if (Regiao_B != 0.0): num_B = 1
            if (Regiao_C != 0.0): num_C = 1
            if (Regiao_D != 0.0): num_D = 1
            if (Regiao_E != 0.0): num_E = 1

            if (orb_total != 0.0):
               Prop[1][wp][point_k][Band_n] = (Regiao_A/orb_total)   # Proporção de contribuição da Região A
               Prop[2][wp][point_k][Band_n] = (Regiao_B/orb_total)   # Proporção de contribuição da Região B
               Prop[3][wp][point_k][Band_n] = (Regiao_C/orb_total)   # Proporção de contribuição da Região C
               Prop[4][wp][point_k][Band_n] = (Regiao_D/orb_total)   # Proporção de contribuição da Região D
               Prop[5][wp][point_k][Band_n] = (Regiao_E/orb_total)   # Proporção de contribuição da Região E

            if (orb_total == 0.0):
               Prop[1][wp][point_k][Band_n] = 0.0
               Prop[2][wp][point_k][Band_n] = 0.0
               Prop[3][wp][point_k][Band_n] = 0.0
               Prop[4][wp][point_k][Band_n] = 0.0
               Prop[5][wp][point_k][Band_n] = 0.0
      
            #-----------------------------------------------------------------------

            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
               Soma_D = (Soma_D/orb_total)*100
               Soma_E = (Soma_E/orb_total)*100
               
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0
               Soma_D = 0.0
               Soma_E = 0.0

            if (Soma_A != 0):
               contribuicao.write(f'Regiao_1 ({rotulo_A}):  {Soma_A:.3f}% \n')
            if (Soma_B != 0):
               contribuicao.write(f'Regiao_2 ({rotulo_B}):  {Soma_B:.3f}% \n')
            if (Soma_C != 0):
               contribuicao.write(f'Regiao_3 ({rotulo_C}):  {Soma_C:.3f}% \n')
            if (Soma_D != 0):
               contribuicao.write(f'Regiao_4 ({rotulo_D}):  {Soma_D:.3f}% \n')
            if (Soma_E != 0):
               contribuicao.write(f'Regiao_5 ({rotulo_E}):  {Soma_E:.3f}% \n')

            contribuicao.write("======================= \n")
            
            ##################################################################
            ##################################################################
            ##################################################################

            for j in range (1,(ni+1)):
               rotulo_temp[j] = rotulo[j]

            nj = (ni - 1)
                     
            for k in range (1,(nj+1)):
                wy = (ni - k)
                for l in range (1,(wy+1)):
                    if (Contrib[l] < Contrib[l+1]):
                     tp1 = Contrib[l]
                     Contrib[l] = Contrib[l+1]
                     Contrib[l+1] = tp1
                     #--------------------
                     tp2 = atomo[l]
                     atomo[l] = atomo[l+1]
                     atomo[l+1] = tp2
                     #--------------------                    
                     tp3 = Reg[l]
                     Reg[l] = Reg[l+1]
                     Reg[l+1] = tp3
                     #--------------------
                     tp4 = rotulo_temp[l]
                     rotulo_temp[l] = rotulo_temp[l+1]
                     rotulo_temp[l+1] = tp4                     

            for ion_n in range (1,(ni+1)):
                if (orb_total != 0):
                   Contrib[ion_n] = (Contrib[ion_n]/orb_total)*100
                Soma = Soma + Contrib[ion_n]
                
                if (Reg[ion_n] == "A"):
                   palavra = "(Regiao_1)"
                if (Reg[ion_n] == "B"):
                   palavra = "(Regiao_2)"
                if (Reg[ion_n] == "C"):
                   palavra = "(Regiao_3)"
                if (Reg[ion_n] == "D"):
                   palavra = "(Regiao_4)"
                if (Reg[ion_n] == "E"):
                   palavra = "(Regiao_5)"   

                contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {Contrib[ion_n]:6,.3f}% | Soma: {Soma:>7,.3f}% | {palavra} \n')

            contribuicao.write(" \n")

        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------

#-------------------    
contribuicao.close()
#-------------------

#========================================================================
# Gravando a informação das bandas para o Plot das Projeções ============
#========================================================================

#---------------------------------------------------------------
bandas = open(dir_files + '/output/Localizacao/Bandas.dat', 'w')
#---------------------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------

#===============================================================================
# Gravando a informação da contribuição de cada região para o Plot das Projeções
#===============================================================================

#-------------------------------------------------------------------------
Localizacao = open(dir_files + '/output/Localizacao/Localizacao.dat', 'w')
#-------------------------------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            Localizacao.write(f'{xx[i][j]} {Energia[i][j][k]}')
            for l in range (1,(5+1)):
                Localizacao.write(f' {Prop[l][i][j][k]}')
            Localizacao.write(f' \n')
                
#------------------
Localizacao.close()
#------------------

#====================================================================================================================================
# Obtendo e gravando as cores no padrão RGB que designam cada região bem como cada combinação de região para o Plot das Projeções ===
#====================================================================================================================================

#---------------------------------------------------------------------
color_rgb = open(dir_files + '/output/Localizacao/color_rgb.dat', 'w')
#---------------------------------------------------------------------

number = -1
for k in range (1, (nb+1)):
    for i in range (1, (n_procar+1)):
        for j in range (1, (nk+1)):       
           number += 1
           
           #---------------------------------------------------------------------------------------------------------------------------------------------         
           # Notação do Matplotlib para o padrão RGB de cores: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------
           # c_red = [1, 0, 0]; c_green = [0, 1, 0]; c_blue = [0, 0, 1]; c_rosybrown = [0.737254902, 0.560784313, 0.560784313]; c_magenta = [1, 0, 1] ---           
           #---------------------------------------------------------------------------------------------------------------------------------------------

           #-----------------------------------------------------------------------------
           # Reg_A = blue; Reg_B = red; Reg_C = green; Reg_D = rosybrown; Reg_E = magenta
           #-----------------------------------------------------------------------------
           # Reg_A = Prop[1][i][j][k]; Reg_B = Prop[2][i][j][k]; Reg_C = Prop[3][i][j][k]
           # Reg_D = Prop[4][i][j][k]; Reg_E = Prop[5][i][j][k] 
           #-----------------------------------------------------------------------------
           
           c_red    =  Prop[2][i][j][k] + 0.737254902*(Prop[4][i][j][k]) + Prop[5][i][j][k] 
           c_green  =  Prop[3][i][j][k] + 0.560784313*(Prop[4][i][j][k])
           c_blue   =  Prop[1][i][j][k] + 0.560784313*(Prop[4][i][j][k]) + Prop[5][i][j][k]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #------------------------------------------------
           color_rgb.write(f'{c_red} {c_green} {c_blue} \n')            

#----------------
color_rgb.close()
#----------------

#======================================================================
# Obtendo o nº pontos-k a serem destacados bem como os seus rótulos ===
#======================================================================
execute_python_file(filename = DFT + '_label.py')

print (" ")          
print ("===============================================")

#========================================================================
#========================================================================
# Plot das Projeções da Localização (Grace) =============================
#======================================================================== 
#========================================================================
if (save_agr == 1):
   execute_python_file(filename = 'plot/Grace/plot_projecao_localizacao.py')

#========================================================================
#========================================================================
# Plot das Projeções da Localização (Matplotlib) ========================
#========================================================================
#========================================================================

# Copiando o codigo Localizacao.py para o diretório de saida ------------

# Teste para saber se o arquivo Localizacao.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Localizacao/Localizacao.py'); f.close(); os.remove(dir_files + '/output/Localizacao/Localizacao.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_localizacao.py'
destination = dir_files + '/output/Localizacao/Localizacao.py'
shutil.copyfile(source, destination)

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Localizacao.py possa ser executado isoladamente ---
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'r')
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
linha += 1; lines.insert(linha, f'num_A = {num_A}; num_B = {num_B}; num_C = {num_C}; num_D = {num_D}; num_E = {num_E}  #  Parametros de controle do plot das projecoes das Regioes/Localizacao \n')
linha += 1; lines.insert(linha, f'rotulo_A = "{rotulo_A}"; rotulo_B = "{rotulo_B}"; rotulo_C = "{rotulo_C}"; rotulo_D = "{rotulo_D}"; rotulo_E = "{rotulo_E}"  #  Rotulos das Regioes \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}  #  Numero de arquivos PROCAR a serem lidos \n')
linha += 1; lines.insert(linha, f'nk  = {nk}  #  Numero de pontos-k do calculo \n')
linha += 1; lines.insert(linha, f'nb = {nb}  #  Numero de bandas do calculo \n')
linha += 1; lines.insert(linha, f'energ_min = {energ_min}  #  Menor valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'energ_max = {energ_max}  #  Maior valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'peso_total = {peso_total}  #  peso/tamanho das esferas no plot das projecões \n')
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

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------
exec(open(dir_files + '/output/Localizacao/Localizacao.py').read())
#------------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
