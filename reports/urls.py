from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.about, name='about'),
    path('report_log/', views.AllReports.as_view(), name='report_log'),
    path('submit_status/', views.submit_status, name='submit_status')
]