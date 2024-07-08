# django imports
from django.urls import path

# local imports
from . import views

app_name = 'app'
# urlpatterns matchesup the incoming request with particular view
urlpatterns = [
    # it attaches index view to an empty path
    path('', views.home, name = 'home'),
    path('generate/', views.generate, name = 'generate-view')
]