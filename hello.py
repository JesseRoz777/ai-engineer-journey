customers = [
    {"name": "Maria", "country": "Spain", "active": True},
    {"name": "Tom", "country": "UK", "active": False},
    {"name": "Yuki", "country": "Japan", "active": True},
]

for customer in customers:
    if customer["active"]:
        print(customer["name"])
