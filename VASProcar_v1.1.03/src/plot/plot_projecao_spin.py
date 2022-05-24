
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================= Plotando as Projecoes =================")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Spin/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

spin = np.loadtxt(dir_output + 'Spin.dat') 
spin.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#----------------------------------------------------------------------

if (esc_fermi == 0):
   dE_fermi = 0.0; dest_fermi = Efermi
if (esc_fermi == 1):
   dE_fermi = (Efermi)*(-1); dest_fermi = 0.0

#----------------------------------------------------------------------

rx = spin[:,0]
ry = spin[:,1] + dE_fermi 

for l in range (1,(3+1)):

    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================
    
    if (l == 1):
       Si_u = spin[:,2]
       Si_d = spin[:,3]
       palavra = r'$S_{x}$'; file = 'Spin_Sx'
    if (l == 2):
       Si_u = spin[:,4]
       Si_d = spin[:,5]
       palavra = r'$S_{y}$'; file = 'Spin_Sy'
    if (l == 3):
       Si_u = spin[:,6]
       Si_d = spin[:,7]
       palavra = r'$S_{z}$'; file = 'Spin_Sz'

    ax.scatter(rx, ry, s = Si_u, c = 'red',  alpha = transp, edgecolors = 'none')
    ax.scatter(rx, ry, s = Si_d, c = 'blue', alpha = transp, edgecolors = 'none')   

   # Gambiarra: A fim de gerar uma legenda cuja esfera colorida possua um tamanho fixo (antes ela adotada o menor ou maior tamanho de esfera do plot)
   #            e sem a transparência do plot, tive que plotar pontos isolados afastados da região do gráfico.
    ax.scatter([-1000.0], [-1000.0], s = [40.0], c = 'red',  alpha = 1.0, edgecolors = 'none', label = palavra + r'$\uparrow$')
    ax.scatter([-1000.0], [-1000.0], s = [40.0], c = 'blue', alpha = 1.0, edgecolors = 'none', label = palavra + r'$\downarrow$')
    
    # Plot das Bandas =====================================================

    x = banda[:,0]

    for i in range (1,(nb+1)):
        y = banda[:,i] + dE_fermi 
        plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [energ_min + dE_fermi, energ_max + dE_fermi], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Rotulando pontos-k de interesse na estrutura de Bandas ==============

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)   
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((energ_min + dE_fermi, energ_max + dE_fermi))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    if (esc_fermi == 0):
       plt.ylabel('$E$ (eV)')
    if (esc_fermi == 1):
       plt.ylabel('$E-E_{f}$ (eV)')    

    ax.set_box_aspect(1.25/1)
    ax.legend(title="")
    ax.legend(loc="upper right", title="")
    # ax.legend(loc="best", title="")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()
    plt.close()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
   print("= gerados na pasta output/Localizacao ======================")   
   print("= arquivos .agr (via Grace) ou Spin.py =====================")
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
