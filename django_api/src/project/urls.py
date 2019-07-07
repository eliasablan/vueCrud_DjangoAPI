from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import urls, routers
from blog_api.views import AuthorAPI, CategoryAPI, PostAPI

from .views import home

apiurl = routers.SimpleRouter()
apiurl.register('autores', AuthorAPI)
apiurl.register('categorias', CategoryAPI)
apiurl.register('publicaciones', PostAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiurl.urls)),

    path('', home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
