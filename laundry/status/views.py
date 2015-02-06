from django.shortcuts import get_object_or_404, render
from status.models import Query, Response

def index(request):
    query_list = Query.objects
    context = {'query_list': query_list}
    return render(request, 'status/index.html', context)

def detail(request, query_id):
    try:
        query = get_object_or_404(Query, pk=query_id)
    return render(request, 'status/detail.html', {'query': query})
