**Introducción 

Un workflow, o flujo de trabajo en español, es un conjunto de actividades relacionadas, que son completadas en un determinado orden para alcanzar un objetivo de la organización.

Aquí hay algunos aspectos o puntos clave a considerar en lo que nos ayuda este flujo de trabajo:

1.  Definición clara de procesos: implica identificar todas las actividades involucradas, los roles de los participantes y las dependencias entre las tareas.

2.  Automatización: Utilizar herramientas de automatización para agilizar y optimizar el flujo de trabajo.

3. Asignación de recursos: Asignar los recursos adecuados.

4. Seguimiento y monitoreo: Implementar sistemas para rastrear el progreso de los flujos de trabajo y monitorear el rendimiento. 

5. Gestión de cambios: Establecer un proceso para gestionar cambios en los flujos de trabajo. 

6. Optimización continua: Buscar constantemente formas de mejorar los flujos de trabajo identificando áreas de ineficiencia.

7. Seguridad y cumplimiento: Garantizar que los flujos de trabajo cumplan con los requisitos de seguridad.

**Desarrollo

Se desarrollo un flujo de trabajo que trabajara con \textit{prefect}, de modo que, utilizando sus API's web, ver como es el proceso de trabajo en nuestro flujo de trabajo.

Esta desarrollado de forma que implementa un flujo de trabajo utilizando la biblioteca Prefect en Python. 

Consiste en tres tareas principales:

1. do_request(url: str): realiza una solicitud y si la solicitud es exitosa la guarda el texto de la respuesta. 

2. do_parse(res): analizar el texto de respuesta JSON que recibe como entrada. Si el análisis tiene éxito, guarda los datos analizados. 

3. do_print(data): imprime los datos analizados que recibe como entrada.

Finalmente, el programa define un flujo principal (main_flow) que conecta estas tres tareas en secuencia.




