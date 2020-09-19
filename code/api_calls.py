import requests
import base64
import json


user = 'Bearer'
token = '8c35a7f0a5cf41a8d7e4c924e60dc7a04f08d006'
# headers1 = {'Authorization': f'{user} {token}'}
# r1 = requests.get('https://api-beta.bite.ai/meals/',
#                         headers = headers1)
# #print(r1.text)
def food_recognition(path, user, token):
    """Food recognition request with picture. Takes path to image and returns
    annotations."""
    img_path = path

    food_rec_url = "https://api-beta.bite.ai/vision/"

    with open(img_path, "rb") as img:
        img_base64 = base64.b64encode(img.read())
        img_base64 = img_base64.decode("utf-8")

    headers2 = {
        'Content-type': 'application/json',
        'Authorization': f'{user} {token}'
    }

    data = {
        'base64': img_base64
    }

    r2 = requests.post(url = food_rec_url, json = data, headers = headers2)

    image_data = json.loads(r2.text)
    food_items = {}
    for item in image_data['items']:
        children = []
        name = item['item']['name']
        #print(name, '\nchildren:')
        for child in item['item']['children']:
            children.append(child['name'])
            #print('\t',child['name'])
        food_items[name] = children
        #print('\n')
    print(food_items)
    return(food_items, image_data)

def nutrition_values(image_data, subclasses):
    # this somehow needs to get the user input for each subclass
    # get calories and macronutrients for chosen subclasses
    pass


food_items, image_data = food_recognition("/mnt/c/hackzurich2020-17/media/meat.JPG", user = user, token = token)
