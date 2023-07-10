Realice al menos dos tipos de restricciones de acceso. En un archivo README.txt debe indicar todas las
características de estas restricciones.

-- Se crea restriccion solo para que usuarios del grupo "Administradores" puedan usar listar_usuarios
-- Se crea restriccion solo para que usuarios del grupo "Administradores" puedan ingresar a panel_admin
-- Se crea restriccion que solo usuarios registrados y pertenezcan al grupo "Usuarios" puedan "actualizar sus datos" e ingresar al home con su nombre en el.

Trabaje en el archivo README, con la finalidad de describir de forma detallada el funcionamiento de su
aplicación, su objetivo y toda la información que considere relevante.

Personalice los aspectos que considere necesarios del Login.
-- Se genera registro y login con solo correo(correo y username es lo mismo) y contraseña, se habilita opcion al logear en el menu para Ingresar los datos como Nombre Apellido, etc.

**************************************************************************************************************************************************************************************

Continuando con el trabajo anterior. Identifique dos grupos de usuarios de su aplicación. En este
sentido, debe crear dos usuarios de cada grupo. Cada grupo tiene permisos diferenciados de acuerdo a
sus características particulares. Es importante que en un archivo README.txt den cuenta de una
reflexión que justifique los permisos diferenciados.

-- Esto se justificó en la primera parte

Los usuarios se deben crear de forma dinámica mediante un formulario. Para realizar esto, debe buscar
la información necesaria en la documentación de Django y en las cápsulas de la sesión.

-- usuarios con panel de registro especial donde username = email, por lo cual pide solamente email y contraseña para registrar, se habilitara panel para agregar datos extras para los pedidos


Verifique que los usuarios quedan registrados en la página de administración de Django.

-- Usuarios verificados