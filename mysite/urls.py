from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
