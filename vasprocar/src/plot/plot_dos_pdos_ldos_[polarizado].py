
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print ("============ Plotting DOS, pDOS, lDOS (Matplotlib) ============")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  
print(" ")

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/DOS/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#-----------------------------------------------------------------------------------------------      
# RGB color standard: color = [Red, Green, Blue] with each component ranging from 0.0 to 1.0 ---       
#-----------------------------------------------------------------------------------------------

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

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#======================================================================

dos_up = np.loadtxt(dir_output + 'DOS_pDOS_lDOS_up.dat') 
dos_up.shape

dos_down = np.loadtxt(dir_output + 'DOS_pDOS_lDOS_down.dat') 
dos_down.shape

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#---------------------------------------------------------------------- 

#======================================================================

if (n_orb <= 4):  loop = 1          
if (n_orb >= 9):  loop = 3

# if (n_orb == 9):  loop = 3
# if (n_orb == 16): loop = 4

transp = 0.25
linew = 0.5

if (esc == 0): label_add = ''
if (esc == 1): label_add = 'l-'

energia = dos_up[:,0] + dE_fermi

for l in range (1,(loop+1)):     # Loop for analysis of projections

    fig, ax = plt.subplots()

    # Plot of Projections ===================================================

    if (l == 1):
       print ("================================") 
       if (n_orb == 3 or n_orb == 9):
          print ("Analyzing DOS and pDOS (S|P|D)  ") 
       if (n_orb == 4 or n_orb == 16):
          print ("Analyzing DOS and pDOS (S|P|D|F)") 
       #---------------------------------------------------
       dos_u_tot = dos_up[:,1];   dos_d_tot = dos_down[:,1]
       ldos_u    = dos_up[:,2];   ldos_d    = dos_down[:,2]
       #---------------------------------------------------
       if (esc == 0):
          pdos_u_S = dos_up[:,3];   pdos_d_S = dos_down[:,3]
          pdos_u_P = dos_up[:,5];   pdos_d_P = dos_down[:,5]
          pdos_u_D = dos_up[:,7];   pdos_d_D = dos_down[:,7]
          pdos_u_F = dos_up[:,9];   pdos_d_F = dos_down[:,9]
       if (esc == 1):   
          pdos_u_S = dos_up[:,4];   pdos_d_S = dos_down[:,4]
          pdos_u_P = dos_up[:,6];   pdos_d_P = dos_down[:,6]
          pdos_u_D = dos_up[:,8];   pdos_d_D = dos_down[:,8]              
          pdos_u_F = dos_up[:,10];  pdos_d_F = dos_down[:,10] 
       #-------------------------
       x_final   = max(dos_u_tot)
       x_inicial = min(dos_d_tot)
       #=============================================================================================================
       ax.plot(dos_u_tot, energia, color = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'DOS')
       ax.fill(dos_u_tot, energia, color = cRGB[c_DOS], alpha = transp)
       #-------------------------------------------------------------------------------------------------------------
       ax.plot(dos_d_tot, energia, color = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = '')
       ax.fill(dos_d_tot, energia, color = cRGB[c_DOS], alpha = transp)
       #=============================================================================================================
       if (esc == 1):
          ax.plot(ldos_u, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = label_add + 'DOS')
          ax.fill(ldos_u, energia, color = cRGB[c_lDOS], alpha = transp)
          #----------------------------------------------------------------------------------------------------------
          ax.plot(ldos_d, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = '')
          ax.fill(ldos_d, energia, color = cRGB[c_lDOS], alpha = transp) 
       #=============================================================================================================
       ax.plot(pdos_u_S, energia, color = cRGB[c_S], linestyle = '-', linewidth = linew, label = label_add + 'S')
       ax.fill(pdos_u_S, energia, color = cRGB[c_S], alpha = transp)
       ax.plot(pdos_u_P, energia, color = cRGB[c_P], linestyle = '-', linewidth = linew, label = label_add + 'P')
       ax.fill(pdos_u_P, energia, color = cRGB[c_P], alpha = transp)
       ax.plot(pdos_u_D, energia, color = cRGB[c_D], linestyle = '-', linewidth = linew, label = label_add + 'D')
       ax.fill(pdos_u_D, energia, color = cRGB[c_D], alpha = transp)
       if (n_orb == 4 or n_orb == 16):
          ax.plot(pdos_u_F, energia, color = cRGB[c_F], linestyle = '-', linewidth = linew, label = label_add + 'F')
          ax.fill(pdos_u_F, energia, color = cRGB[c_F], alpha = transp)          
       #-------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_S, energia, color = cRGB[c_S], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_S, energia, color = cRGB[c_S], alpha = transp)
       ax.plot(pdos_d_P, energia, color = cRGB[c_P], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_P, energia, color = cRGB[c_P], alpha = transp)
       ax.plot(pdos_d_D, energia, color = cRGB[c_D], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_D, energia, color = cRGB[c_D], alpha = transp) 
       if (n_orb == 4 or n_orb == 16):
          ax.plot(pdos_d_F, energia, color = cRGB[c_F], linestyle = '-', linewidth = linew, label = '')
          ax.fill(pdos_d_F, energia, color = cRGB[c_F], alpha = transp)
       #=============================================================================================================
       if (esc == 0): file = 'DOS_pDOS'
       if (esc == 1): file = 'DOS_lpDOS'
       #--------------------------------
       
    if (l == 2):
       print ("Analyzing pDOS (Px|Py|Pz)")
       #----------------------------------------------------
       pdos_u_P = dos_up[:,5];    pdos_d_P = dos_down[:,5]
       ldos_u_P = dos_up[:,6];    ldos_d_P = dos_down[:,6]
       pdos_u_Px = dos_up[:,11];  pdos_d_Px = dos_down[:,11]
       pdos_u_Py = dos_up[:,12];  pdos_d_Py = dos_down[:,12]
       pdos_u_Pz = dos_up[:,13];  pdos_d_Pz = dos_down[:,13]
       #----------------------------------------------------
       x_final   = max(dos_u_tot)
       x_inicial = min(dos_d_tot)         
       #===============================================================================================================
       ax.plot(pdos_u_P, energia, color  = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(pdos_u_P, energia, color  = cRGB[c_DOS], alpha = transp)
       #---------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_P, energia, color  = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_P, energia, color  = cRGB[c_DOS], alpha = transp)
       #=============================================================================================================== 
       if (esc == 1):         
          ax.plot(ldos_u_P, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = label_add + 'P')
          ax.fill(ldos_u_P, energia, color  = cRGB[c_lDOS], alpha = transp)
          #------------------------------------------------------------------------------------------------------------
          ax.plot(ldos_d_P, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = '')
          ax.fill(ldos_d_P, energia, color  = cRGB[c_lDOS], alpha = transp)
       #===============================================================================================================       
       ax.plot(pdos_u_Px, energia, color = cRGB[c_Px],  linestyle = '-', linewidth = linew, label = label_add + 'P$_{x}$')
       ax.fill(pdos_u_Px, energia, color = cRGB[c_Px],  alpha = transp)
       ax.plot(pdos_u_Py, energia, color = cRGB[c_Py],  linestyle = '-', linewidth = linew, label = label_add + 'P$_{y}$')
       ax.fill(pdos_u_Py, energia, color = cRGB[c_Py],  alpha = transp)
       ax.plot(pdos_u_Pz, energia, color = cRGB[c_Pz],  linestyle = '-', linewidth = linew, label = label_add + 'P$_{z}$')
       ax.fill(pdos_u_Pz, energia, color = cRGB[c_Pz],  alpha = transp)
       #---------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_Px, energia, color = cRGB[c_Px],  linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Px, energia, color = cRGB[c_Px],  alpha = transp)
       ax.plot(pdos_d_Py, energia, color = cRGB[c_Py],  linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Py, energia, color = cRGB[c_Py],  alpha = transp)
       ax.plot(pdos_d_Pz, energia, color = cRGB[c_Pz],  linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Pz, energia, color = cRGB[c_Pz],  alpha = transp)
       #===============================================================================================================
       if (esc == 0): file = 'pDOS_P'
       if (esc == 1): file = 'lpDOS_P'
       #------------------------------

    if (l == 3):
       print ("Analyzing pDOS (Dxy|Dyz|Dz2|Dxz|Dx2)") 
       #------------------------------------------------------
       pdos_u_D = dos_up[:,7];     pdos_d_D = dos_down[:,7]
       ldos_u_D = dos_up[:,8];     ldos_d_D = dos_down[:,8] 
       pdos_u_Dxy = dos_up[:,14];  pdos_d_Dxy = dos_down[:,14]
       pdos_u_Dyz = dos_up[:,15];  pdos_d_Dyz = dos_down[:,15]
       pdos_u_Dz2 = dos_up[:,16];  pdos_d_Dz2 = dos_down[:,16]
       pdos_u_Dxz = dos_up[:,17];  pdos_d_Dxz = dos_down[:,17]
       pdos_u_Dx2 = dos_up[:,18];  pdos_d_Dx2 = dos_down[:,18]
       #------------------------------------------------------
       x_final   = max(dos_u_tot)
       x_inicial = min(dos_d_tot)
       #===============================================================================================================
       ax.plot(pdos_u_D, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(pdos_u_D, energia, color   = cRGB[c_DOS], alpha = transp)
       #---------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_D, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_D, energia, color   = cRGB[c_DOS], alpha = transp)
       #=============================================================================================================== 
       if (esc == 1):         
          ax.plot(ldos_u_D, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = label_add + 'D')
          ax.fill(ldos_u_D, energia, color  = cRGB[c_lDOS], alpha = transp)
          #---------------------------------------------------------------------------------------------------------------
          ax.plot(ldos_d_D, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = '')
          ax.fill(ldos_d_D, energia, color  = cRGB[c_lDOS], alpha = transp)
       #===============================================================================================================
       ax.plot(pdos_u_Dxy, energia, color = cRGB[c_Dxy], linestyle = '-', linewidth = linew, label = label_add + 'D$_{xy}$')
       ax.fill(pdos_u_Dxy, energia, color = cRGB[c_Dxy], alpha = transp)
       ax.plot(pdos_u_Dyz, energia, color = cRGB[c_Dyz], linestyle = '-', linewidth = linew, label = label_add + 'D$_{yz}$')
       ax.fill(pdos_u_Dyz, energia, color = cRGB[c_Dyz], alpha = transp)
       ax.plot(pdos_u_Dz2, energia, color = cRGB[c_Dz2], linestyle = '-', linewidth = linew, label = label_add + 'D$_{z^{2}}$')
       ax.fill(pdos_u_Dz2, energia, color = cRGB[c_Dz2], alpha = transp)
       ax.plot(pdos_u_Dxz, energia, color = cRGB[c_Dxz], linestyle = '-', linewidth = linew, label = label_add + 'D$_{xz}$')
       ax.fill(pdos_u_Dxz, energia, color = cRGB[c_Dxz], alpha = transp)
       ax.plot(pdos_u_Dx2, energia, color = cRGB[c_Dx2], linestyle = '-', linewidth = linew, label = label_add + 'D$_{x^{2}}$')
       ax.fill(pdos_u_Dx2, energia, color = cRGB[c_Dx2], alpha = transp)
       #---------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_Dxy, energia, color = cRGB[c_Dxy], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Dxy, energia, color = cRGB[c_Dxy], alpha = transp)
       ax.plot(pdos_d_Dyz, energia, color = cRGB[c_Dyz], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Dyz, energia, color = cRGB[c_Dyz], alpha = transp)
       ax.plot(pdos_d_Dz2, energia, color = cRGB[c_Dz2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Dz2, energia, color = cRGB[c_Dz2], alpha = transp)
       ax.plot(pdos_d_Dxz, energia, color = cRGB[c_Dxz], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Dxz, energia, color = cRGB[c_Dxz], alpha = transp)
       ax.plot(pdos_d_Dx2, energia, color = cRGB[c_Dx2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Dx2, energia, color = cRGB[c_Dx2], alpha = transp)
       #===============================================================================================================
       if (esc == 0): file = 'pDOS_D'
       if (esc == 1): file = 'lpDOS_D'
       #------------------------------

    if (l == 4):
       print ("Analyzing pDOS (Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2)") 
       #---------------------------------------------------------
       pdos_u_F = dos_up[:,9];      pdos_d_F = dos_down[:,9]
       ldos_u_F = dos_up[:,10];     ldos_d_F = dos_down[:,10] 
       pdos_u_Fyx2 = dos_up[:,19];  pdos_d_Fyx2 = dos_down[:,19]
       pdos_u_Fxyz = dos_up[:,20];  pdos_d_Fxyz = dos_down[:,20]
       pdos_u_Fyz2 = dos_up[:,21];  pdos_d_Fyz2 = dos_down[:,21]
       pdos_u_Fzz2 = dos_up[:,22];  pdos_d_Fzz2 = dos_down[:,22]
       pdos_u_Fxz2 = dos_up[:,23];  pdos_d_Fxz2 = dos_down[:,23]
       pdos_u_Fzx2 = dos_up[:,24];  pdos_d_Fzx2 = dos_down[:,24]
       pdos_u_Fxx2 = dos_up[:,25];  pdos_d_Fxx22 = dos_down[:,25]
       #---------------------------------------------------------
       x_final   = max(dos_u_tot)
       x_inicial = min(dos_d_tot)
       #==========================================================================================================================
       ax.plot(pdos_u_F, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'F')
       ax.fill(pdos_u_F, energia, color   = cRGB[c_DOS], alpha = transp)
       #--------------------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_F, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_F, energia, color   = cRGB[c_DOS], alpha = transp)
       #==========================================================================================================================
       if (esc == 1):         
          ax.plot(ldos_u_F, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = label_add + 'F')
          ax.fill(ldos_u_F, energia, color  = cRGB[c_lDOS], alpha = transp)
          #-----------------------------------------------------------------------------------------------------------------------
          ax.plot(ldos_d_F, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = '')
          ax.fill(ldos_d_F, energia, color  = cRGB[c_lDOS], alpha = transp)
       #==========================================================================================================================
       ax.plot(pdos_u_Fyx2, energia, color = cRGB[c_Fyx2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{yx^{2}}$')
       ax.fill(pdos_u_Fyx2, energia, color = cRGB[c_Fyx2], alpha = transp)
       ax.plot(pdos_u_Fxyz, energia, color = cRGB[c_Fxyz], linestyle = '-', linewidth = linew, label = label_add + 'F$_{xyz}$')
       ax.fill(pdos_u_Fxyz, energia, color = cRGB[c_Fxyz], alpha = transp)
       ax.plot(pdos_u_Fyz2, energia, color = cRGB[c_Fyz2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{yz^{2}}$')
       ax.fill(pdos_u_Fyz2, energia, color = cRGB[c_Fyz2], alpha = transp)
       ax.plot(pdos_u_Fzz2, energia, color = cRGB[c_Fzz2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{zz^{2}}$')
       ax.fill(pdos_u_Fzz2, energia, color = cRGB[c_Fzz2], alpha = transp)
       ax.plot(pdos_u_Fxz2, energia, color = cRGB[c_Fxz2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{xz^{2}}$')
       ax.fill(pdos_u_Fxz2, energia, color = cRGB[c_Fxz2], alpha = transp)
       ax.plot(pdos_u_Fzx2, energia, color = cRGB[c_Fzx2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{zx^{2}}$')
       ax.fill(pdos_u_Fzx2, energia, color = cRGB[c_Fzx2], alpha = transp)
       ax.plot(pdos_u_Fxx2, energia, color = cRGB[c_Fxx2], linestyle = '-', linewidth = linew, label = label_add + 'F$_{xx^{2}}$')
       ax.fill(pdos_u_Fxx2, energia, color = cRGB[c_Fxx2], alpha = transp)
       #--------------------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_d_Fyx2, energia, color = cRGB[c_Fyx2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fyx2, energia, color = cRGB[c_Fyx2], alpha = transp)
       ax.plot(pdos_d_Fxyz, energia, color = cRGB[c_Fxyz], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fxyz, energia, color = cRGB[c_Fxyz], alpha = transp)
       ax.plot(pdos_d_Fyz2, energia, color = cRGB[c_Fyz2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fyz2, energia, color = cRGB[c_Fyz2], alpha = transp)
       ax.plot(pdos_d_Fzz2, energia, color = cRGB[c_Fzz2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fzz2, energia, color = cRGB[c_Fzz2], alpha = transp)
       ax.plot(pdos_d_Fxz2, energia, color = cRGB[c_Fxz2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fxz2, energia, color = cRGB[c_Fxz2], alpha = transp)
       ax.plot(pdos_d_Fzx2, energia, color = cRGB[c_Fzx2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fzx2, energia, color = cRGB[c_Fzx2], alpha = transp)
       ax.plot(pdos_d_Fxx2, energia, color = cRGB[c_Fxx2], linestyle = '-', linewidth = linew, label = '')
       ax.fill(pdos_d_Fxx2, energia, color = cRGB[c_Fxx2], alpha = transp)
       #==========================================================================================================================
       if (esc == 0): file = 'pDOS_F'
       if (esc == 1): file = 'lpDOS_F'
       #------------------------------

    # Highlighting the Fermi energy in the Band structure ===============================================================

    plt.plot([-100.0, +100.0], [dest_fermi, dest_fermi], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)

    #====================================================================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((energ_min + dE_fermi , energ_max + dE_fermi))

    plt.xlabel("Density of States")
           
    if (esc_fermi == 0):
       plt.ylabel('$E$ (eV)')
    if (esc_fermi == 1):
       plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(title="")
    ax.legend(loc = "upper right", title = "")    
    # ax.legend(loc="best", title="")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_svg == 1): plt.savefig(dir_output + file + '.svg', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()

#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
    
print(" ")
print("====== Plotting the Magnetization (DOS_Up - DOS_Down) ======")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")
print(" ")

c_label = r'${\Delta}$'
c_file  = '_[Delta]' 

#======================================================================

for l in range (1,(loop+1)):     # Loop for analysis of projections

    fig, ax = plt.subplots()

    # Plot of Projections =============================================

    if (l == 1):
       print ("===================================")
       print ("Analyzing the Magnetization (S|P|D)")
       #--------------------------------------------
       dos_tot = dos_up[:,1] + dos_down[:,1]
       ldos    = dos_up[:,2] + dos_down[:,2]
       if (esc == 0):
          pdos_S   = dos_up[:,3]  + dos_down[:,3]
          pdos_P   = dos_up[:,5]  + dos_down[:,5]
          pdos_D   = dos_up[:,7]  + dos_down[:,7]
          pdos_F   = dos_up[:,9]  + dos_down[:,9]
       if (esc == 1):                 
          pdos_S   = dos_up[:,4]  + dos_down[:,4]
          pdos_P   = dos_up[:,6]  + dos_down[:,6]
          pdos_D   = dos_up[:,8]  + dos_down[:,8]
          pdos_F   = dos_up[:,10] + dos_down[:,10]
       #-------------------------
       x_final   = max(dos_tot)
       x_inicial = min(dos_tot)
       #-------------------------------------------------------------------------------------------------------------------------
       ax.plot(dos_tot, energia, color = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = c_label + 'DOS')
       ax.fill(dos_tot, energia, color = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(ldos, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = c_label + label_add + 'DOS')
          ax.fill(ldos, energia, color = cRGB[c_lDOS], alpha = transp)          
       ax.plot(pdos_S, energia, color = cRGB[c_S], linestyle = '-', linewidth = linew, label = c_label + label_add + 'S')
       ax.fill(pdos_S, energia, color = cRGB[c_S], alpha = transp)
       ax.plot(pdos_P, energia, color = cRGB[c_P], linestyle = '-', linewidth = linew, label = c_label + label_add + 'P')
       ax.fill(pdos_P, energia, color = cRGB[c_P], alpha = transp)
       ax.plot(pdos_D, energia, color = cRGB[c_D], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D')
       ax.fill(pdos_D, energia, color = cRGB[c_D], alpha = transp)  
       if (n_orb == 4 or n_orb == 16):
          ax.plot(pdos_F, energia, color = cRGB[c_F], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F')
          ax.fill(pdos_F, energia, color = cRGB[c_F], alpha = transp)
       #-------------------------------------------------------------------------------------------------------------------------
       if (esc == 0): file = 'DOS_pDOS' + c_file
       if (esc == 1): file = 'DOS_pDOS_lDOS' + c_file
       
    if (l == 2):
       print ("Analyzing the Magnetization (Px|Py|Pz)")       
       #-----------------------------------------------
       pdos_P  = dos_up[:,5]  + dos_down[:,5]
       ldos_P  = dos_up[:,6]  + dos_down[:,6]       
       pdos_Px = dos_up[:,11] + dos_down[:,11]
       pdos_Py = dos_up[:,12] + dos_down[:,12]
       pdos_Pz = dos_up[:,13] + dos_down[:,13]
       #-----------------------       
       x_final   = max(pdos_P)
       x_inicial = min(pdos_P)  
       #-------------------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_P, energia, color  = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = c_label + 'P')
       ax.fill(pdos_P, energia, color  = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(ldos_P, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = c_label + label_add + 'P')
          ax.fill(ldos_P, energia, color = cRGB[c_lDOS], alpha = transp)       
       ax.plot(pdos_Px, energia, color = cRGB[c_Px],  linestyle = '-', linewidth = linew, label = c_label + label_add + 'P$_{x}$')
       ax.fill(pdos_Px, energia, color = cRGB[c_Px],  alpha = transp)
       ax.plot(pdos_Py, energia, color = cRGB[c_Py],  linestyle = '-', linewidth = linew, label = c_label + label_add + 'P$_{y}$')
       ax.fill(pdos_Py, energia, color = cRGB[c_Py],  alpha = transp)
       ax.plot(pdos_Pz, energia, color = cRGB[c_Pz],  linestyle = '-', linewidth = linew, label = c_label + label_add + 'P$_{z}$')
       ax.fill(pdos_Pz, energia, color = cRGB[c_Pz],  alpha = transp)
       #-------------------------------------------------------------------------------------------------------------------------
       if (esc == 0): file = 'pDOS_P' + c_file
       if (esc == 1): file = 'pDOS_lDOS_P' + c_file

    if (l == 3):
       print ("Analyzing the Magnetization (Dxy|Dyz|Dz2|Dxz|Dx2)") 
       #----------------------------------------------------------
       pdos_D   = dos_up[:,7]  + dos_down[:,7]       
       ldos_D   = dos_up[:,8]  + dos_down[:,8]
       pdos_Dxy = dos_up[:,14] + dos_down[:,14]
       pdos_Dyz = dos_up[:,15] + dos_down[:,15]
       pdos_Dz2 = dos_up[:,16] + dos_down[:,16]
       pdos_Dxz = dos_up[:,17] + dos_down[:,17]
       pdos_Dx2 = dos_up[:,18] + dos_down[:,18]
       #-----------------------       
       x_final   = max(pdos_D)
       x_inicial = min(pdos_D)
       #-------------------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_D, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = c_label + 'D')
       ax.fill(pdos_D, energia, color   = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(ldos_D, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D')
          ax.fill(ldos_D, energia, color = cRGB[c_lDOS], alpha = transp)       
       ax.plot(pdos_Dxy, energia, color = cRGB[c_Dxy], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D$_{xy}$')
       ax.fill(pdos_Dxy, energia, color = cRGB[c_Dxy], alpha = transp)
       ax.plot(pdos_Dyz, energia, color = cRGB[c_Dyz], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D$_{yz}$')
       ax.fill(pdos_Dyz, energia, color = cRGB[c_Dyz], alpha = transp)
       ax.plot(pdos_Dz2, energia, color = cRGB[c_Dz2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D$_{z^{2}}$')
       ax.fill(pdos_Dz2, energia, color = cRGB[c_Dz2], alpha = transp)
       ax.plot(pdos_Dxz, energia, color = cRGB[c_Dxz], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D$_{xz}$')
       ax.fill(pdos_Dxz, energia, color = cRGB[c_Dxz], alpha = transp)
       ax.plot(pdos_Dx2, energia, color = cRGB[c_Dx2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'D$_{x^{2}}$')
       ax.fill(pdos_Dx2, energia, color = cRGB[c_Dx2], alpha = transp)
       #-------------------------------------------------------------------------------------------------------------------------
       if (esc == 0): file = 'pDOS_D' + c_file
       if (esc == 1): file = 'pDOS_lDOS_D' + c_file

    if (l == 4):
       print ("Analyzing the Magnetization (Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2)") 
       #-------------------------------------------------------------------------
       pdos_F   = dos_up[:,9]   + dos_down[:,9]       
       ldos_F   = dos_up[:,10]  + dos_down[:,10]
       pdos_Fyx2 = dos_up[:,19] + dos_down[:,19]
       pdos_Fxyz = dos_up[:,20] + dos_down[:,20]
       pdos_Fyz2 = dos_up[:,21] + dos_down[:,21]
       pdos_Fzz2 = dos_up[:,22] + dos_down[:,22]
       pdos_Fxz2 = dos_up[:,23] + dos_down[:,23]
       pdos_Fzx2 = dos_up[:,24] + dos_down[:,24]
       pdos_Fxx2 = dos_up[:,25] + dos_down[:,25]
       #-----------------------       
       x_final   = max(pdos_F)
       x_inicial = min(pdos_F)
       #-------------------------------------------------------------------------------------------------------------------------
       ax.plot(pdos_F, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = c_label + 'F')
       ax.fill(pdos_F, energia, color   = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(ldos_F, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F')
          ax.fill(ldos_F, energia, color = cRGB[c_lDOS], alpha = transp)       
       ax.plot(pdos_Fyx2, energia, color = cRGB[c_Fyx2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{yx^{2}}$')
       ax.fill(pdos_Fyx2, energia, color = cRGB[c_Fyx2], alpha = transp)
       ax.plot(pdos_Fxyz, energia, color = cRGB[c_Fxyz], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{xyz}$')
       ax.fill(pdos_Fxyz, energia, color = cRGB[c_Fxyz], alpha = transp)
       ax.plot(pdos_Fyz2, energia, color = cRGB[c_Fyz2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{yz^{2}}$')
       ax.fill(pdos_Fyz2, energia, color = cRGB[c_Fyz2], alpha = transp)
       ax.plot(pdos_Fzz2, energia, color = cRGB[c_Fzz2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{zz^{2}}$')
       ax.fill(pdos_Fzz2, energia, color = cRGB[c_Fzz2], alpha = transp)
       ax.plot(pdos_Fxz2, energia, color = cRGB[c_Fxz2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{xz^{2}}$')
       ax.fill(pdos_Fxz2, energia, color = cRGB[c_Fxz2], alpha = transp)
       ax.plot(pdos_Fzx2, energia, color = cRGB[c_Fzx2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{zx^{2}}$')
       ax.fill(pdos_Fzx2, energia, color = cRGB[c_Fzx2], alpha = transp)
       ax.plot(pdos_Fxx2, energia, color = cRGB[c_Fxx2], linestyle = '-', linewidth = linew, label = c_label + label_add + 'F$_{xx^{2}}$')
       ax.fill(pdos_Fxx2, energia, color = cRGB[c_Fxx2], alpha = transp)
       #-------------------------------------------------------------------------------------------------------------------------
       if (esc == 0): file = 'pDOS_F' + c_file
       if (esc == 1): file = 'pDOS_lDOS_F' + c_file

    # Highlighting the Fermi energy in the Band structure ===============================================================

    plt.plot([-100.0, +100.0], [dest_fermi, dest_fermi], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)

    #====================================================================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((energ_min + dE_fermi , energ_max + dE_fermi))

    plt.xlabel("Magnetization (DOS_Up - DOS_Down)")
           
    if (esc_fermi == 0):
       plt.ylabel('$E$ (eV)')
    if (esc_fermi == 1):
       plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(title="")
    ax.legend(loc = "upper right", title = "")    
    # ax.legend(loc="best", title="")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_svg == 1): plt.savefig(dir_output + file + '.svg', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#--------------------------------------------------------------------------- 

# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license