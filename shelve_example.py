import shelve


class Pry:
    def __init__(self, name):
        self.name = name


Serik = Pry("Serik")

FILENAME = "states2"

# with shelve.open(FILENAME) as states:
#     states["London"] = "Great Britain"
#     states["Paris"] = Serik
#     states["Berlin"] = "Germany"
#     states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    key = "Paris"
    # obj = states.get(key)
    #
    # p = obj.name if isinstance(obj, Pry) else None
    # print(p)
    if key in states:
        value = states[key]

        if type(value) == Pry or isinstance(value, Pry):
            print(states[key].name)
    print(states["Madrid"])

    for value in states.values():
        print(value)
    for key in states.keys():
        print(key)
    for item in states.items():
        print(item)