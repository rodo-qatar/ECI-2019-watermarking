

#Folder donde se encuentran las imagenes cover
IMAGES_FOLDER = '/home/rodrigo/Documents/Escuelas/ECI_2019/Watermarking/Data' 

#Folder donde se encuentran los textos a ocultar
TEXT_FOLDER = '/home/rodrigo/Documents/Escuelas/ECI_2019/Watermarking' 

#Definir comando de ejecución para el software de steganografia para crear la stego-imagen
command_create = 'steghide embed -cf {} -ef {} -sf {} -Z -K -N -v -p 1234' 

#Definir comando de ejecución para el software de steganografia para extraer de la stego-imagen el mensaje
command_extract = 'steghide extract -sf {} -xf {} -p 1234'

#Código de usuario para los archivos de salida
code_user = 'ROC'
