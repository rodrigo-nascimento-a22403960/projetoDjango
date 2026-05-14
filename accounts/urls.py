from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    
    # Rotas do Professor
    path('login-magico/', views.login_magic_link, name='login_magic'),
    path('autentica/', views.autentica_view, name='autentica_magic'),
]