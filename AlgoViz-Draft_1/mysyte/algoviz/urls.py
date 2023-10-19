from django.urls import path
from .views import (
    AlgoListView,
    AlgoDetailView,
    AlgoCreateView,
    AlgoUpdateView,
    AlgoDeleteView,

)
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='algoviz-home'),
    path('about/', views.about, name='algoviz-about'), 
    path('about/myapp/', 
         RedirectView.as_view(url='http://localhost:5000/visualize.html')),
    # path('terminal/', views.terminal, name='algoviz-terminal'),
    path('docs/', AlgoListView.as_view(), name='algoviz-docs'),
    path('docs/myapp/', 
         RedirectView.as_view(url='http://localhost:5000/visualize.html')),
    path('algorithm/<int:pk>/', AlgoDetailView.as_view(), name='algorithm-details'),
    path('algorithm/<int:pk>/update/', AlgoUpdateView.as_view(), name='algorithm-update'),
    path('algorithm/<int:pk>/delete/', AlgoDeleteView.as_view(), name='algorithm-delete'),
    path('algorithm/new/', AlgoCreateView.as_view(), name='algorithm-create'),
    path('algorithm/new/myapp/', 
         RedirectView.as_view(url='http://localhost:5000/visualize.html')),
]

