
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Localizacao' exists ------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Localizacao'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Localizacao')
#---------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

ABC = [0]*(ni+1)            
rotulo_A = 'null'; rotulo_B = 'null'; rotulo_C = 'null'; rotulo_D = 'null'; rotulo_E = 'null'

for i in range (1,(ni+1)):
    ABC[i] = 'X'

#======================================================================
# Get the input from user =============================================
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
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")    

   print ("##############################################################")
   print ("Would you like to label the k-points?                         ")
   print ("[0] DO NOT label the k-points  ===============================")
   print ("[1] highlight k-points present in KPOINTS file ===============")
   print ("[2] Customize: highlight and Label k-points   ================")
   print ("##############################################################")  
   dest_k = input (" "); dest_k = int(dest_k)
   print (" ")

   if (DFT == '_QE/' and dest_k == 2):
      print ("##############################################################")
      print ("Deseja inserir as simetrias como rotulo dos pontos-k?         ")
      print ("[0] NAO                                                       ")
      print ("[1] SIM                                                       ")
      print ("##############################################################") 
      l_symmetry = input (" "); l_symmetry = int(l_symmetry)
      print (" ")    

   if (dest_k == 2):
      print ("##############################################################")
      print ("label.TXT file should be found inside the 'output' folder ====")
      print ("after reading the PROCAR file ================================")
      print ("##############################################################") 
      print (" ")

      Dimensao = 1

   if (dest_k != 2):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] 2pi/Param. (Param. in Angs.) =============================")
      print ("[2] 1/Angs. ==================================================")
      print ("[3] 1/nm.   ==================================================")
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
   l_symmetry = 0
   peso_total = 1.0
   transp = 1.0

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0   
   
#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
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
############################# PROCAR loop #############################
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
    ####################### Loop over k-points: #######################
    ###################################################################      

    for point_k in range(1, (nk+1)):                                  
        
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(f'K-point {point_k}: Direct coord. ({kb1[wp][point_k]}, {kb2[wp][point_k]}, {kb3[wp][point_k]}) \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(" \n")      

        ###############################################################
        ####################### Loop over Bands #######################
        ###############################################################

        for Band_n in range (1, (nb+1)):

            contribuicao.write("================================================================= \n")
            contribuicao.write(f'Band {Band_n} \n')
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
            ##################### Loop over Ions: #####################
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
            # End of the loop over ions -------------------------------
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
               contribuicao.write(f'Region_1 ({rotulo_A}):  {Soma_A:.3f}% \n')
            if (Soma_B != 0):
               contribuicao.write(f'Region_2 ({rotulo_B}):  {Soma_B:.3f}% \n')
            if (Soma_C != 0):
               contribuicao.write(f'Region_3 ({rotulo_C}):  {Soma_C:.3f}% \n')
            if (Soma_D != 0):
               contribuicao.write(f'Region_4 ({rotulo_D}):  {Soma_D:.3f}% \n')
            if (Soma_E != 0):
               contribuicao.write(f'Region_5 ({rotulo_E}):  {Soma_E:.3f}% \n')

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

                contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribution: {Contrib[ion_n]:6,.3f}% | Sum: {Soma:>7,.3f}% | {palavra} \n')

            contribuicao.write(" \n")

        #----------------------------------------------------------
        # End of the loop over bands ------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # End of the loop over K-points ---------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# End of the PROCAR loop ----------------------------------
#----------------------------------------------------------

#-------------------    
contribuicao.close()
#-------------------

#======================================================================
# Saving data to plot the projections =================================
#====================================================================== 

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
# Getting k-points / labels ===========================================
#======================================================================
execute_python_file(filename = DFT + '_label.py')

print (" ")          
print ("===============================================")

#========================================================================
#========================================================================
# Projections Plot using (GRACE) ========================================
#======================================================================== 
#========================================================================
if (save_agr == 1):
   execute_python_file(filename = 'plot/Grace/plot_projecao_localizacao.py')

#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Localizacao.py to the output folder directory ------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Localizacao/Localizacao.py'); f.close(); os.remove(dir_files + '/output/Localizacao/Localizacao.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_localizacao.py'
destination = dir_files + '/output/Localizacao/Localizacao.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, f'# {VASProcar_name} \n')
linha += 1; lines.insert(linha, f'# {url_1} \n')
linha += 1; lines.insert(linha, f'# {url_2} \n')
linha += 1; lines.insert(linha, '###################################################################### \n')
linha += 1; lines.insert(linha, '# Authors:                                                             \n')
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
linha += 1; lines.insert(linha, '# These are the parameters that allows the code to run separatedly === \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'num_A = {num_A}; num_B = {num_B}; num_C = {num_C}; num_D = {num_D}; num_E = {num_E}  #  Parametros de controle do plot das projecoes das Regioes/Localizacao \n')
linha += 1; lines.insert(linha, f'rotulo_A = "{rotulo_A}"; rotulo_B = "{rotulo_B}"; rotulo_C = "{rotulo_C}"; rotulo_D = "{rotulo_D}"; rotulo_E = "{rotulo_E}"  #  Rotulos das Regioes \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}    #  Total Num. of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk  = {nk}               #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}                #  Total Num. of bands \n')
linha += 1; lines.insert(linha, f'energ_min = {energ_min}  #  Lower energy value of the bands in the plot \n')
linha += 1; lines.insert(linha, f'energ_max = {energ_max}  #  Higher energy value of the bands in the plot \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}    #  [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'peso_total = {peso_total}  #  peso/tamanho das esferas no plot das projecões \n')
linha += 1; lines.insert(linha, f'transp = {transp}          #  Transparencia aplicada ao plot das projecoes \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}          #  [0] DO NOT label the k-points; [1] highlight k-points present in KPOINTS file; [2] Customize: highlight and Label k-points \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}        #  K-points coordinates to be highlighted in the band structure \n')

if (dest_k == 2): 
   for i in range(contador2):
       for j in range(34):
           if (label_pk[i] == '#' + str(j+1)):
              label_pk[i] = r_matplot[j]    
       if (DFT == '_QE/' and l_symmetry == 1):
          label_pk[i] = label_pk[i] + '$_{(' + symmetry_pk[i] + ')}$' 
   #-------------------------------------------------------------- 
   linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  K-points label \n')

linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------
exec(open(dir_files + '/output/Localizacao/Localizacao.py').read())
#------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
