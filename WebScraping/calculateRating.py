import random
import math
from countryList import country
from materialList import materials

# Dummy Material Classification
Materials = ['Safe', 'Moderate', 'Harmful', 'Dangerous']


def compute():
    # Dummy distance [0 - 100]
    distance = math.ceil(random.random()*100)

    chooseCountry = country[random.randint(0, len(country)-1)]

    materialQty = random.randint(0, 4)
    chooseMaterials = []

    for i in range(materialQty):
        chooseMaterials.append(
            materials[random.randint(0, len(materials)-1)])

    get_material_type = random.randint(0, 4)
    material_value = 0

    if get_material_type == 0:
        material_value = 0
    elif get_material_type == 1:
        material_value = 35
    elif get_material_type == 2:
        material_value = 70
    elif get_material_type == 1:
        material_value = 100

    mean_score = (material_value + distance) / 2

    if mean_score > 0 and mean_score < 30:
        classify = Materials[0]
    elif mean_score >= 25 and mean_score < 50:
        classify = Materials[1]
    elif mean_score >= 51 and mean_score < 70:
        classify = Materials[2]
    elif mean_score >= 71 and mean_score <= 100:
        classify = Materials[3]

    result = [
        distance,
        chooseCountry,
        chooseMaterials,
        classify
    ]

    return result
