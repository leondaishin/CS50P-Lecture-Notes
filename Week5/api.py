# api is a way to take information out of a website and put into this code
# importing requests for asking info from the website 
import requests

def main(): 
    try: 
        # requesting and GETTING the info from the URL 
        response = requests.get("https://api.artic.edu/api/v1/artsworks/search")
        response.raise_for_status()
    except requests.HTTPError: 
        print("Could not complete request. ")
        return

    # since the response defined here is only the info amount printed we need the actual information 
    # json is the way to convert the info from response
    content = response.json()
    # reading json is complex 
    # we make it easier to make the printed text easier 
    for artwork in content["data"]:
        print(f"* {artwork['title']}") 
   





main()