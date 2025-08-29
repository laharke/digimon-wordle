def filter_api_info(data):
    #voy a fitlrar las prior y las nextEvolutions
    priorEvolutionIDS = []
    for evolution in data['priorEvolutions']: 
        priorEvolutionIDS.append(evolution['id'])

    nextEvolutionIDS = []
    for evolution in data['nextEvolutions']: 
        nextEvolutionIDS.append(evolution['id'])

    digimon = {
        "id": data['id'],
        "img": data['images'][0]['href'],
        "name": data['name'],
        "level": data['levels'][0]['level'],
        "attribute": data['attributes'][0]['attribute'],
        "type": data['types'][0]['type'],
        "release_date": data['releaseDate'],
        "priorEvolutionsIds": priorEvolutionIDS,
        "nextEvolutionsIds": nextEvolutionIDS
    }
    return digimon


# Hay que tener en cuenta que priorEvolution y nextEvolution se toma en cuenta el digimon2 con respecto al digimon1
# Es decir, si digimon1 es garurumon y digimon2 es gabumon, prior evolution sera True.
# Basicamente, digimon1 se toma como el daily digimon y digimon2 como la guess 


#compare two va ser compare guess_and dailydiigmon
def compare_two_digimons(daily_digimon, guessed_digimon):

    #comapro dgimon 1 con 2 y armo al comaprsion


    comprasion = {
        "level": True if daily_digimon['level'] == guessed_digimon['level'] else False,
        "attribute": True if daily_digimon['attribute'] == guessed_digimon['attribute'] else False,
        "type": True if daily_digimon['type'] == guessed_digimon['type'] else False,
        "relase_date": "higher" if daily_digimon['release_date'] > guessed_digimon['release_date'] else "lower",
        "priorEvolution": True if guessed_digimon['id'] in daily_digimon['priorEvolutionsIds'] else False,
        "nextEvolution": True if guessed_digimon['id'] in daily_digimon['nextEvolutionsIds'] else False
    }

    return comprasion

def compare_digimons(DIGIMON_DEL_DIA, guessed_digimon):

    DIGIMON_DEL_DIA

    info = {
        "id": guessed_digimon["id"],
        "name": guessed_digimon["name"],
        "img": guessed_digimon["img"],
        "level": {"value": guessed_digimon["level"], "correct": True if DIGIMON_DEL_DIA['level'] == guessed_digimon['level'] else False},
        "attribute": {"value": guessed_digimon["attribute"], "correct": True if DIGIMON_DEL_DIA['attribute'] == guessed_digimon['attribute'] else False},
        "type": {"value": guessed_digimon["type"], "correct": True if DIGIMON_DEL_DIA['type'] == guessed_digimon['type'] else False},
        "release_date": {"value": guessed_digimon["release_date"], "correct": True if DIGIMON_DEL_DIA['release_date'] == guessed_digimon['release_date'] else False},
        "priorEvolution": {"value": "Yes" if guessed_digimon['id'] in DIGIMON_DEL_DIA['priorEvolutionsIds'] else "No", "correct": True if guessed_digimon['id'] in DIGIMON_DEL_DIA['priorEvolutionsIds'] else False},
        "nextEvolution": {"value": "Yes" if guessed_digimon['id'] in DIGIMON_DEL_DIA['nextEvolutionsIds'] else "No", "correct": True if guessed_digimon['id'] in DIGIMON_DEL_DIA['nextEvolutionsIds'] else False}
    }

    return info