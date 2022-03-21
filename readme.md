Este proyecto surgió con la idea de realizar un blog del tipo campus para permitir a cualquier institución educativa, tanto terciaria como universitaria, hacer uso de la plataforma para que profesores y alumnos puedan comunicarse, organizarse, y en el caso de estos ultimos, entregar evaluaciones.


Por el momento, estan realizados el registro de alumnos, profesores y carreras, además de la posibilidad de buscar a algun alumno ya registrado.
Obviamente es conveniente registrar a un estudiante antes de probar la herramienta de busqueda, pero las otras dos funciones de registro pueden probarse en cualquier orden.
La pagina utiliza un template de bootstrap, con herencias para todos los urls de la misma. En todas se puede ver una barra de navegación, con botones que llevn al usuario a cualquiera de las paginas. En inicio se puede ver un boton especial que desplaza en la misma pagina y permite ver un texto (completamente innecesario, por cierto).




Aclaración importante:
Es posible que al descargar por primera vez, la página no responda correctamente, y aparezca un error del tipo OperationalError: at/class/forms no such table (para cualquiera de los modelos).
La solución que por ahora encontramos es hacer un makemigrations y un migrate aclarando la carpeta correspondiente "class", que contiene todos los modelos. Desconocemos si existe alguna solución más elegante.