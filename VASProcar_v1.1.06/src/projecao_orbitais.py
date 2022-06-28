
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Orbitais' exists ---------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Orbitais'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Orbitais')
#------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("############### Projecao dos Orbitais (S,P,D): ###############")
print ("##############################################################") 
print (" ")

if (escolha == -1):

   print ("##############################################################") 
   print ("with respect to energy, would you like? ======================")
   print ("[0] Use the default energy value from DFT output =============")
   print ("[1] Shift the Fermi level to 0.0 eV  =========================")
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
      print ("Escolha os intervalos_de_ions a serem analisados: =========== ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("A ordem em que os ions são adicionados, nao altera o resultado")
      print ("--------------------------------------------------------------")
      print ("intervalos_de_ions: 1-5 3-9 11-11 15-27                       ")          
      print ("intervalos_de_ions: 7-49 50-53                                ")
      print ("intervalos_de_ions: 3-3                                       ")
      print ("##############################################################")
      ion_range = input ("intervalo_de_ions: ")
      print (" ")
      #--------------------------------------------------
      selected_ions = ion_range.replace('-', ' ').split()
      loop = int(len(selected_ions)/2)
      #--------------------------------------------------
      
      for i in range (1,(loop+1)):
          #----------------------------------------
          loop_i = int(selected_ions[(i-1)*2])
          loop_f = int(selected_ions[((i-1)*2) +1])
          #----------------------------------------------------------------------
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             confirmacao = input (" ")
             exit()
          #----------------------------------------------------------------------           
          for j in range(loop_i, (loop_f + 1)):
              sim_nao[j] = "sim"    

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
   
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = Orbital portion (S, P or D) referring to each "ni" ion
#  soma_orb = Orbital sum (S, P or D) over all selected "ni" ions
#  tot      = Sum over all orbitals and all ions

color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb]

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

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

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
            # End of the loop over ions -------------------------------
            #----------------------------------------------------------  

            for orb_n in range (1, (n_orb+1)):
                if (total[wp][point_k][Band_n] != 0.0 and DFT == '_VASP/'):
                   soma_orb[wp][orb_n][point_k][Band_n] = ( soma_orb[wp][orb_n][point_k][Band_n]/total[wp][point_k][Band_n] )
                if (DFT == '_QE/'):
                   soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n]      

        #----------------------------------------------------------
        # End of the loop over bands ------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # End of the loop over K-points ---------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# End of the PROCAR loop ----------------------------------
#----------------------------------------------------------

#======================================================================
# Obtendo o nº pontos-k a serem destacados bem como os seus rótulos ===
#======================================================================

for i in range (1,(loop+1)):     # Loop para a analise das Projecoes      

    if (i == 1): s = 1; t = (3+1)      
    if (i == 2): s = 4; t = (6+1)       
    if (i == 3): s = 7; t = (11+1)  

    for j in range (s,t):      
        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):

                    #------------------------------------------------------
                    # Ordem dos Orbitais
                    #       1 | 2  | 3  | 4  | 5   | 6   | 7   | 8   | 9 
                    # VASP: S | Py | Pz | Px | Dxy | Dyz | Dz2 | Dxz | Dx2
                    # QE:   S | Pz | Px | Py | Dz2 | Dxz | Dyz | Dx2 | Dxy                 
                    #------------------------------------------------------
                    if (j == 1): # Orbital S
                       orb_S[wp][point_k][Band_n] = soma_orb[wp][1][point_k][Band_n]
                    #-------------------- lorbit = 10 ---------------------
                    if (j == 2 and lorbit == 10): # Orbital P
                       orb_P[wp][point_k][Band_n] = soma_orb[wp][2][point_k][Band_n]
                    if (j == 3 and lorbit == 10): # Orbital D
                       orb_D[wp][point_k][Band_n] = soma_orb[wp][3][point_k][Band_n]
                    #-------------------- lorbit >= 11 --------------------                     
                    if (j == 2 and lorbit >= 11): # Orbital P = Px + Py + Pz
                       orb_P[wp][point_k][Band_n] = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                    if (j == 3 and lorbit >= 11): # Orbital D = Dxy + Dyz + Dz2 + Dxz + Dx2
                       orb_D[wp][point_k][Band_n] = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                    #------------------------------------------------------
                    if (j == 4): # Orbital Px 
                       if (DFT == '_VASP/'): orb_Px[wp][point_k][Band_n] = soma_orb[wp][4][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Px[wp][point_k][Band_n] = soma_orb[wp][3][point_k][Band_n]
                    if (j == 5): # Orbital Py 
                       if (DFT == '_VASP/'): orb_Py[wp][point_k][Band_n] = soma_orb[wp][2][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Py[wp][point_k][Band_n] = soma_orb[wp][4][point_k][Band_n]
                    if (j == 6): # Orbital pz 
                       if (DFT == '_VASP/'): orb_Pz[wp][point_k][Band_n] = soma_orb[wp][3][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Pz[wp][point_k][Band_n] = soma_orb[wp][2][point_k][Band_n]
                    #------------------------------------------------------
                    if (j == 7): # Orbital Dxy 
                       if (DFT == '_VASP/'): orb_Dxy[wp][point_k][Band_n] = soma_orb[wp][5][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Dxy[wp][point_k][Band_n] = soma_orb[wp][5][point_k][Band_n]
                    if (j == 8): # Orbital Dyz 
                       if (DFT == '_VASP/'): orb_Dyz[wp][point_k][Band_n] = soma_orb[wp][6][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Dyz[wp][point_k][Band_n] = soma_orb[wp][6][point_k][Band_n]
                    if (j == 9): # Orbital Dz2 
                       if (DFT == '_VASP/'): orb_Dz2[wp][point_k][Band_n] = soma_orb[wp][7][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Dz2[wp][point_k][Band_n] = soma_orb[wp][7][point_k][Band_n]
                    if (j == 10): # Orbital Dxz 
                       if (DFT == '_VASP/'): orb_Dxz[wp][point_k][Band_n] = soma_orb[wp][8][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Dxz[wp][point_k][Band_n] = soma_orb[wp][8][point_k][Band_n]
                    if (j == 11): # Orbital Dx2 
                       if (DFT == '_VASP/'): orb_Dx2[wp][point_k][Band_n] = soma_orb[wp][9][point_k][Band_n]
                       if (DFT == '_QE/'):   orb_Dx2[wp][point_k][Band_n] = soma_orb[wp][9][point_k][Band_n]

#======================================================================
# Saving data to plot the projections =================================
#====================================================================== 

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

#======================================================================
# Gravando a informação de cada orbital para o Plot das Projeções =====
#======================================================================

#---------------------------------------------------------------
orbital = open(dir_files + '/output/Orbitais/Orbitais.dat', 'w')
#---------------------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            orbital.write(f'{xx[i][j]} {Energia[i][j][k]}')
            orbital.write(f' {orb_S[i][j][k]} {orb_P[i][j][k]} {orb_D[i][j][k]}')
            if (lorbit > 10):
               orbital.write(f' {orb_Px[i][j][k]} {orb_Py[i][j][k]} {orb_Pz[i][j][k]}')
               orbital.write(f' {orb_Dxy[i][j][k]} {orb_Dyz[i][j][k]} {orb_Dz2[i][j][k]} {orb_Dxz[i][j][k]} {orb_Dx2[i][j][k]}')             
            orbital.write(f' \n')
                
#--------------
orbital.close()
#--------------

#======================================================================
# Getting k-points / labels ===========================================
#======================================================================
execute_python_file(filename = DFT + '_label.py')

#========================================================================
#========================================================================
# Projections Plot using (GRACE) ========================================
#======================================================================== 
#========================================================================
if (save_agr == 1):
   execute_python_file(filename = 'plot/Grace/plot_projecao_orbitais.py')

#=======================================================================================================================================
# Obtendo e gravando as cores no padrão RGB que designam cada orbital bem como cada combinação de orbitais para o Plot das Projeções ===
#=======================================================================================================================================

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
    
#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Orbitais.py to the output folder directory ---------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Orbitais/Orbitais.py'); f.close(); os.remove(dir_files + '/output/Orbitais/Orbitais.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_orbitais.py'
destination = dir_files + '/output/Orbitais/Orbitais.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'r')
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
linha += 1; lines.insert(linha, f'n_procar = {n_procar}    #  Total Num. of PROCAR files \n')
linha += 1; lines.insert(linha, f'nk  = {nk}               #  Total Num. of k-points \n')
linha += 1; lines.insert(linha, f'nb = {nb}                #  Total Num. of bands \n')
linha += 1; lines.insert(linha, f'energ_min = {energ_min}  #  Lower energy value of the bands in the plot \n')
linha += 1; lines.insert(linha, f'energ_max = {energ_max}  #  Higher energy value of the bands in the plot \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'lorbit = {lorbit}        #  Valor da variavel lorbit adotada no calculo \n')
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

file = open(dir_files + '/output/Orbitais/Orbitais.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------
exec(open(dir_files + '/output/Orbitais/Orbitais.py').read())
#------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
