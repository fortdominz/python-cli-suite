import requests


USERNAME = "fortdominz"
url = f"https://api.github.com/users/{USERNAME}/repos"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{USERNAME} has {len(data)} public repositories:")
    
    for repo in data:
        print(f"{repo['description']}")
    
else:
    print(f"Error Retrieving reposotory data")
