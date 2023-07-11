import requests

for x in range(0, 201):
    data = requests.get(f"https://www.mlbstatic.com/team-logos/team-cap-on-dark/{x}.svg")

    if data.status_code == 200:
        try:
            title = data.text.split("<title>")[1].split("</title>")[0]
            print(title, f"({x})")
        except:
            title = f"unknown_team{x}"
            print(title, f"({x})")