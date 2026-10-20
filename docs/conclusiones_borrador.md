# Conclusiones: borrador guardado (pospuestas el 18-oct-2026)

Decisión del usuario: de momento no se incluyen las conclusiones. El capítulo está desactivado en `General.tex` (línea comentada) para que no salga una página vacía. La propuesta de Danny tampoco las incluye. Confirmar con el asesor si una propuesta las requiere.

## Bloque 1: estado por objetivo (revisado por el usuario, sin ajustes pendientes)
Objective 1 (reproducible baseline). Largely achieved. The inherited pipeline was audited, seven problems were corrected, and a baseline with DDPM and Flow Matching was trained and evaluated. What remains is to make the whole process automatic, from training to evaluation, so that every run of the experimental design is reproducible.
Objective 2 (treatments of the data). In progress. Augmentation and masking were implemented and tested in preliminary comparisons that indicate the direction of their effects; the replicates and the experiments of the design are missing to confirm them.
Objective 3 (modifications of the VAE). In progress. The variational output layer and the adversarial loss were implemented and compared in a preliminary way, with hints of their effect; the replicates and the experiments of the design are pending.
Objective 4 (reconstruction against generation). Designed, not yet executed. The analysis is defined in Chapter IV and depends on the experiments of Stage 1.
Objective 5 (DINO). Not started; optional, planned in parallel if time permits.
Objective 6 (paper). Not started; planned after the final analysis.
(El objetivo 7 de Osnabrück se retiró de la propuesta.)

## Bloque 2 pendiente: evidencia preliminar (seis candidatas, el usuario debe elegir y redactar a su manera)
1. Pipeline heredado con 7 problemas, corregidos; Flow Matching ya no colapsa (FID 379 a 171).
2. Reconstrucción y generación no se mueven juntas (PSNR -1.7 dB con GAN y capa variacional, pero FID de reconstrucción 132 a 119; FID de generación igual dentro del ruido).
3. Las diferencias entre configuraciones son del tamaño de la variación dentro de una corrida (hasta 9 puntos): hacen falta réplicas.
4. La profundidad como entrada fue la única señal consistente (8 a 14 puntos de FID en tres comparaciones, receta vieja).
5. Aumento: mejora el error de píxel 3 a 5%, no la generación; enmascarado: empeora la reconstrucción (0.8 y 1.5 dB), efecto en generación sin probar.
6. Flow Matching genera unas diez veces más rápido, con FID parecido a DDPM.

## Bloques 3 y 4 pendientes: aportes esperados; limitaciones y trabajo futuro
Trabajo futuro sin nombres propios: etiquetado de imágenes generadas, conteo con ellas, validación en un segundo cultivo, otros dominios.
