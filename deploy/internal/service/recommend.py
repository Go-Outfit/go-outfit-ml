import random
import pkg.config.config as config
# uncompleted
import os


laki_dir = "Laki-laki"
cewek_dir = "Perempuan"
base_dir = "."


def recommend_output(gender, category, dataset):
    if gender == base_dir:
        gender = "all"
    # path = os.path.join(gender, category)
    path = gender+"/"+category
    path = os.getenv("IMAGEKIT_ENDPOINT_URL")+"/"+path
    # list of the images in the path
    available_images = dataset[gender][category]
    result_image = []
    for item in range(6):
        img = random.choice(available_images)
        img = path+"/"+img
        result_image.append(img)
    return result_image


class OutfitRecommender:
    def __init__(self, gender, weather, situation, fashion_style, dataset):
        self.gender = gender
        self.weather = weather
        self.situation = situation
        self.fashion_style = fashion_style
        self.dataset = dataset

    def recommend(self):
        gender = self.gender
        weather = self.weather
        situation = self.situation
        fashion_style = self.fashion_style
        dataset = self.dataset

        if gender == "male" and situation == "formal" and fashion_style == "formal":
            upperwear = recommend_output(laki_dir, 'jas', dataset)
            bottomwear = recommend_output(
                laki_dir, 'Celana_panjang_cowo', dataset)
            footwear = recommend_output(laki_dir, 'pantofel', dataset)
            result = {
                "upperwear": [upperwear],
                "bottomwear": [bottomwear],
                "footwear": [footwear],
            }
            return result
        elif gender == "female" and situation == "formal" and fashion_style == "formal":
            upperwear = []
            val = recommend_output(cewek_dir, 'jas_cewe', dataset)
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'dress', dataset)
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(cewek_dir, 'rok_formal', dataset)
            bottomwear.append(val)
            val = recommend_output(cewek_dir, 'cp_cewe', dataset)
            bottomwear.append(val)

            footwear = []
            val = recommend_output(cewek_dir, 'pantofel_cewe', dataset)
            footwear.append(val)
            val = recommend_output(cewek_dir, 'heels', dataset)
            footwear.append(val)

            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        elif gender == "male" and situation == "non_formal" and fashion_style != "formal":
            upperwear = []
            val = recommend_output(base_dir, 'Jacket', dataset)
            upperwear.append(val)
            val = recommend_output(laki_dir, 'kaos_cowok', dataset)
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(laki_dir, 'Celana_panjang_cowo', dataset)
            bottomwear.append(val)
            val = recommend_output(laki_dir, 'celana_pendek', dataset)
            bottomwear.append(val)

            footwear = []
            val = recommend_output(base_dir, 'sneakers', dataset)
            footwear.append(val)
            val = recommend_output(laki_dir, 'sandal', dataset)
            footwear.append(val)

            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        elif gender == "female" and situation == "non_formal" and fashion_style != "formal":
            upperwear = []
            val = recommend_output(base_dir, 'Jacket', dataset)
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'kaos_cewe', dataset)
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'onepiece', dataset)
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(cewek_dir, 'rok_non', dataset)
            bottomwear.append(val)
            val = recommend_output(cewek_dir, 'cp_cewe', dataset)
            bottomwear.append(val)

            footwear = []
            val = recommend_output(base_dir, 'sneakers', dataset)
            footwear.append(val)
            val = recommend_output(cewek_dir, 'sandal', dataset)
            footwear.append(val)
            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        else:
            return None
