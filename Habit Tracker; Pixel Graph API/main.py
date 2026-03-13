import requests
from datetime import datetime as dt


USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph1"

# ----------- CREATING PIXEL ACCOUNT
pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# pixela_response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(pixela_response.text)


# ---------- CREATING A PIXEL GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_response.text)


# ----------- POSTING A PIXEL
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.now()
# Remember to change the date, to your preferred date. -today- stores the latest update date for this code.
today_y_m_d_format = today.strftime("%Y%m%d")
post_parameters = {
    "date": today_y_m_d_format,
    "quantity": input("How many kilometers did you cycle today? "),
}
post_response = requests.post(url=post_endpoint, json=post_parameters, headers=headers)
print(post_response.text)


# ---------- UPDATING A PIXEL
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_y_m_d_format}"
# Remember to change the date, to your preferred date. -today- stores the latest update date for this code.

update_parameters = {
    "quantity": "5.0",
}
# update_response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(update_response.text)


# ----------- DELETING A PIXEL
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_y_m_d_format}"
# Remember to change the date, to your preferred date. -today- stores the latest update date for this code.

# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)
