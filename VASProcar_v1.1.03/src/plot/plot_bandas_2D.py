
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================== Plotando as Bandas: ==================")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
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
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================   

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

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

fig, ax = plt.subplots()

# Plot das Bandas =====================================================

x = banda[:,0]

if (ispin == 1):
   for i in range (1,(nb+1)):
       y = banda[:,i] + dE_fermi
       plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25)

if (ispin == 2):
   #--------------------------------
   label = ''
   for i in range (1,(int(nb/2)+1)):
       if (i == int(nb/2)): label = 'Spin 1'
       y = banda[:,i] + dE_fermi      
       plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 0.25, label = label)
   #-------------------------------------
   label = ''
   for i in range ((int(nb/2)+1),(nb+1)):
       y = banda[:,i] + dE_fermi
       if (i == nb): label = 'Spin 2'
       plt.plot(x, y, color = 'blue', linestyle = '-', linewidth = 0.25, label = label)
       
# Destacando a energia de Fermi na estrutura de Bandas ================

if (ispin == 1):
   plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

if (ispin == 2):
   plt.plot([x[0], x[(n_procar*nk)-1]], [dest_fermi, dest_fermi], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

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

if (ispin == 2):
   ax.legend(title = "")
   ax.legend(loc = "upper right", title = "")
   # ax.legend(loc = "best", title = "")
    
if (save_png == 1): plt.savefig(dir_output + 'Bandas.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Bandas.pdf', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Bandas.eps', dpi = 600)

# plt.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("=========================================================")
   print("= Edite o Plot das bandas por meio dos seguintes arquivos")
   print("= gerados na pasta output/Bandas ========================")   
   print("= Bandas.agr (via Grace) ou Bandas.py ===================")
   print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
