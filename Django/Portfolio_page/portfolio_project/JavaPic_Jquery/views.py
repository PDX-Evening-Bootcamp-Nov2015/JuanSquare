from django.shortcuts import render

# Create your views here.
def main(request):
    data = {}
    return render(request, 'JavaPic_Jquery/index.html', data)
