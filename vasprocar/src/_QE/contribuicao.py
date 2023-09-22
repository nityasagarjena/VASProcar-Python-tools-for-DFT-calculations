# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

def execute_python_file(filename: str):
    return exec(open(main_dir + str(filename)).read(), globals())

read_projwfc_up = 1
read_contribuicao = 1

#======================================================================
# GetQE outpout files information =====================================
#======================================================================
execute_python_file(filename = DFT + '_info.py')
execute_python_file(filename = DFT + '_info_b.py')

#======================================================================
# Getting the input parameters ========================================
#======================================================================

print ("##############################################################")
print ("################ Orbital & ions contribution: ################")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Select the bands to be analyzed using intervals:              ")
print ("Type as in the examples below =============================== ")
print ("------------------------------------------------------------- ")
print ("Bands can be added in any order ----------------------------- ")
print ("------------------------------------------------------------- ")
print ("bands_intervals  35:42                                        ")          
print ("bands_intervals  1:15 27:69 18:19 76*                         ")
print ("bands_intervals  7* 9* 11* 13* 14:15                          ")
print ("##############################################################")
bands_range = input ("bands_intervals  ")
print (" ")
#------------------------------------------------------------------------------------------
selected_bands = bands_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
loop = int(len(selected_bands)/2)
#------------------------------------------------------------------------------------------  
bands_sn = ["nao"]*(nb + 1)
#---------------------------
for i in range (1,(loop+1)):
    #--------------------------------------------------------
    loop_i = int(selected_bands[(i-1)*2])
    if (selected_bands[((i-1)*2) +1] == "*"):
       selected_bands[((i-1)*2) +1] = selected_bands[(i-1)*2]
    loop_f = int(selected_bands[((i-1)*2) +1])
    #----------------------------------------------------------------------------------------
    if ((loop_i > nb) or (loop_f > nb) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
       print (" ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("ERROR: The values of the informed bands are incorrect %%%%")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       confirmation = input (" ")
       exit() 
    #----------------------------------------------------------------------     
    for j in range(loop_i, (loop_f + 1)):
        bands_sn[j] = "sim"  

print ("##############################################################")
print ("Select by the k-points to be analyzed:                        ")
print ("Type as in the examples below =============================== ")
print ("------------------------------------------------------------- ")
print ("The k-points can be added in any order ---------------------- ")
print ("------------------------------------------------------------- ")
print ("k-points_intervals  1:50                                      ")          
print ("k-points_intervals  15:25 27:100 150:180 200*                 ")
print ("k-points_intervals  70* 90* 110* 130* 140:150                 ")
print ("##############################################################")
points_range = input ("k-points_intervals  ")
print (" ")
#--------------------------------------------------------------------------------------------
selected_points = points_range.replace(':', ' ').replace('-', ' ').replace('*', ' *').split()
loop = int(len(selected_points)/2)
#--------------------------------------------------------------------------------------------      
points_sn = ["nao"]*(nk + 1)
#--------------------------- 
for i in range (1,(loop+1)):
    #--------------------------------------------------------
    loop_i = int(selected_points[(i-1)*2])
    if (selected_points[((i-1)*2) +1] == "*"):
       selected_points[((i-1)*2) +1] = selected_points[(i-1)*2]
    loop_f = int(selected_points[((i-1)*2) +1])
    #----------------------------------------------------------------------------------------
    if ((loop_i > nk) or (loop_f > nk) or (loop_i < 0) or (loop_f < 0) or (loop_i > loop_f)):
       print (" ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("ERROR: The entered k-point values are incorrect %%%%%%%%%%%")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       confirmation = input (" ")
       exit() 
    #-----------------------------------------------------------------------     
    for j in range(loop_i, (loop_f + 1)):
        points_sn[j] = "sim"

#*****************************************************************
# k-axis units ===================================================
# Dimensao = 1 >> 2pi/Param. (Param. in Angs.) *******************
# Dimensao = 2 >> 1/Angs. ****************************************
# Dimensao = 3 >> 1/nm *******************************************
#*****************************************************************
Dimensao = 1

#===============================================
read_orb = 1; esc_ions = 0
execute_python_file(filename = DFT + '_nscf.py')
#===============================================

os.remove(dir_files + '/output/Bandas.dat')
os.remove(dir_files + '/output/Orbitais.dat')

#-----------------------------------------------------------------
print(" ")
print("====================== Finished ! =======================")
#-----------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
