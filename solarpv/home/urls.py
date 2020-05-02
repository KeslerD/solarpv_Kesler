from django.urls import path
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from . import views

# Create your tests here.
urlpatterns = [path('adminRedirect/', RedirectView.as_view(url=reverse_lazy('admin:index'))),path('', views.index, name='index'),path('index', views.index, name='index'),path('registration/',views.registration,name='registration'),path('login/',views.login,name='login'),path('searchCert/',views.searchCert,name='searchCert')]