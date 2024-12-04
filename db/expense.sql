create database expensedb;
use expensedb;
show databases;
create table Transaction (
							id int primary key auto_increment,
                            title varchar(50) not null,
                            category enum("food","transportation","bills","health","shopping","miscellanious") default "miscellanious",
                            method enum("upi","cash") default "upi",
                            priority enum("need","want") default "need",
                            amount int not null
                            );
alter table Transaction add column  owner varchar(100) not null;
select * from Transaction;
insert into Transaction (title,category,method,priority,amount,owner) value("Break_fast","food","upi","need",190,"akshay");
insert into Transaction (title,category,method,priority,amount,owner) value("Break_fast","food","upi","need",210,"Eiosn");
insert into Transaction (title,category,method,priority,amount,owner) value("Travel","transportation","upi","need",120,"kiran");
insert into Transaction (title,category,method,priority,amount,owner) value("grocery","shopping","upi","want",160,"nandana");
insert into Transaction (title,category,method,priority,amount,owner) value("travel","transportation","cash","need",30,"haritha");
insert into Transaction (title,category,method,priority,amount,owner) value("hostel_fees","bills","cash","want",6500,"aneesh");
insert into Transaction (title,category,method,priority,amount,owner) value("travel","transportation","upi","need",150,"navya");
insert into Transaction (title,category,method,priority,amount,owner) value("grocery","miscellanious","upi","want",400,"mahesh");
select * Transaction;
select * from Transaction;
select count(*) from Transaction where method="upi" and owner="akshay";
select method,sum(amount) as payment_count  from Transaction group by method;
select category,sum(amount)as total from Transaction group by category order by total desc;
select priority,count(*) as total from transaction group by priority order by total;