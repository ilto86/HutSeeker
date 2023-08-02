from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from .huts import views as hutsviews
from .accounts import views as accountsviews


router = routers.DefaultRouter()
router.register(r'huts', hutsviews.HutsListCreateView, 'huts-list')
router.register(r'huts-detail', hutsviews.HutsDetailView, 'huts-detail')
router.register(r'approach', hutsviews.ApproachView, 'approach')
router.register(r'month', hutsviews.MonthView, 'month')
router.register(r'services', hutsviews.ServicesView, 'services')
router.register(r'weather_condition', hutsviews.WeatherConditionView, 'weather_condition')
router.register(r'accounts', accountsviews.AppUserRegisterView, 'user_register')
router.register(r'accounts-detail', accountsviews.AppUserDetailView, 'user_details')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
