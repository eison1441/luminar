create database imdb;
use imdb;
create table movie (
					id int primary key auto_increment,
                    title varchar(100) not null,
                    language enum("Malayalam","Tamil","Hindi","Telugu","Kannada"),
                    genre enum("Action","Comedy","Fiction","Love","Drama"),
                    run_time int,
                    rating decimal
					);
alter table movie add column year int not null; 
insert into movie (title,language,genre,run_time,rating,year) values("Premam","Malayalam","love",164,4.5,2015);
insert into movie (title,language,genre,run_time,rating,year) values("Thattathin Marayathu","Malayalam","love",127,4.2,2012);
insert into movie (title,language,genre,run_time,rating,year) values("Minnal Murali","Malayalam","Action",160,4.2,2021);
insert into movie (title,language,genre,run_time,rating,year) values("Bangalore Days","Malayalam","Drama",171,4.4,2014);
insert into movie (title,language,genre,run_time,rating,year) values("Android Kunjappan Version 5.25","Malayalam","Fiction",120,4.3,2019);

-- end of malayalam movies

insert into movie (title,language,genre,run_time,rating,year) values(96,"Tamil","Love",158,4.5,2018);
insert into movie (title,language,genre,run_time,rating,year) values("Baahubali: The Beginning","Tamil","Fiction",160,4.6,2015);
insert into movie (title,language,genre,run_time,rating,year) values("Soorarai Pottru","Tamil","Drama",149,4.8,2020);
insert into movie (title,language,genre,run_time,rating,year) values("Vikram Vedha","Tamil","Action",147,4.4,2017);

-- end of tamil movies


insert into movie (title,language,genre,run_time,rating,year) values("Dilwale Dulhania Le Jayenge","Hindi","Love",190,4.6,1995);
insert into movie (title,language,genre,run_time,rating,year) values("3 Idiots","Hindi","Comedy",170,4.7,2009),
																	("War","Hindi","Action",154,3.2,2019),
                                                                    ("krrish","Hindi","Fiction",175,4.1,2006);
																
-- end of hindi section

insert into movie (title,language,genre,run_time,rating,year) values("Arjun Reddy","Telugu","Love",186,4.3,2017),
																	("Pushpa: The Rise","Telugu","Action",179,4.4,2021),
                                                                    ("Eega","Telugu","Fiction",134,4.5,2012),
                                                                    ("Mahanati","Telugu","Drama",177,4.6,2018);
						
-- end of telugu movies
insert into movie (title,language,genre,run_time,rating,year) values("KGF: Chapter 1","Telugu","Action",156,4.7,2018),
																	("Kirik Party","Telugu","Comedy",165,4.3,2016),
                                                                    ("Lucia","Kannada","Drama",135,4.6,2013),
                                                                    ("KGF: Chapter 1","Kannada","Action",156,4.7,2018),
																	("Kirik Party","Kannada","Comedy",165,4.3,2016),
                                                                    ("Charlie 777","Kannada","Love",136,4.5,2022);
                                                                    
-- Q1)
select title from movie;

-- Q2)
select title from movie where language="Malayalam";

-- Q3)

select title from movie where genre="Action";

-- Q4)

select title from movie where rating>4;

-- Q5)

select title from movie where year>2015;

-- Q6)

select * from movie order by genre;


-- Q7)
select * from movie order by year;