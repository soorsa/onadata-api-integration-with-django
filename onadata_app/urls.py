from django.urls import path
from . import views

urlpatterns = [
    path('form/<str:form_id>/', views.fetch_form_data, name='fetch_form_data'),
]
