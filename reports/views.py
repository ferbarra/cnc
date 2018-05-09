from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone

from .models import StatusReport
from datetime import datetime
# Create your views here.

def about(request):
    return render(request, 'reports/about.html')

def report_log(request):
    return render(request, 'reports/report_log.html')


@csrf_exempt
@require_http_methods(["POST"])
def submit_status(request):
    id = request.POST.get("id", "")
    status = request.POST.get("status", "")
    time = request.POST.get("time", "")
    if id == '' or status == '' or time == '':
        print("Empty POST")
        return HttpResponse(status=103)
    elif status == 0:
        return HttpResponse(status=204)
    else:
        unix_time = datetime.fromtimestamp(int(time))
        utc_time = timezone.make_aware(unix_time, timezone.utc)
        print("ID: " + id)
        print("Status: " + status)
        print("Time: " + time)
        response = id + '\n' + status + '\n' + time
        return HttpResponse(response, status=200)