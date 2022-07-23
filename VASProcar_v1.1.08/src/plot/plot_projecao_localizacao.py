
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("============= Plotando as Projecoes (Matplotlib): =============")

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
   dir_output = dir_files + '/output/Localizacao/'
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

localizacao = np.loadtxt(dir_output + 'Localizacao.dat') 
localizacao.shape

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

dpi = 2*3.1415926535897932384626433832795

rx = localizacao[:,0]
ry = localizacao[:,1] + dE_fermi 
RegA = localizacao[:,2]; pRegA = ((dpi*RegA)**2)*peso_total
RegB = localizacao[:,3]; pRegB = ((dpi*RegB)**2)*peso_total
RegC = localizacao[:,4]; pRegC = ((dpi*RegC)**2)*peso_total
RegD = localizacao[:,5]; pRegD = ((dpi*RegD)**2)*peso_total
RegE = localizacao[:,6]; pRegE = ((dpi*RegE)**2)*peso_total
RegF = localizacao[:,7]; pRegF = ((dpi*RegF)**2)*peso_total
Regtot = RegA + RegB + RegC + RegD + RegE + RegF; pRegtot = ((dpi*Regtot)**2)*peso_total

#----------------------------------------------------------------------------------------------------------       
# Padrao RGB de cores das Projecoes: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 ---       
#----------------------------------------------------------------------------------------------------------

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
# Plot das Projeções das REGIOES de forma individual: ======================
#===========================================================================

if (num_A == 1):
   ax.scatter(rx, ry, s = pRegA, color = cRGB[c_Reg1], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_1: {label_reg[0]})')
   
if (num_B == 1):
   ax.scatter(rx, ry, s = pRegB, color = cRGB[c_Reg2], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_2: {label_reg[1]})')
   
if (num_C == 1):
   ax.scatter(rx, ry, s = pRegC, color = cRGB[c_Reg3], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_3: {label_reg[2]})')

if (num_D == 1):
   ax.scatter(rx, ry, s = pRegD, color = cRGB[c_Reg4], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_4: {label_reg[3]})')

if (num_E == 1):
   ax.scatter(rx, ry, s = pRegE, color = cRGB[c_Reg5], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_5: {label_reg[4]})') 

if (num_F == 1):
   ax.scatter(rx, ry, s = pRegF, color = cRGB[c_Reg6], alpha = transp, edgecolors = 'none')
   print (f'Analisando a Localizacao dos Estados (Regiao_6: {label_reg[5]})') 

# Gambiarra: A fim de gerar uma legenda cuja esfera colorida possua um tamanho fixo (antes ela adotada o menor ou maior tamanho de esfera do plot)
#            e sem a transparência do plot, tive que plotar pontos isolados afastados da região do gráfico.
if (num_A == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg1], alpha = 1.0, edgecolors = 'none', label = label_reg[0])
if (num_B == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg2], alpha = 1.0, edgecolors = 'none', label = label_reg[1])
if (num_C == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg3], alpha = 1.0, edgecolors = 'none', label = label_reg[2])
if (num_D == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg4], alpha = 1.0, edgecolors = 'none', label = label_reg[3])
if (num_E == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg5], alpha = 1.0, edgecolors = 'none', label = label_reg[4])      
if (num_F == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg6], alpha = 1.0, edgecolors = 'none', label = label_reg[5])

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

if (save_png == 1): plt.savefig(dir_output + 'Localizacao_estados.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Localizacao_estados.pdf', dpi = 600)
if (save_svg == 1): plt.savefig(dir_output + 'Localizacao_estados.svg', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Localizacao_estados.eps', dpi = 600)

# plt.show()
plt.close()

#=============================================================================================================
# Obtendo e gravando as cores no padrão RGB que designam a combinação de REGIOES para o Plot das Projeções ===
#=============================================================================================================

print (" ")
print ("Analisando a sobreposicao de REGIOES (Soma do padrao de cores)")

rgb_Reg = [0]*n_procar*nk*nb

number = -1
for k in range (1, (nb+1)):
    for i in range (1, (n_procar+1)):
        for j in range (1, (nk+1)):       
            number += 1

            #-------------------------------------------------------------------------------------------------
            # Somando as cores das REGIOES 1|2|3|4|5|6: ------------------------------------------------------
            #-------------------------------------------------------------------------------------------------

            color_dat = [0]*3
            
            for i in range(3):
                color_dat[i] = RegA[number]*cRGB[c_Reg1][i] + RegB[number]*cRGB[c_Reg2][i] + RegC[number]*cRGB[c_Reg3][i] + RegD[number]*cRGB[c_Reg4][i]
                color_dat[i] = color_dat[i] + RegE[number]*cRGB[c_Reg5][i] + RegF[number]*cRGB[c_Reg6][i]
                #-------------------------------------------
                if (color_dat[i]  > 1.0): color_dat[i] = 1.0
                #-------------------------------------------
            rgb_Reg[number] = (color_dat[0], color_dat[1], color_dat[2]) 

#==============================================================================
# Plot com as Projeções das Regiões mescladas via soma do padrão de cores: ====
#==============================================================================

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

peso = pRegtot

ax.scatter(rx, ry, s = peso, c = rgb_Reg, alpha = transp, edgecolors = 'none')

# Gambiarra: A fim de gerar uma legenda cuja esfera colorida possua um tamanho fixo (antes ela adotada o menor ou maior (???) tamanho de esfera do plot)
#            e sem a transparência do plot, tive que plotar pontos isolados afastados da região do gráfico.
if (num_A == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg1], alpha = 1.0, edgecolors = 'none', label = label_reg[0])
if (num_B == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg2], alpha = 1.0, edgecolors = 'none', label = label_reg[1])
if (num_C == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg3], alpha = 1.0, edgecolors = 'none', label = label_reg[2])
if (num_D == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg4], alpha = 1.0, edgecolors = 'none', label = label_reg[3])
if (num_E == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg5], alpha = 1.0, edgecolors = 'none', label = label_reg[4])
if (num_F == 1): ax.scatter([-1000.0], [-1000.0], s = [40.0], color = cRGB[c_Reg6], alpha = 1.0, edgecolors = 'none', label = label_reg[5])

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
ax.legend(loc = "upper right", title = "")
# ax.legend(loc = "best", title = "")

if (save_png == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].pdf', dpi = 600)
if (save_svg == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].svg', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].eps', dpi = 600)

# plt.show()
plt.close()

#========================================================================

print(" ")
print ("Plot das projecoes via Matplotlib concluido -------------------")

#------------------------------------------------------------------------
if (dir_output == ''):
   print(" ")
   print("======================= Concluido =======================")
#------------------------------------------------------------------------ 
