#Dictionary is key value pair

d1 = {}
print(type(d1))

rank = {
    "rip": 1,
    "sophi": [2, {"art":1}],
    "lauren":4,
    "bell":3
}

#access elenment form list
print(rank["rip"])
print("rank in art is:- ", rank["sophi"][1]["art"])

#add in distionary
rank["sam"] = 5
print(rank)

#remove from dist
del rank["sam"]
print(rank)

#dictionary is pointer so changee in d2 = d1 will change all
#to avoid co[y issue use .copy method to create copy of dictionary]

#using ,get() in dict
print(rank.get("rip"))

#.update
rank.update({"jules": 6})
print(rank)

#update  existing key value pair
rank["jules"] = 10
print(rank)

#.keys
print(rank.keys())

#.items
print(rank.items())

"""
Dbt
#.values
print(rank.values)
"""

#python dictionay funtion documentation