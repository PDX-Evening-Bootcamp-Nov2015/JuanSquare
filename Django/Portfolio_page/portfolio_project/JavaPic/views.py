from django.shortcuts import render

# Create your views here.
def javapic_main(request):
    data = {}
    return render(request, 'index.html', data)
