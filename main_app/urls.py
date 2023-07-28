from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_show/', views.add_show, name='add_show'),
    path('cars/<int:car_id>/assoc_upgrade<int:upgrade_id>/', views.assoc_upgrade, name='assoc_upgrade'),
    path('cars/<int:car_id>/unassoc_upgrade<int:upgrade_id>/', views.unassoc_upgrade, name='unassoc_upgrade'),
    path('upgrades/', views.UpgradeList.as_view(), name='upgrades_index'),
    path('upgrades/<int:pk>/', views.UpgradeDetail.as_view(), name='upgrades_detail'),
    path('upgrades/create/', views.UpgradeCreate.as_view(), name='upgrades_create'),
    path('upgrades/<int:pk>/update/', views.UpgradeUpdate.as_view(), name='upgrades_update'),
    path('upgrades/<int:pk>/delete/', views.UpgradeDelete.as_view(), name='upgrades_delete'),
]