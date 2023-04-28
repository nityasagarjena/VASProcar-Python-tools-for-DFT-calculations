
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

dos = np.loadtxt(dir_output + 'DOS_pDOS_lDOS.dat') 
dos.shape

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#---------------------------------------------------------------------- 

#======================================================================

if (n_orb <= 4):  loop = 1          
if (n_orb == 9):  loop = 3
if (n_orb == 16): loop = 4

transp = 0.25
linew = 0.5

if (esc == 0): label_add = ''
if (esc == 1): label_add = 'l-'

energia = dos[:,0] + dE_fermi 

for l in range (1,(loop+1)):     # Loop for analysis of projections

    fig, ax = plt.subplots() 

    # Plot of Projections ==================================================

    if (l == 1):
       #---------------------------------------------
       print ("================================") 
       if (n_orb == 3 or n_orb == 9):
          print ("Analyzing DOS and pDOS (S|P|D)  ") 
       if (n_orb == 4 or n_orb == 16):
          print ("Analyzing DOS and pDOS (S|P|D|F)") 
       #---------------------------------------------
       dos_tot = dos[:,1]; ldos    = dos[:,2]
       pdos_S  = dos[:,3]; lpdos_S = dos[:,4]
       pdos_P  = dos[:,5]; lpdos_P = dos[:,6]
       pdos_D  = dos[:,7]; lpdos_D = dos[:,8]
       pdos_F  = dos[:,9]; lpdos_F = dos[:,10]
       #--------------------------------------
       ax.plot(dos_tot, energia, color = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'DOS')
       ax.fill(dos_tot, energia, color = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(ldos, energia, color = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = (label_add + 'DOS'))
          ax.fill(ldos, energia, color = cRGB[c_lDOS], alpha = transp)          
       if (esc == 0):
          ax.plot(pdos_S, energia, color = cRGB[c_S], linestyle = '-', linewidth = linew, label = (label_add + 'S'))
          ax.fill(pdos_S, energia, color = cRGB[c_S], alpha = transp)
          ax.plot(pdos_P, energia, color = cRGB[c_P], linestyle = '-', linewidth = linew, label = (label_add + 'P'))
          ax.fill(pdos_P, energia, color = cRGB[c_P], alpha = transp)
          ax.plot(pdos_D, energia, color = cRGB[c_D], linestyle = '-', linewidth = linew, label = (label_add + 'D'))
          ax.fill(pdos_D, energia, color = cRGB[c_D], alpha = transp)
          if (n_orb == 4 or n_orb == 16):
             ax.plot(pdos_F, energia, color = cRGB[c_F], linestyle = '-', linewidth = linew, label = (label_add + 'F'))
             ax.fill(pdos_F, energia, color = cRGB[c_F], alpha = transp)
       if (esc == 1):
          ax.plot(lpdos_S, energia, color = cRGB[c_S], linestyle = '-', linewidth = linew, label = (label_add + 'S'))
          ax.fill(lpdos_S, energia, color = cRGB[c_S], alpha = transp)
          ax.plot(lpdos_P, energia, color = cRGB[c_P], linestyle = '-', linewidth = linew, label = (label_add + 'P'))
          ax.fill(lpdos_P, energia, color = cRGB[c_P], alpha = transp)
          ax.plot(lpdos_D, energia, color = cRGB[c_D], linestyle = '-', linewidth = linew, label = (label_add + 'D'))
          ax.fill(lpdos_D, energia, color = cRGB[c_D], alpha = transp)       
          if (n_orb == 4 or n_orb == 16):
             ax.plot(lpdos_F, energia, color = cRGB[c_F], linestyle = '-', linewidth = linew, label = (label_add + 'F'))
             ax.fill(lpdos_F, energia, color = cRGB[c_F], alpha = transp)
       #-------------------------------
       if (esc == 0): file = 'DOS_pDOS'
       if (esc == 1): file = 'DOS_lpDOS'
       
    if (l == 2):
       #----------------------------------
       print ("Analyzing pDOS (Px|Py|Pz)")        
       #----------------------------------
       pdos_Px = dos[:,11]
       pdos_Py = dos[:,12]
       pdos_Pz = dos[:,13]
       #------------------
       ax.plot(pdos_P, energia, color  = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(pdos_P, energia, color  = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(lpdos_P, energia, color  = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = (label_add + 'P'))
          ax.fill(lpdos_P, energia, color  = cRGB[c_lDOS], alpha = transp)   
       ax.plot(pdos_Px, energia, color = cRGB[c_Px],  linestyle = '-', linewidth = linew, label = (label_add + 'P$_{x}$'))
       ax.fill(pdos_Px, energia, color = cRGB[c_Px],  alpha = transp)
       ax.plot(pdos_Py, energia, color = cRGB[c_Py],  linestyle = '-', linewidth = linew, label = (label_add + 'P$_{y}$'))
       ax.fill(pdos_Py, energia, color = cRGB[c_Py],  alpha = transp)
       ax.plot(pdos_Pz, energia, color = cRGB[c_Pz],  linestyle = '-', linewidth = linew, label = (label_add + 'P$_{z}$'))
       ax.fill(pdos_Pz, energia, color = cRGB[c_Pz],  alpha = transp)

       #-----------------------------
       if (esc == 0): file = 'pDOS_P'
       if (esc == 1): file = 'lpDOS_P'

    if (l == 3):
       #---------------------------------------------
       print ("Analyzing pDOS (Dxy|Dyz|Dz2|Dxz|Dx2)")          
       #---------------------------------------------
       pdos_Dxy = dos[:,14]
       pdos_Dyz = dos[:,15]
       pdos_Dz2 = dos[:,16]
       pdos_Dxz = dos[:,17]
       pdos_Dx2 = dos[:,18]        
       #-------------------
       ax.plot(pdos_D, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(pdos_D, energia, color   = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(lpdos_D, energia, color   = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = (label_add + 'D'))
          ax.fill(lpdos_D, energia, color   = cRGB[c_lDOS], alpha = transp)          
       ax.plot(pdos_Dxy, energia, color = cRGB[c_Dxy], linestyle = '-', linewidth = linew, label = (label_add + 'D$_{xy}$'))
       ax.fill(pdos_Dxy, energia, color = cRGB[c_Dxy], alpha = transp)
       ax.plot(pdos_Dyz, energia, color = cRGB[c_Dyz], linestyle = '-', linewidth = linew, label = (label_add + 'D$_{yz}$'))
       ax.fill(pdos_Dyz, energia, color = cRGB[c_Dyz], alpha = transp)
       ax.plot(pdos_Dz2, energia, color = cRGB[c_Dz2], linestyle = '-', linewidth = linew, label = (label_add + 'D$_{z^{2}}$'))
       ax.fill(pdos_Dz2, energia, color = cRGB[c_Dz2], alpha = transp)
       ax.plot(pdos_Dxz, energia, color = cRGB[c_Dxz], linestyle = '-', linewidth = linew, label = (label_add + 'D$_{xz}$'))
       ax.fill(pdos_Dxz, energia, color = cRGB[c_Dxz], alpha = transp)
       ax.plot(pdos_Dx2, energia, color = cRGB[c_Dx2], linestyle = '-', linewidth = linew, label = (label_add + 'D$_{x^{2}}$'))
       ax.fill(pdos_Dx2, energia, color = cRGB[c_Dx2], alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_D'
       if (esc == 1): file = 'lpDOS_D'

    if (l == 4):
       #------------------------------------------------------------
       print ("Analyzing pDOS (Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2)")          
       #------------------------------------------------------------
       pdos_Fyx2 = dos[:,19]
       pdos_Fxyz = dos[:,20]
       pdos_Fyz2 = dos[:,21]
       pdos_Fzz2 = dos[:,22]
       pdos_Fxz2 = dos[:,23]        
       pdos_Fzx2 = dos[:,24]
       pdos_Fxx2 = dos[:,25]  
       #--------------------
       ax.plot(pdos_F, energia, color   = cRGB[c_DOS], linestyle = '-', linewidth = linew, label = 'F')
       ax.fill(pdos_F, energia, color   = cRGB[c_DOS], alpha = transp)
       if (esc == 1):
          ax.plot(lpdos_F, energia, color   = cRGB[c_lDOS], linestyle = '-', linewidth = linew, label = (label_add + 'F'))
          ax.fill(lpdos_F, energia, color   = cRGB[c_lDOS], alpha = transp)          
       ax.plot(pdos_Fyx2, energia, color = cRGB[c_Fyx2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{yx^{2}}$'))
       ax.fill(pdos_Fyx2, energia, color = cRGB[c_Fyx2], alpha = transp)
       ax.plot(pdos_Fxyz, energia, color = cRGB[c_Fxyz], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{xyz}$'))
       ax.fill(pdos_Fxyz, energia, color = cRGB[c_Fxyz], alpha = transp)
       ax.plot(pdos_Fyz2, energia, color = cRGB[c_Fyz2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{yz^{2}}$'))
       ax.fill(pdos_Fyz2, energia, color = cRGB[c_Fyz2], alpha = transp)
       ax.plot(pdos_Fzz2, energia, color = cRGB[c_Fzz2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{zz^{2}}$'))
       ax.fill(pdos_Fzz2, energia, color = cRGB[c_Fzz2], alpha = transp)
       ax.plot(pdos_Fxz2, energia, color = cRGB[c_Fxz2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{xz^{2}}$'))
       ax.fill(pdos_Fxz2, energia, color = cRGB[c_Fxz2], alpha = transp)
       ax.plot(pdos_Fzx2, energia, color = cRGB[c_Fzx2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{zx^{2}}$'))
       ax.fill(pdos_Fzx2, energia, color = cRGB[c_Fzx2], alpha = transp)
       ax.plot(pdos_Fxx2, energia, color = cRGB[c_Fxx2], linestyle = '-', linewidth = linew, label = (label_add + 'F$_{xx^{2}}$'))
       ax.fill(pdos_Fxx2, energia, color = cRGB[c_Fxx2], alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_F'
       if (esc == 1): file = 'lpDOS_F'

    # Highlighting the Fermi energy in the Band structure =================

    plt.plot([x_inicial, x_final], [dest_fermi, dest_fermi], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)

    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((energ_min + dE_fermi , energ_max + dE_fermi ))

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

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------
 
# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license