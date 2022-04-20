
import numpy as np

def execute_python_file(filename: str):
   return exec(open(str(filename)).read(), globals())

#-----------------------------------------------------------------------
# Verificando se a pasta "BSE" existe, se não existe ela é criada -----
#-----------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/BSE'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/BSE')
#-------------------------------------

#======================================================================
# Verificando a presenca do arquivo vasprun.xml =======================
#======================================================================

try:
    f = open(dir_files + '/vasprun.xml')
    f.close()
except:
    print('----------------------------------------------------------------------------------------')
    print('Arquivo vasprun.xml ausente no diretorio, insira o arquivo e aperte ENTER para continuar')
    print('----------------------------------------------------------------------------------------')
    confirmacao = input (" "); confirmacao = str(confirmacao)   

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################# Plot da Funcao Dieletrica: #################")
print ("##############################################################")
print (" ")
 
print ("##############################################################")
print ("Deseja informar a energia de Fermi? ==========================")
print ("[0] NAO                                                       ")
print ("[1] SIM                                                       ")
print ("##############################################################") 
esc_ef = input (" "); esc_ef = int(esc_ef)
print (" ")

if (esc_ef == 0):
   e_fermi = 0.0
   
if (esc_ef == 1):
   print ("##############################################################")
   print ("Qual o valor da energia de Fermi? ============================")
   print ("##############################################################") 
   e_fermi = input (" "); e_fermi = float(e_fermi)
   print (" ")

print ("##############################################################")
print ("Deseja escolher o range de energia do Plot? ==================")
print ("[0] NAO                                                       ")
print ("[1] SIM                                                       ")
print ("##############################################################") 
esc_energ = input (" "); esc_energ = int(esc_energ)
print (" ")
 
if (esc_energ == 1):
   
   print ("##############################################################")
   print ("Digite o valor inicial da energia ============================")
   print ("##############################################################") 
   x_inicial = input (" "); x_inicial = float(x_inicial)
   print (" ")

   print ("##############################################################")
   print ("Digite o valor final da energia ============================")
   print ("##############################################################") 
   x_final = input (" "); x_final = float(x_final)
   print (" ")



#----------------------------------------------------------------------
# Extraindo os resultados do arquivo vasprun.xml ----------------------
#----------------------------------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  

for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

palavra = '<set>'

for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

palavra = '</set>'

passo = -1

for line in vasprun:
    passo += 1
    if palavra in line: 
       break

#--------------
vasprun.close()
#--------------

#==============================================

#----------------------------------------------
vasprun = open(dir_files + '/vasprun.xml', 'r')
#----------------------------------------------

palavra = '<imag>'  

for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

palavra = '<set>'

for line in vasprun:   
    if palavra in line: 
       break

#----------------------------------------------

energ = [0.0]*passo
X_i   = [0.0]*passo;  X_r  = [0.0]*passo
Y_i   = [0.0]*passo;  Y_r  = [0.0]*passo
Z_i   = [0.0]*passo;  Z_r  = [0.0]*passo
XY_i  = [0.0]*passo;  XY_r = [0.0]*passo
YZ_i  = [0.0]*passo;  YZ_r = [0.0]*passo
ZX_i  = [0.0]*passo;  ZX_r = [0.0]*passo
media_i  = [0.0]*passo;  media_r  = [0.0]*passo
modulo_i = [0.0]*passo;  modulo_r = [0.0]*passo

#----------------------------------------------

for i in range(passo):
    VTemp = vasprun.readline().split()
    energ[i] = float(VTemp[1])
    X_i[i]   = float(VTemp[2])
    Y_i[i]   = float(VTemp[3])
    Z_i[i]   = float(VTemp[4])
    media_i[i]  = (X_i[i] + Y_i[i] + Z_i[i])/3
    modulo_i[i] = ((X_i[i]**2) + (Y_i[i]**2) + (Z_i[i]**2))**0.5
    XY_i[i]  = float(VTemp[5])
    YZ_i[i]  = float(VTemp[6])
    ZX_i[i]  = float(VTemp[7])

palavra = '<set>'

for line in vasprun:   
    if palavra in line: 
       break

for i in range(passo):
    VTemp = vasprun.readline().split()
    # energ[i] = float(VTemp[1])
    X_r[i]   = float(VTemp[2])
    Y_r[i]   = float(VTemp[3])
    Z_r[i]   = float(VTemp[4])
    media_r[i]  = (X_r[i] + Y_r[i] + Z_r[i])/3
    modulo_r[i] = ((X_r[i]**2) + (Y_r[i]**2) + (Z_r[i]**2))**0.5
    XY_r[i]  = float(VTemp[5])
    YZ_r[i]  = float(VTemp[6])
    ZX_r[i]  = float(VTemp[7])

#--------------
vasprun.close()
#--------------

#======================================================================
# Gravando dados para o Plot da Função Dieletrica: ====================
#======================================================================     

#-------------------------------------------------
BSE = open(dir_files + '/output/BSE/BSE.dat', 'w')
#-------------------------------------------------

for i in range (passo):
    BSE.write(f'{energ[i]}')
    BSE.write(f' {modulo_i[i]} {media_i[i]}')
    BSE.write(f' {X_i[i]} {Y_i[i]} {Z_i[i]}')
    # BSE.write(f' {XY_i[i]} {YZ_i[i]} {ZX_i[i]}')
    BSE.write(f' {media_r[i]} {modulo_r[i]}')
    BSE.write(f' {X_r[i]} {Y_r[i]} {Z_r[i]}')
    # BSE.write(f' {XY_r[i]} {YZ_r[i]} {ZX_r[i]}')
    BSE.write(f' \n')
    
#----------
BSE.close()
#----------

#======================================================================
#======================================================================
# Plot da Funcao Dieletrica (GRACE) ===================================
#====================================================================== 
#======================================================================

# Rotulos ============================================================= 

rot = [0]*(8)
rot[0] = 'Mod'; rot[1] = 'Med'
rot[2] = 'X'; rot[3] = 'Y'; rot[4] = 'Z'
# rot[5] = 'XY';     rot[6] = 'YZ';    rot[7] = 'ZX'

# Cores ===============================================================

# Codigo de cores do GRACE
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14

color = [0]*(8)
color[0] = '1'; color[1] = '10';  
color[2] = '4'; color[3] = '2'; color[4] = '3'
# color[5] = '9'; color[6] = '12'; color[7] = '14'

# =====================================================================

func_dielet = np.loadtxt(dir_files + '/output/BSE/BSE.dat') 
func_dielet.shape

# =====================================================================

if (esc_energ == 0):
   x_inicial = min(energ)
   x_final   = max(energ)

for i in range(2):
   
    y_inicial = +1000.0
    y_final   = -1000.0
   
    #---------------------------------------------------------------------------------
    if (i == 0): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_IMAG.agr', 'w')
    if (i == 1): BSE = open(dir_files + '/output/BSE/Funcao_Dieletrica_REAL.agr', 'w')
    #---------------------------------------------------------------------------------

    for j in range(5):
        if (i == 0): m = (j +1)         
        if (i == 1): m = (j +6) 
        temp_min = min(func_dielet[:,m])
        temp_max = max(func_dielet[:,m])
        if (temp_min < y_inicial): y_inicial = temp_min
        if (temp_max > y_final):   y_final   = temp_max
    

    # Escrita dos arquivos ".agr" do GRACE ============================

    BSE.write("# Grace project file \n")
    BSE.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
    BSE.write("# \n")
    BSE.write("@version 50122 \n")
    BSE.write("@with g0 \n")
    BSE.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    BSE.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    BSE.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    BSE.write(f'@    xaxis  label "Energia (eV)" \n')    
    BSE.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    BSE.write(f'@    yaxis  label "Funcao Dieletrica (BSE)" \n')       
    BSE.write(f'@    legend {fig_xmax + leg_x - 0.035}, {fig_ymax + leg_y} \n')

    for j in range(5):
        BSE.write(f'@    s{j} type xy \n')
        BSE.write(f'@    s{j} line type 1 \n')
        BSE.write(f'@    s{j} line color {color[j]} \n')
        BSE.write(f'@    s{j} line linewidth 2.0 \n')
        # BSE.write(f'@    s{j} fill type 1 \n')
        # BSE.write(f'@    s{j} fill color {color[j]} \n')
        # BSE.write(f'@    s{j} fill pattern 4 \n')
        BSE.write(f'@    s{j} legend  "{rot[j]}" \n')
    BSE.write("@type xy")
    BSE.write(" \n")

    # Plot das componentes da Função Dielétrica =======================

    for j in range(5):
        #---------------------------------------
        if (i == 0): temp = func_dielet[:,(j+1)]
        if (i == 1): temp = func_dielet[:,(j+6)]
        #---------------------------------------
        for k in range (passo):
            BSE.write(f'{energ[k]} {temp[k]} \n')
        BSE.write(" \n")

    #----------
    BSE.close()
    #----------




























    




