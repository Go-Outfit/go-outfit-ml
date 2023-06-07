import random
# uncompleted


def recommend_output(dir_path, outfit_type):
    available_images = []  # list of the images in the path
    result_image = []
    for item in range(6):
        img = random.choice(available_images)
        result_image.append(img)
    return result_image


class OutfitRecommender:
    def __init__(self, gender, weather, situation, fashion_style):
        self.gender = gender
        self.weather = weather
        self.situation = situation
        self.fashion_style = fashion_style

    def recommend(self):
        gender = self.gender
        weather = self.weather
        situation = self.situation
        fashion_style = self.fashion_style

        laki_dir = ""
        cewek_dir = ""
        base_dir = ""
        if gender == "male" and situation == "formal" and fashion_style == "formal":
            upperwear = recommend_output(laki_dir, 'Jas_cowok')
            bottomwear = recommend_output(laki_dir, 'Celana_panjang_cowok')
            footwear = recommend_output(laki_dir, 'Pantofel')
            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        elif gender == "female" and situation == "formal" and fashion_style == "formal":
            upperwear = []
            val = recommend_output(cewek_dir, 'Jas_Cewek')
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'Dress')
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(cewek_dir, 'Rok_formal')
            bottomwear.append(val)
            val = recommend_output(cewek_dir, 'Celana_panjang_cewek')
            bottomwear.append(val)

            footwear = []
            val = recommend_output(cewek_dir, 'Pantofel_cewek')
            footwear.append(val)
            val = recommend_output(cewek_dir, 'Heels')
            footwear.append(val)

            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        elif gender == "male" and situation == "non_formal" and fashion_style != "formal":
            upperwear = []
            val = recommend_output(base_dir, 'Jacket')
            upperwear.append(val)
            val = recommend_output(laki_dir, 'Kaos_Laki')
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(laki_dir, 'Celana_panjang_cowok')
            bottomwear.append(val)
            val = recommend_output(laki_dir, 'Celana_pendek_cowok')
            bottomwear.append(val)

            footwear = []
            val = recommend_output(base_dir, 'Sneakers')
            footwear.append(val)
            val = recommend_output(laki_dir, 'Sandal_cowok')
            footwear.append(val)

            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        elif gender == "female" and situation == "non_formal" and fashion_style != "formal":
            upperwear = []
            val = recommend_output(base_dir, 'Jacket')
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'Kaos_Cewek')
            upperwear.append(val)
            val = recommend_output(cewek_dir, 'Onepiece')
            upperwear.append(val)

            bottomwear = []
            val = recommend_output(cewek_dir, 'Rok_nonformal')
            bottomwear.append(val)
            val = recommend_output(cewek_dir, 'Celana_panjang_cewek')
            bottomwear.append(val)

            footwear = []
            val = recommend_output(base_dir, 'Sneakers')
            footwear.append(val)
            val = recommend_output(cewek_dir, 'Sendal_cewek')
            footwear.append(val)
            result = {
                "upperwear": upperwear,
                "bottomwear": bottomwear,
                "footwear": footwear,
            }
            return result
        else:
            return {}
