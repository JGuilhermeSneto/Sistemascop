
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('Forms/', include('FormsAulas.urls')),
    path('banco/', include('banco.urls')),
    path('usuarios/', include('users.urls'))
]
