
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
   dir_output = dir_files + '/output/Psi/'
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

psi = np.loadtxt(dir_output + 'Psi.dat') 
psi.shape
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

#===========================================================================
# Analysis of projections of Psi States individually: ======================
#===========================================================================

fig, ax = plt.subplots()

# Plot of Projections ======================================================

dpi = 2*3.1415926535897932384626433832795  

rx = psi[:,0]
ry = psi[:,1] + dE_fermi 
Psi1 = psi[:,2]; pPsi1 = ((dpi*Psi1)**2)*peso_total
Psi2 = psi[:,3]; pPsi2 = ((dpi*Psi2)**2)*peso_total
Psi3 = psi[:,4]; pPsi3 = ((dpi*Psi3)**2)*peso_total
Psi4 = psi[:,5]; pPsi4 = ((dpi*Psi4)**2)*peso_total
Psi5 = psi[:,6]; pPsi5 = ((dpi*Psi5)**2)*peso_total
Psi6 = psi[:,7]; pPsi6 = ((dpi*Psi6)**2)*peso_total
Psitot = Psi1 + Psi2 + Psi3 + Psi4 + Psi5 + Psi6; pPsitot = ((dpi*Psitot)**2)*peso_total

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
# Plot of projections of Psi States individually: ==========================
#===========================================================================

for i in range(1,(n_psi+1)):
    if (i == 1):
       print (f'Analyzing the Projection of the Psi_State_1 {(label_psi[0])}')
       ax.scatter(rx, ry, s = pPsi1, color = cRGB[c_Psi1], alpha = transp, edgecolors = 'none')
       
    if (i == 2):
       print (f'Analyzing the Projection of the Psi_State_2 {(label_psi[1])}')
       ax.scatter(rx, ry, s = pPsi2, color = cRGB[c_Psi2], alpha = transp, edgecolors = 'none')
       
    if (i == 3):
       print (f'Analyzing the Projection of the Psi_State_3 {(label_psi[2])}')
       ax.scatter(rx, ry, s = pPsi3, color = cRGB[c_Psi3], alpha = transp, edgecolors = 'none')
       
    if (i == 4):
       print (f'Analyzing the Projection of the Psi_State_4 {(label_psi[3])}')
       ax.scatter(rx, ry, s = pPsi4, color = cRGB[c_Psi4], alpha = transp, edgecolors = 'none')
       
    if (i == 5):
       print (f'Analyzing the Projection of the Psi_State_5 {(label_psi[4])}')
       ax.scatter(rx, ry, s = pPsi5, color = cRGB[c_Psi5], alpha = transp, edgecolors = 'none')

    if (i == 6):
       print (f'Analyzing the Projection of the Psi_State_6 {(label_psi[5])}')
       ax.scatter(rx, ry, s = pPsi6, color = cRGB[c_Psi6], alpha = transp, edgecolors = 'none')

# Inserting legend's spheres: =========================================
for i in range(1,(n_psi+1)):
    if (i == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi1], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 2): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi2], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 3): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi3], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 4): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi4], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 5): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi5], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 6): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi6], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    
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

if (save_png == 1): plt.savefig(dir_output + 'Estados_Psi.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Estados_Psi.pdf', dpi = 600)
if (save_svg == 1): plt.savefig(dir_output + 'Estados_Psi.svg', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Estados_Psi.eps', dpi = 600)

# plt.show()
plt.close()

#===================================================================================================================================
# Obtaining and recording the colors in the RGB pattern that designate the combination of Psi_states for the Plot of Projections ===
#===================================================================================================================================

print (" ")
print ("Analyzing Psi_State Overlay (Color Pattern Sum)")

rgb_psi = [0]*n_procar*nk*num_bands

number = -1 
for Band_n in range (1, (num_bands+1)):
    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):       
            number += 1

            #-------------------------------------------------------------------------------------------------
            # Summing the colors of the Psi_States 1|2|3|4|5|6: ----------------------------------------------
            #-------------------------------------------------------------------------------------------------            

            color_dat = [0]*3
            
            for i in range(3):
                color_dat[i] += Psi1[number]*cRGB[c_Psi1][i] + Psi2[number]*cRGB[c_Psi2][i] + Psi3[number]*cRGB[c_Psi3][i] + Psi4[number]*cRGB[c_Psi4][i]
                color_dat[i] += Psi5[number]*cRGB[c_Psi5][i] + Psi6[number]*cRGB[c_Psi6][i]
                #-------------------------------------------
                if (color_dat[i]  > 1.0): color_dat[i] = 1.0
                #-------------------------------------------
            rgb_psi[number] = (color_dat[0], color_dat[1], color_dat[2]) 

#==========================================================================================
# Plot with the Projections of the Psi_States merged via the sum of the color pattern: ====
#==========================================================================================
  
fig, ax = plt.subplots()

# Plot of Projections =================================================

peso = pPsitot

ax.scatter(rx, ry, s = peso, c = rgb_psi, alpha = transp, edgecolors = 'none')

# Inserting legend's spheres: =========================================
for i in range(1,(n_psi+1)):
    if (i == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi1], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 2): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi2], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 3): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi3], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 4): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi4], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 5): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi5], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    if (i == 6): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Psi6], alpha = 1.0, edgecolors = 'none', label = label_psi[i-1])
    
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

if (save_png == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].pdf', dpi = 600)
if (save_svg == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].svg', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].eps', dpi = 600)

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