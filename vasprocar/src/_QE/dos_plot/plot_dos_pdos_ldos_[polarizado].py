# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("==================== Plotando a DOS: ====================")

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(" ")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/DOS/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
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

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

transp = 0.25
linew = 0.5

energia = dos_up[:,0] + dE_fermi

for esc_dos in range(2):

    for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

        fig, ax = plt.subplots() 

        # Plot das Projeções ===================================================

        if (l == 1):
           print ("=================================") 
           print ("Analisando a DOS e pDOS (S, P, D)") 
           #-----------------------------------------------------
           if (esc_dos == 0):
              c_label = ''
              c_file  = '' 
              dos_u_tot = dos_up[:,1];  dos_d_tot = dos_down[:,1]
              l_u_dos   = dos_up[:,2];  l_d_dos   = dos_down[:,2]
              dos_u_S   = dos_up[:,3];  dos_d_S   = dos_down[:,3]
              dos_u_P   = dos_up[:,4];  dos_d_P   = dos_down[:,4]
              dos_u_D   = dos_up[:,5];  dos_d_D   = dos_down[:,5]
              x_final   = max(dos_u_tot)
              x_inicial = min(dos_d_tot)
           #-----------------------------------------------------
           if (esc_dos == 1):
              c_label = r'${\Delta}$'
              c_file  = '_[Delta]' 
              dos_u_tot = dos_up[:,1] + dos_down[:,1]
              l_u_dos   = dos_up[:,2] + dos_down[:,2]
              dos_u_S   = dos_up[:,3] + dos_down[:,3]
              dos_u_P   = dos_up[:,4] + dos_down[:,4]
              dos_u_D   = dos_up[:,5] + dos_down[:,5]
              x_final   = max(dos_u_tot)
              x_inicial = min(dos_u_tot)
           #-----------------------------------------------------
           ax.plot(dos_u_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = c_label + 'DOS')
           ax.fill(dos_u_tot, energia, color = 'gray', alpha = transp)
           if (esc == 1):
              ax.plot(l_u_dos, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = c_label + 'l-DOS')
              ax.fill(l_u_dos, energia, color = 'magenta', alpha = transp)          
           ax.plot(dos_u_S, energia, color = 'blue', linestyle = '-', linewidth = linew, label = c_label + 'S')
           ax.fill(dos_u_S, energia, color = 'blue', alpha = transp)
           ax.plot(dos_u_P, energia, color  = 'red', linestyle = '-', linewidth = linew, label = c_label + 'P')
           ax.fill(dos_u_P, energia, color  = 'red', alpha = transp)
           ax.plot(dos_u_D, energia, color  = 'limegreen', linestyle = '-', linewidth = linew, label = c_label + 'D')
           ax.fill(dos_u_D, energia, color  = 'limegreen', alpha = transp)
           #=============================================================================================================
           if (esc_dos == 0):
              ax.plot(dos_d_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_tot, energia, color = 'gray', alpha = transp)
              if (esc == 1):
                 ax.plot(l_d_dos, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = '')
                 ax.fill(l_d_dos, energia, color = 'magenta', alpha = transp)          
              ax.plot(dos_d_S, energia, color = 'blue', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_S, energia, color = 'blue', alpha = transp)
              ax.plot(dos_d_P, energia, color  = 'red', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_P, energia, color  = 'red', alpha = transp)
              ax.plot(dos_d_D, energia, color  = 'limegreen', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_D, energia, color  = 'limegreen', alpha = transp)      
           #---------------------------------------------
           if (esc == 0): file = 'DOS_pDOS' + c_file
           if (esc == 1): file = 'DOS_pDOS_lDOS' + c_file
       
        if (l == 2):
           print ("Analisando a pDOS (Px, Py, Pz)")
           #---------------------------------------------------
           if (esc_dos == 0):
              dos_u_Px = dos_up[:,6];  dos_d_Px = dos_down[:,6]
              dos_u_Py = dos_up[:,7];  dos_d_Py = dos_down[:,7]
              dos_u_Pz = dos_up[:,8];  dos_d_Pz = dos_down[:,8]
              x_final   = max(dos_u_tot)
              x_inicial = min(dos_d_tot)         
           #---------------------------------------------------
           if (esc_dos == 1):
              dos_u_Px = dos_up[:,6] + dos_down[:,6]
              dos_u_Py = dos_up[:,7] + dos_down[:,7]
              dos_u_Pz = dos_up[:,8] + dos_down[:,8]
              x_final   = max(dos_u_P)
              x_inicial = min(dos_u_P)  
           #---------------------------------------------------
           ax.plot(dos_u_P, energia, color  = 'gray', linestyle = '-', linewidth = linew, label = c_label + 'P')
           ax.fill(dos_u_P, energia, color  = 'gray', alpha = transp)
           ax.plot(dos_u_Px, energia, color = 'blue', linestyle = '-', linewidth = linew, label = c_label + 'P$_{x}$')
           ax.fill(dos_u_Px, energia, color = 'blue', alpha = transp)
           ax.plot(dos_u_Py, energia, color = 'red', linestyle = '-', linewidth = linew, label = c_label + 'P$_{y}$')
           ax.fill(dos_u_Py, energia, color = 'red', alpha = transp)
           ax.plot(dos_u_Pz, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = c_label + 'P$_{z}$')
           ax.fill(dos_u_Pz, energia, color = 'limegreen', alpha = transp)
           #===============================================================================================================
           if (esc_dos == 0):
              ax.plot(dos_d_P, energia, color  = 'gray', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_P, energia, color  = 'gray', alpha = transp)
              ax.plot(dos_d_Px, energia, color = 'blue', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Px, energia, color = 'blue', alpha = transp)
              ax.plot(dos_d_Py, energia, color = 'red', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Py, energia, color = 'red', alpha = transp)
              ax.plot(dos_d_Pz, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Pz, energia, color = 'limegreen', alpha = transp)
           #-------------------------------------------
           if (esc == 0): file = 'pDOS_P' + c_file
           if (esc == 1): file = 'pDOS_lDOS_P' + c_file


        if (l == 3):
           print ("Analisando a pDOS (Dxy, Dyz, Dz2, Dxz, Dx2)") 
           #-------------------------------------------------------
           if (esc_dos == 0):
              dos_u_Dxy = dos_up[:,9];   dos_d_Dxy = dos_down[:,9]
              dos_u_Dyz = dos_up[:,10];  dos_d_Dyz = dos_down[:,10]
              dos_u_Dz2 = dos_up[:,11];  dos_d_Dz2 = dos_down[:,11]
              dos_u_Dxz = dos_up[:,12];  dos_d_Dxz = dos_down[:,12]
              dos_u_Dx2 = dos_up[:,13];  dos_d_Dx2 = dos_down[:,13]        
              x_final   = max(dos_u_tot)
              x_inicial = min(dos_d_tot)
           #-------------------------------------------------------
           if (esc_dos == 1):
              dos_u_Dxy = dos_up[:,9]  + dos_down[:,9]
              dos_u_Dyz = dos_up[:,10] + dos_down[:,10]
              dos_u_Dz2 = dos_up[:,11] + dos_down[:,11]
              dos_u_Dxz = dos_up[:,12] + dos_down[:,12]
              dos_u_Dx2 = dos_up[:,13] + dos_down[:,13]
              x_final   = max(dos_u_D)
              x_inicial = min(dos_u_D)
           #-------------------------------------------------------
           ax.plot(dos_u_D, energia, color   = 'gray', linestyle = '-', linewidth = linew, label = c_label + 'D')
           ax.fill(dos_u_D, energia, color   = 'gray', alpha = transp)
           ax.plot(dos_u_Dxy, energia, color = 'blue', linestyle = '-', linewidth = linew, label = c_label + 'D$_{xy}$')
           ax.fill(dos_u_Dxy, energia, color = 'blue', alpha = transp)
           ax.plot(dos_u_Dyz, energia, color = 'red', linestyle = '-', linewidth = linew, label = c_label + 'D$_{yz}$')
           ax.fill(dos_u_Dyz, energia, color = 'red', alpha = transp)
           ax.plot(dos_u_Dz2, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = c_label + 'D$_{z^{2}}$')
           ax.fill(dos_u_Dz2, energia, color = 'limegreen', alpha = transp)
           ax.plot(dos_u_Dxz, energia, color = 'rosybrown', linestyle = '-', linewidth = linew, label = c_label + 'D$_{xz}$')
           ax.fill(dos_u_Dxz, energia, color = 'rosybrown', alpha = transp)
           ax.plot(dos_u_Dx2, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = c_label + 'D$_{x^{2}}$')
           ax.fill(dos_u_Dx2, energia, color = 'magenta', alpha = transp)
           #====================================================================================================================
           if (esc_dos == 0):
              ax.plot(dos_d_D, energia, color   = 'gray', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_D, energia, color   = 'gray', alpha = transp)
              ax.plot(dos_d_Dxy, energia, color = 'blue', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Dxy, energia, color = 'blue', alpha = transp)
              ax.plot(dos_d_Dyz, energia, color = 'red', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Dyz, energia, color = 'red', alpha = transp)
              ax.plot(dos_d_Dz2, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Dz2, energia, color = 'limegreen', alpha = transp)
              ax.plot(dos_d_Dxz, energia, color = 'rosybrown', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Dxz, energia, color = 'rosybrown', alpha = transp)
              ax.plot(dos_d_Dx2, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = '')
              ax.fill(dos_d_Dx2, energia, color = 'magenta', alpha = transp)
           #-------------------------------------------
           if (esc == 0): file = 'pDOS_D' + c_file
           if (esc == 1): file = 'pDOS_lDOS_D' + c_file

        # Destacando a energia de Fermi na estrutura de Bandas ==============================================================

        plt.plot([-100.0, +100.0], [dest_fermi, dest_fermi], color = 'gray', linestyle = '--', linewidth = 0.75, alpha = 0.5)

        #====================================================================================================================

        plt.xlim((x_inicial, x_final))
        plt.ylim((energ_min + dE_fermi , energ_max + dE_fermi))

        if (esc_dos == 0):
           plt.xlabel("Density of States")
        if (esc_dos == 1):
           plt.xlabel("Density of States [Delta]")
           
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
        if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

        # plt.show()
    
#======================================================================

if (dir_output != ''):
   print(" ")
   print("================================================================")
   print("= Edite o Plot da DOS por meio dos arquivos DOS_pDOS_lDOS.py ou ")
   print("= .agr (via Grace) gerados na pasta output/DOS =================")   
   print("================================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
