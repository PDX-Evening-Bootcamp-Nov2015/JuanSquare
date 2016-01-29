from django.shortcuts import render

# Create your views here.
def javapic_main(request):
    data = {}
    return render(request, 'JavaPic/index.html', data)

def join(request):
    data = {}
    return render(request, 'JavaPic/join.html', data)

def gallery(request):
    data = {}
    return render(request, 'JavaPic/gallery.html', data)
