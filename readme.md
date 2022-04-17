Integrantes:

- Gabriel Graterol
- Franco Parnetti

Sobre el blog:
Todo lo relacionado al CRUD de los modelos de Estudiantes, Profesores y Carreras, asi como el login, logout, y registro fue realizado por Gabriel, mientras que la parte de edición del usuario, modelos y CRUD del blog, y detalles estéticos fue realizado por Franco.


Aclaración importante:
Es posible que al descargar por primera vez, la página no responda correctamente, y aparezca un error del tipo OperationalError: at/class/forms no such table (para cualquiera de los modelos).
La solución que por ahora encontramos es hacer un makemigrations y un migrate aclarando la carpeta correspondiente "class", que contiene todos los modelos. Desconocemos si existe alguna solución más elegante.
Aun así, para las ultimas pruebas que hicimos no fue necesario.