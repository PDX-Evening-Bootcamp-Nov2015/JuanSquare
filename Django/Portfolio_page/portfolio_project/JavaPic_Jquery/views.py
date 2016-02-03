from django.shortcuts import render

# Create your views here.
def main(request):
    data = {}
    return render(request, 'JavaPic_Jquery/index.html', data)

def join(request):
    data = {}
    return render(request, 'JavaPic_Jquery/join.html', data)

def gallery(request):
    data = {}
    return render(request, 'JavaPic_Jquery/gallery.html', data)
