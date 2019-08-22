# Script para calcular métricas

Este es un script de Python que realiza las siguientes acciones:
* Genera las stego-imágenes a partir de la base de datos, el texto a ocultar y del comando utilizado para llamar al software de steganografía.
* Calcula las métricas de imperceptibilidad (PSNR y SSIM) para cada imagen y las guarda en formato .csv.
* Aplica deformaciones a las stego-imágenes para testear la robustez.

## Para correr el script:

Copiar localmente [metrics_script.py](https://github.com/rodo-qatar/ECI-2019-watermarking/tree/master/code/metrics_script.py) y [config.py](https://github.com/rodo-qatar/ECI-2019-watermarking/tree/master/code/config.py)
y setear en *config.py* los directorios, comandos y nombre de usuario que se utilizarán.
