from django.shortcuts import render

# Create your views here.
def main(request):
    data = {}
    return render(request, 'angry_dice/angry_dice.html', data)
