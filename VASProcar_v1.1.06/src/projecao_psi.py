
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'Psi' exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Psi'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Psi')
#-------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

ion_orb = [[[0]*(n_orb+1) for i in range(ni+1)] for j in range(5+1)]  #  ion_orb[n_psi][ni][n_orb]

psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  psi[n_psi][n_procar][nk][nb]          
total = [[[0.0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]  #  total[n_procar][nk][nb] 

l_psi = ['null']*(5+1)

#======================================================================
# Get the input from user =============================================
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
   print ("s p d                                                      ")
if (lorbit >= 11):
   print ("s p d px py pz dxy dyz dz2 dxz dx2                         ")
print ("==============================================================")
print ("Exemplos:                                                     ")
if (lorbit == 10):
   print ("ion_inicial ion_final orbitais: 3  3  S P D                ")
   print ("ion_inicial ion_final orbitais: 5  14 S P                  ")
   print ("ion_inicial ion_final orbitais: 14 49 S                    ")
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
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'):
                      ion_orb[i][p][1] = 1                    
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'):
                      ion_orb[i][p][2] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'):
                      ion_orb[i][p][3] = 1
                #------------------------      
                if (lorbit >= 11):                   
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'):
                      ion_orb[i][p][1] = 1                      
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'):
                      ion_orb[i][p][2] = 1; ion_orb[i][p][3] = 1; ion_orb[i][p][4] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'):
                      ion_orb[i][p][5] = 1; ion_orb[i][p][6] = 1; ion_orb[i][p][7] = 1; ion_orb[i][p][8] = 1; ion_orb[i][p][9] = 1                                          
                   if (psi_io[t+1] == 'py' or psi_io[t+1] == 'Py' or psi_io[t+1] == 'PY'):
                      if (DFT == '_VASP/'): ion_orb[i][p][2] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][4] = 1
                   if (psi_io[t+1] == 'pz' or psi_io[t+1] == 'Pz' or psi_io[t+1] == 'PZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][3] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][2] = 1
                   if (psi_io[t+1] == 'px' or psi_io[t+1] == 'Px' or psi_io[t+1] == 'PX'):
                      if (DFT == '_VASP/'): ion_orb[i][p][4] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][3] = 1 
                   if (psi_io[t+1] == 'dxy' or psi_io[t+1] == 'Dxy' or psi_io[t+1] == 'DXY'):
                      if (DFT == '_VASP/'): ion_orb[i][p][5] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][9] = 1 
                   if (psi_io[t+1] == 'dyz' or psi_io[t+1] == 'Dyz' or psi_io[t+1] == 'DYZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][6] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][7] = 1 
                   if (psi_io[t+1] == 'dz2' or psi_io[t+1] == 'Dz2' or psi_io[t+1] == 'DZ2'):
                      if (DFT == '_VASP/'): ion_orb[i][p][7] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][5] = 1 
                   if (psi_io[t+1] == 'dxz' or psi_io[t+1] == 'Dxz' or psi_io[t+1] == 'DXZ'):
                      if (DFT == '_VASP/'): ion_orb[i][p][8] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][6] = 1 
                   if (psi_io[t+1] == 'dx2' or psi_io[t+1] == 'Dx2' or psi_io[t+1] == 'DX2'):
                      if (DFT == '_VASP/'): ion_orb[i][p][9] = 1
                      if (DFT == '_QE/'):   ion_orb[i][p][8] = 1 

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
            # End of the loop over ions -------------------------------
            #----------------------------------------------------------
            
            for p in range (1,(n_psi+1)):
                if (total[wp][k][b] != 0.0):
                   psi[p][wp][k][b] = ( psi[p][wp][k][b]/total[wp][k][b] )                 

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

#======================================================================
# Gravando a informação de cada estado Psi para o Plot das Projeções ==
#======================================================================

#------------------------------------------------------
psi_file = open(dir_files + '/output/Psi/Psi.dat', 'w')
#------------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            psi_file.write(f'{xx[i][j]} {Energia[i][j][k]}')
            psi_file.write(f' {psi[1][i][j][k]} {psi[2][i][j][k]} {psi[3][i][j][k]} {psi[4][i][j][k]} {psi[5][i][j][k]}')         
            psi_file.write(f' \n')
                
#---------------
psi_file.close()
#---------------

#=======================================================================================================================================
# Obtendo e gravando as cores no padrão RGB que designam cada orbital bem como cada combinação de orbitais para o Plot das Projeções ===
#=======================================================================================================================================

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
           c_red    =  psi[2][wp][point_k][Band_n] + 0.737254902*(psi[5][wp][point_k][Band_n]) + psi[4][wp][point_k][Band_n]
           c_green  =  psi[3][wp][point_k][Band_n] + 0.560784313*(psi[5][wp][point_k][Band_n])
           c_blue   =  psi[1][wp][point_k][Band_n] + 0.560784313*(psi[5][wp][point_k][Band_n]) + psi[4][wp][point_k][Band_n]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #-------------------------------------------------
           color_rgb.write(f' {c_red} {c_green} {c_blue} \n')         

#----------------
color_rgb.close()
#----------------

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
   execute_python_file(filename = 'plot/Grace/plot_projecao_psi.py')
    
#========================================================================
#========================================================================
# Projections Plot using (Matplotlib) ===================================
#========================================================================
#========================================================================

#----------------------------------------------------------------------
# Copy Psi.py to the output folder directory --------------------------
#----------------------------------------------------------------------

try: f = open(dir_files + '/output/Psi/Psi.py'); f.close(); os.remove(dir_files + '/output/Psi/Psi.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_psi.py'
destination = dir_files + '/output/Psi/Psi.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/Psi/Psi.py', 'r')
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
linha += 1; lines.insert(linha, f'n_psi = {n_psi}  #  Numero de estados Psi \n')
linha += 1; lines.insert(linha, f'l_psi = {l_psi}  #  Rotulos dos estados Psi \n')
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

file = open(dir_files + '/output/Psi/Psi.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------
exec(open(dir_files + '/output/Psi/Psi.py').read())
#--------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
