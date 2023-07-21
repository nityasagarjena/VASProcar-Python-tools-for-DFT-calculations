
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print ("=============== Plotting the bands (Matplotlib) ===============")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Bandas/'
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
        bands_sn[j] = "sim"  

#----------------------------------------------------------------------

fig, ax = plt.subplots()

# Plot of Bands =======================================================

n_s1 = 0
n_s2 = 0

x = banda[:,0]

if (ispin == 1):

   for i in range (1,(nb+1)):
       if (bands_sn[i] == "sim"):
          y = banda[:,i] + dE_fermi
          plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25)

if (ispin == 2):

   for i in range (1,(int(nb/2)+1)):
       if (bands_sn[i] == "sim"):
          y = banda[:,i] + dE_fermi
          #------------------------
          n_s1 += 1
          if (n_s1 == 1): plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 0.25, label = 'Spin '+ r'$\uparrow$')
          if (n_s1 != 1): plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 0.25)
          #------------------------      

   for i in range ((int(nb/2)+1),(nb+1)):
       if (bands_sn[i] == "sim"):
          y = banda[:,i] + dE_fermi
          #------------------------
          n_s2 += 1
          if (n_s2 == 1): plt.plot(x, y, color = 'blue', linestyle = '-', linewidth = 0.25, label = 'Spin ' + r'$\downarrow$')
          if (n_s2 != 1): plt.plot(x, y, color = 'blue', linestyle = '-', linewidth = 0.25)
          #------------------------
       
# Highlighting the Fermi energy in the Band structure =================

if (ispin == 1):
   plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

if (ispin == 2):
   plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

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

if (ispin == 2):
   ax.legend(title = "")
   ax.legend(loc = "upper right", title = "")
   # ax.legend(loc = "best", title = "")
    
if (save_png == 1): plt.savefig(dir_output + 'Bandas.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Bandas.pdf', dpi = 600)
if (save_svg == 1): plt.savefig(dir_output + 'Bandas.svg', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Bandas.eps', dpi = 600)

# plt.show()

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------

# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license
 