from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView

from .models import StatusReport
from datetime import datetime
# Create your views here.

def about(request):
    return render(request, 'reports/about.html')

def all_machines(request):
    # For now there is no table for machines so all availble machines
    # can be found in the status report table.
    queryset = StatusReport.objects.values('machine_id').distinct()
    machines = []
    for x in queryset:
        machines.append(x['machine_id'])
    context = {'machines': machines}
    return render(request, 'reports/machines.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def submit_status(request):
    id = request.POST.get("id", "")
    status = request.POST.get("status", "")
    time = request.POST.get("time", "")
    if id == '' or status == '' or time == '':
        print("Empty POST")
        return HttpResponse(status=103)
    elif status == '0':
        return HttpResponse(status=204)
    unix_time = datetime.fromtimestamp(int(time))
    mountain_time = timezone.make_aware(unix_time, timezone.utc)
    machine_states = {
        '1': "Malfunction detected",
        '2': "Intervention required",
        '3': "Operating correctly",
        '4': "Requires action from operator",
        '5': "Requires constant action from operator",
    }
    print("ID: " + id)
    print("Status: " + status)
    print("Time: " + time)
    # Create new status report based on the Post Request.
    StatusReport.objects.create(
        machine_id=int(id),
        status=machine_states[status],
        timestamp=unix_time
    )
    response = id + '\n' + status + '\n' + str(unix_time)
    print(response)
    return HttpResponse(response, status=200)

class AllReports(ListView):
    model = StatusReport
    context_object_name = "reports"
    template_name = "reports/all_reports.html"
    paginate_by = 10

    def get_queryset(self):
        return StatusReport.objects.all().order_by('-timestamp')

class MachineReports(ListView):
    model = StatusReport
    context_object_name = 'reports'
    template_name = 'reports/machine_report.html'
    paginate_by = 10

    def get_queryset(self):
        return StatusReport.objects.filter(
            machine_id = self.kwargs['machine_id']
        ).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['machine'] = self.kwargs['machine_id']
        return context