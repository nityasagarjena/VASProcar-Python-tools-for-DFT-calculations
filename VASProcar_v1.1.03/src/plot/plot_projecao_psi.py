
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================ Plotando os estados Psi ================")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
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
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

psi = np.loadtxt(dir_output + 'Psi.dat') 
psi.shape

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

#===========================================================================
# Plot as Projeções das Regiões de forma individual: =======================
#===========================================================================

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

rx = psi[:,0]
ry = psi[:,1] + dE_fermi 
ra = psi[:,2]
rb = psi[:,3]
rc = psi[:,4]
rd = psi[:,5]
re = psi[:,6]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------         
# Notação do Matplotlib para o padrão RGB de cores: color = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------------------
# red = [1.0, 0.0, 0.0]; green = [0.0, 1.0, 0.0]; blue = [0.0, 0.0, 1.0]; rosybrown = [0.737254902, 0.560784313, 0.560784313]; magenta = [1.0, 0.0, 1.0] ---           
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(1,(n_psi+1)):
    if (i == 1): ax.scatter(rx, ry, s = ra, color = [0.0, 0.0, 1.0], alpha = transp, edgecolors = 'none')
    if (i == 2): ax.scatter(rx, ry, s = rb, color = [1.0, 0.0, 0.0], alpha = transp, edgecolors = 'none')
    if (i == 3): ax.scatter(rx, ry, s = rc, color = [0.0, 1.0, 0.0], alpha = transp, edgecolors = 'none')
    if (i == 4): ax.scatter(rx, ry, s = rd, color = [0.737254902, 0.560784313, 0.560784313], alpha = transp, edgecolors = 'none')
    if (i == 5): ax.scatter(rx, ry, s = re, color = [1.0, 0.0, 1.0], alpha = transp, edgecolors = 'none')

# Gambiarra: A fim de gerar uma legenda cuja esfera colorida possua um tamanho fixo (antes ela adotada o menor ou maior tamanho de esfera do plot)
#            e sem a transparência do plot, tive que plotar pontos isolados afastados da região do gráfico.
for i in range(1,(n_psi+1)):
    if (i == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.0, 0.0, 1.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 2): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [1.0, 0.0, 0.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 3): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.0, 1.0, 0.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 4): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.737254902, 0.560784313, 0.560784313], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 5): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [1.0, 0.0, 1.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])

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
ax.legend(title = "")
ax.legend(loc = "upper right", title = "")
# ax.legend(loc = "best", title = "")

if (save_png == 1): plt.savefig(dir_output + 'Estados_Psi.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Estados_Psi.pdf', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Estados_Psi.eps', dpi = 600)

# plt.show()
plt.close()



#==============================================================================
# Plot com as Projeções das Regiões mescladas via soma do padrão de cores: ====
#==============================================================================

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------
   
color  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
passo = n_procar*nk*nb

#===========================================================================

color_rbg = open(dir_output + 'color_rgb.dat', "r")

for i in range(passo):
    VTemp = color_rbg.readline().split()
    color[i] = [VTemp[0], VTemp[1], VTemp[2]]

#----------------
color_rbg.close()
#----------------

#=======================================================================

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

peso = ra + rb + rc + rd + re

ax.scatter(rx, ry, s = peso, c = color, alpha = transp, edgecolors = 'none')

# Gambiarra: A fim de gerar uma legenda cuja esfera colorida possua um tamanho fixo (antes ela adotada o menor ou maior (???) tamanho de esfera do plot)
#            e sem a transparência do plot, tive que plotar pontos isolados afastados da região do gráfico.
for i in range(1,(n_psi+1)):
    if (i == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.0, 0.0, 1.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 2): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [1.0, 0.0, 0.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 3): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.0, 1.0, 0.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 4): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [0.737254902, 0.560784313, 0.560784313], alpha = 1.0, edgecolors = 'none', label = l_psi[i])
    if (i == 5): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = [1.0, 0.0, 1.0], alpha = 1.0, edgecolors = 'none', label = l_psi[i])

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

plt.ylabel('$E-E_{f}$ (eV)')

ax.set_box_aspect(1.25/1)
ax.legend(loc = "upper right", title = "")
# ax.legend(loc = "best", title = "")

if (save_png == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].pdf', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Estados_Psi_[sum_colors].eps', dpi = 600)

# plt.show()
plt.close()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
   print("= gerados na pasta output/Psi ==============================")   
   print("= arquivos .agr (via Grace) ou Psi.py ======================")
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
