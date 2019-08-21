#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import re
import numpy as np
from PIL import Image
from natsort import natsorted
from skimage.measure import compare_psnr as psnr
from skimage.measure import compare_ssim as ssim
from skimage.transform import resize, rotate
from skimage.util import random_noise as add_noise
from config import *

#Seleccionar texto a ocultar
text_to_hide = 'Text_to_hide.txt'

#Seleccionar flag para guardar los archivos de salida
output = False

#------------------------------------------------------------------

#Agarrar lista de imágenes
img_list = natsorted([i for i in os.listdir(IMAGES_FOLDER)])

#Sufijo para el nombre de la stego-imagen
suffix_stego_img = '_steg'

#Sufijo para el nombre del texto extraido de la stego-imagen
suffix_extract_txt = '_xtxt'

#Definir arrays para computar estadística
psnr_N = np.zeros([20])
psnr_S = np.zeros([20])
psnr_P = np.zeros([20])
psnr_T = np.zeros([20])
ssim_N = np.zeros([20])
ssim_S = np.zeros([20])
ssim_P = np.zeros([20])
ssim_T = np.zeros([20])

for i,img in enumerate(img_list):
    
    print('Procesando {}/{}. Imagen: {}'.format(i+1,len(img_list),img))
    
    #Configurar nombre para la stego-imagen
    splitted_name = re.split('\.',img)
    out_img_name = splitted_name[0]+suffix_stego_img+'.'+splitted_name[1]
    type_image = re.split('_',splitted_name[0])[0]
    num_image = int(re.split('_',splitted_name[0])[1])
    
    out_txt_name = 'aux.txt'
    
    path_to_cover_image = os.path.join(IMAGES_FOLDER,img)
    path_to_text = os.path.join(TEXT_FOLDER,text_to_hide)
    path_to_stego_image = os.path.join(TEXT_FOLDER,out_img_name)
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_create.format(path_to_cover_image,path_to_text,path_to_stego_image))
    
    #Cargar imagenes y transformalas en arrays
    img_ground_truth = np.array(Image.open(path_to_cover_image))
    img_out = np.array(Image.open(path_to_stego_image))
    
    #Calcular métricas de imperceptibilidad
    globals()['psnr_{}'.format(type_image)][num_image] = psnr(img_ground_truth,img_out) #Resultado en decibeles
    globals()['ssim_{}'.format(type_image)][num_image] = ssim(img_ground_truth,img_out,multichannel=True) #multichannel=True porque trabajamos con imágenes a color. Cada canal es el canal de color.
    

    #A la stego-imagen se les aplica 5 transformaciones y se calculan las métricas de robustez
    
    #------------------------------------------------------------------------------------------
    #-----------Tampering (se borra completamente el 10% de la stego-imagen en la zona central)
    #------------------------------------------------------------------------------------------    
    
    img_aux = img_out.copy()
    
    central_x = int(img_aux.shape[0]/2)
    central_y = int(img_aux.shape[1]/2)
    
    pixels_removal = int(np.sqrt(img_aux.shape[0]*img_aux.shape[1]*0.1)/2)
    
    img_aux[central_x-pixels_removal:central_x+pixels_removal,
            central_y-pixels_removal:central_y+pixels_removal:,
            :] = 0
            
    #Crear imagen auxiliar para extraer con el software de steganografía
    Image.fromarray(img_aux, 'RGB').save('aux.jpg')
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_extract.format('aux.jpg',out_txt_name))   
    
    os.system('rm {}'.format(out_txt_name))
    
    #-------------------------------------------------------------
    #-----------Gaussian noise (se agrega ruido a la stego-imagen)
    #-------------------------------------------------------------
    
    img_aux = img_out.copy()    
    
    img_aux = add_noise(img_aux, mode='gaussian', var=0.05**2)
    
    img_aux = (255*img_aux).astype(np.uint8)
    
    Image.fromarray(img_aux, 'RGB').save('aux.jpg')
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_extract.format('aux.jpg',out_txt_name))   
    
    os.system('rm {}'.format(out_txt_name))
    
    #---------------------------------------------------------------------
    #-----------Stretching (se estira la stego-imagen horizontalmente 30%)
    #---------------------------------------------------------------------
        
    img_aux = img_out.copy()
    
    new_y = int(img_aux.shape[1]*1.3)
    
    img_aux = resize(img_aux, (img_aux.shape[0], new_y))
    
    img_aux = (255*img_aux).astype(np.uint8)
    
    Image.fromarray(img_aux, 'RGB').save('aux.jpg')
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_extract.format('aux.jpg',out_txt_name))   
    
    os.system('rm {}'.format(out_txt_name))
    
    #------------------------------------------------
    #-----------Mirroring (se espeja la stego-imagen)
    #------------------------------------------------
    
    img_aux = img_out.copy()
    
    img_aux = img_aux[:,::-1,:]
    
    Image.fromarray(img_aux, 'RGB').save('aux.jpg')
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_extract.format('aux.jpg',out_txt_name))   

    os.system('rm {}'.format(out_txt_name))    
    
    #-------------------------------------------------
    #-----------Rotation (se rota la stego-imagen 20º)
    #-------------------------------------------------
    
    img_aux = img_out.copy()
    
    img_aux = rotate(img_aux,20)
    
    img_aux = (255*img_aux).astype(np.uint8)
    
    Image.fromarray(img_aux, 'RGB').save('aux.jpg')
    
    #Ejecutar comando para llamar al software de steganografía
    os.system(command_extract.format('aux.jpg',out_txt_name))   
    
    os.system('rm {}'.format(out_txt_name))
    
    
    

#Al final hacer estadística por tipo de imagen y mostrar resultados
print('+----------------------------------------------------+')       
print('|        |           PSNR          |      SSIM       |')     
print('+--------+-------------------------+-----------------+')    
print('| Tipo N | {:10.2f} ± {:10.2f} | {:.4f} ± {:.4f} |'.format(psnr_N.mean(),psnr_N.std(),ssim_N.mean(),ssim_N.std()))
print('+--------+-------------------------+-----------------+') 
print('| Tipo S | {:10.2f} ± {:10.2f} | {:.4f} ± {:.4f} |'.format(psnr_S.mean(),psnr_S.std(),ssim_S.mean(),ssim_S.std()))
print('+--------+-------------------------+-----------------+') 
print('| Tipo P | {:10.2f} ± {:10.2f} | {:.4f} ± {:.4f} |'.format(psnr_P.mean(),psnr_P.std(),ssim_P.mean(),ssim_P.std()))
print('+--------+-------------------------+-----------------+') 
print('| Tipo T | {:10.2f} ± {:10.2f} | {:.4f} ± {:.4f} |'.format(psnr_T.mean(),psnr_T.std(),ssim_T.mean(),ssim_T.std()))
print('+----------------------------------------------------+') 
