class Movie:
    id:int

    name:str

    hero:str

    director:str

    duration:int

    genre:str

    releasing_year:int

    def __init__(self,id,name,hero,director,duration,genre,releasing_year):

        self.id=id

        self.name=name

        self.hero=hero

        self.director=director

        self.duration=duration

        self.genre=genre

        self.releasing_year=releasing_year

    def display_movie(self):
        print(self.id,self.name,self.hero,self.director,self.duration,self.releasing_year)


Movie_instance1=Movie()
Movie_instance2=Movie()
Movie_instance1.__init__(1,"ARM","tovino","Jithin Lal",150,"action adventure",2024)
Movie_instance1.display_movie()
Movie_instance2.__init__(2,"KGF chapter1","Yash","Prashanth Neel",154,"action",2018)
Movie_instance2.display_movie()



# constructor is used to iinitialize the attributes of the object.