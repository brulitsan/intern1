from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'page', views.UserViewSet, basename='pages')
print(router.urls)


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main_page', views.success_view, name='main_page'),
    path('user/', include(router.urls), name='userProfile_ListCreate'),
    # path('user/<int:pk>/', views.UserProfileDetailView.as_view(), name='userDetail'),
    path('user_profile/', views.UserProfileView, name='UserProfileView'),
    path('page/<int:user_pk>', views.UserProfileView),
    path('page/<int:pk>/', views.login_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)