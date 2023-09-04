# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

# -----------------------------------------------------------------------
# Regarding the Plot of graphics via Matplotlib, how do you want to save?
# Check [0] to disable or [1] to enable the respective format
# -----------------------------------------------------------------------

save_agr = 1
save_png = 1
save_pdf = 0
save_svg = 0
save_eps = 0

sum_save = save_png + save_pdf + save_eps + save_svg

#----------------------------------------------------------------------
# Colors used in the Projections plot: --------------------------------
#----------------------------------------------------------------------

# Note: Color code
# 0 White | 1  Black   | 2  Red    | 3  Green  | 4  Blue   | 5 Yellow    | 6  Borwn | 7 Grey | 8 Violet
# 9 Cyan  | 10 Magenta | 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green |

#---------------------------------------------------------------------------------------------------       
# RGB color standard: color = [Red, Green, Blue] with each component ranging from 0.0 to 1.0 -------
#---------------------------------------------------------------------------------------------------

cRGB = [0]*16
f = 255

cRGB[0]  = (255/f, 255/f, 255/f)  # White (Red + Green + Blue)
cRGB[1]  = (  0/f,   0/f,   0/f)  # Black
cRGB[2]  = (255/f,   0/f,   0/f)  # Red
cRGB[3]  = (  0/f, 255/f,   0/f)  # Green
cRGB[4]  = (  0/f,   0/f, 255/f)  # Blue
cRGB[5]  = (255/f, 255/f,   0/f)  # Yellow (Red + Green)
cRGB[6]  = (188/f, 143/f, 143/f)  # Brown
cRGB[7]  = (220/f, 220/f, 220/f)  # Grey
cRGB[8]  = (148/f,   0/f, 211/f)  # Violet
cRGB[9]  = (  0/f, 255/f, 255/f)  # Cyan (Green + Blue)
cRGB[10] = (255/f,   0/f, 255/f)  # Magenta (Red + Blue)
cRGB[11] = (255/f, 165/f,   0/f)  # Orange
cRGB[12] = (114/f,  33/f, 188/f)  # Indigo
cRGB[13] = (103/f,   7/f,  72/f)  # Maroon
cRGB[14] = ( 64/f, 224/f, 208/f)  # Turquoise
cRGB[15] = (  0/f, 139/f,   0/f)  # Intense Green: Green 4 "Grace"

#===================================================================================================

                   #---------------------------------------
                   # VASProcar default values:
                   #---------------------------------------
c_spin_null = 1    # Spin's Null component color (Preto)            
c_spin_up   = 2    # Spin's Up component color   (Vermelho)         
c_spin_down = 4    # Spin's Down component color (Azul)
                   #---------------------------------------
c_DOS  = 7         # DOS color (Grey) 
c_lDOS = 13        # lDOS color (Maroon)
                   #---------------------------------------
c_S    = 4         # S Orbital color    (Blue)
c_P    = 2         # P Orbital color    (Red)
c_D    = 3         # D Orbital color    (Green)
c_F    = 10        # F Orbital color    (Magenta)
c_Px   = 4         # Px Orbital color   (Blue)
c_Py   = 2         # Py Orbital color   (Red)
c_Pz   = 3         # Pz Orbital color   (Green)
c_Dxy  = 4         # Dxy Orbital color  (Blue)
c_Dyz  = 2         # Dyz Orbital color  (Red)
c_Dz2  = 3         # Dz2 Orbital color  (Green)
c_Dxz  = 10        # Dxz Orbital color  (Magenta)
c_Dx2  = 9         # Dx2 Orbital color  (Cyan)
c_Fyx2 = 4         # Fyx2 Orbital color (Blue)
c_Fxyz = 2         # Fxyz Orbital color (Red)
c_Fyz2 = 3         # Fyz2 Orbital color (Green)
c_Fzz2 = 10        # Fzz2 Orbital color (Magenta)
c_Fxz2 = 9         # Fxz2 Orbital color (Cyan)
c_Fzx2 = 5         # Fzx2 Orbital color (Yellow)
c_Fxx2 = 11        # Fxx2 Orbital color (Orange)
                   #---------------------------------------
c_Reg1 = 4         # Region_1 color (Blue)
c_Reg2 = 2         # Region_2 color (Red)
c_Reg3 = 3         # Region_3 color (Green)
c_Reg4 = 10        # Region_4 color (Magenta)
c_Reg5 = 9         # Region_5 color (Cyan)
c_Reg6 = 5         # Region_6 color (Yellow)
                   #---------------------------------------
c_Psi1 = 4         # Psi_1 State color (Blue)
c_Psi2 = 2         # Psi_2 State color (Red)
c_Psi3 = 3         # Psi_3 State color (Green)
c_Psi4 = 10        # Psi_4 State color (Magenta)
c_Psi5 = 9         # Psi_5 State color (Cyan)
c_Psi6 = 5         # Psi_6 State color (Yellow)
                   #---------------------------------------

#===================================================================================================
# Old Color Standard, must be removed from all codes: ==============================================
#===================================================================================================

                   #------------------------------------------
cor_spin = [1]*4   # Initialization of the cor_spin vector
cor_orb  = [1]*14  # Initialization of the cor_orb vector 
                   #------------------------------------------
                   # Valores padrão:
                   #------------------------------------------
cor_spin[1] = 1    # Spin's Null component color (Black)            
cor_spin[2] = 2    # Spin's Up component color   (Red)         
cor_spin[3] = 4    # Spin's Down component color (Blue)
                   #------------------------------------------
cor_orb[1]  = 4    # S Orbital color   (Blue)
cor_orb[2]  = 2    # P Orbital color   (Red)
cor_orb[3]  = 3    # D Orbital color   (Green)
cor_orb[4]  = 4    # Px Orbital color  (Blue)
cor_orb[5]  = 2    # Py Orbital color  (Red)
cor_orb[6]  = 3    # Pz Orbital color  (Green)
cor_orb[7]  = 4    # Dxy Orbital Dxy|Reg_A color (Blue)
cor_orb[8]  = 2    # Dyz Orbital Dyz|Reg_B color (Red)
cor_orb[9]  = 3    # Dz2 Orbital Dz2|Reg_C color (Green)
cor_orb[10] = 10   # Dxz Orbital Dxz|Reg_D color (Magenta)
cor_orb[11] = 9    # Dx2 Orbital Dx2|Reg_E color (Cyan)
                   #------------------------------------------
cor_A  = 4         # Region_A color (Blue)
cor_B  = 2         # Region_B (Red)
cor_C  = 3         # Region_C (Green)
cor_D  = 10        # Region_D (Magenta)
cor_E  = 9         # Region_E (Cyan)
cor_F  = 5         # Region_F (Yellow)
                   #------------------------------------------

#----------------------------------------------------------------------
# Dimensions that define the proportions of 2D graphics: (GRACE) ------
#----------------------------------------------------------------------
                   # Default values:
fig_xmin = 0.12    # 0.12
fig_xmax = 0.82    # 0.82
fig_ymin = 0.075   # 0.075
fig_ymax = 0.95    # 0.95
