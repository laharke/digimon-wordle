from django.shortcuts import render
import os
import json







# Create your views here.
def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(BASE_DIR, 'wordle','static' ,'data', 'digimons.json')) as f:
        digimons = json.load(f)

    #digimons[id]
    #digimons[image]
    print(digimons[0])

    # Tal vez puedo agarrar toda la info y armamre un config file , la parseo y creo un json que sea
    # {id, name, foto} y con esto armo el dropdown menu.
    # Y cuando selecciona algo el usuario hago el submit y un llamdo ajax a la api para taer la info.
    
    return render(request, 'index.html')

# necesito testear si la api anda o ageraru n config file
