movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vaazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]


print(len(movies))

title=[m.get("title")for m in movies]
print(title)

mal=[m.get("title") for m in movies if m.get("language")=="malayalam"]
print(mal)

least_run_time=min(movies,key=lambda m:m.get("run_time"))
print("movie with minimum runtime >>> ",least_run_time.get("title"))

maximum_run_time=max(movies,key=lambda m:m.get("run_time"))
print("movie with maximum run time >>> ",maximum_run_time.get("title"))

same_release_date=[m.get("title") for m in movies if m.get("year")==2024]
print(same_release_date)

all_language=[m.get("language") for m in movies]
language_count={m:all_language.count(m) for m in all_language}
print(language_count)