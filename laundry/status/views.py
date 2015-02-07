from django.shortcuts import get_object_or_404, render
from status.models import Query, Response

def index(request):
    query_list = Query.objects.all()
    context = {'query_list': query_list}
    return render(request, 'index.html', context)

def detail(request, query_id):
    query = get_object_or_404(Query, pk=query_id)
    return render(request, 'detail.html', {'query': query})
