from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def station(request, statio):
    context = {
        'stati':statio,
    }
    return render(request, 'station/index.html', context=context)
    
