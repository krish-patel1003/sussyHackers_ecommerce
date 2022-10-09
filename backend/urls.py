from django.urls import path
from .views import home, SignUpView, category, products
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='backend/logout.html'), name='logout'),

    path('categories/', category, name="categories"),
    path('products/', products, name="products"),

]