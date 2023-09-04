
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print ("========== Plotting the Wave Function (Matplotlib) ==========")

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
   dir_output = dir_files + '/output/Wave_Function/'
else:
   dir_files = ''
   dir_output = ''
#-----------------
   
#======================================================================
#======================================================================
# File Structure for Plot via Matplotlib ==============================
#======================================================================
#======================================================================   

for l in range(1,(3+1)):

    fig, ax = plt.subplots()

    #=====================================================================

    if (l == 1):
       print ("Analyzing the X-direction ===============================")       
       #----------------------------------------------------
       wave = np.loadtxt(dir_output + 'Wave_Function_X.dat') 
       wave.shape
       #-------------
       X  = wave[:,0]
       Vx = wave[:,1]
       #-------------

    if (l == 2):
       print ("Analyzing the Y-direction ===============================") 
       #----------------------------------------------------
       wave = np.loadtxt(dir_output + 'Wave_Function_Y.dat') 
       wave.shape
       #-------------
       Y  = wave[:,0]
       Vy = wave[:,1]
       #-------------

    if (l == 3):
       print ("Analyzing the Z-direction ===============================") 
       #----------------------------------------------------
       wave = np.loadtxt(dir_output + 'Wave_Function_Z.dat') 
       wave.shape
       #-------------
       Z  = wave[:,0]
       Vz = wave[:,1]
       #-------------

    # Plot of the average value of the Wave Function in a given direction:

    if (l == 1):
        plt.plot(X, Vx, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Wave_Function_x'; eixo = 'X '; coord = ion_x
        dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
        dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)  
        
    if (l == 2):
        plt.plot(Y, Vy, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Wave_Function_y'; eixo = 'Y '; coord = ion_y
        dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
        dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
        
    if (l == 3):
        plt.plot(Z, Vz, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Wave_Function_z'; eixo = 'Z '; coord = ion_z
        dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
        dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    # Highlighting the lattice ions coordinates:

    if (destaque == 1):
       for i in range(ni):
           plt.plot([coord[i], coord[i]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 0.5)

    #======================================================================

    if (Dimensao == 1):
       label = eixo + '($\AA$)'

    if (Dimensao == 2):
       label = eixo + '(nm)'        
    
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    plt.xlabel(label)
    plt.ylabel('Wave Function')

    # ax.set_box_aspect(1.25/1)  

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