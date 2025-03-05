from django.urls import path
from .views import main, MedsList, MedDetail, MedCreate, MedUpdate, MedDelete


urlpatterns = [
    path('', main, name='main'),
    path('meds-list', MedsList.as_view(), name='meds-list'),
    path('med-detail/<int:pk>/', MedDetail.as_view(), name='med-detail'),
    path('med-create/', MedCreate.as_view(), name='med-create'),
    path('med-update/<int:pk>/', MedUpdate.as_view(), name='med-update'),
    path('med-delete/<int:pk>/', MedDelete.as_view(), name='med-delete'),
]
