
def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Check whether the folder 'DOS' exists --------------------------------
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/DOS'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/DOS')
#-------------------------------------

#======================================================================
# Getting the input parameters ========================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')

#======================================================================
# Get the input from user =============================================
#======================================================================

print ("##############################################################")
print ("########### Densidade de Estados (Spin Polarizado) ###########")
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

      print (" ")

if (escolha == 1):
   esc_fermi = 1  
   esc = 0 

#----------------------------------------------------------------------
# Obtaining the results from DOSCAR -----------------------------------
#----------------------------------------------------------------------

#----------------------------------------
doscar = open(dir_files + '/DOSCAR', "r")
#----------------------------------------

for i in range(6):
    VTemp = doscar.readline().split()

E_max = float(VTemp[0])
E_min = float(VTemp[1])
NEDOS = int(VTemp[2])
Efermi = float(VTemp[3])

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0 

#----------------------------------------------------------------------
# Initialization of Variables, Vectors and Matrices -------------------
#----------------------------------------------------------------------

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

energia = [0]*(NEDOS+1)  #  energia[NEDOS]
dos_u   = [0]*(NEDOS+1)  #  dos_u[NEDOS]
dos_d   = [0]*(NEDOS+1)  #  dos_d[NEDOS]
l_dos_u = [0]*(NEDOS+1)  #  l_dos[NEDOS]
l_dos_d = [0]*(NEDOS+1)  #  l_dos[NEDOS]

pdos_u     = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]   # pdos_u[9][ni][NEDOS]
pdos_d     = [[[0]*(NEDOS+1) for i in range(ni+1)] for j in range(n_orb+1)]   # pdos_d[9][ni][NEDOS]
pdos_u_tot = [[0]*(NEDOS+1) for i in range(n_orb+1)]                          # pdos_u_tot[9][NEDOS]
pdos_d_tot = [[0]*(NEDOS+1) for i in range(n_orb+1)]                          # pdos_d_tot[9][NEDOS]

# pdos[1][ni][NEDOS] = Orbital S    //  pdos_tot[1][ni][NEDOS] = Orbital S total
# pdos[2][ni][NEDOS] = Orbital Py   //  pdos_tot[2][ni][NEDOS] = Orbital Py total
# pdos[3][ni][NEDOS] = Orbital Pz   //  pdos_tot[3][ni][NEDOS] = Orbital Pz total
# pdos[4][ni][NEDOS] = Orbital Px   //  pdos_tot[4][ni][NEDOS] = Orbital Px total
# pdos[5][ni][NEDOS] = Orbital Dxy  //  pdos_tot[5][ni][NEDOS] = Orbital Dxy total
# pdos[6][ni][NEDOS] = Orbital Dyz  //  pdos_tot[6][ni][NEDOS] = Orbital Dyz total
# pdos[7][ni][NEDOS] = Orbital Dz2  //  pdos_tot[7][ni][NEDOS] = Orbital Dz2 total
# pdos[8][ni][NEDOS] = Orbital Dxz  //  pdos_tot[8][ni][NEDOS] = Orbital Dxz total
# pdos[9][ni][NEDOS] = Orbital Dx2  //  pdos_tot[9][ni][NEDOS] = Orbital Dx2 total

pdos_u_P     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_u_P[ni][NEDOS]
pdos_d_P     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_u_P[ni][NEDOS]
pdos_u_D     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_u_D[ni][NEDOS]
pdos_d_D     = [[0]*(NEDOS+1) for i in range(ni+1)]   # pdos_u_D[ni][NEDOS]
pdos_u_P_tot = [0]*(NEDOS+1)                          # pdos_u_P_tot[NEDOS]
pdos_d_P_tot = [0]*(NEDOS+1)                          # pdos_u_P_tot[NEDOS]
pdos_u_D_tot = [0]*(NEDOS+1)                          # pdos_u_D_tot[NEDOS]
pdos_d_D_tot = [0]*(NEDOS+1)                          # pdos_u_D_tot[NEDOS]

y_inicial = E_min
y_final   = E_max

x_inicial = +1000.0
x_final   = -1000.0

#-------------------------------------------------------------------------------------------------

for i in range (1,(NEDOS+1)):
      VTemp = doscar.readline().split()
      energia[i] = float(VTemp[0])
      
for i in range (1,(ni+1)):
    if (esc == 1): temp_sn = sim_nao[i]
    #------------------------
    VTemp = doscar.readline()
    #----------------------------
    for j in range (1,(NEDOS+1)):

        VTemp = doscar.readline()
        #-----------------------------------------------------
        for k in range(10):
            VTemp = VTemp.replace(str(k) + '-', str(k) + 'E-')
            VTemp = VTemp.replace(str(k) + '+', str(k) + 'E+')
        VTemp = VTemp.split()
        #-----------------------------------------------------

        for k in range(1,(n_orb+1)):
            if (esc == 0 or (esc == 1 and temp_sn == "sim")):
               pdos_u[k][i][j] = float(VTemp[(2*k) -1])
               pdos_d[k][i][j] = float(VTemp[2*k])*(-1)
           
            if (lorbit == 10 and k == 2):
               pdos_u_P[i][j] = pdos_u_P[i][j] + pdos_u[k][i][j]
               pdos_d_P[i][j] = pdos_d_P[i][j] + pdos_d[k][i][j]
               
            if (lorbit == 10 and k == 3):
               pdos_u_D[i][j] = pdos_u_D[i][j] + pdos_u[k][i][j]
               pdos_d_D[i][j] = pdos_d_D[i][j] + pdos_d[k][i][j]
               
            if (lorbit >= 11 and (k == 2 or k == 3 or k == 4)):
               pdos_u_P[i][j] = pdos_u_P[i][j] + pdos_u[k][i][j]
               pdos_d_P[i][j] = pdos_d_P[i][j] + pdos_d[k][i][j]
               
            if (lorbit >= 11 and (k == 5 or k == 6 or k == 7 or k == 8 or k == 9)):
               pdos_u_D[i][j] = pdos_u_D[i][j] + pdos_u[k][i][j]
               pdos_d_D[i][j] = pdos_d_D[i][j] + pdos_d[k][i][j]

            pdos_u_tot[k][j] = pdos_u_tot[k][j] + pdos_u[k][i][j]
            pdos_d_tot[k][j] = pdos_d_tot[k][j] + pdos_d[k][i][j]
            
            dos_u[j] = dos_u[j] + float(VTemp[(2*k) -1])
            dos_d[j] = dos_d[j] + float(VTemp[2*k])*(-1)
            
            l_dos_u[j] = l_dos_u[j] + pdos_u[k][i][j]
            l_dos_d[j] = l_dos_d[j] + pdos_d[k][i][j]
            
        pdos_u_P_tot[j] = pdos_u_P_tot[j] + pdos_u_P[i][j]
        pdos_d_P_tot[j] = pdos_d_P_tot[j] + pdos_d_P[i][j]
        
        pdos_u_D_tot[j] = pdos_u_D_tot[j] + pdos_u_D[i][j]
        pdos_d_D_tot[j] = pdos_d_D_tot[j] + pdos_d_D[i][j]

        if (dos_d[j] <= x_inicial): x_inicial = dos_d[j]
        if (dos_u[j] >= x_final):   x_final   = dos_u[j] 
               
#-------------
doscar.close()
#-------------

#====================================================================================
# Saving data to plot the DOS, pDOS e lDOS (Up Component) ===========================
#====================================================================================

#------------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS_up.dat', 'w')
#------------------------------------------------------------------------

for k in range (1,(NEDOS+1)):
    #--------------------------------------------------------------------------------
    if (esc == 0): dos_pdos_ldos.write(f'{energia[k]} {dos_u[k]} 0.0')
    if (esc == 1): dos_pdos_ldos.write(f'{energia[k]} {dos_u[k]} {l_dos_u[k]}')
    dos_pdos_ldos.write(f' {pdos_u_tot[1][k]} {pdos_u_P_tot[k]} {pdos_u_D_tot[k]}')
    if (lorbit > 10): dos_pdos_ldos.write(f' {pdos_u_tot[4][k]} {pdos_u_tot[2][k]} {pdos_u_tot[3][k]} {pdos_u_tot[5][k]} {pdos_u_tot[6][k]} {pdos_u_tot[7][k]} {pdos_u_tot[8][k]} {pdos_u_tot[9][k]}')
    dos_pdos_ldos.write(f' \n')       

#--------------------
dos_pdos_ldos.close()
#--------------------

#====================================================================================
# Saving data to plot the DOS, pDOS e lDOS (Down Component) =========================
#====================================================================================

#--------------------------------------------------------------------------
dos_pdos_ldos = open(dir_files + '/output/DOS/DOS_pDOS_lDOS_down.dat', 'w')
#--------------------------------------------------------------------------s

for k in range (1,(NEDOS+1)):
    #-----------------------------------------------------------------
    if (esc == 0): dos_pdos_ldos.write(f'{energia[k]} {dos_d[k]} 0.0')
    if (esc == 1): dos_pdos_ldos.write(f'{energia[k]} {dos_d[k]} {l_dos_d[k]}')
    dos_pdos_ldos.write(f' {pdos_d_tot[1][k]} {pdos_d_P_tot[k]} {pdos_d_D_tot[k]}')
    if (lorbit > 10): dos_pdos_ldos.write(f' {pdos_d_tot[4][k]} {pdos_d_tot[2][k]} {pdos_d_tot[3][k]} {pdos_d_tot[5][k]} {pdos_d_tot[6][k]} {pdos_d_tot[7][k]} {pdos_d_tot[8][k]} {pdos_d_tot[9][k]}')
    dos_pdos_ldos.write(f' \n')       

#--------------------
dos_pdos_ldos.close()
#--------------------

#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (GRACE) ===============================================
#==================================================================================== 
#====================================================================================
if (save_agr == 1):
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos_[polarizado].py')  
   execute_python_file(filename = 'plot/Grace/plot_dos_pdos_ldos_[polarizado_delta].py')

#====================================================================================
#====================================================================================
# DOS, pDOS e lDOS Plot using (Matplotlib) ==========================================
#====================================================================================
#====================================================================================

#------------------------------------------------------------------------
# Copy DOS_pDOS_lDOS.py to the output folder directory ------------------
#------------------------------------------------------------------------

try: f = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py'); f.close(); os.remove(dir_files + '/output/DOS/DOS_pDOS_lDOS.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_dos_pdos_ldos_[polarizado].py'
destination = dir_files + '/output/DOS/DOS_pDOS_lDOS.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Allowing Bandas.py to be executed separatedly ---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'r')
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
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; x_inicial = {x_inicial}; x_final = {x_final}; energ_min = {y_inicial}; energ_max = {y_final}; lorbit = {lorbit}; esc = {esc} \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}        #  Fermi energy from DFT outpout file \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Would you like to shift the Fermi level? [0] No, use the value obtained from VASP [1] Yes, shift the Fermi level to 0.0 eV \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Plotting output format, onde [0] = NO e [1] = YES \n')                       
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------
exec(open(dir_files + '/output/DOS/DOS_pDOS_lDOS.py').read())
#------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
