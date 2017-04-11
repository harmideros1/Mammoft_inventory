from django.conf.urls import include, url
from django.contrib import admin
from app.login.views import *
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'MAMMOFT_inventory_1_0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # LA URL ADMINITRADOR ES mammoft_staff POR CUESTIONES DE SEGURIDAD, YA NO ES ADMIN
    url(r'^mammoft_staff/', include(admin.site.urls)),
    url(r'^$', index_view, name='vista_principal' ),
    url(r'^home$', home_page, name='home_page' ),
    url(r'^login$', login_view, name='vista_login' ),
    url(r'^logout$', logout_view, name='logout' ),
    url(r'^change_password/$', change_password, name='change_password' ),
    url(r'^profile/$', profile_view, name='profile' ),

    # A esta url se redirecciona cuando un usuario no tiene permisos de acceso
    # Por ejemplo, se dispara al loguearse con un usuario con roles de staff
    # Los usuarios Staff solo pueden acceder por el sitio administrativo
    url(r'^error/denied$', denied, name='denied' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
