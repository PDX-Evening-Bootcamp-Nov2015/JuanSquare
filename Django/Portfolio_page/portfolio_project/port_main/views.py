from django.shortcuts import render

class Project():
    def __init__(self, name, url, tagline):
        self.name = name
        self.url = url
        self.tagline = tagline

# Create your views here.
def main(request):
    context = {
        'project_list' : [
            Project('Angry Dice', 'angry_dice/', 'A simple html/css/javascript dice game implementation.'),
            Project('Forum', 'forum/', 'A forum using a star wars poster as design inspiration and Google Spreasheet API for a simple databse.'),
            Project('Javapic', 'JavaPic/', 'Using provided HTML/CSS, students were assigned to use only javascript to acheive certain objectives.'),
            Project('Javapic JQuery', 'JavaPic_Jquery/', 'A re-write of the JavaPic assignment using the JQuery library.'),
            Project('Random Quote', 'random_quote', 'An exercise in API use, with design inspiration from a provided image.'),
        ]
    }
    return render(request, 'port_main/main.html', context)
