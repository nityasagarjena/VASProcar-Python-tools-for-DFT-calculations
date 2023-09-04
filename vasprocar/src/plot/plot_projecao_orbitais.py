
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("=========== Plotting the Projections (Matplotlib): ===========")

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
   dir_output = dir_files + '/output/Orbitais/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#======================================================================

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

orbitais = np.loadtxt(dir_output + 'Orbitais.dat') 
orbitais.shape

#----------------------------------------------------------------------

if (esc_fermi == 0):
   #---------------------
   dE_fermi = 0.0
   dest_fermi = Efermi
   #---------------------
   E_min = E_min + Efermi
   E_max = E_max + Efermi
   
if (esc_fermi == 1):
   #-----------------------
   dE_fermi = (Efermi)*(-1)
   dest_fermi = 0.0
   #-----------------------
   E_min = E_min
   E_max = E_max

#----------------------------------------------------------------------

num_bands = 0
bands_sn = ["nao"]*(nb + 1)
selected_bands = bands_range.replace(':', ' ').replace('-', ' ').split()
loop = int(len(selected_bands)/2)
    
for i in range (1,(loop+1)):
    #-----------------------------------------
    loop_i = int(selected_bands[(i-1)*2])
    loop_f = int(selected_bands[((i-1)*2) +1])
    #----------------------------------------------------------------------------------------
    if ((loop_i > nb) or (loop_f > nb) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
       print (" ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("ERROR: The values of the informed bands are incorrect %%%%")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       confirmacao = input (" ")
       exit()
    #----------------------------------------------------------------------     
    for j in range(loop_i, (loop_f + 1)):
        num_bands += 1
        bands_sn[j] = "sim"  

#----------------------------------------------------------------------

#---------------------------------------------------------
# Initialization of Variables and Vectors to be used -----
#---------------------------------------------------------

if (n_orb <= 4):  loop = 1          
if (n_orb == 9):  loop = 3
if (n_orb == 16): loop = 4

rx = orbitais[:,0]
ry = orbitais[:,1] + dE_fermi

dpi = 2*3.1415926535897932384626433832795

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

#===========================================================================
# Plot of the projections of the Orbitals individually: ====================
#===========================================================================
    
for l in range (1,(loop+1)):     # Loop for analysis of projections

    fig, ax = plt.subplots()

    # Plot of Projections ==================================================

    if (l == 1):
       #----------------------------------------------
       S = orbitais[:,2]; pS = ((dpi*S)**2)*peso_total 
       P = orbitais[:,3]; pP = ((dpi*P)**2)*peso_total 
       D = orbitais[:,4]; pD = ((dpi*D)**2)*peso_total
       F = orbitais[:,5]; pF = ((dpi*F)**2)*peso_total
       Orb_tot = S+P+D+F; pOrb_tot = ((dpi*Orb_tot)**2)*peso_total
       #----------------------------------------------------------
       ax.scatter(rx, ry, s = pS, color = cRGB[c_S], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pP, color = cRGB[c_P], alpha = transp, edgecolors = 'none') 
       ax.scatter(rx, ry, s = pD, color = cRGB[c_D], alpha = transp, edgecolors = 'none') 
       if (n_orb == 4 or n_orb == 16):
          ax.scatter(rx, ry, s = pF, color = cRGB[c_F], alpha = transp, edgecolors = 'none') 
       #------------------------------------------------------------------------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_S], alpha = 1.0, edgecolors = 'none', label = 'S')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_P], alpha = 1.0, edgecolors = 'none', label = 'P') 
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_D], alpha = 1.0, edgecolors = 'none', label = 'D')
       if (n_orb == 4 or n_orb == 16):
          ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_F], alpha = 1.0, edgecolors = 'none', label = 'F')
       #--------------------       
       if (n_orb == 3 or n_orb == 9):  file = 'Orbitais_SPD'
       if (n_orb == 4 or n_orb == 16): file = 'Orbitais_SPDF'
    
    if (l == 2):
       #--------------------------------------------------
       Px = orbitais[:,6];  pPx = ((dpi*Px)**2)*peso_total
       Py = orbitais[:,7];  pPy = ((dpi*Py)**2)*peso_total
       Pz = orbitais[:,8];  pPz = ((dpi*Pz)**2)*peso_total
       #--------------------------------------------------
       ax.scatter(rx, ry, s = pPx, color = cRGB[c_Px], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pPy, color = cRGB[c_Py], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pPz, color = cRGB[c_Pz], alpha = transp, edgecolors = 'none')
       #-----------------------------------------------------------------------------------
       # Inserting legend's spheres: ======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Px], alpha = 1.0, edgecolors = 'none', label = r'${P}_{x}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Py], alpha = 1.0, edgecolors = 'none', label = r'${P}_{y}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Pz], alpha = 1.0, edgecolors = 'none', label = r'${P}_{z}$')
       #------------------
       file = 'Orbitais_P'
    
    if (l == 3):
       Dxy = orbitais[:,9];   pDxy = ((dpi*Dxy)**2)*peso_total
       Dyz = orbitais[:,10];  pDyz = ((dpi*Dyz)**2)*peso_total
       Dz2 = orbitais[:,11];  pDz2 = ((dpi*Dz2)**2)*peso_total
       Dxz = orbitais[:,12];  pDxz = ((dpi*Dxz)**2)*peso_total
       Dx2 = orbitais[:,13];  pDx2 = ((dpi*Dx2)**2)*peso_total
       #------------------------------------------------------      
       ax.scatter(rx, ry, s = pDxy, color = cRGB[c_Dxy], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pDyz, color = cRGB[c_Dyz], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pDz2, color = cRGB[c_Dz2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pDxz, color = cRGB[c_Dxz], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pDx2, color = cRGB[c_Dx2], alpha = transp, edgecolors = 'none')
       #-------------------------------------------------------------------------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dxy], alpha = 1.0, edgecolors = 'none', label = r'${D}_{xy}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dyz], alpha = 1.0, edgecolors = 'none', label = r'${D}_{yz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dz2], alpha = 1.0, edgecolors = 'none', label = r'${D}_{z^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dxz], alpha = 1.0, edgecolors = 'none', label = r'${D}_{xz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dx2], alpha = 1.0, edgecolors = 'none', label = r'${D}_{x^{2}}$')
       #------------------
       file = 'Orbitais_D'
    
    if (l == 4):
       Fyx2 = orbitais[:,14]; pFyx2 = ((dpi*Fyx2)**2)*peso_total
       Fxyz = orbitais[:,15]; pFxyz = ((dpi*Fxyz)**2)*peso_total
       Fyz2 = orbitais[:,16]; pFyz2 = ((dpi*Fyz2)**2)*peso_total
       Fzz2 = orbitais[:,17]; pFzz2 = ((dpi*Fzz2)**2)*peso_total
       Fxz2 = orbitais[:,18]; pFxz2 = ((dpi*Fxz2)**2)*peso_total
       Fzx2 = orbitais[:,19]; pFzx2 = ((dpi*Fzx2)**2)*peso_total
       Fxx2 = orbitais[:,20]; pFxx2 = ((dpi*Fxx2)**2)*peso_total
       #--------------------------------------------------------      
       ax.scatter(rx, ry, s = pFyx2, color = cRGB[c_Fyx2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFxyz, color = cRGB[c_Fxyz], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFyz2, color = cRGB[c_Fyz2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFzz2, color = cRGB[c_Fzz2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFxz2, color = cRGB[c_Fxz2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFzx2, color = cRGB[c_Fzx2], alpha = transp, edgecolors = 'none')
       ax.scatter(rx, ry, s = pFxx2, color = cRGB[c_Fxx2], alpha = transp, edgecolors = 'none')
       #---------------------------------------------------------------------------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fyx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{yx^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxyz], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xyz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fyz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{yz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fzz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{zz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fzx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{zx^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xx^{2}}$')
       #------------------
       file = 'Orbitais_F'

    # Plot of Bands =======================================================

    x = banda[:,0]

    for i in range (1,(nb+1)):
        if (bands_sn[i] == "sim"):
           y = banda[:,i] + dE_fermi
           plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Highlighting the Fermi energy in the Band structure =================

    plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Highlighting k-points of interest in the Band structure =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [E_min, E_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Labeling k-points of interest in the Band structure =================

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)        
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((E_min, E_max))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    if (esc_fermi == 0):
       plt.ylabel('$E$ (eV)')
    if (esc_fermi == 1):
       plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(title = "")
    ax.legend(loc = "upper right", title = "")
    # ax.legend(loc = "best", title = "")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_svg == 1): plt.savefig(dir_output + file + '.svg', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()
    plt.close()

    if (l == 1):
       if (n_orb == 3 or n_orb == 9):  print ("Plot of the projection of orbitals S|P|D completed --------------------------------")
       if (n_orb == 4 or n_orb == 16): print ("Plot of the projection of orbitals S|P|D|F completed ------------------------------")
    if (l == 2):
       print ("Plot of the projection of orbitals Px|Py|Pz completed -----------------------------")
    if (l == 3):
       print ("Plot of the projection of orbitals Dxy|Dyz|Dz2|Dxz|Dx2 completed ------------------")
    if (l == 4):      
       print ("Plot of the projection of orbitals Fyx2|Fxyz|Fyz2|Fzz2|Fxz2|Fzx2|Fxx2 completed ---")

#=================================================================================================================================
# Obtaining and recording the colors in the RGB pattern that designate the combination of Orbitals for the Plot of Projections ===
#=================================================================================================================================

print ("Analyzing the overlap of Orbitals (Sum of color pattern)")

# Initialization of Matrices to be used:
   
rgb_SPDF = [0]*n_procar*nk*num_bands
rgb_P    = [0]*n_procar*nk*num_bands
rgb_D    = [0]*n_procar*nk*num_bands
rgb_F    = [0]*n_procar*nk*num_bands

#--------------------------------------------------------------------------

number = -1
for Band_n in range (1, (num_bands+1)):
    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):       
            number += 1

            #--------------------------------------------------------------------------------------------------
            # Summing the colors of the orbitals (S,P,D,F): ---------------------------------------------------
            #--------------------------------------------------------------------------------------------------

            color_dat = [0]*3
           
            for i in range(3):
                color_dat[i]  = S[number]*cRGB[c_S][i] + P[number]*cRGB[c_P][i] + D[number]*cRGB[c_D][i] + F[number]*cRGB[c_F][i]
                #-------------------------------------------
                if (color_dat[i]  > 1.0): color_dat[i] = 1.0
                #-------------------------------------------
            rgb_SPDF[number] = (color_dat[0], color_dat[1], color_dat[2])    

            #---------------------------------------------------------------------------------------------------
            # Summing the colors of the orbitals (Px,Py,Pz): ---------------------------------------------------
            #---------------------------------------------------------------------------------------------------

            color_dat = [0]*3

            if (P[number] != 0 and n_orb >= 9):
               Px[number]  =  Px[number]/P[number]
               Py[number]  =  Py[number]/P[number]
               Pz[number]  =  Pz[number]/P[number]              
           
            if (n_orb >= 9):
               for i in range(3):
                   color_dat[i] = Px[number]*cRGB[c_Px][i] + Py[number]*cRGB[c_Py][i] + Pz[number]*cRGB[c_Pz][i]
                   #------------------------------------------
                   if (color_dat[i] > 1.0): color_dat[i] = 1.0
                   #------------------------------------------
               rgb_P[number] = (color_dat[0], color_dat[1], color_dat[2])
            
            #---------------------------------------------------------------------------------------------------
            # Summing the colors of the orbitals (Dxy,Dyz,Dz2,Dxz,Dx2): ----------------------------------------
            #---------------------------------------------------------------------------------------------------

            color_dat = [0]*3

            if (D[number] != 0 and n_orb >= 9):
               Dxy[number]  =  Dxy[number]/D[number]
               Dyz[number]  =  Dyz[number]/D[number]
               Dz2[number]  =  Dz2[number]/D[number]
               Dxz[number]  =  Dxz[number]/D[number]
               Dx2[number]  =  Dx2[number]/D[number]           
           
            if (n_orb >= 9):
               for i in range(3):
                   color_dat[i] = Dxy[number]*cRGB[c_Dxy][i] + Dyz[number]*cRGB[c_Dyz][i] + Dz2[number]*cRGB[c_Dz2][i]
                   color_dat[i] = color_dat[i] + Dxz[number]*cRGB[c_Dxz][i] + Dx2[number]*cRGB[c_Dx2][i]
                   #------------------------------------------
                   if (color_dat[i] > 1.0): color_dat[i] = 1.0
                   #------------------------------------------
               rgb_D[number] = (color_dat[0], color_dat[1], color_dat[2])
            
            #---------------------------------------------------------------------------------------------------
            # Summing the colors of the orbitals (Fyx2,Fxyz,Fyz2,Fzz2,Fxz2,Fzx2,Fxx2): -------------------------
            #---------------------------------------------------------------------------------------------------

            color_dat = [0]*3

            if (F[number] != 0 and n_orb == 16):
               Fyx2[number]  =  Fyx2[number]/F[number]
               Fxyz[number]  =  Fxyz[number]/F[number]
               Fyz2[number]  =  Fyz2[number]/F[number]
               Fzz2[number]  =  Fzz2[number]/F[number]
               Fxz2[number]  =  Fxz2[number]/F[number]           
               Fzx2[number]  =  Fzx2[number]/F[number]
               Fxx2[number]  =  Fxx2[number]/F[number]
           
            if (n_orb == 16):
               for i in range(3):
                   color_dat[i] = Fyx2[number]*cRGB[c_Fyx2][i] + Fxyz[number]*cRGB[c_Fxyz][i] + Fyz2[number]*cRGB[c_Fyz2][i]
                   color_dat[i] = color_dat[i] + Fzz2[number]*cRGB[c_Fzz2][i] + Fxz2[number]*cRGB[c_Fxz2][i]
                   color_dat[i] = color_dat[i] + Fzx2[number]*cRGB[c_Fzx2][i] + Fxx2[number]*cRGB[c_Fxx2][i]
                   #------------------------------------------
                   if (color_dat[i] > 1.0): color_dat[i] = 1.0
                   #------------------------------------------
               rgb_F[number] = (color_dat[0], color_dat[1], color_dat[2])



#========================================================================================
# Plot with the Projections of the Orbitals merged via the sum of the color pattern: ====
#========================================================================================
    
for l in range (1,(loop+1)):     # Loop for analysis of projections

    fig, ax = plt.subplots()

    # Plot of Projections =================================================   

    if (l == 1):
       peso = pOrb_tot
       if (n_orb == 3 or n_orb == 9): file = 'Orbitais_SPD'
       if (n_orb == 4 or n_orb == 16): file = 'Orbitais_SPDF'
       #----------------------
       ax.scatter(rx, ry, s = peso, c = rgb_SPDF, alpha = transp, edgecolors = 'none')            
       #----------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_S], alpha = 1.0, edgecolors = 'none', label = 'S')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_P], alpha = 1.0, edgecolors = 'none', label = 'P') 
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_D], alpha = 1.0, edgecolors = 'none', label = 'D')
       if (n_orb == 4 or n_orb == 16): 
          ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_F], alpha = 1.0, edgecolors = 'none', label = 'F')  
       #----------------------
       
    if (l == 2):
       peso = pP
       file = 'Orbitais_P'
       #------------------
       ax.scatter(rx, ry, s = peso, c = rgb_P, alpha = transp, edgecolors = 'none')
       #------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Px], alpha = 1.0, edgecolors = 'none', label = r'${P}_{x}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Py], alpha = 1.0, edgecolors = 'none', label = r'${P}_{y}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Pz], alpha = 1.0, edgecolors = 'none', label = r'${P}_{z}$')
       #------------------
       
    if (l == 3):
       peso = pD
       file = 'Orbitais_D'
       #------------------
       ax.scatter(rx, ry, s = peso, c = rgb_D, alpha = transp, edgecolors = 'none')      
       #------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dxy], alpha = 1.0, edgecolors = 'none', label = r'${D}_{xy}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dyz], alpha = 1.0, edgecolors = 'none', label = r'${D}_{yz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dz2], alpha = 1.0, edgecolors = 'none', label = r'${D}_{z^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dxz], alpha = 1.0, edgecolors = 'none', label = r'${D}_{xz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Dx2], alpha = 1.0, edgecolors = 'none', label = r'${D}_{x^{2}}$')
       #------------------
       
    if (l == 4):
       peso = pF
       file = 'Orbitais_F'
       #------------------
       ax.scatter(rx, ry, s = peso, c = rgb_F, alpha = transp, edgecolors = 'none')      
       #------------------
       # Inserting legend's spheres: =======================================================
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fyx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{yx^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxyz], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xyz}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fyz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{yz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fzz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{zz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxz2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xz^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fzx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{zx^{2}}$')
       ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Fxx2], alpha = 1.0, edgecolors = 'none', label = r'${F}_{xx^{2}}$')
       #------------------

    # Plot of Bands =======================================================

    for i in range (1,(nb+1)):
        if (bands_sn[i] == "sim"):
           y = banda[:,i] + dE_fermi
           plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Highlighting the Fermi energy in the Band structure =================

    plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Highlighting k-points of interest in the Band structure =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [E_min, E_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Labeling k-points of interest in the Band structure =================

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)        
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((E_min, E_max))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    if (esc_fermi == 0):
       plt.ylabel('$E$ (eV)')
    if (esc_fermi == 1):
       plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(loc = "upper right", title = "")
    # ax.legend(loc = "best", title = "")

    if (save_png == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.pdf', dpi = 600)
    if (save_svg == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.svg', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.eps', dpi = 600)

    # plt.show()
    plt.close()
    
#===========================================================================

print(" ")
print ("Plot of projections via Matplotlib completed ---------------------")

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------

# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license