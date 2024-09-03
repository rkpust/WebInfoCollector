from django.shortcuts import render

# Create your views here.
def InfoCollect(request):
    return render(request, 'InfoCollector.html')