Objetivo del proyecto

Se construyó un sitio web para una consultora económica especializada en infomes económicos sectoriales (en la cual trabajo). La idea fue poder mostrar tres modelos(clientes, Informes sectoriales y noticias de prensa).
Allí se puede verificar quiénes son clientes de la empresa y se pueden agregar nuevos.
También se pueden ver y agregar nuevos informes, verificar si hay informes disponibles para descargar y fecha de publicacion
Tambíen se puede consultar/agregar las salidas en los medios de comunicación y ver el link que llevaría a la nota.

Se creó una página de quiénes somos y el buscador (no logré que el filtro me duvelva la búsqueda. Me redirige a la página indicada, pero creo que tengo un probema en el contexto. Estoy seguro que el error es una pavada, pero ya estoy quemado).

A continuación copio las rutas para consultar las distintas páginas:
urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('informesSectoriales/', InformesSectoriales, name="informesSectoriales"),
    path('prensa', prensa, name="prensa"),
    path('quienesSomos', quienesSomos, name="quienesSomos"),
    path('clienteForm', clientesForm, name="clienteForm"),
    path('prensaForm', PrensaForm, name="prensaForm"),
    path('informesSectorialesForm', InformesForm, name="informesSectorialesForm"),
    path('buscarClientes', buscarClientes, name="buscarClientes"),
    path('encontrarClientes', encontrarClientes, name="encontrarClientes"),
