# ECI-2019-watermarking

Este repo es para trabajar en conjunto con el trabajo de watermarking

[Data.tar](https://github.com/rodo-qatar/ECI-2019-watermarking/blob/master/Data.tar) es un archivo que contiene 80 imágenes: 20 imágenes de cada tipo:
* N (naturaleza)
* S (objetos inanimados)
* P (retratos)
* T (texto)

[Text_to_hide.txt](https://github.com/rodo-qatar/ECI-2019-watermarking/blob/master/Text_to_hide.txt) es un texto para ocultar en las imágenes (primeras tres estrofas del Martín Fierro).
Se pueden usar una, dos o tres estrofas para testear la **capacidad**.

[Report.tex](https://github.com/rodo-qatar/ECI-2019-watermarking/blob/master/Report.tex) es el template de LaTeX del reporte final
que podemos ir completando.

En el directorio [/Refs](https://github.com/rodo-qatar/ECI-2019-watermarking/tree/master/Refs) se puede ir poniendo bibliografía relevante.
El paper de [Rabie et al (2019)](https://github.com/rodo-qatar/ECI-2019-watermarking/blob/master/Refs/Rabie-2019.pdf) contiene un repaso de métricas estándar para evaluar esteganografía. Entre ellas:

### Para testear capacidad:
* Secret bits per sample

### Para testear imperceptibility:
* PSNR
* SSIM
* Feature similarity

### Para testear robustness:
* Bit error rate of extracted secret data

Hagan cualquier observación, crítica o cambio que crean conveniente! Aportemos todos!! :)

