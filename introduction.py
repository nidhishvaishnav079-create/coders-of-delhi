import json
#Lets write a function to load a data
def load_data (filename):
    with open(filename, "r") as f:
        data1 = json.load(f)
    return data1



# Display users and their connections
def display_users(data):
    print("Users and Their Connections:\n")
    for user in data["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")
    for page in data["pages"]:
        print(f"{page['id']}: {page['name']}")


# Load and display the data
data = load_data("codebook_data.json")
display_users(data)

