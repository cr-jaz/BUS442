use finalprojectdb;

create table book_sales (
	transactionid int primary key, 
    customername varchar(100),
    booktitle varchar(100),
    quantity int,
    total int);
    
create user 'finaluser'@'localhost' identified by 'finaluser';
grant all privileges on finalprojectdb.* to 'finaluser'@'localhost';


SELECT * FROM book_sales;
