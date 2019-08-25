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
* Depende de la implementación de cada software. Hay que ver si para una imagen cover dada, el software que uno tiene le da información de la capacidad que permite esa imagen.

### Para testear imperceptibility:
* [PSNR](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio) (En Python se puede usar [skimage.measure.compare_psnr](https://scikit-image.org/docs/dev/api/skimage.measure.html))
* [SSIM](https://en.wikipedia.org/wiki/Structural_similarity) (En Python se puede usar [skimage.metrics.structural_similarity](https://scikit-image.org/docs/dev/api/skimage.metrics.html#skimage.metrics.structural_similarity))

### Para testear robustness:
* Bit error rate of extracted secret data

## Propuesta para subir resultados:
Subir los resultados al directorio [/Results](https://github.com/rodo-qatar/ECI-2019-watermarking/tree/master/Results) como .csv con el siguiente formato de nomenclatura:

```
<Código de nombre>_<Código de métrica>_<Código de tipo de imagen>_<Cantidad de estrofas>.csv
```
  
Este debe ser un archivo de 20 filas y una columna con los resultados numéricos de las 20 imágenes ordenado desde la 0 (primera fila, la de arriba) hasta la 19 (última fila la de abajo de todo).

Cada código para la nomenclatura puede tomar los siguientes valores:

```
<Código de nombre> = [FRA, # Para Francisco Acha
                      JPC, # Para Juan Pablo Caldo
                      ROC, # Para Rodrigo Cardenas
                      FRC, # Para Franco Castagna
                      ELR # Para Elías Remedi]
                      
<Código de métrica> = [PSNR, # Para Peak Signal to Noise Ratio
                       SSIM, # Para Structural Similarity
                       BER # Para Bit Error Rate]

<Código de tipo de imagen> = [N, # Para Paisajes
                              S, # Para Objetos inanimados
                              P, # Para Retratos
                              N # Para texto]
                       
<Cantidad de estrofas> = [1,2,3]
```

## Software a testear por cada uno:

* Francisco Acha: *Outguess*
* Juan Pablo Caldo: 
* Rodrigo Cardenas: *StegHide*
* Franco Castagna: *SilentEye*
* Elías Remedi: *SteganPEG*

Hagan cualquier observación, crítica o cambio que crean conveniente! Aportemos todos!! :)


