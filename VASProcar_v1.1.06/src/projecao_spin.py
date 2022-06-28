
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Spin' exists -------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin')
#--------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("######### Plot 2D das Componentes de Spin (Sx|Sy|Sz) #########")
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

   if (esc == 1):

      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  
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
   print ("Esta opcao e util para verificar sobreposicoes.               ")   
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
read_spin = 1
execute_python_file(filename = DFT + '_nscf.py')  

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

soma_sx = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sx[n_procar][3][nk][nb]
soma_sy = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sy[n_procar][3][nk][nb]
soma_sz = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sz[n_procar][3][nk][nb]    

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  soma_sx[n_procar][1][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital S de Sx
#  soma_sx[n_procar][2][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Py ou P (lorbit = 10) de Sx
#  soma_sx[n_procar][3][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Pz ou D (lorbit = 10) de Sx
#  soma_sx[n_procar][4][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Px de Sx
#  soma_sx[n_procar][5][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxy de Sx
#  soma_sx[n_procar][6][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dyz de Sx
#  soma_sx[n_procar][7][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dz2 de Sx
#  soma_sx[n_procar][8][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxz de Sx
#  soma_sx[n_procar][9][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dx2 de Sx
#  tot_sx   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_sx = Soma de todos os orbitais (para todos os ions) de Sx

#----------------------------------------------------------------------

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):              
                #------------------------------------------------------ 
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------ 
                for orb_n in range(1,(n_orb+1)):
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       tot_sx[wp][point_k][Band_n] = ( tot_sx[wp][point_k][Band_n] + Sx[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sy[wp][point_k][Band_n] = ( tot_sy[wp][point_k][Band_n] + Sy[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sz[wp][point_k][Band_n] = ( tot_sz[wp][point_k][Band_n] + Sz[wp][orb_n][point_k][Band_n][ion_n] )

            #----------------------------------------------------------           
            # End of the loop over ions -------------------------------
            #----------------------------------------------------------
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
# Saving data to plot the projections =================================
#====================================================================== 

#--------------------------------------------------------
bandas = open(dir_files + '/output/Spin/Bandas.dat', 'w')
#--------------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------

#========================================================================
# Gravando a informação das componentes de Spin para o Plot das Projeções
#========================================================================

#----------------------------------------------------
spin = open(dir_files + '/output/Spin/Spin.dat', 'w')
#----------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            spin.write(f'{xx[i][j]} {Energia[i][j][k]}')
            #---------------------------------------------------------------------------------------
            if (tot_sx[i][j][k] > 0):  spin.write(f' {tot_sx[i][j][k]}')
            if (tot_sx[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sx[i][j][k] < 0):  spin.write(f' {tot_sx[i][j][k]}')
            if (tot_sx[i][j][k] >= 0): spin.write(f' 0.0')             
            #---------------------------------------------------------------------------------------
            if (tot_sy[i][j][k] > 0):  spin.write(f' {tot_sy[i][j][k]}')
            if (tot_sy[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sy[i][j][k] < 0):  spin.write(f' {tot_sy[i][j][k]}')
            if (tot_sy[i][j][k] >= 0): spin.write(f' 0.0') 
            #---------------------------------------------------------------------------------------
            if (tot_sz[i][j][k] > 0):  spin.write(f' {tot_sz[i][j][k]}')
            if (tot_sz[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sz[i][j][k] < 0):  spin.write(f' {tot_sz[i][j][k]}')
            if (tot_sz[i][j][k] >= 0): spin.write(f' 0.0')
            spin.write(f' \n')    
                
#-----------
spin.close()
#-----------
 
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
   execute_python_file(filename = 'plot/Grace/plot_projecao_spin.py')

#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Spin.py to the output folder directory -------------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Spin/Spin.py'); f.close(); os.remove(dir_files + '/output/Spin/Spin.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_spin.py'
destination = dir_files + '/output/Spin/Spin.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin/Spin.py', 'r')
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

file = open(dir_files + '/output/Spin/Spin.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------
exec(open(dir_files + '/output/Spin/Spin.py').read())
#----------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
