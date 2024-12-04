create database landDb;
use landDb;
create table property(
						place varchar(100) not null,
                        property_type varchar(100) not null,
                        bed_room_count int,
                        price decimal,
                        square_footage decimal   
);
select * from property;
insert into property (place,property_type,bed_room_count,price,square_footage) value("kakkanad","villa",3,300000,8000);
insert into property (place,property_type,bed_room_count,price,square_footage) value("kakkanad","villa",2,315000,5000);
insert into property (place,property_type,bed_room_count,price,square_footage) value("mavelipuram","apartment",5,500000,9000);
insert into property (place,property_type,bed_room_count,price,square_footage) value("mavelipuram","apartment",3,250000,2000);
insert into property (place,property_type,bed_room_count,price,square_footage) value("chengannur","villa",5,350000,3000);
insert into property (place,property_type,bed_room_count,price,square_footage) value("chengannur","apartment",5,450000,3500);
select * from property where bed_room_count >=2 and price <500000;
select max(price) from property;
select * from property where bed_room_count=2;
select * from property where property_type="villa";
select min(square_footage) from property;
use landDb;