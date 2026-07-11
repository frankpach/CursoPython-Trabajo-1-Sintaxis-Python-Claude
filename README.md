# Comparandome Con Claude Code

Estoy haciendo un curso de Python para recordar como es volver a la academia y he decidico hacer una serie conparativa de los trabajos que realizo yo para las notas del curso, vs lo logra Claude, con el mismo enunciado.

##Reflexión del Trabajo 1 de curso sobre el uso de LLM para generar este código (calculadora_promedios.py). 

Este fragmento de código fue generado con ayuda de un LLM (Claude). Quise compararlo con el tiempo y el esfuerzo que me habría tomado implementarlo manualmente. Me sorprende la diferencia entre lo que logre yo y el nivel de codigo del LLM.

Con un promp escueto, has el siguiente trabajo "...", el modelo produjo una solución funcional en aproximadamente 3 minutos. Haciendo el mismo ejercicio por mi cuenta, me tomó cerca de **15 minutos** solo organizar la idea, escribir el código inicial, probarlo y comenzar a corregir errores.

Lo más interesante es que el código generado no solo fue más rápido de obtener, sino que en este caso el nivel del codigo también resultó igual o mejor que mi primera implementación, ademas las notas de cada funcion.

Esto refuerza una conclusión importante: **los LLM ya son extraordinariamente buenos resolviendo problemas bien delimitados**. Para componentes específicos, funciones aisladas, algoritmos, transformaciones de datos o tareas de complejidad moderada, el aumento de productividad es enorme.

Eso no significa que el *Vibe Coding* sea una solución mágica. El codigo no cumple en el 100% de los requerimeintos pero no fue el mejor promp. Es claro para mi que dandole mas skills e instrucciones de hacer loops de verificacion estoy seguro que hubiera logrado el 100%.

En proyectos grandes o aplicaciones completas, todavía aparecen problemas importantes:

- El modelo puede introducir inconsistencias arquitectónicas.
- Puede romper funcionalidades existentes al modificar otras.
- Borrar codigo importante.
- Hacer commits excesivos imposibles de seguir.
- Tiende a perder contexto conforme crece el proyecto.
- No siempre toma las mejores decisiones de diseño a largo plazo.
- El código generado requiere revisión, pruebas y criterio de ingeniería.

Sin embargo, para problemas concretos, la diferencia de productividad es difícil de ignorar.

Sigue cometiendo errores. A veces hay que corregirlo o incluso reescribir partes. Pero incluso considerando ese trabajo de revisión, el costo total suele ser muy inferior al de desarrollar la misma solución completamente desde cero. La idea no es implementar de ninguna manera el token MAXIMISING.

Y estoy seguro almenos por ahora, que el verdadero cambio no consiste en reemplazar al desarrollador, sino en cambiar dónde invierte su tiempo. Cada vez dedicamos menos esfuerzo a escribir o buscar para reutilizar código y más a definir la arquitectura, validar decisiones, trabajar de verdad con TDD, pensar en seguridad, integrar componentes y verificar que el resultado sea correcto.

La programación está evolucionando desde escribir cada línea de código hacia dirigir inteligentemente sistemas capaces de producirlo. Quien aprenda a combinar criterio de ingeniería con el uso efectivo de LLM tendrá una ventaja significativa en productividad.

---

> **Los LLM no eliminan la necesidad de buenos ingenieros; aumentan enormemente el rendimiento de quienes ya saben cómo construir software.**
