
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print ("========= Plotting the Dielectric Function (Matplotlib) =========")

print(" ")
print(".........................")
print("..... Wait a moment .....")
print(".........................")  

#------------------------------------------------------------------------
# Test to know which directories must be correctly informed -------------
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/BSE/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#======================================================================   

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#==========================================================================

func_dielet = np.loadtxt(dir_output + 'BSE.dat') 
func_dielet.shape

energ = func_dielet[:,0] + dE_fermi

if (esc_energ == 0):
   x_inicial = min(energ)
   x_final   = max(energ)
   
#----------------------------------------------------------

for i in range(2):

    y_inicial = +1000.0
    y_final   = -1000.0

    #-------------------------
    if (i == 0): name = 'IMAG'
    if (i == 1): name = 'REAL'
    #-------------------------   

    #==================================================

    fig, ax = plt.subplots()

    for j in range(5):
        if (i == 0): m = (j +1)         
        if (i == 1): m = (j +6) 
        temp_min = min(func_dielet[:,m])
        temp_max = max(func_dielet[:,m])
        if (temp_min < y_inicial): y_inicial = temp_min
        if (temp_max > y_final):   y_final   = temp_max

        #----------------------------------------------
        if (i == 0): func_d = func_dielet[:,(j+1)]
        if (i == 1): func_d = func_dielet[:,(j+6)]
        #----------------------------------------------

        if (j == 0): plt.plot(energ, func_d, color = 'black', linestyle = '-', linewidth = 1.0, label = 'Mod')
        if (j == 1): plt.plot(energ, func_d, color = 'magenta', linestyle = '-', linewidth = 1.0, label = 'Med')
        if (j == 2): plt.plot(energ, func_d, color = 'blue', linestyle = '-', linewidth = 1.0, label = 'X')
        if (j == 3): plt.plot(energ, func_d, color = 'red', linestyle = '-', linewidth = 1.0, label = 'Y')
        if (j == 4): plt.plot(energ, func_d, color = 'limegreen', linestyle = '-', linewidth = 1.0, label = 'Z')

    # Highlighting the Fermi energy in the Band structure =================
    plt.plot([dest_fermi, dest_fermi], [y_inicial, y_final], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)        

    # Highlighting the null value of the Dielectric Function ==============
    plt.plot([x_inicial, x_final], [0.0, 0.0], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)   
  
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    if (esc_fermi == 0): plt.xlabel('$E$ (eV)')
    if (esc_fermi == 1): plt.xlabel('$E-E_{f}$ (eV)')
    
    plt.ylabel('Dielectric Function (BSE)')

    ax.legend(title = "")
    ax.set_box_aspect(1.25/1)   

    if (save_png == 1): plt.savefig(dir_output + name + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + name + '.pdf', dpi = 600)
    if (save_svg == 1): plt.savefig(dir_output + name + '.svg', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + name + '.eps', dpi = 600)

    # plt.show()  

#---------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("========================== Concluded! ==========================")
#---------------------------------------------------------------------------

# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license