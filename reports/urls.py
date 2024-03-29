from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.about, name='about'),
    path('report_log/', views.AllReports.as_view(), name='report_log'),
    path('submit_status/', views.submit_status, name='submit_status'),
    path('machines/', views.all_machines, name='machines'),
    path('machines/<int:machine_id>/', views.MachineReports.as_view(), name='machine_reports')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)