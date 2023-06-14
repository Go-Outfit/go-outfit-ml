import random
import pkg.config.config as config
# uncompleted
import os


laki_dir = "male"
cewek_dir = "female"
base_dir = "."


def recommend_output(gender, category, dataset):
    path = ""
    if category == "jacket" or category == "sneakers":
        gender = "all"
    if gender == "all":
        path = category
    else:
        path = gender+"/"+category
            
    # print(gender)
    # if gender == base_dir:
    #     gender = "all"
    # path = os.path.join(gender, category)
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
    def __init__(self, gender, weather, situation, fashion_style, dataset, conditions):
        self.gender = gender
        self.weather = weather
        self.situation = situation
        self.fashion_style = fashion_style
        self.dataset = dataset
        self.conditions = conditions

    def recommend(self):
        gender = self.gender
        weather = self.weather
        situation = self.situation
        fashion_style = self.fashion_style
        dataset = self.dataset
        conditions = self.conditions

        concat = gender+weather+situation+fashion_style
        key = config.hash_value(concat)
        if key in conditions.keys():
            upperwear = []
            for clothe in conditions[key]["upperwear"]:
                result = recommend_output(gender, clothe, dataset)
                upperwear.append(result)
            bottomwear = []
            for clothe in conditions[key]["bottomwear"]:
                result = recommend_output(gender, clothe, dataset)
                bottomwear.append(result)
            footwear = []
            for clothe in conditions[key]["footwear"]:
                result = recommend_output(gender, clothe, dataset)
                footwear.append(result)
            return {
                "upperwear":upperwear,
                "bottomwear":bottomwear,
                "footwear":footwear,
            }
        else:
            return None

        # if gender == "male" and situation == "formal" and fashion_style == "formal":
        #     upperwear = recommend_output(laki_dir, 'coat-shirt', dataset)
        #     bottomwear = recommend_output(
        #         laki_dir, 'trousers', dataset)
        #     footwear = recommend_output(laki_dir, 'loafers', dataset)
        #     result = {
        #         "upperwear": [upperwear],
        #         "bottomwear": [bottomwear],
        #         "footwear": [footwear],
        #     }
        #     return result
        # elif gender == "female" and situation == "formal" and fashion_style == "formal":
        #     upperwear = []
        #     val = recommend_output(cewek_dir, 'coat-shirt', dataset)
        #     upperwear.append(val)
        #     val = recommend_output(cewek_dir, 'dress', dataset)
        #     upperwear.append(val)

        #     bottomwear = []
        #     val = recommend_output(cewek_dir, 'formal-skirt', dataset)
        #     bottomwear.append(val)
        #     val = recommend_output(cewek_dir, 'trousers', dataset)
        #     bottomwear.append(val)

        #     footwear = []
        #     val = recommend_output(cewek_dir, 'loafers', dataset)
        #     footwear.append(val)
        #     val = recommend_output(cewek_dir, 'heels', dataset)
        #     footwear.append(val)

        #     result = {
        #         "upperwear": upperwear,
        #         "bottomwear": bottomwear,
        #         "footwear": footwear,
        #     }
        #     return result
        # elif gender == "male" and situation == "non_formal" and fashion_style != "formal":
        #     upperwear = []
        #     val = recommend_output(base_dir, 'jacket', dataset)
        #     upperwear.append(val)
        #     val = recommend_output(laki_dir, 'tshirt', dataset)
        #     upperwear.append(val)

        #     bottomwear = []
        #     val = recommend_output(laki_dir, 'trousers', dataset)
        #     bottomwear.append(val)
        #     val = recommend_output(laki_dir, 'pants', dataset)
        #     bottomwear.append(val)

        #     footwear = []
        #     val = recommend_output(base_dir, 'sneakers', dataset)
        #     footwear.append(val)
        #     val = recommend_output(laki_dir, 'slippers', dataset)
        #     footwear.append(val)

        #     result = {
        #         "upperwear": upperwear,
        #         "bottomwear": bottomwear,
        #         "footwear": footwear,
        #     }
        #     return result
        # elif gender == "female" and situation == "non_formal" and fashion_style != "formal":
        #     upperwear = []
        #     val = recommend_output(base_dir, 'jacket', dataset)
        #     upperwear.append(val)
        #     val = recommend_output(cewek_dir, 'tshirt', dataset)
        #     upperwear.append(val)
        #     val = recommend_output(cewek_dir, 'onepiece', dataset)
        #     upperwear.append(val)

        #     bottomwear = []
        #     val = recommend_output(cewek_dir, 'non-formal-skirt', dataset)
        #     bottomwear.append(val)
        #     val = recommend_output(cewek_dir, 'trousers', dataset)
        #     bottomwear.append(val)

        #     footwear = []
        #     val = recommend_output(base_dir, 'sneakers', dataset)
        #     footwear.append(val)
        #     val = recommend_output(cewek_dir, 'slippers', dataset)
        #     footwear.append(val)
        #     result = {
        #         "upperwear": upperwear,
        #         "bottomwear": bottomwear,
        #         "footwear": footwear,
        #     }
        #     return result
        # else:
        #     return None
