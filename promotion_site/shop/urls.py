from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('main/', main_page, name='home'),
    # path('reg/', reg, name='reg'),
    path('<slug:shop>/', ShowShop.as_view(), name='showshop'),
    path('<str:shop>/<str:cat>/', ShowCategory.as_view(), name='showcategory')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
