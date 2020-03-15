from django.http import HttpResponse
from django.template import loader
from football.models import Match


def index(request):
    fields = Match._meta.get_fields()
    latest_results = Match.objects.order_by("id")[:3]
    template = loader.get_template('index.html')
    context = {
        'fields': fields,
        'latest_results': latest_results,
    }
    return HttpResponse(template.render(context, request))
