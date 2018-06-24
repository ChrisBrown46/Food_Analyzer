import json

from usda_ndb_client.client import Client

with open("usda_nbd_api_keys") as file:
    api_keys = json.load(file)
nutrition_api = Client(api_key=api_keys["api_key"])

nutrient_ids = {
    "208": "calories",
    "203": "protein",
    "204": "total_fat",
    "606": "saturated_fat",
    "601": "cholesterol",
    "205": "carbohydrates",
    "307": "sodium",
    "269": "sugar",
}


def get_nutrition_info(food):
    food_key = nutrition_api.search(q=food, max="1").list.item[0].ndbno

    food_info = (
        nutrition_api.nutrients(
            max="1", ndbno=food_key, nutrients=[nutrient for nutrient in nutrient_ids]
        )
            .report.foods[0]
            .nutrients
    )

    return formatted_food_info(food_info)


def formatted_food_info(food_info):
    reformatted_food_info = {}

    for nutrient in food_info:
        if nutrient.gm == "--" or nutrient.gm == 0.0:
            gm = 0
            unit = ""
        else:
            gm = nutrient.gm
            unit = nutrient.unit

        reformatted_food_info[nutrient_ids[nutrient.nutrient_id]] = [gm, unit]

    sugar = (
            str(reformatted_food_info["sugar"][0])
            + reformatted_food_info["sugar"][1]
            + " Sugar | "
            + str(100 * round((reformatted_food_info["sugar"][0] / 37.5), 2))
            + "%"
    )
    sodium = (
            str(reformatted_food_info["sodium"][0])
            + reformatted_food_info["sodium"][1]
            + " Sodium | "
            + str(100 * round((reformatted_food_info["sodium"][0] / 1500.0), 2))
            + "%"
    )
    protein = (
            str(reformatted_food_info["protein"][0])
            + reformatted_food_info["protein"][1]
            + " Protein | "
            + str(100 * round((reformatted_food_info["protein"][0] / 60.0), 2))
            + "%"
    )
    calories = (
            str(reformatted_food_info["calories"][0])
            + " Calories | "
            + str(100 * round((reformatted_food_info["calories"][0] / 2000.0), 2))
            + "%"
    )
    total_fat = (
            str(reformatted_food_info["total_fat"][0])
            + reformatted_food_info["total_fat"][1]
            + " Total Fat | "
            + str(100 * round((reformatted_food_info["total_fat"][0] / 65.0), 2))
            + "%"
    )
    cholesterol = (
            str(reformatted_food_info["cholesterol"][0])
            + reformatted_food_info["cholesterol"][1]
            + " Cholesterol | "
            + str(100 * round(reformatted_food_info["cholesterol"][0] / 300.0, 2))
            + "%"
    )
    carbohydrates = (
            str(reformatted_food_info["carbohydrates"][0])
            + reformatted_food_info["carbohydrates"][1]
            + " Carbohydrates | "
            + str(100 * round(reformatted_food_info["carbohydrates"][0] / 300.0, 2))
            + "%"
    )
    saturated_fat = (
            str(reformatted_food_info["saturated_fat"][0])
            + reformatted_food_info["saturated_fat"][1]
            + " Saturated Fat | "
            + str(100 * round(reformatted_food_info["saturated_fat"][0] / 20.0, 2))
            + "%"
    )

    return [
        calories,
        protein,
        total_fat,
        saturated_fat,
        cholesterol,
        carbohydrates,
        sodium,
        sugar,
    ]
