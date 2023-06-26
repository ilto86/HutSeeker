from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from backend.huts import views

router = routers.DefaultRouter()
router.register(r'huts', views.HutsView, 'huts')
router.register(r'approach', views.ApproachView, 'approach')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
