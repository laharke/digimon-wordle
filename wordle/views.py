from django.shortcuts import render
import os
import json
import requests
from django.http import JsonResponse



# Digimon del día (en un caso real podrías guardarlo en BD)
# VOY A GUARDAR LA INFO EN OTRO ARCHIOV JSON DE UN DIGIMO NQEU VOY A USAR PARA BASE
with open('wordle/static/data/dailyDigimon.json') as f:
    DIGIMON_DEL_DIA = json.load(f)

    evolutionIDS = []

for evolution in DIGIMON_DEL_DIA['priorEvolutions']: 
    evolutionIDS.append(evolution['id'])

DIGIMON_DEL_DIA['priorEvolutionsIds'] = evolutionIDS



# Create your views here.
def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(BASE_DIR, 'wordle','static' ,'data', 'digimons.json')) as f:
        digimons = json.load(f)
    print(DIGIMON_DEL_DIA)

    print(DIGIMON_DEL_DIA['id'])
    print(DIGIMON_DEL_DIA['name'])
    print(DIGIMON_DEL_DIA['priorEvolutionsIds'])


    #digimons[id]
    #digimons[image]
    #print(digimons[0])

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
    

    #Proceso ERRORES
    print (data)
    digimon_info = data[0]  # La API devuelve una lista


    # Extraer info relevante
    guess_data = {
        "name": digimon_info["name"],
        "type": digimon_info["type"],
        "attribute": digimon_info["attribute"],
        "level": digimon_info["level"]
    }

    # Comparar con el Digimon del día
    comparison = {
        "type": guess_data["type"] == DIGIMON_DEL_DIA["type"],
        "attribute": guess_data["attribute"] == DIGIMON_DEL_DIA["attribute"],
        "level": guess_data["level"] == DIGIMON_DEL_DIA["level"]
    }

    return JsonResponse({
        "guess": guess_data,
        "comparison": comparison
    })
