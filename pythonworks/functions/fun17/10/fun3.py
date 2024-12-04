def details(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("cpu"))

details(name="iqoo",price="18000",model="z9x",cpu="snapdragon")