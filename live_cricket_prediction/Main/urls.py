from django.contrib import admin
from django.urls import path
from .views import home as x1
from .views import frontend_data as f

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', x1, name='home'),
    path('data', f, name='data'),
]
