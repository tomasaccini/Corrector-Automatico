# Generador de respuestas automáticas según los errores de los alumnos.
Como correctores, una gran parte del tiempo la empleamos en explicar o corregir muchas veces las mismas cosas a diferentes alumnos. Este proyecto busca automatizar la generacion de esas correcciones, pudiendo seleccionar errores comunes agrupados por TDA, y obteniendo una respuesta completa y genérica para que puedas customizar para el caso particular de tu alumno.

## Cómo usar la interfaz web:
- Descargar el  repositorio. 
- Abrir el archivo corrector.html en un navegador
- Seleccionar los TDAs de los cuales querés ver errores comunes y apretar actualizar filtros
- Seleccionar los errores que tiene tu alumno y apretar generar mail

## Cómo usar la línea de comandos para generar respuestas:
- Descargar el repositorio
- Abrir una consola en la carpeta donde lo descargaste
- Correr el comando "python main.py"
- Elegir entre las opciones "Agregar un error con solución", "Agregar un error sin solución", "Ver todos los errores sin resolver", "Ver todos los errores sin resolver de un determinado TDA", "Resolver un error existente" o "Guardar y salir"
- La escritura del archivo se hace cada vez que agregas un error o una solucion, y es transparente para el usuario.

## Cómo colaborar:
- Hacer mas linda la web que usa bootstrap
- Agregar funcionalidad al archivo .js que hace un render de las soluciones
- Usar el archivo main.py para ir cargando errores y soluciones completas, clasificadas por TDA. Despues pushear el archivo soluciones.txt actualizado.
- Automatizar el pasaje del archivo soluciones.txt archivo .js (desde javascript es dificil leer archivos locales)
