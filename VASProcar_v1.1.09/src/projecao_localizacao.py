
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
print ("A ordem em que os ions sao adicionados, nao altera o resultado")
print ("==============================================================")
print ("Exemplos:                                                     ")
print ("--------------------------------------------------------------")
print ("rotulo:  Surface                                              ")
print ("intervalos_de_ions 1:5 7:9 15:27 11:11                        ")
print ("                                                              ") 
print ("rotulo:  Bulk                                                 ")
print ("intervalos_de_ions 7:49 50:53                                 ")
print ("                                                              ") 
print ("rotulo:  Edge                                                 ")
print ("intervalos_de_ions 3:3                                        ")
print ("##############################################################")
print(" ")

print ("##############################################################")
print ("Qual o numero de diferentes REGIOES da rede a ser analisada?  ")
print ("============ (Sao permitido no maximo 6 REGIOES) =============")
print ("##############################################################")
n_reg = input (" "); n_reg = int(n_reg)
print(" ")

if (n_reg <= 0): n_reg = 1
if (n_reg > 6):  n_reg = 6

label_reg = ['null']*(6)

for i in range(1,(n_reg+1)):

    print ("==============================================================")
    print (f'Digite o rotulo da REGIAO_{i}: =================================')
    print ("==============================================================")
    label_reg[i-1] = input ("rotulo: "); label_reg[i-1] = str(label_reg[i-1])
    print(" ")

    if (i == 1): loop_cha = "A"
    if (i == 2): loop_cha = "B"
    if (i == 3): loop_cha = "C"
    if (i == 4): loop_cha = "D"
    if (i == 5): loop_cha = "E"    
    if (i == 6): loop_cha = "F"
       
    print ("==============================================================")
    print (f'Digite os intervalos_de_ions da REGIAO_{i}: ====================')
    print ("==============================================================")
    ion_range = input ("intervalos_de_ions  ")
    print (" ")
    #--------------------------------------------------
    selected_ions = ion_range.replace(':', ' ').split()
    loop = int(len(selected_ions)/2)
    #--------------------------------------------------

    for j in range (1,(loop+1)):
        #-------------------------------------
        loop_i = int(selected_ions[((j-1)*2) +0])
        loop_f = int(selected_ions[((j-1)*2) +1])
        #----------------------------------------------------------------------------------------
        if ((loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
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
   print ("Deseja alterar o padrao de cores das projecoes de cada REGIAO?")
   print ("[0] NAO                                                       ")
   print ("[1] SIM                                                       ")
   print ("##############################################################") 
   esc_color = input (" "); esc_color = int(esc_color)
   print (" ")  

   if (esc_color == 1):
      print ("##############################################################")
      print ("Codigo de cores:                                              ")
      print ("0  White   | 1  Black | 2  Red    | 3  Green  | 4  Blue       ")
      print ("5  Yellow  | 6  Borwn | 7  Grey   | 8  Violet | 9  Cyan       ")
      print ("10 Magenta |11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa   ")
      print ("15 Dark_Green                                                 ")
      print ("##############################################################")       
      print ("Padrao de cores do VASProcar:                                 ")
      print ("                                                              ")
      print ("Cor das REGIOES 1|2|3|4|5|6:  4 2 3 10 9 5                    ")
      print ("(Blue, Red, Green, Magenta, Cyan, Yellow)                     ")
      print ("##############################################################") 
      print (" ")

      print ("==============================================================") 
      print ("Digite em sequencia as cores das REGIOES que vc definiu:      ")
      cor_reg = input ("Cores_das_REGIOES: ")
      #---------------------
      tcor = cor_reg.split()
      #-------------------------
      for i in range(len(tcor)):         
          if (i == 0): c_Reg1 = int(tcor[0])
          if (i == 1): c_Reg2 = int(tcor[1])
          if (i == 2): c_Reg3 = int(tcor[2])
          if (i == 3): c_Reg4 = int(tcor[3])
          if (i == 4): c_Reg5 = int(tcor[4])
          if (i == 5): c_Reg6 = int(tcor[5])
      #-------------------------------------
      print (" ") 

   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
   print ("##############################################################")
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ")    

   print ("##############################################################") 
   print ("Do you want to modify the energy range to be plotted? ========")
   print ("[0] NOT                                                       ")
   print ("[1] YES                                                       ")
   print ("##############################################################")
   esc_range_E = input (" "); esc_range_E = int(esc_range_E)
   print (" ")

   if (esc_range_E == 1):
      print ("##############################################################") 
      print ("Enter the energy range to be plotted: ========================")
      print ("Note: Enter the lowest and highest energy value to be plotted ")
      print ("            in relation to the Fermi Level                    ")
      print ("Examples:                                                     ")
      print ("--------------------------------------------------------------")
      print ("E_min E_max: -3.0 15.0                                        ")
      print ("E_min E_max: -5.1 5.0                                         ")
      print ("##############################################################")      
      range_E = input ("E_min E_max:  ")
      print (" ")
      #--------------------------------------------------
      selected_energ = range_E.replace('-', ' -').replace('+', ' +').replace(':', ' ').split()
      E_min = float(selected_energ[0])
      E_max = float(selected_energ[1])

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
   print ("      o valor de transparencia utilizado, comece por 0.1 =====")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")    

if (escolha == 1):
   esc_fermi = 1
   esc_range_E = 0
   dest_k = 1
   Dimensao = 1
   l_symmetry = 0
   peso_total = 1.0
   transp = 1.0
 
#======================================================================
# Obtaining the results from DFT outpout files ========================
#======================================================================
read_orb = 1
execute_python_file(filename = DFT + '_nscf.py')

#----------------------------
if (esc_fermi == 0):
   dE_fermi = 0.0
   dest_fermi = Efermi

if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1)
   dest_fermi = 0.0

if (esc_range_E == 0):
   E_min = energ_min - Efermi
   E_max = energ_max - Efermi
#----------------------------

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

Prop = [[[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(6+1)]   # Prop[6][wp][nk][nb]
# Prop[1][wp][nk][nb] = Proporção de contribuição da Região_1 (A)
# Prop[2][wp][nk][nb] = Proporção de contribuição da Região_2 (B)
# Prop[3][wp][nk][nb] = Proporção de contribuição da Região_3 (C)
# Prop[4][wp][nk][nb] = Proporção de contribuição da Região_4 (D)
# Prop[5][wp][nk][nb] = Proporção de contribuição da Região_5 (E)
# Prop[6][wp][nk][nb] = Proporção de contribuição da Região_6 (F)

atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*(4+1)

num_A = 0
num_B = 0
num_C = 0
num_D = 0
num_E = 0
num_F = 0

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
            Regiao_F = 0.0
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            Soma_D = 0.0
            Soma_E = 0.0
            Soma_F = 0.0
            
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

                if (temp_sm == "F"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_F          =  Soma_F     +  Contrib[ion_n]
                   Regiao_F        =  Regiao_F   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n] 

            #----------------------------------------------------------           
            # End of the loop over ions -------------------------------
            #----------------------------------------------------------

            if (Regiao_A != 0.0): num_A = 1
            if (Regiao_B != 0.0): num_B = 1
            if (Regiao_C != 0.0): num_C = 1
            if (Regiao_D != 0.0): num_D = 1
            if (Regiao_E != 0.0): num_E = 1
            if (Regiao_F != 0.0): num_F = 1

            if (orb_total != 0.0):
               Prop[1][wp][point_k][Band_n] = (Regiao_A/orb_total)   # Proporção de contribuição da Região A
               Prop[2][wp][point_k][Band_n] = (Regiao_B/orb_total)   # Proporção de contribuição da Região B
               Prop[3][wp][point_k][Band_n] = (Regiao_C/orb_total)   # Proporção de contribuição da Região C
               Prop[4][wp][point_k][Band_n] = (Regiao_D/orb_total)   # Proporção de contribuição da Região D
               Prop[5][wp][point_k][Band_n] = (Regiao_E/orb_total)   # Proporção de contribuição da Região E
               Prop[6][wp][point_k][Band_n] = (Regiao_F/orb_total)   # Proporção de contribuição da Região F

            if (orb_total == 0.0):
               Prop[1][wp][point_k][Band_n] = 0.0
               Prop[2][wp][point_k][Band_n] = 0.0
               Prop[3][wp][point_k][Band_n] = 0.0
               Prop[4][wp][point_k][Band_n] = 0.0
               Prop[5][wp][point_k][Band_n] = 0.0
               Prop[6][wp][point_k][Band_n] = 0.0
      
            #-----------------------------------------------------------------------

            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
               Soma_D = (Soma_D/orb_total)*100
               Soma_E = (Soma_E/orb_total)*100
               Soma_F = (Soma_F/orb_total)*100
               
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0
               Soma_D = 0.0
               Soma_E = 0.0
               Soma_F = 0.0

            if (Soma_A != 0): contribuicao.write(f'Region_1 ({label_reg[0]}):  {Soma_A:.3f}% \n')
            if (Soma_B != 0): contribuicao.write(f'Region_2 ({label_reg[1]}):  {Soma_B:.3f}% \n')
            if (Soma_C != 0): contribuicao.write(f'Region_3 ({label_reg[2]}):  {Soma_C:.3f}% \n')
            if (Soma_D != 0): contribuicao.write(f'Region_4 ({label_reg[3]}):  {Soma_D:.3f}% \n')
            if (Soma_E != 0): contribuicao.write(f'Region_5 ({label_reg[4]}):  {Soma_E:.3f}% \n')
            if (Soma_F != 0): contribuicao.write(f'Region_6 ({label_reg[5]}):  {Soma_F:.3f}% \n')
               
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
                
                if (Reg[ion_n] == "A"): palavra = "(Region_1)"
                if (Reg[ion_n] == "B"): palavra = "(Region_2)"
                if (Reg[ion_n] == "C"): palavra = "(Region_3)"
                if (Reg[ion_n] == "D"): palavra = "(Region_4)"
                if (Reg[ion_n] == "E"): palavra = "(Region_5)"   
                if (Reg[ion_n] == "F"): palavra = "(Region_6)"
                   
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
            for l in range (1,(6+1)):
                Localizacao.write(f' {Prop[l][i][j][k]}')
            Localizacao.write(f' \n')
                
#------------------
Localizacao.close()
#------------------

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

   print(" ")
   print ("================ Plotando as Projecoes (Grace) ================")

   execute_python_file(filename = 'plot/Grace/plot_projecao_localizacao.py')

   print ("Plot das projecoes via Grace (arquivos .agr) concluido --------")

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
linha += 1; lines.insert(linha, '# [2022-2023] CNPEM|Ilum|LNNano (Campinas-SP/Brazil)                   \n')
linha += 1; lines.insert(linha, '# [2007-2022] Federal University of Uberlandia (Uberlândia-MG/Brazil)  \n')
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
linha += 1; lines.insert(linha, f'num_A = {num_A}; num_B = {num_B}; num_C = {num_C}; num_D = {num_D}; num_E = {num_E}; num_F = {num_F}  #  Parametros de controle do plot das projecoes das Regioes/Localizacao \n')
linha += 1; lines.insert(linha, f'label_reg = {label_reg}  #  Rotulos das Regioes \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}    #  Total Num. of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk = {nk}                #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}                #  Total Num. of bands \n')
linha += 1; lines.insert(linha, f'E_min = {E_min}          #  Lower energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'E_max = {E_max}          #  Higher energy value of the bands in the plot (in relation to the Fermi level) \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}    #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}      #  [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'peso_total = {peso_total}  #  peso/tamanho das esferas no plot das projecões \n')
linha += 1; lines.insert(linha, f'transp = {transp}          #  Transparencia aplicada ao plot das projecoes \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}          #  [0] DO NOT label the k-points; [1] highlight k-points present in KPOINTS file; [2] Customize: highlight and Label k-points \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}        #  K-points coordinates to be highlighted in the band structure \n')

if (dest_k != 2):
   label_pk = ['null']*len(dest_pk) 
#-------------------------------------------------------------------------------
if (dest_k == 2): 
   for i in range(contador2):
       for j in range(34):
           if (label_pk[i] == '#' + str(j+1)):
              label_pk[i] = r_matplot[j]    
       if (DFT == '_QE/' and l_symmetry == 1):
          label_pk[i] = label_pk[i] + '$_{(' + symmetry_pk[i] + ')}$' 
#------------------------------------------------------------------------------
linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  K-points label \n')
#------------------------------------------------------------------------------

if (sum_save == 0): save_png = 1
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_svg = {save_svg}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#======================================================================== \n')
linha += 1; lines.insert(linha, '# Codigo de cores:                                                        \n')
linha += 1; lines.insert(linha, '# 0  White  | 1  Black  | 2  Red    | 3  Green    | 4  Blue    | 5 Yellow \n')
linha += 1; lines.insert(linha, '# 6  Borwn  | 7  Grey   | 8  Violet | 9  Cyan     | 10 Magenta |          \n')
linha += 1; lines.insert(linha, '# 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green   |          \n')
linha += 1; lines.insert(linha, '#------------------------------------------------------------------------ \n')
linha += 1; lines.insert(linha, '# Cores aplicadas as REGIOES:                                             \n')
linha += 1; lines.insert(linha, f'c_Reg1 = {c_Reg1}; c_Reg2 = {c_Reg2}; c_Reg3 = {c_Reg3}; c_Reg4 = {c_Reg4}; c_Reg5 = {c_Reg5}; c_Reg6 = {c_Reg6} \n') 
linha += 1; lines.insert(linha, '#======================================================================== \n')

file = open(dir_files + '/output/Localizacao/Localizacao.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------------------
if (sum_save != 0):
   exec(open(dir_files + '/output/Localizacao/Localizacao.py').read())
#---------------------------------------------------------------------

#=======================================================================

print(" ")
print("==============================================================")
print("= Edite o Plot das projecoes por meio dos seguintes arquivos =")
print("= Localizacao.py ou .agr (via Grace) gerados na pasta ========")
print("= output/Localizacao =========================================")
print("==============================================================")

#-----------------------------------------------------------------------
print(" ")
print("-------------------------- Concluido! --------------------------")
#-----------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
