# Mapa de afirmaciones a fuentes (capítulo II, sección Problem)

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
