# Lista de verificación de integridad (propuesta de tesis, entrega 23-oct-2026)

Estado: [x] hecho y verificado, [ ] pendiente, [~] parcial.
Última actualización: 18-oct-2026.

## A. Uso de herramientas de IA
- [ ] Preguntar al asesor (reunión del lunes 12-oct) qué se permite en la propuesta y cómo se declara.
- [ ] Incluir la declaración de uso de herramientas de IA al final del documento (borrador abajo; ajustar a lo que diga el asesor).
- [ ] Poder explicar con mis palabras cada sección (ver C).

Borrador de declaración (ajustar):
> Se utilizó un asistente de inteligencia artificial (Claude, de Anthropic) para: organizar y redactar borradores del texto, buscar y resumir literatura, verificar metadatos bibliográficos y revisar el código de entrenamiento. Las decisiones de investigación (pregunta, hipótesis, objetivos, diseño experimental y alcance), los experimentos y el análisis de resultados fueron realizados por el autor, quien revisó y es responsable de todo el contenido.

## B. Citas (clave de `biblio.bib`): qué verificar y leer
Leyenda: Meta = autores, título y año verificados en arXiv; Resumen = se leyó el resumen oficial; Leer = falta abrir el paper y confirmar lo que se cita.

| Clave | Meta | Resumen | Leer yo |
|---|---|---|---|
| Rombach2022, Yao2025, Skorokhodov2025, Zhong2026, Zheng2025, Hu2025, Krishnan2025, Chen2025, He2022 | [x] | [x] | [x] leídos por el autor (11-oct) |
| Sehwag2025 | [x] | [x] (sección 6.2 leída) | [x] leído por el autor |
| Gonzalez2026 (paper del grupo) | [x] | [x] (texto leído) | [x] leído por el autor |
| Kingma2014, vandenOord2017, Ho2020, Lipman2023, Goodfellow2014, Isola2017, Heusel2017, Binkowski2018 | [x] | n/a (clásicos) | [x] leídos por el autor |
| Paszke2019, Kingma2015, Loshchilov2019, Loshchilov2017, He2016, Wu2018, Ronneberger2015 | [x] verificados en Semantic Scholar (18-oct) | n/a | [ ] |
| Goodfellow2016, Rumelhart1986, LeCun1998, Higgins2017 | [ ] confirmar en editorial | n/a | [ ] |

- [ ] Confirmar las sedes (ICLR, NeurIPS, CVPR, ICML, ICCV) de todas las entradas.
- [ ] Reemplazar la versión de arXiv por la publicada donde exista.
- [ ] Confirmar el venue de Chen2025 (ICML 2025).

## C. Escritura con mi propia voz
- [x] Problem: revisado oración por oración (oraciones 7, 9, 15 y "by hand" reescritas con el autor).
- [x] Hypothesis y Objectives: formulados con el autor (verbos de Bloom, "tratamientos", VAE).
- [~] Background: leído por el autor; falta la reescritura con su voz si algo no le suena.
- [ ] Related Work (estado del arte): por escribir.
- [ ] Metodología y diseño de experimentos: por escribir.
- [ ] Resultados iniciales: por escribir (hay datos).
- [ ] Plan de trabajo y abstract: por escribir.

## D. Números que aparecen en el texto: verificados contra el código o los datos
- [x] 4,908 imágenes de 960x544 (atributos del archivo .h5; fuente original 1920x1088).
- [x] Divisiones: 3,536 entrenamiento, 381 validación, 346 prueba (columna `split` del .h5; las 645 marcadas `drop` se excluyen).
- [x] Profundidad monocular relativa, normalizada por imagen (atributo `depth_semantics` del .h5).
- [x] Latente 4x32x32 para recortes de 256x256.
- [x] beta = 0.001 (`kl_beta` en los configs del VAE).
- [x] lambda = 0.01 (`adv_weight` en la configuración y en `train_step`).
- [x] Tamaño de lote 8 (`batch_size` en los configs).
- [x] DDPM con 1000 pasos de entrenamiento (`models/ddpm.py`) y 1000 de muestreo en la evaluación; Flow Matching con 50 pasos de Euler.
- [x] FID y KID con 400 imágenes generadas y un conjunto de referencia fijo.
- [x] Unas 26 horas de GPU por entrenamiento de generador (25 h 09 min a 26 h 39 min en las corridas v2). Corregido en el texto (antes decía 28).
- [x] Tabla de FID/KID de las corridas: salida de `compare_v2_augall` (20:11 del 11-oct).
- [~] Frases del texto con "se ha estudiado con datos grandes": respaldadas por los resúmenes (ver mapa de fuentes), falta leer los papers.

## E. Compilación y formato
- [ ] Compilar en Overleaf y corregir errores (el capítulo I, con ecuaciones y la figura PRISMA, no se ha compilado nunca).
- [ ] Decidir el idioma con el asesor (la plantilla y la propuesta de Danny están en inglés).
- [ ] Revisar la portada (el nombre del curso se asumió de la portada de Danny).

## F. Preguntas para el asesor (lunes 12-oct)
1. Idioma de la entrega y política de uso de IA.
2. Extensión esperada y formato de citas.
3. Hipótesis y alcance: dos hipótesis (mejora y límite), DINO y enmascarado como parte del trabajo.
4. Hallazgo del scheduler de LR del repositorio base: ¿era intencional? (resumen en `resumen_profesor_bug_LR.md`).
5. Propuesta de medir propiedades del latente (alta frecuencia, suavidad): ¿le parece una línea útil?

## G. Cronograma hasta el 23
| Fecha | Qué |
|---|---|
| 12-oct | Reunión con el asesor; compilar |
| 13-16 | Metodología, diseño de experimentos y resultados iniciales |
| 17-19 | Estado del arte |
| 20-21 | Plan de trabajo, abstract, reescritura propia |
| 22 | Revisión completa y verificación de citas |
| 23 | Entrega |


## H. Versiones del documento
- [ ] v1 para retroalimentación del asesor: congelar el estado actual (commit con etiqueta `v1-feedback` y PDF compilado en Overleaf).
- [ ] Registrar los cambios que pida el asesor y aplicarlos en v2.

## E. Background ampliado (18-oct-2026)
- [x] Nuevas subsecciones: motivación (conteo con UAV), detección clásica y YOLO, problema de los datos, imágenes sintéticas, línea del grupo.
- [x] 26 referencias nuevas en `biblio.bib`; metadatos comprobados en Semantic Scholar y nombres tal como los indexa la fuente.
- [x] Búsqueda complementaria registrada: `docs/s2/topic_search_s2_2026-10-18.csv` (14 consultas) y descrita en "Complementary searches" de c1.tex.
- [ ] Leer los papers nuevos (columna "Leer yo" en `literature_map.md`) y confirmar cada afirmación.
- [x] Propuestas de otros compañeros (Fernando, Martín, general): no se citan, no tienen que ver con la tesis. Solo se cita la línea de Danny, Gonzalez y Fabián (XieLi2024, Gonzalez2026).
- [x] Búsqueda de novedad (S1 a S5) repetida en Semantic Scholar (18-oct): texto y tabla en c1.tex; datos en `docs/s2/`.
- [ ] Leer los resúmenes de los 49 registros que cumplen C1, C2 y C3 (`screening_s2_2026-10-18.csv`, filtrar C1=C2=1 y C3) y confirmar que ninguno responde la pregunta; leer Fallah2026 y Dombrowski2026.
- [ ] Decidir si se menciona Fallah2026 en el Problem de c2.tex (hoy la frase de novedad dice que 'no se ha estudiado' en el régimen de pocos datos homogéneos y multimodales: sigue siendo cierta, pero un jurado puede citar a Fallah).

## F. Cambios del 18-oct (tarde)
- [x] Hipótesis única (la de "Mejora"), por pedido del asesor; el límite de rendimientos pasó a RQ3 como análisis exploratorio. Borrador v1 en c2.tex, por pulir con el asesor.
- [x] Oración sobre Fallah y Herzog agregada al Problem (c2.tex).
- [x] Introducción seccionada: 1.1 Background and Motivation, 1.2 Theoretical Framework, 1.3 Related Work (c1.tex).
- [x] Figura PRISMA nueva con dos fuentes (`Imagenes/prisma_flow.png`, script `docs/s2/draw_prisma.py`); cifras en `docs/s2/prisma_combined_numbers.json`.
- [x] PRISMA 2020 citado (`Page2021`, metadatos de Crossref). El texto dice que se sigue solo para reportar el flujo; no es revisión sistemática completa.
- [x] Quitada la frase sobre conteo en tiempo real a bordo (la línea del grupo, Danny, procesa fuera de línea).
- [x] Capítulos separados como Danny (19-oct): I Introduction (c1, nueva y corta), II Background and State of the Art (c2), III Hypothesis and Objectives (c3), IV Research Proposal (c4, vacío), V Initial Results (c5, esqueleto), VI Workplan (c6, vacío). `General.tex` incluye c1 a c6.
- [ ] Revisar con el asesor si la hipótesis debe nombrar solo 4 factores (aumento, enmascarado, capa variacional, GAN) o los 6 actuales (con selección y modalidad).

## G. Dataset y papers del grupo (18-oct, noche)
- [x] Paper BIP 2025 leído: no evalúa generación; respalda beta = 0.001; describe la colección (Upala Agrícola, vista cenital, 2 m).
- [x] Procedencia del dataset descrita en c4.tex con cita a Gonzalez2026 y XieLi2025VAE.
- [ ] Confirmar con el asesor que nuestro `.h5` es exactamente el mismo subconjunto (quién armó el `.h5` y con qué grabaciones).

## H. Capítulo IV escrito (18-oct, noche): decisiones tomadas por defecto, por confirmar
- [x] c4.tex: dataset, pipeline, factores A-F, parámetros fijos, evaluación, etapas 0 a 3, diseño 2^(6-2) resolución IV (E=ABC, F=BCD; I=ABCE=BCDF=ADEF), análisis, presupuesto, amenazas. Alias y poder verificados por cálculo.
- [ ] Confirmar: nivel del enmascarado (25%), punto de partida común (VAE RGB-D), etapa 0 con 5 réplicas de la celda base, margen de equivalencia provisional de 5 puntos de FID, 3 semillas por celda.
- [ ] Código pendiente: interruptor "sin capa variacional" (decoder determinista) y semillas distintas por réplica (hoy seed 42 fijo).
- [ ] Preguntar al asesor si el FID de 400 imágenes es suficiente o conviene generar más.

## I. Decisiones del 18-oct (noche) confirmadas por el usuario
- [x] Enmascarado en el tamizaje: 50% (25% y 0 en la etapa 2). [x] Todo desde cero (Tesis II: no reciclar nada de lo preliminar); épocas fijas del VAE (~100) a confirmar en la etapa 0. [x] 3 semillas por celda, justificadas por análisis de potencia.
- [x] Citas agregadas: Colas2018 (cuántas semillas, potencia), Bouthillier2021 (varianza en benchmarks), Agarwal2021 (pocas corridas), Hurlbert1984 (pseudorreplicación), Chong2020 (sesgo del FID).
- [ ] Leer Colas2018 y Chong2020 completos antes de la defensa. [ ] Decidir si se usa FID infinito (extrapolado) además de KID.

## J. Plan de trabajo escrito (18-oct, noche)
- [x] c6.tex: tareas (propuesta, código, etapas 0 a 3, extensión y escritura) y cronograma de ~26 semanas con cómputo por fase.
- [x] Plan de 6 meses (26 semanas, sin fechas) con Gantt suave (`Imagenes/gantt_workplan.png`, script `docs/s2/draw_gantt.py`); intercambio en Osnabrück como opcional (semanas 18 a 21).
- [ ] Compilar TODO en Overleaf (nunca se ha compilado) y corregir errores de LaTeX.

## K. Estado del arte y figuras (18-oct, noche)
- [x] Related Work escrito (~1 050 palabras, 5 subsecciones + tabla de posicionamiento) con Flow Matching y publicaciones del asesor.
- [x] Figura del pipeline (`Imagenes/pipeline_diagram.png`, script `docs/s2/draw_pipeline.py`); PSNR y SSIM definidos con ecuaciones en c4.tex.
- [ ] (Usuario) Verificar las referencias del marco teórico sin confirmar (Goodfellow2016, Rumelhart1986, LeCun1998, Higgins2017) y compilar, al terminar todo.
- [ ] Contexto aplicado en la Introducción (país, proyecto): pospuesto por el usuario.
- [ ] Resumen y conclusiones: pendientes. Muestras del dataset como figura: pendiente.
- [ ] Leer los papers del estado del arte antes de la defensa (Esser2024, Ma2024, Kong2026, Lee2025LDMAE, Chen2025 y los del profe).
