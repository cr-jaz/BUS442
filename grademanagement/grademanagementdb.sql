use project4db;

create table studentinfo (
	studentid int primary key,
    studentname varchar(45),
    studentscore int);
    
-- DB creations statement
create user 'projectuser'@'localhost' identified by 'projectuser';

-- Grant required privileges to the DB user
grant all privileges on project4db.* to 'projectuser'@'localhost';

select * from studentinfo;