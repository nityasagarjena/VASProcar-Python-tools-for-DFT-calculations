# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

# set GRACE variables
execute_python_file(filename = "plot/_plot_settings.py")

#------------------------------------------------ ------------------------------
# Regarding the network parameter, choose: -------------------------------------
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
print("## [555] Generate KPOINTS file (2D Plane or 3D Mesh in ZB)  ##")
print("## ======================================================== ##")
print("## [665] POSCAR - Ion substitution in the lattice           ##")
print("## ======================================================== ##")
print("## [777] Tip: Using Multiple PROCAR Files                   ##")
print("## ======================================================== ##")
print("## [888] Check and fix VASP output files                    ##")
print("## ======================================================== ##")
print("## [999] Install/Update Python modules                      ##")
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
   print("## along a given Band and Contour level (constant energy)   ##")
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
   print("## Contribution of Orbitals and ions on states: (Table)     ##")
   print("## [34] Default   --   [-34] Custom                         ##")
   print("## ======================================================== ##")
   print("##############################################################") 
   opcao = input(" "); opcao = int(opcao)
   print(" ")
   
if (opcao == 4 or opcao == -4):
   print("## ======================================================== ##")
   print("## Electrostatic Potential in X,Y,Z - 2D Plot               ##")
   print("## [40] Default   --   [-40] Custom                         ##")
   print("## ======================================================== ##")
   print("## Partial Charge Density in X,Y,Z - 2D Plot                ##")
   print("## [41] Default   --   [-41] Custom                         ##")
   print("## ======================================================== ##")
   print("## Dielectric Function in X,Y,Z (Real|Imaginary) - 2D Plot  ##")
   print("## [42] Default   --   [-42] Custom                         ##")
   print("## ======================================================== ##")
   # print("##         !!!!! UNDER TESTS - Non-Functional !!!!!         ##")
   # print("## Wave Function in X,Y,Z (Real and Imaginary) - 2D Plot    ##")
   # print("## [43] Default   --   [-43] Custom                         ##")
   # print("## ======================================================== ##")
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

if (opcao > -100 and opcao < 100):
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
   execute_python_file(filename = 'projecao_orbitais.py')
    
if (opcao == 31 or opcao == -31):
   if (ispin == 1): execute_python_file(filename = DFT + 'dos_pdos_ldos.py')
   if (ispin == 2): execute_python_file(filename = DFT + 'dos_pdos_ldos_[polarizado].py')
    
if (opcao == 32 or opcao == -32):
   execute_python_file(filename = 'projecao_localizacao.py')
    
if (opcao == 33 or opcao == -33):
   execute_python_file(filename = 'projecao_psi.py')

if (opcao == 34 or opcao == -34):
   execute_python_file(filename = DFT + 'contribuicao.py')
    
if (opcao == 40 or opcao == -40):
   execute_python_file(filename = DFT + 'potencial.py')
    
if (opcao == 41 or opcao == -41):
   execute_python_file(filename = DFT + 'parchg.py')

if (opcao == 42 or opcao == -42):
   execute_python_file(filename = DFT + 'dielectric_function.py')
    
# if (opcao == 43 or opcao == -43):
#    execute_python_file(filename = DFT + 'wave_function.py')

if (opcao == 555 or opcao == -555):
   execute_python_file(filename = DFT + 'kpoints_2D_3D.py')

if (opcao == 665 or opcao == -665):
   execute_python_file(filename = DFT + 'poscar_replace.py')

if (opcao == 777 or opcao == -777):
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
       
if (opcao == 888 or opcao == -888):
   execute_python_file(filename = 'correction_file.py')

if (opcao == 999 or opcao == -999):
   execute_python_file(filename = '_update.py')
   
