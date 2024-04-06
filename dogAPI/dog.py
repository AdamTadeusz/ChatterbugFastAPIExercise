from fastapi import Response
import requests

def dog_breed_list():
    request_url = "https://dog.ceo/api/breeds/list/all"
    try:
        request_return = requests.get(request_url).json()
        return request_return
    except requests.exceptions.RequestException as e:
        return {"message": "An exception has occured", "status": "error"}

def dog_picture(breed: str=None, sub_breed: str=None):
    request_url = "https://dog.ceo/api/breeds/image/random"
    if (not sub_breed and breed):
        request_url = "https://dog.ceo/api/breed/{0}/images/random".format(breed)
    if (sub_breed and breed):
        request_url = "https://dog.ceo/api/breed/{0}/{1}/images/random".format(breed, sub_breed)

    # get url of random image
    try:
        request_return = requests.get(request_url).json()
        image_url = request_return["message"]
        status = request_return["status"]
        if (status == "error"):
            data = "<!DOCTYPE html><html><body><img src='' alt='{0}'></body></html>".format(image_url)
        else:
            data = "<!DOCTYPE html><html><body><img src='{0}' alt='{0}'></body></html>".format(image_url)
        return Response(content=data)
    except requests.exceptions.RequestException as e:
        return {"message": "An exception has occured", "status": "error"}