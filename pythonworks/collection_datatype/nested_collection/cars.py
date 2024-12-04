cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torqe"]},
]
print(len(cars))

name=[c.get("name") for c in cars]
print(name)

baleno=[c.get("colors") for c in cars if c.get("name")=="baleno"][0]#[0]is used to avoid two  list!
print(baleno)

# print all brands

all_brand={c.get("brand") for c in cars }#to avoid repeating brands 
print(all_brand) 

amt=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt)

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(blue_cars)

transmission_type={t for c in cars for t in c.get("transmissions")}

print(transmission_type)


all_color={co for c in cars for co in c.get("colors")}
print(all_color)

color_grp=[co for c in cars for co in c.get("colors")]
popular_color={b:color_grp.count(b) for b in color_grp}
print(popular_color)
print(max(popular_color))

costly_car=max(cars,key=lambda c:c.get("price"))
print(costly_car.get("name"))

costly_car=min(cars,key=lambda c:c.get("price"))
print(costly_car.get("name"))

sorted_cars=sorted(cars,key=lambda c:c.get("price"),reverse=True)
sorted_car={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_cars}
print(sorted_car)

