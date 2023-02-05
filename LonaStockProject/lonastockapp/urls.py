from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.Login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('change_password/', views.change_password, name='change_password' ),
    path('password_changed/', views.password_changed, name='password_changed' ),
    path('list_products/',  views.list_products, name='list_products' ),
    path('add_product/', views.add_product, name='add_product' ),
    path('update_product/<str:pk>', views.update_product, name='update_product' ),
    path('delete_product/', views.delete_product, name='delete_product' ),
    # path('delete_product/<str:pk>', views.delete_product, name='delete_product' ),
    # path("accounts/", include("django.contrib.auth.urls")),
    ]