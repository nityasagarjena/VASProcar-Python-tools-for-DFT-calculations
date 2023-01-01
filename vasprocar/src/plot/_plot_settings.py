# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

# -----------------------------------------------------------------------
# Com relação ao Plot dos Gráficos via Matplotlib, como deseja salvar?
# Marque [0] para desabilitar ou [1] para habilitar o respectivo formato
# -----------------------------------------------------------------------
save_agr = 1
save_png = 1
save_pdf = 0
save_svg = 0
save_eps = 0

sum_save = save_png + save_pdf + save_eps + save_svg

#----------------------------------------------------------------------
# Cores utilizadas no plot das Projeções: -----------------------------
#----------------------------------------------------------------------

# Obs.: Codigo das cores
# 0 White | 1  Black   | 2  Red    | 3  Green  | 4  Blue   | 5 Yellow    | 6  Borwn | 7 Grey | 8 Violet
# 9 Cyan  | 10 Magenta | 11 Orange | 12 Indigo | 13 Maroon | 14 Turquesa | 15 Green |

#---------------------------------------------------------------------------------------------------       
# Padrao RGB de cores: cor = [Red, Green, Blue] com cada componente variando de 0.0 a 1.0 ----------
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

                   #------------------------------------------
                   # Valores padrão do VASProcar:
                   #------------------------------------------
c_spin_null = 1    # Cor da componente Nula do Spin (Preto)            
c_spin_up   = 2    # Cor da componente Up do Spin   (Vermelho)         
c_spin_down = 4    # Cor da componente Down do Spin (Azul)
                   #------------------------------------------
c_DOS  = 7         # Cor da DOS  (Grey) 
c_lDOS = 13        # Cor da lDOS (Maroon)
                   #------------------------------------------
c_S    = 4         # Cor do Orbital S    (Blue)
c_P    = 2         # Cor do Orbital P    (Red)
c_D    = 3         # Cor do Orbital D    (Green)
c_F    = 10        # Cor do Orbital F    (Magenta)
c_Px   = 4         # Cor do Orbital Px   (Blue)
c_Py   = 2         # Cor do Orbital Py   (Red)
c_Pz   = 3         # Cor do Orbital Pz   (Green)
c_Dxy  = 4         # Cor do Orbital Dxy  (Blue)
c_Dyz  = 2         # Cor do Orbital Dyz  (Red)
c_Dz2  = 3         # Cor do Orbital Dz2  (Green)
c_Dxz  = 10        # Cor do Orbital Dxz  (Magenta)
c_Dx2  = 9         # Cor do Orbital Dx2  (Cyan)
c_Fyx2 = 4         # Cor do Orbital Fyx2 (Blue)
c_Fxyz = 2         # Cor do Orbital Fxyz (Red)
c_Fyz2 = 3         # Cor do Orbital Fyz2 (Green)
c_Fzz2 = 10        # Cor do Orbital Fzz2 (Magenta)
c_Fxz2 = 9         # Cor do Orbital Fxz2 (Cyan)
c_Fzx2 = 5         # Cor do Orbital Fzx2 (Yellow)
c_Fxx2 = 11        # Cor do Orbital Fxx2 (Orange)
                   #------------------------------------------
c_Reg1 = 4         # Cor da Região_1 (Blue)
c_Reg2 = 2         # Cor da Região_2 (Red)
c_Reg3 = 3         # Cor da Região_3 (Green)
c_Reg4 = 10        # Cor da Região_4 (Magenta)
c_Reg5 = 9         # Cor da Região_5 (Cyan)
c_Reg6 = 5         # Cor da Região_6 (Yellow)
                   #------------------------------------------
c_Psi1 = 4         # Cor do Estado Psi_1 (Blue)
c_Psi2 = 2         # Cor do Estado Psi_2 (Red)
c_Psi3 = 3         # Cor do Estado Psi_3 (Green)
c_Psi4 = 10        # Cor do Estado Psi_4 (Magenta)
c_Psi5 = 9         # Cor do Estado Psi_5 (Cyan)
c_Psi6 = 5         # Cor do Estado Psi_6 (Yellow)
                   #------------------------------------------

#===================================================================================================
#Padrão antigo de Cores, deve ser eliminado de todos os códigos ====================================
#===================================================================================================

                   #------------------------------------------
cor_spin = [1]*4   # Inicialização do vetor cor_spin
cor_orb  = [1]*14  # Inicialização do vetor cor_orb
                   #------------------------------------------
                   # Valores padrão:
                   #------------------------------------------
cor_spin[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor_spin[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor_spin[3] = 4    # Cor da componente Down do Spin (Azul)
                   #------------------------------------------
cor_orb[1]  = 4    # Cor do Orbital S   (Azul)
cor_orb[2]  = 2    # Cor do Orbital P   (Vermelho)
cor_orb[3]  = 3    # Cor do Orbital D   (Verde)
cor_orb[4]  = 4    # Cor do Orbital Px  (Azul)
cor_orb[5]  = 2    # Cor do Orbital Py  (Vermelho)
cor_orb[6]  = 3    # Cor do Orbital Pz  (Verde)
cor_orb[7]  = 4    # Cor do Orbital Dxy|Reg_A (Azul)
cor_orb[8]  = 2    # Cor do Orbital Dyz|Reg_B (Vermelho)
cor_orb[9]  = 3    # Cor do Orbital Dz2|Reg_C (Verde)
cor_orb[10] = 10   # Cor do Orbital Dxz|Reg_D (Magenta)
cor_orb[11] = 9    # Cor do Orbital Dx2|Reg_E (Ciano)
                   #------------------------------------------
cor_A  = 4         # Cor da Região A (Azul)
cor_B  = 2         # Cor da Região B (Vermelho)
cor_C  = 3         # Cor da Região C (Verde)
cor_D  = 10        # Cor da Região D (Magenta)
cor_E  = 9         # Cor da Região E (Ciano)
cor_F  = 5         # Cor da Região F (Amarelo)
                   #------------------------------------------

#----------------------------------------------------------------------
# Dimensoes que definem as proporcões dos gráficos 2D: (GRACE) --------
#----------------------------------------------------------------------
                   # Valores padrão:
fig_xmin = 0.12    # 0.12
fig_xmax = 0.82    # 0.82
fig_ymin = 0.075   # 0.075
fig_ymax = 0.95    # 0.95
