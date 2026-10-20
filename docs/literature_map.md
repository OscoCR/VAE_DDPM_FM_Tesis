# Mapa de afirmaciones a fuentes (capítulo III, sección Problem; antes capítulo II)

Cada fila dice qué se afirma en el texto, qué referencia lo respalda (clave de `TFC1/biblio.bib`), qué dice la fuente y cómo se verificó.
Estado: **Sí** = leí el resumen oficial de arXiv o el texto del paper; **Parcial** = solo vi un resumen de búsqueda, hay que abrir el paper antes de dar la cita por buena.
Fecha de la verificación de metadatos (autores, título, año): 11-oct-2026, contra la API de arXiv.

| # | Afirmación en el texto | Clave | Qué dice la fuente | Verificado |
|---|---|---|---|---|
| 1 | La difusión latente comprime con un autoencoder y es más barata que en píxeles | `Rombach2022` | Aplican difusión en el espacio latente de autoencoders preentrenados para entrenar con recursos limitados | Sí (resumen arXiv 2112.10752) |
| 2 | El diseño del latente se estudia sobre todo en benchmarks grandes como ImageNet | `Yao2025`, `Skorokhodov2025`, `Zheng2025` | Reportan resultados en ImageNet 256 (Skorokhodov también en Kinetics) | Sí (resúmenes arXiv: Yao, ImageNet 256x256; Skorokhodov, ImageNet-1K y Kinetics-700; Zheng, ImageNet) |
| 3 | Las aplicaciones agrícolas regionales tienen datos pequeños y homogéneos; los modelos de difusión se diseñan para datos masivos y diversos | `Gonzalez2026` | Lo dice en la introducción | Sí (texto del PDF) |
| 4 | Datasets limitados y muestras desbalanceadas son un reto frecuente en imágenes agrícolas | `Hu2025` | El resumen menciona "limited annotated datasets and imbalanced sample distributions" | Sí (resumen arXiv 2507.18376) |
| 5 | Hay modelos que generan apariencia y geometría conjuntamente desde un latente compartido, a gran escala | `Krishnan2025` | VAE conjunto de RGB, profundidad y normales con difusión latente | Sí para el latente compartido (resumen arXiv 2501.13087). "a gran escala" se retiró del texto porque no se pudo confirmar en el resumen |
| 6 | Más dimensión por token mejora la reconstrucción pero exige modelos mayores y más entrenamiento para igualar la generación | `Yao2025` | Es el "dilema de optimización" de su resumen | Sí (resumen arXiv 2501.01423) |
| 7 | Latentes con exceso de componentes de alta frecuencia estorban a la difusión | `Skorokhodov2025` | Análisis espectral; hipotetizan que interfieren con la síntesis de lo grueso a lo fino | Sí (resumen arXiv 2502.14831) |
| 8 | Mejor reconstrucción del tokenizer no implica mejor generación | `Zhong2026` | Primera frase del resumen | Sí (resumen arXiv 2606.03578; es un preprint de 2026) |
| 9 | Con presupuesto de entrenamiento limitado, un latente de mayor dimensión empeoró la generación | `Sehwag2025` | Sección 6.2: el modelo de 4 canales superó al de 16 en FID, Clip-FID, CLIP y GenEval. Es presupuesto de cómputo, no pocos datos | Sí (texto HTML del paper) |
| 10 | El enmascarado aleatorio se usa para aprender representaciones y tokenizers para difusión | `He2022`, `Chen2025` | MAE; MAETok (autoencoder con enmascarado para difusión) | Sí para el contenido (resúmenes arXiv 2111.06377 y 2502.03444). Pendiente: confirmar el venue de `Chen2025` (ICML 2025) |
| 11 | En este contexto, un latente de VAE continuo conservó la estructura del cultivo donde uno discreto falló | `Gonzalez2026` | Resultado central del paper | Sí (texto del PDF) |
| 12 | Las decisiones sobre datos y estructura del VAE se toman por experimentación manual | `Gonzalez2026` | Conclusiones: "architectural adaptations were manually derived through systematic experimentation" | Sí (texto del PDF) |

## Identificadores para traer las referencias desde Zotero ("Add Item by Identifier")

```
2112.10752   Rombach2022
2501.01423   Yao2025
2502.14831   Skorokhodov2025
2606.03578   Zhong2026
2407.15811   Sehwag2025
2510.11690   Zheng2025
2507.18376   Hu2025
2501.13087   Krishnan2025
2502.03444   Chen2025
2111.06377   He2022
10.1145/3795101.3814709   Gonzalez2026 (DOI)
```

## Pendientes
- Abrir los papers marcados "Parcial" y confirmar lo que dicen.
- Cambiar a la versión publicada (venue) en las entradas de arXiv que ya se publicaron.


## Registro de cribado en arXiv que respalda la afirmación de novedad (frase final del Problem)
Fecha: 11-oct-2026. Buscador: API de arXiv (envíos desde 2022). Criterios, aplicados a título y resumen:
C1 = varía algo del VAE/autoencoder o de sus datos de entrenamiento; C2 = mide la generación (FID, KID, calidad de generación);
C3 = pocos datos o datos homogéneos. Cribado automático por palabras clave; es un primer filtro, no sustituye leer los resúmenes.
Detalle por paper en `docs/screening_arxiv_2026-10-11.csv`.

| Cadena | Total en arXiv |
|---|---|
| Q1 `"latent diffusion" + autoencoder/VAE/tokenizer + augmentation` | 30 |
| Q2 `"latent diffusion" + autoencoder/VAE/tokenizer + adversarial/KL/regularization/latent channels` | 73 |
| Q3 `"latent diffusion" + autoencoder + aerial/agricultural/crop/plant/UAV/remote sensing` | 9 |
| Q4 `"latent diffusion" + masked/masking + autoencoder/VAE/tokenizer` | 47 |
| Q5 `"latent diffusion" + depth + RGB/appearance + joint/shared latent` | 7 |

Resultado: 151 papers únicos; 34 cumplen C1 y C2; solo 4 de ellos cumplen además datos escasos o dominio, y los 4 son aplicaciones médicas (MRI, embriones, corazón 4D) que usan un VAE para sintetizar datos, no estudian cómo el diseño del VAE o sus datos afectan la generación. Ninguno cumple las tres a la vez en un dominio aéreo o agrícola.
En el dominio aéreo/agrícola (Q3) no apareció ningún trabajo sobre el diseño del VAE. En RGB+profundidad (Q5) aparecen Orchid, LDM3D-VR e IDOL, todos a gran escala.
Conclusión: la frase del Problem ("a nuestro leal saber") queda respaldada por este cribado. Limitaciones: solo arXiv, filtro por palabras clave y cinco cadenas.

## Candidatas para el Related Work (resúmenes de búsqueda, POR VERIFICAR antes de citar)
- Latent Denoising Diffusion GAN, arXiv 2406.11713: autoencoders con pérdida adversarial sin KL; mejor generación pese a peor reconstrucción.
- REGLUE, arXiv 2512.16636: subir el peso de KL empeora la generación.
- TADA (NeurIPS 2023): aumento de datos en la difusión con pocos datos.
- Emu, arXiv 2309.15807: latente de 16 canales frente a 4 para detalle fino.
- PlantLDM y SPROUT (arXiv 2603.27519): difusión en plantas y agricultura con datos grandes.
- Remote Diffusion, arXiv 2405.04717: ajuste fino de Stable Diffusion en imágenes aéreas.
- LDMAE ("Latent Diffusion Models with Masked AutoEncoders"), arXiv 2507.09984: dice que las propiedades deseables y el diseño óptimo de los autoencoders para LDM están poco explorados; propone VMAE. Muy cercano al enmascarado; datos grandes.
- arXiv 2506.13307: compara ajuste fino de UNet, VAE y codificadores de texto de un LDM preentrenado para imágenes SAR (100 mil imágenes).
- arXiv 2605.07915 (autoencoders alineados con un prior), 2602.08620 (mejora de la reconstrucción de RAE), 2508.00413 (DC-AE 1.5): diseño del latente a gran escala.


## Referencias del marco teórico: metadatos PENDIENTES de verificar
No se pudieron verificar contra la API de arXiv (límite de peticiones el 11-oct-2026); los datos salen de mi conocimiento. Verificar antes de entregar:
`Paszke2019` (1912.01703), `Kingma2015` (1412.6980), `Loshchilov2019` (1711.05101), `Loshchilov2017` (1608.03983), `He2016` (1512.03385), `Wu2018` (1803.08494), `Ronneberger2015` (1505.04597).
Sin arXiv, confirmar en la editorial: `Goodfellow2016` (libro, MIT Press), `Rumelhart1986` (Nature 323), `LeCun1998` (Proc. IEEE 86(11)), `Higgins2017` (ICLR 2017).
Las sedes (ICLR, NeurIPS, CVPR) de Kingma2014, vandenOord2017, Ho2020, Lipman2023, Goodfellow2014, Isola2017, Heusel2017 y Binkowski2018 también salen de memoria; autores, títulos y años sí se verificaron.


## Referencias nuevas del Background (18-oct-2026): motivación, detección, datos y datos sintéticos
Fuente: 14 consultas en la API de Semantic Scholar (Academic Graph, con clave, 20 resultados por consulta, desde 2012). Registro completo en `docs/s2/topic_search_s2_2026-10-18.csv`. Metadatos (título, autores, año, sede) comprobados en Semantic Scholar por DOI o arXiv (`docs/s2/cited_full_2026-10-18.json`, `shortlist_new_s2_2026-10-18.json`). Los nombres se dejaron como los indexa la fuente (iniciales cuando da iniciales).
"Resumen" = leí el resumen que devuelve la API. "Leer" = falta que el autor abra el paper.

| Clave | Qué se afirma en el texto | Qué dice la fuente (resumen) | Resumen | Leer yo |
|---|---|---|---|---|
| Kitano2019 | La densidad de plantas determina el rendimiento y medirla en campo es impráctica por la mano de obra; conteo de maíz con UAV | Lo dice el resumen | Sí | [ ] |
| Osco2021 | Conteo de plantas y detección de hileras desde UAV (maizal entre los casos) | Resumen: CNN que detecta hileras y cuenta plantas; evaluado en maizal | Sí | [ ] |
| Machefer2020 | Conteo de papa y lechuga con Mask R-CNN | Resumen: conteo y medida de plantas, cultivos de baja densidad (papa, lechuga) | Sí | [ ] |
| Feng2025 | Conteo de plántulas de maíz con YOLOv8n ligero en tiempo real | Título y resumen | Sí | [ ] |
| Shiu2023 | Faster R-CNN ubica y cuenta frutos maduros de piña en UAV | Resumen | Sí | [ ] |
| Lai2023 | YOLOv7 mejorado detecta piñas en el campo (estimación temprana del rendimiento) | Resumen | Sí | [ ] |
| Osco2021Review, Kamilaris2018 | El deep learning con UAV es común en agricultura de precisión | Osco: 232 artículos; "UAV-based applications have dominated aerial sensing research". Kamilaris: encuesta (sin resumen devuelto por la API) | Parcial (Kamilaris sin resumen) | [ ] |
| Viola2001, Dalal2005, Girshick2014, Ren2017, Redmon2016 | Historia de la detección: rasgos manuales, R-CNN, Faster R-CNN (propuestas casi gratis), YOLO en tiempo real | Clásicos; metadatos comprobados | Metadatos | [ ] |
| Tang2024, Shafiee2017 | Variantes de YOLO adaptadas a imágenes aéreas y a hardware embebido | Tang: encuesta de detección para UAV. Shafiee: título "Real-time Embedded" | Sí | [ ] |
| Lempitsky2010, Ayalew2020 | Conteo por mapa de densidad, también en plantas | Ayalew: estimación de mapas de densidad para conteo | Ayalew sí; Lempitsky solo título | [ ] |
| Bumbaca2025 | Modelos entrenados fuera de dominio no alcanzaron conteo aceptable; 60 a 130 imágenes en dominio bastaron (maíz) | Resumen | Sí | [ ] |
| Bah2018 | Anotar pixel a pixel por un experto es extremadamente lento | Resumen | Sí | [ ] |
| Cai2022 | Falta de datos por el etiquetado manual es un cuello de botella para detectar y contar panículas de sorgo; GANs mejoran | Resumen | Sí | [ ] |
| Muhammad2023, Hirahara2025, Fang2024, Deng2023, Bernardo2023 | Imágenes sintéticas (difusión/GAN) para aumentar datos de detección; en UAV embebido con datos sintéticos | Resúmenes leídos. Deng: "promising results for certain classes" | Sí | [ ] |
| XieLi2024 | Detección de piñas sin entrenamiento, con datos etiquetados escasos y caros | Resumen | Sí | [ ] |

Resuelto el 18-oct con Crossref: `Hirahara2025` (Comput. Electron. Agric. 230, 109849, DOI 10.1016/j.compag.2024.109849) y los 3 autores de `Feng2025` (Pengbo Feng, Zhigang Nie, Guang Li; Front. Plant Sci. 16, 1639533). Pendiente: `Tang2024` aparece como 2023 en Semantic Scholar pero el DOI (rs16) es del volumen 2024.

## Referencias del marco teórico: actualización 18-oct-2026
Verificadas en Semantic Scholar (por arXiv): Paszke2019 (NeurIPS 2019), Kingma2015 (ICLR), Loshchilov2019 (arXiv 1711.05101, publicado en ICLR 2019 como "Decoupled Weight Decay Regularization"), Loshchilov2017 (SGDR, ICLR 2017), He2016 (CVPR), Wu2018 (Group Normalization; ECCV 2018, versión extendida en IJCV), Ronneberger2015 (MICCAI). Sin verificar aún: Goodfellow2016, Rumelhart1986, LeCun1998, Higgins2017.
También verificadas por Semantic Scholar las candidatas del Related Work: 2406.11713 (Latent Denoising Diffusion GAN, IEEE Access 2024), 2512.16636 (REGLUE), 2309.15807 (Emu), 2603.27519 (SPROUT), 2405.04717 (Remote Diffusion), 2507.09984 (LDMAE, ICCV-W/2025), 2506.13307 (ISPRS J. 2025), 2605.07915, 2602.08620, 2508.00413 (DC-AE 1.5). Los resúmenes de estas candidatas aún no se leyeron: siguen "por verificar" antes de citarlas.


## Repetición de S1 a S5 en Semantic Scholar (18-oct-2026)
Script: `docs/s2/s2_screening.py` (búsqueda masiva booleana sobre título y resumen, desde 2022). Detalle por registro: `docs/s2/screening_s2_2026-10-18.csv`; cifras: `screening_s2_2026-10-18_summary.json`.
Los criterios C1 a C3 se reimplementaron como reglas de palabras clave a partir de su definición escrita (el script de arXiv no se conservó). C3 se aplicó como "pocos datos O dominio aéreo/agrícola/médico" sin separar.

| Cadena | Semantic Scholar | arXiv (11-oct) |
|---|---|---|
| S1 | 48 | 30 |
| S2 | 123 | 73 |
| S3 | 18 | 9 |
| S4 | 79 | 47 |
| S5 | 8 | 7 |

244 registros únicos (137 ya estaban en arXiv, 107 nuevos); 112 cumplen C1 y C2; 49 cumplen además C3 o dominio (arXiv: 34 y 4; la regla de C3 de esta vez es más amplia, por eso la diferencia).
Revisé los 49 títulos y los resúmenes de los más cercanos. 44 son aplicaciones médicas o biomédicas; 5 son de otros dominios (espectros hiperespectrales de suelo, espectros de calidad del agua, datos de ingeniería, difusión de formas de onda, generación de imágenes de teledetección).

Los más cercanos a la pregunta de revisión (ninguno la responde):
- `Fallah2026` (J. Imaging, DOI 10.3390/jimaging12090426): VAE 256x256 a 32x32x8 + difusión latente con 295 participantes; una ablación controlada que varía solo el preprocesamiento mejoró KID en 0.0147 (FID no separó las configuraciones). Es un tratamiento de datos con pocos datos, pero en MRI, un solo tratamiento y sin cambios estructurales del VAE.
- `Dombrowski2026` (arXiv 2605.17087): la estructura del latente de autoencoders preentrenados, no su fidelidad, limita la utilidad de imágenes médicas sintéticas. Médico, datos grandes preentrenados.
- OmniRSI (arXiv 2610.15414): generación multimodal de teledetección con un VAE propio, 11.5 M de imágenes. No se cita; es gran escala.

Consecuencia para la afirmación de novedad: sigue en pie para la combinación (tratamientos de datos + modificaciones del VAE + régimen aéreo, agrícola y multimodal con pocos datos), pero NO se puede decir que el efecto de un tratamiento de datos sobre la generación con pocos datos nunca se midió (Fallah2026 lo hizo en MRI).
Pendiente: abrir y leer Fallah2026 y Dombrowski2026.

`Page2021` (PRISMA 2020, BMJ 2021, n71): metadatos comprobados en Crossref el 18-oct-2026.


## Papers del grupo leídos el 18-oct-2026 (PDF)
- `XieLi2025VAE` (BIP 2025, 6 páginas; PDF en OneDrive/Maestria/Tesis/Papers): compara beta-VAE (beta = 0, 0.001, 0.1, 1, 10) y VQ-VAE (codebook 128/256, dimensión 64/128) con unas 4 000 imágenes de Upala Agrícola (1920x1080, vista cenital de 90 grados, reducidas a 256x256), validación cruzada de 5 pliegues, 400 épocas, lote 4, Adam 1e-4. Mide reconstrucción (FD, precision, recall, autenticidad, SSIM) y separación de plantas y fondo en el latente (PCA + t-SNE). Resultado: un beta intermedio (0.001) da el mejor balance; el VQ-VAE separa bien fondo y plantas. Un VAE preentrenado de difusión latente generaliza mal (FD 1159.9). NO evalúa generación. El README de su repositorio pide citarlo a quien use el dataset. No cambia la afirmación de novedad, que es sobre generación.
- `Gonzalez2026` y `XieLi2025VAE` describen la misma colección de grabaciones (Upala Agrícola, vista cenital, 2 m). Nuestro `.h5` (cuadros 1920x1088, colección "vertical") es consistente con eso; falta confirmar con el asesor que es exactamente el mismo subconjunto.
- `XieLi2025PineSORT` (CVPRW 2025): seguimiento de piñas en video de drone para estimar rendimiento, validado con 5 pliegues frente a BoTSORT y AgriSORT; resumen leído.


## Estado del arte (Related Work) y publicaciones del profe, 18-oct-2026 (noche)
Metadatos comprobados en Semantic Scholar (nombres como los indexa la fuente); resúmenes leídos de la API. Búsquedas en `docs/s2/` (`fm_refs`, `advisor_papers`, `fm_absence_queries`).
| Clave | Qué se afirma en el texto | Fuente (resumen) |
|---|---|---|
| Lipman2023, Liu2023 | Flow Matching: regresión de campos de vectores de caminos fijos, más robusto y estable con caminos de difusión; rectified flow: trayectorias rectas, modelos eficientes | Resúmenes |
| Esser2024, Ma2024 | A gran escala, rectified flow supera a formulaciones de difusión en texto a imagen; SiT supera a DiT con la misma arquitectura | Resúmenes |
| Song2021 | DDIM: mismo entrenamiento, muestreo 10 a 50 veces más rápido | Resumen |
| Kong2026 (AgriUFM) | Flow Matching para pares imagen-máscara de plagas y enfermedades: menor FID que GAN y difusión en 4 datasets, mejora la segmentación | Resumen. No es imagen aérea |
| Lee2025LDMAE, Chen2025, He2022 | LDMAE: propiedades de un autoencoder para LDM; MAETok: forma variacional no necesaria; MAE: enmascarar 75% | Resúmenes |
| Fallas2023, Gonzalez2023MS, Fallas2026Count, Fallas2025Pseudo | Publicaciones del profe: detección en piña con pocos ejemplos y SAM; multiespectral con fusión temprana; conteo con modelos fundacionales y 5 a 10 imágenes; calidad de pseudoetiquetas | Resúmenes |
| Wang2004 | SSIM | Metadatos; sin resumen en la API |
No se citaron (resumen no confirma lo que se creía): REGLUE (el resumen no habla del peso de KL) y Latent Denoising Diffusion GAN (resumen truncado, no confirma lo del GAN sin KL). Las dos candidatas quedan descartadas hasta leer el paper.
Búsquedas de ausencia: 4 consultas de Flow Matching con agricultura, pocos datos e imágenes aéreas; solo apareció AgriUFM. Registradas en c2.tex (Complementary searches).

## Referencias del marco teórico: verificación final (20-oct-2026)
Rumelhart1986 (Nature 323(6088):533-536, 1986; DOI 10.1038/323533a0) y LeCun1998 (Proc. IEEE 86(11):2278-2324, 1998; DOI 10.1109/5.726791): comprobadas en Crossref; se agregaron DOI y número. Higgins2017 (beta-VAE, ICLR 2017; 8 autores): comprobada en Semantic Scholar. Goodfellow2016 (libro, MIT Press, 2016): autores, editorial y año corroborados por una reseña que lo cita en Semantic Scholar; es un libro, sin DOI. Quedan todas las referencias del documento con metadatos verificados. Pendiente de la verificación de metadatos de Paszke2019, Kingma2015, Loshchilov2019, Loshchilov2017, He2016, Wu2018, Ronneberger2015: ya verificadas el 18-oct en Semantic Scholar.
