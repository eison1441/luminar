-- create database augdb;
-- show database;
-- use augdb;
create table student(
						id int primary key auto_increment,
                        name varchar(100) not null,
						course varchar(100) not null,
                        total int not null
					);
-- insert into table_name (field,field,field) value(value1,value2,value3)
insert into student(name,course,total) value("hari","Django",450);
insert into student(name,course,total) value("vipin","Django",475);
insert into student(name,course,total) value("Eison","Django",480);
insert into student(name,course,total) value("fathima","Django",475); 
insert into student(name,course,total) value("alljo","asp",475);
insert into student(name,course,total) value("abhishek","asp",500);

select * from student;

select name from student;
select name,course from student;
-- augdbaugdbselect distinct course from student;

select * from student where course="Django";


select * from student where total=450;
select * from student where total>450;
select * from student where course!="Django";
select  min(total) from student;
select max(total) from student;
select  avg(total) from student;
select  count(total) from student;

select max(total) from student;
select max(total) from student where total !=(select max(total) from student);

select name from student where total =(select max(total) from student);
select name from student where total!=(select max(total) from student where total !=(select max(total) from student));
select name from student where total=(select max(total) from student where total !=(select max(total) from student));

update student set total=550 where id =3;
select *from student where id=3;
update student set course="asp",total=520 where id=4;
select * from student where id=4;


insert into student(name,course,total) value("abhishekpp","asp",570);

select course,count(*) as stcount from student group by course;
select course,count(*) as stcount from student group by course having stcount >3
-- select course,count(*) as studcount from student group by course order by studcount desc;
select course,count(*) as studcount from student group by course order by studcount desc;

alter table student add column cgpa varchar(30) default 5;
select * from student;
