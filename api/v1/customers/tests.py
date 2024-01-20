import requests

for i in range(1000):
    r = requests.get("https://octagonleague.com/fighter/mukhamadzhon-kurbanov")
    print(r)
