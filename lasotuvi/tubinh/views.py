from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tubinh(request):
    return HttpResponse('Day la Tu binh')
    # return render(request,asdsd)
