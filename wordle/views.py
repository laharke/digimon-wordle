from django.shortcuts import render
import os
import json
import requests
from django.http import JsonResponse
from . import utils




# Digimon del día (en un caso real podrías guardarlo en BD)
# VOY A GUARDAR LA INFO EN OTRO ARCHIOV JSON DE UN DIGIMO NQEU VOY A USAR PARA BASE
with open('wordle/static/data/dailyDigimon.json') as f:
    DIGIMON_DEL_DIA = json.load(f)

DIGIMON_DEL_DIA = utils.filter_api_info(DIGIMON_DEL_DIA)


# Create your views here.
def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(BASE_DIR, 'wordle','static' ,'data', 'digimons.json')) as f:
        digimons = json.load(f)

    print(DIGIMON_DEL_DIA['id'])
    print(DIGIMON_DEL_DIA['name'])



    # Tal vez puedo agarrar toda la info y armamre un config file , la parseo y creo un json que sea
    # {id, name, foto} y con esto armo el dropdown menu.
    # Y cuando selecciona algo el usuario hago el submit y un llamdo ajax a la api para taer la info.
    
    return render(request, 'index.html')

# necesito testear si la api anda o ageraru n config file



def check_guess(request):

    digimonID = request.GET.get("digimon_id")  # o request.POST si lo mandás como POST

    if not digimonID:
        return JsonResponse({"error": "No se envió el nombre"}, status=400)

    # Llamada a la API externa
    api_url = f"https://digi-api.com/api/v1/digimon/{digimonID}"
    r = requests.get(api_url)

    if r.status_code != 200:
        return JsonResponse({"error": "No se encontró el Digimon"}, status=404)

    data = r.json()

    if not data:
        return JsonResponse({"error": "Datos vacíos"}, status=404)
    

    guessed_digimon = utils.filter_api_info(data)

    
    # Ahora puedo comprar DIGIMON_DEL_DIA con el guessed_digimon y enviar la response
    # En la response no necesito enviar la info del digimon 
    # Igual es muy sencillo, envio dos arrays, una con la info del digimon y otra con los resultados
    
    # Si los ids coinciden WIN. Pero esto LATer.
    # La comrpacion de "level": true/false    "attribute": true/false   "type": true/false    "release_date": mayor/menor/igual      
    # "priorEvolutionsIds": true/false,   "nextEvolutionsIds": true/false


    # Defini una funcoin que le des dos DIGMONS y la COMPARE  y ya
    comparison = utils.compare_two_digimons(DIGIMON_DEL_DIA, guessed_digimon)

    info = utils.compare_digimons(DIGIMON_DEL_DIA, guessed_digimon)

    print(info)

    
    # El return va a ser como un json con al data y va a tener por ejemplo 
    # type: inccorect, 
    #level: correct
    # no se si encseiot al DATA del digmo qneu adinvo en eflront me chupa un HUEVO tbh

    return JsonResponse({
        "info": info
    })
