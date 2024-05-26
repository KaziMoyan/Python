#d1 ={}
#print(type(d1))
#d2 = {"Moyeen":"Egg","kazi":"Burger","Sakil":"Water"}
#print(d2)
#print(d2["Moyeen"])
d2 = {"Moyeen":"Egg","kazi":"Burger","Sakil":"Water",
      "Sunny" : {"B": "Water","L":"Roti", "D" :"chicken"}
      }
d2["Ankit"] ="junk Food"
d2[420] = "Kababs"
print(d2)
del d2[420]


#print(d2["Sunny"])
print(d2)
d3 = d2
del d3["Moyeen"]
print(d2.copy())
d2.update({"kazi":"Orange"})
print(d2)
print(d2.keys())


