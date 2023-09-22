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

dos = np.loadtxt(dir_output + 'DOS_pDOS_lDOS.dat') 
dos.shape

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

energia = dos[:,0] + dE_fermi 

for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots() 

    # Plot das Projeções ===================================================

    if (l == 1):
       #-----------------
       print ("=================================") 
       print ("Analisando a DOS e pDOS (S, P, D)") 
       #-----------------
       dos_tot = dos[:,1]
       l_dos   = dos[:,2]
       dos_S   = dos[:,3]
       dos_P   = dos[:,4]
       dos_D   = dos[:,5]
       #-------------------------------
       ax.plot(dos_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = 'DOS')
       ax.fill(dos_tot, energia, color = 'gray', alpha = transp)
       if (esc == 1):
          ax.plot(l_dos, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = 'l-DOS')
          ax.fill(l_dos, energia, color = 'magenta', alpha = transp)          
       ax.plot(dos_S, energia, color = 'blue', linestyle = '-', linewidth = linew, label = 'S')
       ax.fill(dos_S, energia, color = 'blue', alpha = transp)
       ax.plot(dos_P, energia, color  = 'red', linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(dos_P, energia, color  = 'red', alpha = transp)
       ax.plot(dos_D, energia, color  = 'limegreen', linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(dos_D, energia, color  = 'limegreen', alpha = transp)
       #-------------------------------
       if (esc == 0): file = 'DOS_pDOS'
       if (esc == 1): file = 'DOS_pDOS_lDOS'
       
    if (l == 2):
       #----------------
       print ("Analisando a pDOS (Px, Py, Pz)")        
       #----------------
       dos_Px = dos[:,6]
       dos_Py = dos[:,7]
       dos_Pz = dos[:,8]
       #-----------------------------
       ax.plot(dos_P, energia, color  = 'gray', linestyle = '-', linewidth = linew, label = 'P')
       ax.fill(dos_P, energia, color  = 'gray', alpha = transp)
       ax.plot(dos_Px, energia, color = 'blue', linestyle = '-', linewidth = linew, label = 'P$_{x}$')
       ax.fill(dos_Px, energia, color = 'blue', alpha = transp)
       ax.plot(dos_Py, energia, color = 'red', linestyle = '-', linewidth = linew, label = 'P$_{y}$')
       ax.fill(dos_Py, energia, color = 'red', alpha = transp)
       ax.plot(dos_Pz, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = 'P$_{z}$')
       ax.fill(dos_Pz, energia, color = 'limegreen', alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_P'
       if (esc == 1): file = 'pDOS_lDOS_P'


    if (l == 3):
       #------------------
       print ("Analisando a pDOS (Dxy, Dyz, Dz2, Dxz, Dx2)")          
       #------------------
       dos_Dxy = dos[:,9]
       dos_Dyz = dos[:,10]
       dos_Dz2 = dos[:,11]
       dos_Dxz = dos[:,12]
       dos_Dx2 = dos[:,13]        
       #-----------------------------
       ax.plot(dos_D, energia, color   = 'gray', linestyle = '-', linewidth = linew, label = 'D')
       ax.fill(dos_D, energia, color   = 'gray', alpha = transp)
       ax.plot(dos_Dxy, energia, color = 'blue', linestyle = '-', linewidth = linew, label = 'D$_{xy}$')
       ax.fill(dos_Dxy, energia, color = 'blue', alpha = transp)
       ax.plot(dos_Dyz, energia, color = 'red', linestyle = '-', linewidth = linew, label = 'D$_{yz}$')
       ax.fill(dos_Dyz, energia, color = 'red', alpha = transp)
       ax.plot(dos_Dz2, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = 'D$_{z^{2}}$')
       ax.fill(dos_Dz2, energia, color = 'limegreen', alpha = transp)
       ax.plot(dos_Dxz, energia, color = 'rosybrown', linestyle = '-', linewidth = linew, label = 'D$_{xz}$')
       ax.fill(dos_Dxz, energia, color = 'rosybrown', alpha = transp)
       ax.plot(dos_Dx2, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = 'D$_{x^{2}}$')
       ax.fill(dos_Dx2, energia, color = 'magenta', alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_D'
       if (esc == 1): file = 'pDOS_lDOS_D'

    # Destacando a energia de Fermi na estrutura de Bandas ================

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
