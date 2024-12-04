from json import load
f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\countries.json",encoding="utf-8")
data=load(f)
# print(len(data))
all_country_name=[country.get("name") for country in data]
# print(all_country_name)
all_regions=[country.get("region") for country in data]
# print(set(all_regions))
region_count={region:all_regions.count(region) for region in all_regions}
# print(region_count)
max_region=max(region_count,key=lambda k:region_count.get(k))
# print(max_region,region_count.get(max_region))
capital=[country.get("capital") for country in data if country.get("name")=="India" ]
# print(capital)

# boders=[country.get("borders") for country in data ]
# max_border=max()
border_count={country.get("name"):len(country.get("borders",[] )) for country in data }
# print(border_count)

max_border_count=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border_count,border_count.get(max_border_count))


population={country.get("name"):country.get("population") for country in data}

max_population=max(data,key=lambda country:country.get("population")).get("name")
print(max_population,population.get(max_population))


india_border=[country.get("borders") for country in data if country.get("name")=="India"][0]
for code in india_border:
    for country in data:
        if country.get("alpha3Code")==code:
            print(country.get("name"))





# from json import load


# f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\datasets\\countries.json",encoding="utf-8")

# data=load(f)

# # print number of countries
# # print(len(data))

# # /print all country names

# all_country_names=[country.get("name") for country in data ]

# # print(all_country_names)

# # print all regions

# all_regions=[country.get("region") for country in data ]

# # print(set(all_regions))

# region_count={region:all_regions.count(region) for region in all_regions}
# # print(region_count)

# # printing maximum region count

# max_region_count=max(region_count,key=lambda k:region_count.get(k))

# # print(max_region_count,region_count.get(max_region_count))

# # capital of India

# country_capital=[country.get("capital") for country in data if country.get("name")=="India"]


# # print(country_capital)


# # countries with most number of borders

# # country_borders={country.get("name"):len(country.get("borders",[])) for country in data}

# # print(country_borders)


# max_border_count=max(data,key=lambda country: len(country.get("borders",[]))).get("name")

# # print(max_border_count)


# # most populated country


# most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")
# # print(most_populated_country)



# aplfa_three_codes=[country.get("borders") for country in data if country.get("name")=="Afghanistan"][0]

# for code in aplfa_three_codes:

#     for country in data:

#         if country.get("alpha3Code")==code:

#             print(country.get("name"))