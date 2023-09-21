# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

# set GRACE variables
execute_python_file(filename = "plot/_plot_settings.py")

#------------------------------------------------ ------------------------------
# Regarding the lattice parameter, choose: -------------------------------------
#------------------------------------------------ ------------------------------
# [1] Use the parameter informed in the CONTCAR (VASP) or nscf.out (QE) file
# [2] Adopt as a parameter the smallest value among the modules of the primitive
#     vectors of the crystal lattice (A1, A2 and A3).
#------------------------------------------------ ------------------------------
param_estim = 1

# ------------------------------------------------------------------------------
# Checking if the "output" folder exists, if it does not exist it is created ---
# ------------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output'):
    0 == 0
else:
    os.mkdir(dir_files + '/output')
# ---------------------------------

# ----------------------------------------------------------------------
# Obtaining the code input parameters: ---------------------------------
# ----------------------------------------------------------------------

if (len(inputs) == 0 and DFT == '_VASP/'):

   print("##############################################################")
   print("################ What do you want to Analyze? ################")
   print("##############################################################")
   print("## ======================================================== ##")
   print("## [1] Energy: 2D|3D|isosurface Plot, Fermi Surfaces,       ##")
   print("##             Contour levels                               ##")
   print("## ======================================================== ##")  
   print("## [2] Spin: 2D|3D|isosurface Plot,                         ##")
   print("##           Projection on Contour levels                   ##")
   print("## ======================================================== ##") 
   print("## [3] Projection Orbital and Spacial of the states,        ##")
   print("##     Density of States (DOS, p-DOs, l-DOS),               ##")
   print("##     Projection of Character of the states                ##")
   print("## ======================================================== ##") 
   print("## [4] Charge Density, Electrostatic Potential,             ##")
   print("##     Dielectric Function                                  ##")
   print("## ======================================================== ##")
   print("## [5] Creation, correction and manipulation of VASP output ##")
   print("##     files: KPOINTS|POSCAR|POTCAR|PROCAR|OUTCAR|CHGCAR    ##")
   print("## ======================================================== ##")
   print("## [6] Input files (code automation)                        ##")
   print("## ======================================================== ##")
   print("## [888] Install/Update Python modules                      ##")
   print("## ======================================================== ##")
   print("## [999] DFT2kp: effective kp models from ab-initio data    ##")
   print("## ======================================================== ##")
   print("##############################################################")
   opcao = input(" "); opcao = int(opcao)
   print(" ")

   # ======================================================================

   if (opcao > -10 and opcao < 10):
      print("##############################################################")
      print("####################### Choose option: #######################")
      print("##############################################################")

   if (opcao == 1 or opcao == -1):
      print("## ======================================================== ##")
      print("## Band Structure - 2D Plot:  [k-path, E(eV)]               ##")
      print("## [10] Default   --   [-10] Custom                         ##")
      print("## ======================================================== ##")
      print("## Fermi surface - 2D projection:  [ki, kj, E(eV)]          ##")
      print("## [11] Default   --   [-11] Custom                         ##")
      print("## ======================================================== ##")
      print("## Band Contour levels (2D Projection and 3D Plot):         ##")
      print("## [12] Default   --   [-12] Custom                         ##")
      print("## ======================================================== ##")
      print("## Band Structure - 3D Plot: [ki, kj, E(eV)]                ##")
      print("## [13] Default   --   [-13] Custom                         ##")
      print("## ======================================================== ##")
      print("## Band isosurfaces:  [kx, ky, kz, E(eV) or dE(eV)]         ##")
      print("## [14] Default   --   [-14] Custom                         ##")
      print("## ======================================================== ##")
      print("##############################################################")
      opcao = input(" "); opcao = int(opcao)
      print(" ")

   if (opcao == 2 or opcao == -2):
      print("## ======================================================== ##")
      print("## 2D Projection of Components Sx|Sy|Sz:  [k-path, E(eV)]   ##")
      print("## [20] Default   --   [-20] Custom                         ##")
      print("## ======================================================== ##")
      print("## Projections 2D|3D|Isosurface of Components Sx|Sy|Sz      ##")
      print("## and of the vectors SiSj e SxSySz                         ##")
      print("## [21] Default   --   [-21] Custom                         ##")
      print("## ======================================================== ##")
      print("## Plot of Components Sx|Sy|Sz and of the vectors SiSj      ##")
      print("## along a given Contour level (constant energy)            ##")
      print("## [22] Default   --   [-22] Custom                         ##")
      print("## ======================================================== ##")
      print("## Video showing the evolution of Sx|Sy|Sz or SiSj vectors  ##")
      print("## as a function of Energy (Contour level)                  ##")
      print("## [23] Default   --   [-23] Custom                         ##")
      print("## ======================================================== ##")
      print("##############################################################")   
      opcao = input(" "); opcao = int(opcao)
      print(" ")
   
   if (opcao == 3 or opcao == -3):
      print("## ======================================================== ##")
      print("## 2D Projection of Orbitals S|P|D|F:  [k-path, E(eV)]      ##")       
      print("## [30] Default   --   [-30] Custom                         ##")
      print("## ======================================================== ##")
      print("## DOS, p-DOS e l-DOS (Plot 2D)                             ##")
      print("## [31] Default   --   [-31] Custom                         ##")
      print("## ======================================================== ##")
      print("## 2D projection of the spatial location of bands (regions) ##")
      print("## [32] Default   --   [-32] Custom                         ##")
      print("## ======================================================== ##")
      print("## 2D projection of states Character:                       ##")
      print("## [33] Default   --   [-33] Custom                         ##")
      print("## ======================================================== ##")
      print("## 2D Projection of Orbital Texture (Fermi surface)         ##")
      print("## (Orbital contribution intensity color map)               ##")
      print("## [34] Default   --   [-34] Custom                         ##")
      print("## ======================================================== ##")
      print("##                !!!!!  UNDER TESTS  !!!!!                 ##")
      print("## 2D Projection of Orbital Texture (Level Contour)         ##")
      print("## (Plot of Components Px|Py|Pz and of the vectors PiPj)    ##")
      print("## [35] Default   --   [-35] Custom                         ##")
      print("## ======================================================== ##")
      print("## Contribution of Orbitals and ions on states: (Table)     ##")
      print("## [36] Default   --   [-36] Custom                         ##")
      print("## ======================================================== ##")
      print("##############################################################") 
      opcao = input(" "); opcao = int(opcao)
      print(" ")
   
   if (opcao == 4 or opcao == -4):
      print("## ======================================================== ##")
      print("## Electrostatic Potential in X,Y,Z direction - 2D Plot     ##")
      print("## [40] Default   --   [-40] Custom                         ##")
      print("## ======================================================== ##") 
      print("## Charge Density in X,Y,Z direction - 2D Plot              ##")
      print("## [41] Default   --   [-41] Custom                         ##")
      print("## ======================================================== ##")
      print("## Partial Charge Density in X,Y,Z direction - 2D Plot      ##")
      print("## [42] Default   --   [-42] Custom                         ##")
      print("## ======================================================== ##")
      print("## Dielectric Function in X,Y,Z (Real|Imaginary) - 2D Plot  ##")
      print("## [43] Default   --   [-43] Custom                         ##")
      print("## ======================================================== ##")
      # print("##         !!!!! UNDER TESTS - Non-Functional !!!!!         ##")
      # print("## Wave Function in X,Y,Z (Real and Imaginary) - 2D Plot    ##")
      # print("## [44] Default   --   [-44] Custom                         ##")
      # print("## ======================================================== ##")
      print("##############################################################")
      opcao = input(" "); opcao = int(opcao)
      print(" ")

   if (opcao == 5 or opcao == -5):
      print("## ======================================================== ##")
      print("## [51] Generate KPOINTS file (2D Plane or 3D Mesh in ZB)   ##")
      print("## [52] POSCAR - Ion substitution in the lattice            ##")
      print("## [53] Combining/Merging different POTCAR files            ##")
      print("## [54] Tip: Using Multiple PROCAR Files                    ##")
      print("## [55] Check and fix VASP output files                     ##")
      print("## ======================================================== ##")
      print("##############################################################")
      opcao = input(" "); opcao = int(opcao)
      print(" ")

if (len(inputs) == 0 and DFT == '_QE/'):

   print("##############################################################")
   print("################ What do you want to Analyze? ################")
   print("##############################################################")
   print("## ======================================================== ##")
   print("## Band Structure - 2D Plot:  [k-path, E(eV)]               ##")
   print("## [10] Default   --   [-10] Custom                         ##")
   print("## ======================================================== ##")  
   print("## 2D Projection of Orbitals S|P|D|F:  [k-path, E(eV)]      ##")       
   print("## [30] Default   --   [-30] Custom                         ##")
   print("## ======================================================== ##")
   print("## DOS, p-DOS e l-DOS (Plot 2D)                             ##")
   print("## [31] Default   --   [-31] Custom                         ##")
   print("## ======================================================== ##")
   print("## 2D projection of the spatial location of bands (regions) ##")
   print("## [32] Default   --   [-32] Custom                         ##")
   print("## ======================================================== ##")
   print("## [888] Install/Update Python modules                      ##")
   print("## ======================================================== ##")
   print("## [999] DFT2kp: effective kp models from ab-initio data    ##")
   print("## ======================================================== ##")
   print("##############################################################")
   opcao = input(" "); opcao = int(opcao)
   print(" ")
   
# ----------------------------------------------------------------------
# Copying file to "output" folder: -------------------------------------
# ----------------------------------------------------------------------

source = main_dir + '/etc/BibTeX.dat'
destination = dir_files + '/output/BibTeX.dat'
shutil.copyfile(source, destination)

source = main_dir + '/etc/DOI.png'
destination = dir_files + '/output/DOI.png'
shutil.copyfile(source, destination)

# ----------------------------------------------------------------------
# Getting information from CONTCAR/OUTCAR/PROCAR files: ----------------
# ----------------------------------------------------------------------

if (opcao > -100 and opcao < 100 and opcao != 41 and opcao != -41 and opcao != 52 and opcao != -52 and opcao != 53 and opcao != -53 and opcao != 6 and opcao != -6):
   execute_python_file(filename = DFT + '_info_b.py')

   print("#######################################################################")
   print("# Obtaining information from the lattice and the calculation performed:")
   print("#######################################################################")

   print(" ")
   print(".........................")
   print("...   Wait a moment   ...")
   print(".........................")
   print(" ")

   # ----------------------------------------------------------------------
   # Getting information from CONTCAR/OUTCAR/PROCAR files: ----------------
   # ----------------------------------------------------------------------

   #??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
   #??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
   #??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
   if ((LNC != 2) and ((opcao >= 20 and opcao < 30) or (opcao >= -29 and opcao < -19))):
      #???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
      #???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
      #???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

      print("@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#")
      print("@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#")
      print("==============================================================")
      print("= Its calculation does not allow analysis of the Sx|Sy|Sz ====")
      print("= components or the SiSj and SxSySz spin vectors =============")
      print("==============================================================")
      print("@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#")
      print("@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#$%&@#")   

      print(" ")
      print("...................................................")
      print("...     Please close the code and try again     ...")
      print("...................................................")
      confirmacao = input (" "); confirmacao = str(confirmacao)

      exit()

# ----------------------------------------------------------------------
# Executing the code corresponding to the task informed above: ---------
# ----------------------------------------------------------------------

#--------------------------------
escolha = opcao/((opcao**2)**0.5)
#--------------------------------

if (opcao == 10 or opcao == -10):
   read_projwfc_up = 0
   execute_python_file(filename = 'bandas_2D.py')
    
if (opcao == 11 or opcao == -11):
   execute_python_file(filename = 'fermi_surface.py')
    
if (opcao == 12 or opcao == -12):
   execute_python_file(filename = 'level_countour.py')
    
if (opcao == 13 or opcao == -13):
   execute_python_file(filename = 'bandas_3D.py')
    
if (opcao == 14 or opcao == -14):
   execute_python_file(filename = 'bandas_4D.py')
    
if (opcao == 20 or opcao == -20):
   execute_python_file(filename = 'projecao_spin.py')
    
if (opcao == 21 or opcao == -21):
   execute_python_file(filename = 'spin_texture.py')

if (opcao == 22 or opcao == -22):
   execute_python_file(filename = 'spin_texture_contour.py')

if (opcao == 23 or opcao == -23):
   execute_python_file(filename = 'spin_texture_contour_video.py') 
        
if (opcao == 30 or opcao == -30):
   read_projwfc_up = 1
   execute_python_file(filename = 'projecao_orbitais.py')
    
if (opcao == 31 or opcao == -31):
   read_projwfc_up = 0
   if (ispin == 1): execute_python_file(filename = DFT + 'dos_pdos_ldos.py')
   if (ispin == 2): execute_python_file(filename = DFT + 'dos_pdos_ldos_[polarizado].py')
    
if (opcao == 32 or opcao == -32):
   read_projwfc_up = 1
   execute_python_file(filename = 'projecao_localizacao.py')
    
if (opcao == 33 or opcao == -33):
   execute_python_file(filename = 'projecao_psi.py')

if (opcao == 34 or opcao == -34):
   execute_python_file(filename = 'orbital_texture.py')

if (opcao == 35 or opcao == -35):
   execute_python_file(filename = 'orbital_texture_vector.py')
    
if (opcao == 36 or opcao == -36):
   execute_python_file(filename = DFT + 'contribuicao.py')
    
if (opcao == 40 or opcao == -40):
   execute_python_file(filename = DFT + 'potencial.py')
    
if (opcao == 41 or opcao == -41):
   execute_python_file(filename = DFT + 'chgcar.py')

if (opcao == 42 or opcao == -42):
   execute_python_file(filename = DFT + 'parchg.py')

if (opcao == 43 or opcao == -43):
   execute_python_file(filename = DFT + 'dielectric_function.py')
    
# if (opcao == 44 or opcao == -44):
#    execute_python_file(filename = DFT + 'wave_function.py')

if (opcao == 51 or opcao == -51):
   execute_python_file(filename = DFT + 'kpoints_2D_3D.py')

if (opcao == 52 or opcao == -52):
   execute_python_file(filename = DFT + 'poscar_replace.py')

if (opcao == 53 or opcao == -53):
   execute_python_file(filename = DFT + 'postar_combination.py')

if (opcao == 54 or opcao == -54):
   print("##############################################################")
   print("## ======================================================== ##")
   print("## ------------- Using Multiple PROCAR Files: ------------- ##")
   print("## ======================================================== ##")
   print("##                                                          ##")
   print("## For the use of Multiple PROCAR files, they must be       ##")
   print("## renamed sequentially, as below:                          ##")
   print("##                                                          ##")
   print("## PROCAR.1 PROCAR.2 PROCAR.3 PROCAR.4 PROCAR.5 ...         ##")
   print("##                                                          ##")
   print("## Note: All PROCAR files used must contain exactly the     ##") 
   print("##       same number of k-points                            ##")
   print("##############################################################")
   pausa = input (" ")
   exit()
       
if (opcao == 55 or opcao == -55):
   execute_python_file(filename = 'correction_file.py')

if (opcao == 6 or opcao == -6):
   execute_python_file(filename = 'inputs/' + 'inputs_files.py')

if (opcao == 888 or opcao == -888):
   execute_python_file(filename = '_update.py')

if (opcao == 999 or opcao == -999):
   execute_python_file(filename = '_dft2kp.py')
