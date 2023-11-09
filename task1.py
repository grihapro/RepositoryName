import json


def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)
    llist = [dictionary["score"] * dictionary["weight"] for dictionary in data]
    return round(sum(llist), 3)


print(task())
