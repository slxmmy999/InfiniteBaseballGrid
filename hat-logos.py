import requests

for x in range(0, 201):
    data = requests.get(f"https://www.mlbstatic.com/team-logos/team-cap-on-dark/{x}.svg")

    if data.status_code == 200:
        try:
            title = data.text.split("<title>")[1].split("</title>")[0]
        except:
            title = f"unknown_team{x}"
        with open(f"./logos/{title}.svg", "wb") as f:
            f.write(data.content)
            print(f"Downloaded {title}.svg")