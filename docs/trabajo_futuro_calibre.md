# Trabajo futuro: estimar el calibre de la piña (idea del asesor, 25-oct-2026)

**Decisión del usuario (25-oct-2026):** NO se incluye en la tesis. Queda como análisis guardado para una versión futura.

## La idea
Con el dron a 2 m del cultivo se espera capturar más detalle del fruto. Eso podría servir, más allá del conteo, para estimar el **calibre** (tamaño) de la piña. El calibre define la clase comercial (primera, segunda, tercera) y, según el asesor, el pago al productor. Con modelos generativos se podrían generar imágenes de piña que lleven información del calibre.

## Búsqueda (Semantic Scholar, 25-oct-2026, 16 consultas)
Temas: tamaño, peso, calificación y rendimiento de piña; tamaño de fruta desde dron; imágenes sintéticas y generación condicionada para tamaño de fruta.

| Trabajo | Qué hace | Metadatos verificados en Crossref |
|---|---|---|
| Langpoklakpam, Murry, Kumar (2025). Automated pineapple detection, ripeness classification, and weight prediction using YOLOv8 and drone imagery | Detección, madurez y peso de piña desde dron. **Solo se leyó el título; falta leer el resumen.** | J. Food Meas. Charact. 19(11), 8657-8678. DOI 10.1007/s11694-025-03565-3 |
| Harris y Er (2025). Pineapple fruit detection and size determination in a juicing factory in the Eastern Cape, South Africa | Tamaño de piña (diámetro, largo, área) con Mask R-CNN, en fábrica de jugo | S. Afr. J. Sci. 121(9/10). DOI 10.17159/sajs.2025/18277 |
| Lin, Jiang, Zhao, Zou, Xue (2025). DPD-YOLO | Detección de piñas desde dron para rendimiento; la corona de hojas suele ocultar el fruto | Front. Plant Sci. 16, 1523552. DOI 10.3389/fpls.2025.1523552 |
| Ferrer-Ferrer et al. (2023). Simultaneous fruit detection and size estimation using multitask deep neural networks | Diámetro de manzanas en campo con datos RGB-D | Biosyst. Eng. 233, 63-75. DOI 10.1016/j.biosystemseng.2023.07.010 |
| Kim et al. (2025). De-occlusion models and diffusion-based data augmentation for size estimation of on-plant oriental melons | Un modelo de difusión genera hojas sintéticas para aumentar datos de estimación de tamaño | Plant Phenomics 7(3), 100097. DOI 10.1016/j.plaphe.2025.100097 |
| Gómez y Ríos-Rojas (2020). "Mal de cintura" disorder characterization of pineapple MD2... Valle del Cauca | En MD2, el peso es el parámetro más importante para la clasificación de calidad | Rev. Colomb. Cienc. Hortic. 14(2), 153-167. DOI 10.17584/rcch.2020v14i2.10735 |
| Liu, Nie, Wu, Zhang, Liu et al. (2022). Pineapple fruit detection and localization in natural environment based on binocular stereo vision | Detección y localización de piña en campo con visión estéreo | Precis. Agric. 24(1), 139-160. DOI 10.1007/s11119-022-09935-x |

**No se encontró** (entre los resultados recuperados) ningún trabajo que genere imágenes aéreas de piña con información del calibre. Es una ausencia en 16 consultas, no una prueba de inexistencia.

## Advertencias
1. Desde arriba la corona oculta parte del fruto (Lin 2025); a 2 m ayuda, no lo elimina.
2. La profundidad del dataset es relativa (monocular), no métrica. Medir milímetros exige escala (altura del dron, cámara o profundidad métrica). Conecta con el factor D (canal de profundidad).
3. La clase comercial y el pago por categoría vienen del asesor y del productor; no hay fuente propia. Confirmar con productores antes de afirmar tarifas.
4. El calibre exige etiquetar las imágenes generadas (hoy es una limitación declarada en c3).

## Texto listo para usar si se decide incluirlo
**c3, Scope (junto a "Extension: second crop..."):**

> Future work: since the images are captured at two meters, where more detail of the fruit is expected than at the altitudes of usual flights, the approach could support the estimation of the caliber, that is, the size of the fruit, which defines its commercial class, and not only the count of plants; this requires labeling the generated images with the caliber and a metric scale, which the relative depth of this dataset does not provide.

**c2, subsección "Plant counting and detection" (una frase):**

> Counting is not the only use of the images: the size or weight of the fruit determines its commercial class \cite{Gomez2020}, and it has been estimated from images for pineapples in a juicing factory \cite{Harris2025}, from drone imagery \cite{Langpoklakpam2025}, and for apples with RGB-D data \cite{FerrerFerrer2023}; diffusion models have also been used to enrich datasets for fruit size estimation \cite{Kim2025}. In 16 complementary queries (Semantic Scholar, 25 October 2026), no work was found that generates aerial pineapple images with information on fruit size.

Si se incluye: agregar las referencias a `TFC1/biblio.bib` (claves sugeridas Gomez2020, Harris2025, Langpoklakpam2025, FerrerFerrer2023, Kim2025), actualizar el párrafo "Complementary searches" de c2 con las 16 consultas, y leer antes el resumen de Langpoklakpam 2025.
