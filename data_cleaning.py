#Task 1: Identify Issues in the Data
#Your manager provides you with an example dataset where some records are incomplete or incorrect. Here’s an example:
#Load the data
import json

def clean_data(data):

    # Remove users whose name is empty
    data["users"] = [
        user for user in data["users"]
        if user["name"].strip()
    ]

    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Keep users who have friends OR liked pages
    data["users"] = [
        user for user in data["users"]
        if user["friends"] or user["liked_pages"]
    ]

    # Remove duplicate pages
    unique_pages = {}

    for page in data["pages"]:
        unique_pages[page["id"]] = page

    data["pages"] = list(unique_pages.values())

    return data
data = json.load(open("data.json"))
data = clean_data(data)
json.dump(data,open("clean_data.json","w"),indent=4)

