
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Spin_Texture' exists -----------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin_Texture'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin_Texture')
#----------------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Analyzing the variation of the coordinates of the K-points ==========
#======================================================================
execute_python_file(filename = DFT + '_var_kpoints.py')

soma_1 = dk[0] + dk[1] + dk[2]
soma_2 = dk[3] + dk[4] + dk[5]

#======================================================================
# Get the input from user =============================================
#======================================================================
 
print ("##############################################################")
print ("## O que deseja analisar quanto a proj. da textura de Spin? ##")
print ("## -------------------------------------------------------- ##")
print ("## [1] Projecao 2D do vetor SiSj e das componentes Sx|Sy|Sz ##")
print ("##     no plano kikj da ZB                                  ##")
print ("## [2] Proj. 3D do vetor SxSySz e das componentes Sx|Sy|Sz  ##")
print ("##     no grid [ki, kj, E(eV)]                              ##") 
print ("## [3] Proj. 3D do vetor SxSySz e das componentes Sx|Sy|Sz  ##")
print ("##     no grid [kx,ky,kz] ou [k1,k2,k3]                     ##")
print ("## [4] Isosuperficies das componentes Sx|Sy|Sz no grid      ##")
print ("##     [kx,ky,kz] ou [k1,k2,k3]                             ##")
print ("##############################################################") 
escolha_d = input (" "); escolha_d = int(escolha_d)  
print (" ")

if (escolha_d < 0): escolha_d = (escolha_d**2)**0.5

if (escolha_d <= 2): number = 2
if (escolha_d > 2):  number = 3
   
if (soma_1 != number and soma_2 != number):
   print ("============================================================")
   print ("!!! ERROR !!!                                               ")
   print ("============================================================")
   if (escolha_d <= 2):
      print ("The calculation performed does not correspond to a 2D plan  ")
      print ("in the BZ. kikj-plan (i,j = x,y,z or i,j = 1,2,3)           ")
   if (escolha_d > 2):
      print ("The calculation performed does not correspond to a GRID 3D  ")
      print ("in the BZ (GRID kxkykz or k1k2k3)                           ")
   print ("------------------------------------------------------------")
   print ("Please, use the option [888] to get the correct KPOINTS file")
   print ("============================================================")
   confirmacao = input (" ")
   exit()   

print ("##############################################################")
print ("Qual banda quer analisar? ====================================")
print ("##############################################################") 
Band = input (" "); Band = int(Band)
print (" ")

if (escolha == -1):
   
   if (escolha_d == 2):
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

if (escolha == -1 and escolha_d == 4): 
   print ("##############################################################")
   print ("How many isosurfaces would you like to plot? =================")
   print ("Hint: use 15 (unless more precision is required) =============") # ???????????????????????????????????????????????????????
   print ("##############################################################") 
   n_iso = input (" "); n_iso = int(n_iso)
   print (" ")

#-----------------------------------------------------------------------------

if (soma_1 == number or soma_2 == number):
   #----------------------------------   
   if (soma_2 == number and escolha == -1):
      print ("##############################################################")
      print ("Would you like to choose k-axis units?                        ")
      print ("[1] (kx,ky,kz) 2pi/Param. (Param. in Angs.) ==================")
      print ("[2] (kx,ky,kz) 1/Angs. =======================================")
      print ("[3] (kx,ky,kz) 1/nm.   =======================================")  
   #----------------------------------
   if (soma_1 == number and soma_2 == number and escolha == -1):    
      print ("[4] (k1,k2,k3) Fractional coord: K = k1*B1 + k2*B2 + k3*B3 ===")
   #----------------------------------
   if (soma_2 == number and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != number):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != number and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == number and soma_2 == number and escolha == 1):
      Dimensao = 4
   #----------------------------------

   if (escolha_d <= 2):   
      #----------------------------------
      if (Dimensao < 4):
         if (dk[3] == 1 and dk[4] == 1): Plano_k = 1  #  kxky-plan
         if (dk[3] == 1 and dk[5] == 1): Plano_k = 2  #  kxkz-plan
         if (dk[4] == 1 and dk[5] == 1): Plano_k = 3  #  kykz-plan
   
      if (Dimensao == 4):
         if (dk[0] == 1 and dk[1] == 1): Plano_k = 1  #  k1k2-plan
         if (dk[0] == 1 and dk[2] == 1): Plano_k = 2  #  k1k3-plan
         if (dk[1] == 1 and dk[2] == 1): Plano_k = 3  #  k2k3-plan   

#-----------------------------------------------------------------------------   

if (escolha == -1):

   if (escolha_d == 1):
      print ("##############################################################")  
      print ("Digite [0] caso deseje manter a densidade de vetores de Spin. ")
      print ("==============================================================")
      print ("Caso deseje reduzir a densidade, digite um numero inteiro > 0,")
      print ("correspondendo ao numero de vetores de Spin ignorados de forma")
      print ("intercalada ao longo do plano da ZB.                          ") 
      print ("##############################################################") 
      pulo = input (" "); pulo = int(pulo)  
      print (" ")
      #----------------------
      if (pulo < 0): pulo = 0

      print ("##############################################################")  
      print ("Para manter o comprimento dos vetores de Spin, Digite 1.0     ")
      print ("Para aumentar o comprimento, Digite um valor Positivo >  1.0  ")
      print ("Para diminuir o comprimento, Digite um valor Negativo < -1.0  ")
      print ("==============================================================")
      print ("Estes valores correspondem a quantas vezes, o comprimento do  ") 
      print ("vetor sera multiplicado (aumentado) ou dividido (diminuido).  ")
      print ("##############################################################")    
      fator = input (" "); fator = float(fator)  
      print (" ")    
   
   if (escolha_d == 2):     
      print ("##############################################################")
      print ("Choose the K-mesh grid (DxD) to be interpolated: =============")
      print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
      print ("       used as a reference. You are free to increase/decrease ")
      print ("       the numberof kpoints to be interpolated.               ")
      print ("Hint:  use 101 (unless more precision is required).           ") # ???????????????????????????????????????????????????????
      print ("##############################################################")
      n_d = input (" "); n_d = int(n_d)  
      print (" ")
      
   if (escolha_d == 4):
      
      print ("##############################################################")
      print ("Choose the K-mesh grid (DxDxD) to be interpolated: ===========")
      print ("Note:  The k-mesh grid used in your DFT calculation can be    ")
      print ("       used as a reference you are free to increase/decrease  ")
      print ("       the number of kpoints to be interpolated               ")
      print ("Hint:  use 31 (unless more precision is required)             ") # ???????????????????????????????????????????????????????
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")     

if (escolha == 1):
   esc_fermi = 1   
   esc = 0
   Dimensao = 1
   #-------------------
   if (escolha_d == 1):   
      pulo = 0
      fator = 1.0
   if (escolha_d == 2):
      n_d = 101
   if (escolha_d == 4):
      n_d = 31; n_iso = 15

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

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  tot_si (i = x,y,z)   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_si (i = x,y,z) = Soma de todos os orbitais (para todos os ions) de Sx
                                              
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
# Saving data to plot the Spin Texture ================================
#======================================================================

#-----------------------------------------------------------------------
spin_3D = open(dir_files + '/output/Spin_Texture/Spin_Texture.dat', 'w')
#-----------------------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           spin_3D.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')       
        if (Dimensao == 4):
           spin_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')
               
#--------------
spin_3D.close()
#--------------

#----------------------------------------------------------------------
# Copy Spin_Texture_?D.py to the output folder directory --------------
#----------------------------------------------------------------------

if (escolha_d == 1):
   name = '2D'
   
if (escolha_d == 2):
   name = '3D'
   
if (escolha_d == 3):
   name = '4D'
   
if (escolha_d == 4):
   name = '4D_[iso]'

try: f = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py'); f.close(); os.remove(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_spin_texture_' + name + '.py'
destination = dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py', 'r')
lines = file.readlines()
file.close()

if (escolha_d == 1):
   linha = 12
if (escolha_d == 2):
   linha = 7
if (escolha_d == 3):
   linha = 7
if (escolha_d == 4):
   linha = 7

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
if (escolha_d == 1):
   linha += 1; lines.insert(linha, f'fator = {fator}  #  Fator pelo qual o comprimento dos vetores de spin serao aumentados ou diminuidos \n')   
   linha += 1; lines.insert(linha, f'pulo = {pulo}    #  Numero de vetores de spin a serem ignorados de forma intercalada no plano da ZB \n')
if (escolha_d == 2): 
   linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout files \n')
   linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
   linha += 1; lines.insert(linha, f'n_d = {n_d}              #  Interpolation grid (DxD) \n') 
if (escolha_d == 4):
   linha += 1; lines.insert(linha, f'n_d = {n_d}          #  Interpolation grid (DxDxD) \n') 
   linha += 1; lines.insert(linha, f'n_iso = {n_iso}      #  Numero de isosuperficies no plot \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}   #  [1] (kx,ky,kz) 2pi/Param.; [2] (kx,ky,kz)  1/Angs.; [3] (kx,ky,kz) 1/nm.; [4] (k1,k2,k3) \n')
if (escolha_d < 3):
   linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}  #  [1] kxky or k1k2; [2] kxkz or k1k3; [3] kykz or k2k3  \n')
if (escolha_d != 4):
   linha += 1; lines.insert(linha, f'nk = {nk}  #  Total Num. of k-points \n')
if (escolha_d == 1):
   linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_' + name + '.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------------------------
if (escolha_d == 1):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_2D.py').read())
   
if (escolha_d == 2):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_3D.py').read())
   
if (escolha_d == 3):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_4D.py').read())
   
if (escolha_d == 4):
   exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_4D_[iso].py').read())
#--------------------------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
