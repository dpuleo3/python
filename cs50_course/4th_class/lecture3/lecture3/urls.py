from django.contrib import admin

from django.urls import include, path

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('first_app/', include("first_app.urls")),
    
    path('tasks/', include("tasks.urls")),
    
    path('newyear/', include("newyear.urls"))
    
]
