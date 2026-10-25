# Registro de comentarios del asesor (primera revisión, 21-oct-2026; leídos en Overleaf el 24-oct-2026)

Método acordado: se revisa comentario por comentario, archivo por archivo, decidiendo juntos antes de cambiar el texto. Después se atienden las otras mejoras.
Fuente: panel de revisión de Overleaf (Overview y comentarios resueltos), leído en solo lectura; no se resolvió ni se cambió nada allí. Textos copiados tal cual.
Conteo (confirmado por el usuario): 25 entradas abiertas (c1: 5, c2: 2, c3: 13, c4: 3, c5: 2) + 1 resuelta (abstract). De las 13 de c3, 3 son un cambio con control de cambios (objetivo 5) y 1 es una nota dentro del texto.

## abstract.tex (1, resuelta por el usuario el 24-oct)
A1. "no me parece adecuado empezar el abstract dando énfasis a algo que tu no resuelves... la primera oración debería ser relacionada a image generation más que counting (que no es el énfasis de tu tesis)"
   - Decisión: abrir con generación de imágenes sintéticas en agricultura de precisión (versión 2 elegida por el usuario); el conteo queda como aplicación posterior; "seldom examined when data are few and homogeneous".
   - Estado: RESUELTO en el repositorio local (abstract.tex). El PDF de Overleaf todavía muestra el resumen viejo hasta que se suba el cambio.

## c1.tex (Introducción), 5 entradas
C1-1. "El problema de la escasez de datos es clara, pero la conexión con la generación de imágenes sintéticas requiere una mayor justificación... el porqué la generación de imágenes es útil... tenemos que decirle al lector que tu contribución es de suma importancia y que el lector se identifica con la utilidad de la tesis."
C1-2. "La introducción explica las ventajas de la latent diffusion, pero debería dejar más claro por qué el VAE es un componente fundamental que influye en la calidad de la generación, especialmente cuando los datos de entrenamiento son limitados! hay que ahondar más en esta explicación y que genere "excitement""
C1-3. "La contribución propuesta debe ser más explícita. ¿El objetivo es simplemente identificar la mejor configuración de un VAE, o bien comprender cómo los distintos tratamientos de los datos y las modificaciones estructurales influyen en el rendimiento generativo? Esto último daría a entender una contribución científica más sólida y robusta!!!"
C1-4. "Mencionas que los resultados preliminares muestran una variabilidad considerable entre los puntos de control. ¿Podrías explicar por qué esto es importante? Por ejemplo, ¿significa esto que una mejora aparente derivada de una modificación en el VAE podría deberse, sencillamente, a la variabilidad durante el entrenamiento, en lugar de a la modificación en sí misma? Hacer explícita esta relación ayuda a justificar el uso de múltiples ejecuciones experimentales.... también acá puedes hablar de experimentos futuros (no extendiéndote mucho eso si)"
C1-5. (Nota agregada en el texto) "%Me parece que con lo que comentaba anteriormente, le falta profundidad a la intro!"

## c2.tex (Antecedentes y estado del arte), 2 entradas
C2-1. "Sugiero acomodar mejor esta sección. Dado que la tesis se centra en la generación de imágenes (y no en la detección de objetos), no resulta necesaria iniciar con object detection, primero empezar con generación y luego OD, además la parte de OD puede ser mucho más corta! por la misma razón que indico al inicio."
C2-2. "Los ejemplos son buenos, pero sugiero abordar las limitaciones de la generación de datos sintéticos (hacer más énfasis en las limitantes). En particular, ¿pueden los modelos generativos entrenados con conjuntos de datos pequeños y homogéneos producir una diversidad significativa, o acaso se limitan a reproducir la variabilidad restringida de los datos originales? Esta cuestión es directamente relevante para la motivación de su tesis!!!! y en parte esto motiva la investigación, este GAP de conocimiento"

## c3.tex (Hipótesis y objetivos), 13 entradas
C3-1. (Nota agregada en el texto) "usar cursiva para resaltar el texto de la hipótesis... visiblemente debe resaltar el texto que corresponde solamente a la hipótesis! no sé, cursive, centrada" + "la hipótesis debe estar en un solo párrafo, es más claro, yo asumo que los demás párrafos están apoyando lo que dice la hipótesis!"
   - Estado: formato aplicado localmente (cursiva, centrada, un párrafo); falta confirmar.
C3-2. "Sugiero reconsiderar la escritura. Actualmente, esta asume que al menos 1 modificación (treatment) mejorará la calidad de la generación. Peroooooo, ¿no sería científicamente más relevante investigar si estas modificaciones afectan a la calidad de la generación (y de qué manera lo hacen), incluyendo los posibles efectos negativos? (que hemos visto preliminarmente algunos). Esto permitiría que la investigación se centrara menos en encontrar una mejora y más en comprender la influencia del diseño del VAE. ¿No sé si me explico bien?"
C3-3. "poner el acrónimo entero (variational auto encoder), porque muchos lectores vienen directo a la hipótesis"
C3-4, C3-5, C3-6. "same: poner el acrónimo entero" (tres veces; otros acrónimos de la hipótesis y objetivos)
C3-7. "rewrite" (sin más texto; ubicar a qué fragmento apunta)
C3-8. "Parece haber una inconsistencia entre la hipótesis y este objetivo. La regularización se incluye aquí como una modificación estructural, pero no se contempla explícitamente entre los factores experimentales descritos en la sección de hipótesis. hay que aclarar si la regularización es un factor experimental independiente o un componente fijo del VAE a explorar"
C3-9. (Cambio del asesor, objetivo 5, tres entradas) "experiment" -> "explore"; "with" -> "the feasibility of using"; agregado "representation for image generation under limited training data, and to compare its performance witht the VAE baseline" (typo "witht" corregido localmente).
C3-10. "no me gusta mucho tantas preguntas de investigación... las preguntas de investigación motivan la hipótesis y no al revés! Entonces, yo me dejaría las preguntas que realmente estén conectadas con la hipótesis... en los objetivos las exploraciones adicionales son suficiente de mencionar ahí"
C3-11. "esto es cierto, pero suavizar este constraint! ¿a qué me refiero? decir que es un dataset pero meter la justificación de porqué este dataset es interesante, porqué a esa altura, porqué vale la pena, etc, etc"

## c4.tex (Metodología y diseño), 3 entradas
C4-1. "justificar el uso de 400 imágenes, ¿Por qué 400?"
C4-2. "¿Por qué solo 3 réplicas? no sería mejor aumentar este número?"
C4-3. "justificar por qué estas métricas son suficientes en la exploración de este problema!"

## c5.tex (Resultados iniciales), 2 entradas
C5-1. "¿Se podrían agregar imágenes para soportar este claim?"
C5-2. "yo movería esto a un apéndice"

## Temas que se repiten
- Énfasis en generación de imágenes, no en conteo ni detección: A1, C1-1, C1-5, C2-1.
- Por qué importa el VAE y qué se aporta (comprender, no solo encontrar la mejor configuración): C1-2, C1-3, C3-2.
- Limitaciones de las imágenes sintéticas con pocos datos (¿diversidad real?): C2-2.
- Variabilidad de los puntos de control como motivo de las réplicas: C1-4, C4-2.
- Justificar decisiones de metodología (400 imágenes, 3 réplicas, métricas): C4-1, C4-2, C4-3.
- Coherencia hipótesis-objetivos-preguntas, y claridad (acrónimos): C3-2 a C3-8, C3-10.

## Conteo confirmado
El usuario contó 25 entradas abiertas en el panel, igual que el registro. Más 1 resuelta (resumen). Orden de trabajo acordado: archivo por archivo (c1, c2, c3, c4, c5).

## Decisiones tomadas (24-oct-2026)
- C1-3: la contribución se redacta con el verbo "characterize" (no "understand": promete un porqué que el diseño no da). Versión elegida por el usuario (A): "The contribution of this work is to characterize, with replicated experiments, the effect that the treatments of the training data of a variational autoencoder and the modifications of its structure have on the quality of the images generated with latent diffusion, in a regime of few and homogeneous data, estimating its direction, size, and interactions, and identifying which of these effects are favorable, which are harmful, and which are negligible." Opcional: "Explaining the mechanisms behind these effects is left as future work."
- Respaldo en el comentario del asesor: C3-2 pide incluir "los posibles efectos negativos" ("que hemos visto preliminarmente algunos"); C1-4 pide explicar que una mejora aparente puede ser variabilidad.
- Pendiente de decidir: hipótesis no direccional (C3-2) con acrónimos completos (C3-3 a C3-6), y su criterio de apoyo/refutación (refutada si todos los efectos son equivalentes a cero dentro del margen).

## Pregunta para el asesor (pendiente de enviar), sobre C3-2 "y de qué manera lo hacen"
Dos lecturas: (1) dirección, tamaño e interacciones de los efectos (lo que entrega el diseño factorial: 6 factores, 48 entrenamientos, ANOVA, equivalencia); (2) mecanismo (por qué), que se atendería con un análisis exploratorio y correlacional de propiedades del latente (suavidad, altas frecuencias, uso de capacidad) y de la diversidad de lo generado (precisión, recall, memorización), que además responde C2-2. Propuesta del usuario: la 1 como núcleo, la 2 como exploratorio si hay tiempo; contribución redactada con "characterize" para no prometer causalidad. Se redactó un correo con contexto (versión larga) y una versión corta para responder en Overleaf.
- Si la respuesta es la lectura 1: contribución A sin cambios.
- Si es la 2: agregar "and explores properties of the latent space and of the diversity of the generated images that may account for these effects", una línea en el diseño (capítulo IV) y en el plan de trabajo (capítulo VI).

## Reinterpretación de C3-2 (24-oct-2026, acordada con el usuario)
Releído frase por frase: "de qué manera lo hacen" va junto a "incluyendo los posibles efectos negativos", así que se refiere a la DIRECCIÓN del efecto (para bien o para mal), no a un mecanismo. El asesor pide pasar de "¿algo mejora?" a "¿cómo influye cada decisión del VAE?", y cierra con "¿no sé si me explico bien?". Lectura adoptada: la lectura 1 (dirección, tamaño, interacciones), que el diseño factorial ya entrega.
- El análisis exploratorio del latente y de la diversidad queda DESCARTADO por ahora (más profundo de lo que se quiere llegar). Costo estimado, por si se pide: sin entrenamientos nuevos, ~2 a 5 h de GPU, ~5 a 7 días de trabajo, ~+20 GB de almacenamiento.
- El "porqué" del VAE (C1-2) se atiende en la Introducción con literatura (el latente fija el techo; reconstrucción no es generación; el VAE pesa más con pocos datos), no con experimentos nuevos.
- Mensaje corto opcional al asesor para confirmar la lectura (WhatsApp).
- (Aclaración del usuario, 24-oct) No se le escribe al asesor para confirmar la lectura de C3-2: se razona y se cambia directamente. La Introducción SÍ necesita cambios.

## Recapitulación del usuario de las ideas del asesor (24-oct-2026), vara para reescribir la Introducción
1. Justificar la importancia de crear o generar imágenes sintéticas.
2. Explicar y resaltar el componente VAE: por qué es importante, por qué es óptimo para generar imágenes sintéticas y por qué realmente un VAE.
3. Recalcar la utilidad y la contribución de la maestría, hacerla atractiva.
4. Relación explícita entre los resultados preliminares y las variantes, para justificar el aporte científico.
5. En general, más profundidad.
Método acordado: se construye la Introducción por pasos de Swales (CARS, 7 pasos) con preguntas del asistente y respuestas del usuario, contrastando cada paso con estos 5 puntos. El asistente no redacta todo de una vez.

## Avance de la reescritura de la Introducción por pasos CARS (24-oct-2026), respuestas del usuario
Paso 1, territorio: gancho = "qué chévere que con pocos datos un VAE aprenda características y luego se generen imágenes no vistas"; beneficiarios: empresas de conteo de cultivos, creación de imágenes de plagas, medicina (mención leve), entrenar modelos con esas imágenes; lo llamativo: generar imágenes de enfermedades poco vistas para diagnóstico. Cuidados: "no vistas" es la promesa, no un hecho (C2-2: ¿diversidad real o copia?); el VAE aprendiendo features con pocos datos es lo que se pone a prueba.
Paso 2, problema: con poca variabilidad no hay buenos resultados; un modelo grande tiene un latente con desajuste de dominio (VAE preentrenado: FD ~1160 en piña, XieLi2025VAE); hoy se reentrenan modelos grandes o se crea un latente desde cero (el VAE); el diseño se decide a mano.
Paso 3, lo que se sabe: Rombach (el latente fija el techo), Yao o Zhong (reconstrucción no es generación), Gonzalez2026 (pocos datos), y una aplicación de imágenes sintéticas (candidatos: Hirahara2025 con +28.65% mAP; Cai2022 UAV y conteo; Fallah2026 para la mención médica, AUC 0.779 sintético contra 0.869 real).
Justificación del VAE (usuario): modelo manipulable, estándar en difusión latente, y conservó la estructura del cultivo (Gonzalez2026). No decir "óptimo".
Alternativas al VAE verificadas: VQ-VAE/VQGAN (falló con pocos datos en piña), RAE con codificadores preentrenados tipo DINO (datos grandes; es el objetivo 5), DC-AE 1.5, MAETok y LDMAE (variantes), difusión en píxeles (cara), GAN (menos estable según Hu2025).
Siguiente: paso 4 (brecha), 5 (propuesta y contribución), 6 (enfoque y alcance), 7 (mapa).

## Contribución y alcance acordados (24-oct-2026)
- La contribución científica es CARACTERIZAR cómo influyen los tratamientos de datos y las modificaciones del VAE (no hallar "los mejores"); encontrar qué conviene es la consecuencia. Beneficio para el lector: saber qué modificaciones valen la pena y cuáles no, dentro de las condiciones estudiadas.
- Alcance: un dataset de piña; otros cultivos o dominios (medicina), comparación sistemática con otros latentes (solo estudio de factibilidad, objetivo 5) y la explicación de mecanismos quedan como trabajo futuro, junto con etiquetar y contar.
- Borrador completo en docs/intro_borrador.tex (8 párrafos, ~930 palabras); c1.tex sin tocar hasta la aprobación final.

## Costa Rica y corrección del párrafo 2 (24-oct-2026)
- Se agrega el contexto de la piña: Castro (Acta Horticulturae 1239, 2019; DOI 10.17660/actahortic.2019.1239.6; resumen leído): más de 40 000 ha y 60 000 a 100 000 plantas por ha. El monitoreo manual: frase del paper del grupo (Gonzalez2026). FALTA agregar la entrada Castro2019 a biblio.bib al aplicar a c1.tex (autor indexado como Z. Castro). Ingwersen 2012 no tiene resumen disponible; no se usa.
- Corrección propia: se retiraron "would depend less on the conditions of a single field" y "without manual annotation": un generador entrenado en un campo reproduce sus condiciones y las imágenes generadas no vienen etiquetadas. Ahora: "could enlarge such datasets ... with more instances of the scenes that the generator has learned ... Whether they add real variety depends on the generator and on the latent space."
- Pendiente: justificar el dataset (altura, interés, por qué vale la pena) en c3/c4 (C3-11).

## Párrafo 3 reordenado (24-oct-2026)
- Cadena: el autoencoder es la base -> en la práctica se usa uno preentrenado (Zheng2025: estrategia estándar) -> con pocos datos no basta (VAE preentrenado: precisión 0.05 en piña; el paper concluye que generaliza mal y necesita fine-tuning, XieLi2025VAE, Tabla I: FD 1159.93, precisión 0.05, recall 0.34, un solo modelo, evaluado sobre reconstrucciones) -> hay que adaptarlo (no necesariamente desde cero) -> su diseño es una decisión con consecuencias (Gonzalez2026) -> no se guía solo por reconstrucción (Yao2025, Zhong2026) -> es estándar y controlable.
- Incluido el número (0.05) por decisión del usuario. Se corrigió "trained from scratch" a "adapted".

## Estado al 24-oct-2026 (tarde)
- ABSTRACT (A1): aplicado y subido (commit "Fix of comment 1"); el usuario ya respondió y resolvió el comentario en Overleaf.
- C3-1 (formato de la hipótesis) y la corrección del objetivo 5: subidos (commit "Fix Hypotesis Estructure"). Falta aún C3-2 (hipótesis no direccional), C3-3 a C3-6 (acrónimos completos), C3-7, C3-8, C3-10, C3-11.
- C1-1, C1-2, C1-3, C1-4 y C1-5: ATENDIDOS en la nueva Introducción (c1.tex, 8 párrafos, ~1 100 palabras). Se agregó Castro2019 a biblio.bib. Pendiente: que el usuario suba los cambios, compile y resuelva los comentarios en Overleaf si el contenido le convence.
- Siguiente archivo: c2.tex (C2-1: empezar por generación y acortar detección; C2-2: limitaciones de los datos sintéticos).

## c2.tex atendido (24-oct-2026, tarde)
- C2-1: la sección "Application Context" se reordenó: 1) Synthetic images from few data (97 palabras, primero), 2) The data problem in agriculture (145), 3) Limits of synthetic images with few data (220, nueva), 4) Plant counting and detection (118; fusión de las dos subsecciones previas, antes 374 palabras; se quitó la historia clásica: Viola-Jones, HOG, R-CNN, Faster R-CNN), 5) Research line of the group (403, sin cambios).
- C2-2: la nueva subsección 3 trata las limitaciones: diversidad (incluye memorización, Dar2024: los modelos de difusión latente memorizan más que autoencoders y GAN), utilidad real (Fallah2026, Deng2023) y etiquetas (Fallas2025Pseudo, Kong2026). Cierra con la pregunta abierta de la diversidad ligada al latente, que motiva la tesis.
- Bibliografía: se agregó Dar2024 (arXiv 2402.01054; nombres como los indexa Semantic Scholar).
- Siguiente: c3.tex (C3-2 hipótesis no direccional; C3-3 a C3-6 acrónimos completos; C3-7 "rewrite" sin ubicar; C3-8 regularización; C3-10 preguntas de investigación; C3-11 justificar el dataset). Después c4 y c5.

## c3.tex: hipótesis y criterio atendidos (24-oct-2026, noche)
- Ancla de C3-7 ("rewrite") confirmada en Overleaf: el párrafo "The hypothesis is supported if...". C3-2 y C3-3 a C3-7 se resolvieron juntos sobre la hipótesis y su criterio.
- C3-2: la hipótesis ya no es direccional. Dice que los tratamientos y modificaciones "have a non-zero effect" sobre FID y KID, y define el efecto como la diferencia respecto del VAE base (puede ser positivo, negativo o cero). Se descartó "favorable or unfavorable" por introducir un juicio de valor (decisión del usuario). El abstract usa la misma redacción.
- C3-3 a C3-6: se desplegaron en la hipótesis variational autoencoder (VAE), Fréchet Inception Distance (FID), Kernel Inception Distance (KID) y Denoising Diffusion Probabilistic Model (DDPM). También en el abstract (se agregó DDPM en el primer uso) y en c1 (DDPM, primer uso).
- C3-7: el criterio ya no exige que el FID baje. Tres desenlaces: apoyada (algún efecto significativo en el FID, con el KID en el mismo sentido), refutada (todos los efectos equivalentes a cero dentro del margen fijado con el ruido de la Etapa 0, pruebas de equivalencia) e inconclusa (ninguno de los dos). Razón: "no significativo" no demuestra ausencia de efecto.
- Regla de FM (pedida por el usuario): "Flow Matching (FM)" se define en el primer uso del abstract, c1, c2 (también en la definición técnica, línea 108), c3 (Problema e hipótesis, forma "Flow Matching, FM" para no anidar paréntesis), c4, c5 y c6. Después se usa FM. Títulos de sección, leyendas, la etiqueta "Stage 3: confirmation with Flow Matching", las keywords y los términos de búsqueda de c2 conservan el nombre completo.
- Pendiente en c3: C3-8 (regularización: factor independiente o componente fijo), C3-10 (preguntas de investigación), C3-11 (justificar el dataset).
- C3-8 (24-oct-2026, noche): decidido con el usuario que la regularización es un COMPONENTE FIJO, no un factor (opción a). Se quitó "regularization" del objetivo 3, del entregable 3 y de RQ2 en c3.tex, y se agregó al alcance: "The weight of the KL regularization of the VAE is kept fixed in all runs (β=0.001 for the latent); it is not an experimental factor and its effect is not evaluated." Se descartó el factor G (β): rompería la fracción 2^(6-2) y subiría los ~1 900 GPU-h. Las menciones de "regularization" en c1:18, c2:82, c2:186 y c2:197 se dejan: describen la literatura y la teoría, no nuestros factores.
- C3-10 (24-oct-2026, noche): acordado con el usuario dejar solo RQ1 y RQ2 (efecto de los tratamientos de datos y de las modificaciones estructurales del VAE, "solos o combinados" para cubrir interacciones), conectadas con la hipótesis. RQ3 (reconstrucción vs generación) y RQ4 (DINO) se quitan como preguntas: siguen como objetivos 4 y 5. La sección "Research Questions" pasó a ir entre "Problem" e "Hypothesis" con la frase puente "The problem motivates two research questions, which in turn motivate the hypothesis". Referencias a RQ3 en c4 (dos) y c5 (una) cambiadas a "objective 4".
- C3-8, complemento (24-oct-2026, noche): se agregó a Limitations de c3.tex (después del punto de la profundidad) que el peso KL del latente (β=0.001, XieLi2025VAE: elegido por reconstrucción y estructura del latente, no por generación) y el de la capa de salida (sin fuente citada) son fijos, que otro valor podría cambiar los resultados y que su efecto queda como trabajo futuro. Nota: configs/dualvae.yaml del repo base dice "kl_beta: 0.001 (used in Optuna)"; no se sabe qué optimizó esa búsqueda.
- C3-11 (24-oct-2026, noche): el usuario propuso "nadie vuela a 2 m / sería revolucionario para el conteo"; se descartó tras buscar en Semantic Scholar: hay estudios de conteo a muy baja altura (3 a 7 m, trigo, Jin2017; 5 m, plántulas de abeto, Lopatin2023) y comparaciones típicas de 30 a 70 m (maíz, Barboza2025); Guess2025 respalda el compromiso resolución–cobertura–tiempo de vuelo. Ancla de C3-11 confirmada en Overleaf: primer punto del Scope ("A single dataset..."). Se reescribió en dos puntos: (1) dataset elegido por representar el régimen de interés y por pertenecer a la línea del grupo (XieLi2024, Fallas2023, XieLi2025VAE, Gonzalez2026); (2) altura de 2 m con contexto y el dato 17 609 cajas / 4 908 frames = 3.6 plantas anotadas por frame (hay que verificar que las cajas cubran todas las plantas). Referencias nuevas verificadas en Crossref: Jin2017, Lopatin2023, Barboza2025 (publicada en línea el 2025-12-20, volumen 18 n.º 1), Guess2025. PENDIENTE: confirmar con el asesor la altura de 2 m y la procedencia del dataset (mensaje corto de WhatsApp).

## c4.tex, C4-1 "¿Por qué 400?" (24/25-oct-2026)
- Hallazgos: el 400 lo introdujo el usuario el 13-sep-2026 (commit 7a104fb, "Add FID computation tooling and 400-image generation jobs"), sin justificación escrita; no lo recuerda. La referencia de FID son las 346 imágenes del split de prueba. El muestreo es de una imagen por pasada (inference.py, shape=(1,...)): DDPM 1000 pasos, 9 a 27 s por imagen (1 a 3 h por 400); FM unos 11 min por 400.
- Corrección del asistente: se dijo que el sesgo del FID era común a las corridas con N fijo; es falso (Chong2020: E[FID_N]=FID∞+K/N, Var≈K1/N, K depende del generador; comparar a N fijo es poco fiable; remedio FID∞ por regresión en 1/N con al menos 5 000 imágenes). c4 ya lo decía bien.
- Aplicado (versión mínima): párrafo "Number of images" en c4 con tres condiciones (i) N>2 048 (rango completo de la covarianza; también la referencia, >2 048 recortes del split de entrenamiento), (ii) ruido de muestreo ≤ 1/3 de la desviación entre corridas (infla un 5 %), medido en Etapa 0, (iii) costo en el presupuesto. Cambios de coherencia: fila de la tabla de parámetros fijos, "The N images", presupuesto (el 1 900 GPU-h no incluía el muestreo), amenazas (c4), Limitations (c3), nota del protocolo preliminar (c5), Etapa 0 y muestreo por lotes (c6).
- DECISIONES ASUMIDAS SIN CONFIRMAR (revisar): referencia desde el split de entrenamiento; N no se fija hoy sino en Etapa 0.
- Pospuesto por el usuario ("qué pereza"): validación de métricas en Etapa 0 con 4 chequeos (control nulo, sensibilidad, control positivo, acuerdo) y regla de decisión; FID/KID con DINOv2 como chequeo de robustez (acordado complementar, no sustituir; falta redactarlo en C4-3). Idea aún abierta: KID como respuesta principal y FID∞ (Chong2020) solo en confirmación.
- Referencias candidatas para C4-3 (leí resúmenes): Stein2023 (NeurIPS, 10.48550/arXiv.2306.04675), Jayasumana2024 (CVPR, 10.1109/CVPR52733.2024.00889), Kynkäänniemi2019, Naeem2020, Borji2021 (10.1016/j.cviu.2021.103329), Gretton2012 y Raudenbush1997 (no leídos). Limitaciones de las métricas a declarar: la profundidad generada no se mide (FID/KID solo con RGB), no detectan memorización, Inception no está entrenada para escenas agrícolas.

## c4.tex, C4-2 "¿Por qué solo 3 réplicas?" (25-oct-2026)
- Cálculo exacto (t no central; 2^(6-2), 16 celdas; efecto principal = 8r corridas contra 8r; SE = σ·sqrt(2/(8r)); gl del error = 16(r-1)): con σ=5, r=3 detecta efectos de 4.17 FID (potencia 0.8) y tiene potencia 0.92 para equivalencia (TOST, Δ=5, efecto 0); con σ=8 hace falta r=6 (3 840 GPU-h, 40 días con 4 trabajos). Tabla en c4 (tab:replicates) con r=2..6; sin ajuste por comparaciones múltiples (BH reduce la potencia).
- Argumentos para el profe: (1) 3 por celda no son 3 por comparación: cada efecto usa las 48 corridas (24 contra 24); (2) el error estándar baja con raíz de r y el costo sube lineal; (3) r es un valor de planificación derivado de σ y Δ, no fijo; (4) σ=5 es SUPUESTO (no medido; la variación de 9 puntos entre checkpoints de una misma corrida no es una desviación entre corridas); (5) la estimación de σ de la Etapa 0 (5 corridas, 4 gl) es rugosa, por eso se revisa con la Etapa 1 (32 gl); (6) si el resultado es inconclusivo se agrega una réplica a cada celda (bloque de 16 corridas, unos 640 GPU-h); (7) las réplicas extra se gastan en la Etapa 2 sobre los factores que importan.
- Riesgo declarado: si σ real es 8 o más, el diseño con r=3 solo detecta efectos de unos 6.7 puntos (mayores que Δ=5), y el cronograma se extiende (c6 ya lo dice).
- Nota técnica: el parámetro σ del texto es la desviación entre corridas independientes de la celda base.

## Calendario 2027 y réplicas (25-oct-2026)
- Datos del usuario: la fase de investigación empieza en febrero de 2027 (vacaciones antes), entrega de la tesis hacia octubre de 2027, Osnabrück es 1 mes de fecha flexible ("cuando el clima ande bien"), hay un curso de autómatas pesado (dos proyectos, dos exámenes, quices) y trabajo en INTEL, clúster de 4 trabajos siempre disponible. No hay definiciones oficiales de Tesis II/III; el artículo no está atado a un congreso concreto.
- Decisión del usuario: se mantienen 3 réplicas por celda y se justifican (valor de planificación, no un techo; el calendario deja espacio hasta 5; el paso de 3 a 5 mejora la detección en 1 punto de FID por 13 días más de cómputo). El profe pregunta "¿por qué no 5?".
- Aplicado: frase simple sobre el efecto de cada factor en c4; frase de las 3 réplicas en c4; c6 reescrito por meses (texto, tabla de fases con periodo, pie de figura, párrafo final); Gantt regenerado por meses de nov-2026 a oct-2027 (docs/s2/draw_gantt.py); fila "Paper and thesis drafting (parallel)" desde febrero.
- Supuestos míos no confirmados: el curso va de febrero a junio; la etapa 1 en mayo-junio es compatible con el curso; la estancia en Osnabrück cae entre abril y septiembre.
- PENDIENTE: apartado de estadística en el marco teórico (Capítulo II): tabla de temas y referencias verificadas en Crossref (Wu & Hamada 2021 doi 10.1002/9781119470007, Box & Hunter 1961, Cohen 1992, Shapiro & Wilk 1965, Benjamini & Hochberg 1995, Tukey 1949, Schuirmann 1987, Lakens 2017; Holm 1979 sin verificar); frase que fundamenta σ=5 con el Capítulo V (RMS 4.7 entre pares, unos 3.4 por corrida) y que la potencia de 0.8 es convencional (r=3 también cumple 0.9); C4-3 (métricas).

## c4.tex, C4-3 "justificar por qué estas métricas son suficientes" (25-oct-2026)
- Aplicado: párrafo "Why these metrics" en c4 (después del de FID/KID/PSNR/SSIM): el estudio compara configuraciones bajo el mismo protocolo, no reclama calidad absoluta ni utilidad; FID (estándar, comparable con Gonzalez2026) y KID (insesgado, sin supuesto de normalidad; Binkowski2018) como estimadores de la misma distancia, conclusión solo si coinciden; FID y KID también con características de DINOv2 (Oquab2023) como chequeo de robustez definido de antemano (se reporta la correlación de rangos entre extractores sobre las celdas de la Etapa 1; si discrepan, se declara como limitación); límites: no detectan memorización (Stein2023), solo RGB (la profundidad generada no se evalúa; la reconstruida sí con PSNR), no miden utilidad para conteo; se muestran muestras generadas. Nuevo punto en Limitations de c3 con lo mismo. Referencias nuevas verificadas en Semantic Scholar: Stein2023, Oquab2023.
- Decisión del usuario: DINOv2 complementa, no sustituye. Se dejó fuera (por pereza del usuario) la validación de Etapa 0 con 4 chequeos (control nulo, sensibilidad, control positivo, acuerdo); queda solo el acuerdo entre extractores en la Etapa 1.
- Abierto: KID como respuesta principal (hoy la hipótesis exige FID significativo con KID en el mismo sentido); FID infinito por extrapolación (Chong2020).

## c5.tex (25-oct-2026): C5-1 y C5-2
- Anclas confirmadas en Overleaf: C5-1 ("¿Se podrían agregar imágenes para soportar este claim?") está en la frase "but the reconstructions look more realistic"; C5-2 ("yo movería esto a un apéndice") está en el título de la sección "Audit of the Training Pipeline".
- C5-2 aplicado: la auditoría completa (tabla de 7 problemas y efecto de las correcciones) pasó al Anexo A (TFC1/annexA.tex, \chapter bajo \appendix en General.tex, etiqueta app:audit). En c5 queda un resumen de un párrafo con referencia al anexo; c4 ahora cita "the audit of Annex A".
- C5-1 aplicado: dos figuras nuevas hechas con imágenes ya guardadas en KABRÉ (acceso de solo lectura, no se lanzó ningún job): Imagenes/recon_comparison.png (4 recortes de prueba en las posiciones 0, 90, 180, 270, elegidos por posición y no por calidad; originales y reconstrucciones de vae, vae_rgbd y vae_rgbd_gan) e Imagenes/generated_samples.png (6 recortes reales y las 6 primeras imágenes generadas por DDPM y FM, checkpoints finales, VAE v2 aug_all, decoder mean). Script: docs/s2/draw_samples.py.
- HALLAZGO: las reconstrucciones de prueba salen de model(images), cuya primera salida es la del decodificador MUESTREADA (ruido de píxel de la capa variacional). El grano de la última columna es ese ruido; no es detalle recuperado. Por eso la frase "look more realistic" se reescribió: el FID de las reconstrucciones mejora por una textura que se parece a la real, no por una copia más fiel. Implicación: el FID/KID de reconstrucción de las variantes con capa variacional mezcla ese ruido; los números de la tabla de reconstrucción se calcularon con esas salidas muestreadas.
- Las muestras generadas se describen con cautela: reproducen color y textura de hojas, con artefactos de borde y zonas planas; 2 de las 6 muestras de FM muestran suelo desnudo. Consistente con FID de 159.1 (DDPM) y 170.6 (FM).
