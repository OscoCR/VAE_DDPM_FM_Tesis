# Hoja de defensa: las referencias principales

Para repasar antes de hablar de la propuesta. Son las 12 referencias más citadas; las otras 72 son datos puntuales.
Estado de la verificación: los datos bibliográficos (autores, año, revista) están confirmados en Crossref o Semantic Scholar. La columna «qué dice» sale de lo que afirma la tesis con cada una; solo la tabla I de Xie y Li (2025) se contrastó con el texto completo. Lo demás conviene confirmarlo leyendo el resumen y las conclusiones de cada artículo (unos 10 minutos cada uno).

## El núcleo del grupo (lo más importante)

| Referencia | Qué es | Qué afirma la tesis con ella | Dónde |
|---|---|---|---|
| **González et al. (2026)**, GECCO. «Peeling Back the Pixels» | Trabajo del grupo sobre difusión latente con pocos datos de piña | Un VAE continuo conservó la estructura de un campo de piña donde uno discreto falló. Mide la generación (FD). Es el trabajo más cercano. Se cita 21 veces. | Cap. I, II (tabla de posición), IV (datos) |
| **Xie-Li et al. (2025)**, conferencia IEEE | Estudio de variantes de VAE en campos agrícolas | Compara β-VAE y VQ-VAE con unos 4 000 cuadros de piña y mide reconstrucción y estructura del latente, no la generación. Un β intermedio dio el mejor balance (de ahí β = 0.001). Un VAE preentrenado obtuvo precisión 0.05 frente a 0.7–0.8 de los entrenados con esas imágenes. **Verificado contra la tabla I.** | Cap. I, II, IV |
| **Fallah y Herzog (2026)**, J. Imaging | Difusión latente condicional para resonancias de cerebro con pocos datos | Cohorte médica pequeña; varía el preprocesamiento y mide la generación (FID, KID). | Cap. II (tabla de posición) |

## La idea central: reconstruir mejor no garantiza generar mejor

| Referencia | Qué es | Qué afirma la tesis con ella |
|---|---|---|
| **Yao et al. (2025)**, CVPR. «Reconstruction vs. Generation» | Dilema de optimización en difusión latente | Una mejor reconstrucción no garantiza una mejor generación. Es el respaldo de tu indicio preliminar. |
| **Zhong et al. (2026)**, «Diffusing in the Right Space» | Estudio sistemático de qué tan «difundible» es un espacio latente | Más canales mejoran la reconstrucción pero exigen difusores más grandes. Una mejor reconstrucción no implica una mejor generación. |
| **Skorokhodov et al. (2025)**, ICML. «Improving the Diffusability of Autoencoders» | Contenido de alta frecuencia del latente | Los espacios latentes con exceso de alta frecuencia dificultan la difusión. |
| **Sehwag et al. (2025)**, CVPR. «Stretching Each Dollar» | Entrenar difusión con presupuesto mínimo | Varía la dimensión del latente con un benchmark grande. Aparece en la tabla de posición. |
| **Chen et al. (2025)**, ICML. «Masked Autoencoders Are Effective Tokenizers» | Enmascarado para entrenar tokenizadores de difusión | El enmascarado se ha usado para entrenar tokenizadores; la forma variacional del autoencoder no sería necesaria. Respalda el factor B. |

## Base técnica y contexto agrícola

| Referencia | Qué es | Qué afirma la tesis con ella |
|---|---|---|
| **Rombach et al. (2022)**, CVPR | Modelos de difusión latente | Separan compresión y generación: el autoencoder fija el techo de lo que el generador puede aprender. |
| **Cai et al. (2022)**, CVPR Workshops | Imágenes de dron generadas para detectar panículas de sorgo | Imágenes generadas con GAN mejoraron la detección y el conteo en imágenes de dron. |
| **Hu et al. (2025)**, revisión | Modelos de difusión en agricultura inteligente | La escasez de datos anotados es un problema recurrente y la difusión se ha revisado como respuesta. |
| **Kong et al. (2026)**, Agriculture. «AgriUFM» | Flow Matching para pares imagen-máscara agrícolas | Un modelo FM alcanzó un FID menor que GAN y difusión en cuatro conjuntos y mejoró la segmentación. |

## Preguntas que pueden hacerte, y respuestas que son ciertas

- **«¿Leyó todo esto?»** Responde solo con lo que es verdad. Por ejemplo: «La literatura la encontré con una búsqueda documentada (sección 2.3.7). Conozco bien las referencias del núcleo, y el resto lo uso para datos puntuales.» Si alguna no la leíste completa, dilo tal cual.
- **«¿Por qué tantas referencias?»** 71 de las 84 están en el Capítulo II, que es el marco teórico y los trabajos relacionados. 45 se citan una sola vez, cada una para un dato concreto. El núcleo es pequeño: González et al. (21 veces), Xie-Li (10) y Fallah (7).
- **«¿Cómo buscó la literatura?»** Con dos fuentes, arXiv (11 de octubre de 2026) y Semantic Scholar (18 de octubre de 2026), cinco cadenas de búsqueda, desde 2022. El cribado fue por palabras clave. La tesis declara esas limitaciones.
- **«¿Usó IA?»** Sí, y está declarado en la última página: para redactar y mejorar el texto, buscar literatura y verificar datos bibliográficos, revisar el código, comparar alternativas de diseño y generar los diagramas con scripts. Las decisiones y la responsabilidad del contenido, incluidas las referencias, son del autor.

## Lo que falta de tu parte (honesto)

1. Lee el resumen y las conclusiones de las 12 de arriba, empezando por González et al. y Xie-Li. Tómate unos 10 minutos cada una.
2. Para cada una, escribe en una línea qué dice con tus propias palabras. Si no puedes, léela otra vez.
3. Para las otras 72: sabe para qué dato concreto la citas, mirando la frase donde aparece.
