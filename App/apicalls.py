import requests
import time


# calls to Api to receive the aurora hunt locations
def get_aurora_locations():
    locations_list = {}
    location = requests.get("http://api.auroras.live/v1/?type=locations").json()

    # loop narrows the information to the name and description data
    for i in range(len(location) - 1):
        name = location[str(i)]["name"]
        decription = location[str(i)]["description"]
        locations_list[name] = decription
    # returns simplified data
    return locations_list


# calls to API to get data on individuals in the International Space Station
def get_people_in_ISS():
    people_in_ISS = []
    space_people = requests.get("http://api.open-notify.org/astros.json").json()
    # this filters the people who are in the ISS specifically.
    for i in space_people["people"]:
        if i["craft"] == "ISS":
            people_in_ISS.append(i["name"])
    return people_in_ISS


# Retrieves Aurora Image data from the API
def get_aurora_images_info():
    images_info = {}
    images_json = requests.get("http://api.auroras.live/v1/?type=images&action=list").json()

    # sorts through data to get id and name values
    for i in images_json["images"]:
        id = images_json["images"][i]["id"]
        name = images_json["images"][i]["name"]
        images_info[id] = name
    return images_info


# Calls to API and downloads image
def get_aurora_image(value):
    image = requests.get("http://api.auroras.live/v1/?type=images&image=" + value)
    file = open("C:/Users/Owner/Desktop/Coding Programs/Coding/Python/APIProject/App/static/" + value + ".png", "wb")
    file.write(image.content)
    file.close()
    # Program waits so the image can have time downloading before it is posted in html
    time.sleep(2)
