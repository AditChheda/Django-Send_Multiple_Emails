from django.urls import path
from . import views

urlpatterns = [
    path('multiple-gmail/', views.multiple_gmail, name='multiple_gmail'),
    path('send-multiple-gmail/', views.send_multiple_gmail, name='send_multiple_gmail'),
    path('download-success-csv/', views.download_success_csv, name='download_success_csv'),
    path('download-failure-csv/', views.download_failure_csv, name='download_failure_csv'),
    path('download-all-csv/', views.download_all_csv, name='download_all_csv'),
]