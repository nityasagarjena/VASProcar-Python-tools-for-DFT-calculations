# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license


################################################################
# Regarding the Plot of Bands, choose ==========================
# [0] Plot/Analyze all bands ===================================
# [1] Plot/Analyze selected bands ==============================
################################################################
esc_bands = 0

if (esc_bands == 1):     
   ################################################################
   # Select the bands to be analyzed using intervals: =============
   # Type as in the examples below =============================== 
   # ------------------------------------------------------------- 
   # Bands can be added in any order ----------------------------- 
   # -------------------------------------------------------------
   # Examples:   
   # '35:42'                                                  
   # '1:15 27:69 18:19 76*'                         
   # '7* 9* 11* 13* 16:21'                         
   ################################################################
   bands_range = '1:1 2:2 3:3' 



################################################################ 
# with respect to energy, would you like? ======================
# [0] Use the default energy value from DFT output =============
# [1] Shift the Fermi level to 0.0 eV  =========================
################################################################ 
esc_fermi = 1



##############################################################################################
# What orbital contributions should be considered for plotting the spin components (Sx|Sy|Sz)?
# Use [0] to ignore an orbital and [1] to use its contribution in the projection of Spin components.
# ==================================================================================================
# Observations:
# For LORBIT < 10, orbitals S|P|D|F are present in the PROCAR file.
# For LORBIT < 10, orbitals S|Px|Py|Pz|Dxy|Dyz|Dz2|Dxz|Dx2|Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2 are present in the PROCAR file.
# Uncheck the correct option below for LORBIT<10 or LORBIT>10
#############################################################################################################################
s=1
## =======================
## Apenas para LORBIT < 10
## =======================
p=1
d=1
f=1
## =======================
## Apenas para LORBIT > 10
## =======================
px=1; py=1; pz=1
dxy=1; dyz=1; dz2=1; dxz=1; dx2=1
fyx2=1; fxyz=1; fyz2=1; fzz2=1; fxz2=1; fzx2=1; fxx2=1
# ===========================================================
# Uncheck the correct option below for LORBIT<10 or LORBIT>10
# ===========================================================
# Orb_spin = [s,p,d,f]
# Orb_spin = [s,px,py,pz,dxy,dyz,dz2,dxz,dx2,fyx2,fxyz,fyz2,fzz2,fxz2,fzx2,fxx2]



################################################################ 
# Do you want to modify the energy range to be plotted? ========
# [0] NOT                                                       
# [1] YES                                                       
################################################################
esc_range_E = 0

if (esc_range_E == 1):
   ################################################################ 
   # Enter the energy range to be plotted: ========================
   # Note: Enter the lowest and highest energy value to be plotted 
   #             in relation to the Fermi Level.                   
   #--------------------------------------------------------------- 
   # Examples:                                                     
   # -3.0 15.0                                        
   # -5.1 5.0                                         
   ################################################################      
   range_E = '-1.0 1.0'  
  


################################################################
# What do you want to Plot/Analyze? ============================
# [0] to analyze all ions in the lattice =======================
# [1] to analyze selected ions =================================
################################################################
esc_ions = 0
 
if (esc_ions == 1):
   ##################################################################
   ##Choose the intervals_of_ions to be analyzed: ===================
   ##Type as in the examples below ==================================
   ##----------------------------------------------------------------
   ##The order in which the ions are added does not change the result
   #--------------------------------------------------------------- 
   # Examples: 
   # '1:5 3:9 11* 15:27'                                      
   # '7:49 50:53'                                   
   # '3* 6* 8:11'                                           
   ################################################################## 
   ion_range = '1:1'



################################################################
# Would you like to label the k-points?                         
# [0] DO NOT label the k-points  ===============================
# [1] highlight k-points present in KPOINTS file ===============
# [2] Customize: highlight and Label k-points   ================
################################################################ 
dest_k = 1

if (dest_k != 2):
   ################################################################
   # Would you like to choose k-axis units?                        
   # [1] 2pi/Param. (Param. in Angs.) =============================
   # [2] 1/Angs. ==================================================
   # [3] 1/nm.   ==================================================
   ################################################################
   Dimensao = 1



################################################################
# Enter the weight/size of the spheres in the projection: ======
# #Enter a value between 0.0 and 1.0 ============================
################################################################
peso_total = 1.0

##################################################################
# Enter the transparency value to apply to the projections:       
# This option is useful for checking for overlaps ================   
# Enter a value between 0.0 and 1.0 ==============================
# ================================================================
# Hint: The higher the k-point density, the lower the transparency
#       value used, start with 0.5 ===============================
##################################################################
transp = 1.0       



# ==============================================================================================
# do not edit ### do not edit ### do not edit ### do not edit ### do not edit ### do not edit ##
# ==============================================================================================
esc_color = 0  
l_symmetry = 0 
# ==============================================================================================
# do not edit ### do not edit ### do not edit ### do not edit ### do not edit ### do not edit ##
# ==============================================================================================
