# Preguntas difíciles del lector de la propuesta (preparación)

Guion para responder con calma y con los números verificados. Fuente: capítulo V (`TFC1/c5.tex`).

## "¿Ya hizo experimentos previos?"
Sí. Entre el 15 de septiembre y el 14 de octubre entrené VAE y generadores (DDPM y Flow Matching) con una semilla por configuración, para tener una línea base y saber qué se puede medir.

## "¿Y cuáles fueron?"
1. Auditoría del pipeline heredado: 7 problemas (por ejemplo, un scheduler de learning rate que hacía 4 ciclos y terminaba en el máximo, y un modelo "final" colapsado con FID 379). Todos corregidos.
2. Comparé VAE con y sin GAN y capa variacional, con y sin aumento, y con y sin profundidad como entrada, y entrené DDPM y Flow Matching sobre ellos.
3. Implementé enmascarado y probé la reconstrucción con 25% y 50%.

## "¿Y qué resultados dieron?"
- La profundidad como entrada del VAE fue la única diferencia consistente en la generación: entre 8 y 14 puntos de FID en tres comparaciones.
- El GAN, la capa variacional y el aumento no produjeron una diferencia de FID mayor que la que hay entre dos checkpoints de un mismo entrenamiento (hasta 9 puntos).
- El GAN mejoró el aspecto de las reconstrucciones (FID de reconstrucción 132 a 119) pero bajó el PSNR 1.7 dB. Reconstrucción y generación se movieron en direcciones distintas.

## "Entonces, ¿para qué siguió si nada sirvió?"
Porque los experimentos previos no dicen que nada sirva: dicen que **con una semilla no se puede distinguir**. La diferencia entre dos checkpoints de un mismo entrenamiento es tan grande como la de la mayoría de los cambios. Eso es justo lo que la propuesta resuelve: un diseño factorial con réplicas, análisis de varianza y pruebas de equivalencia, para poder decir "esto sí ayuda" o "esto no ayuda más que X", con evidencia. Además, hay una señal que vale la pena confirmar (la profundidad) y una pregunta abierta en la literatura (si mejor reconstrucción implica mejor generación) que en este régimen de pocos datos no se había medido.

## "¿Y si al final nada mejora?"
La hipótesis queda refutada, y con las pruebas de equivalencia se puede afirmar que el efecto es menor que un margen declarado. Es un resultado útil para quien trabaje con pocos datos homogéneos: invertir en esos tratamientos no rinde.

## Lo que no hay que decir
- No decir que el VAE nuevo "reconstruye mejor": el PSNR bajó. Decir "se ve más real, con menos fidelidad de píxel".
- No decir que Flow Matching genera mejor: genera más rápido (11 min frente a 1 a 3 horas con 1000 pasos), pero el FID es parecido o algo peor.
