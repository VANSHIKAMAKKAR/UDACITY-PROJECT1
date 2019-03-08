PROJECT LOG ANALYSIS
****************************************The Questions were***************************************
1) What are the most popular three articles of all time?
2)Who are the most popular article authors of all time?
3)On which days did more than 1% of requests lead to errors?
*************************************************************************************************
PREREQUIREMENTS:
Basic understanding of Python,
HTML and CSS
Git
*************************************************************************************************
INSTALLATION AND DOWNLOADING DATABASE:
Download vagrant from the link->->https://www.vagrantup.com/downloads.html
Install it and run vagrant up in command line.Then run vagrant ssh.
The databse of news is provided to us which is having three tables as articles,authors,log.
To download the database of the news use the link->->->->https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
To connect to  the database:
Run psql -d news -f newsdata.sql in command line. 
To access the database run psql news in the command-line.
\dt is used to get the tables of the database.
\d table_name will give the schema of the mentioned table.
****************************************THE FIRST QUERY******************************************
Question:1) What are the most popular three articles of all time?
Solution:
The html code for the first query is written in solution1.py and the queries for it are in solution1_db.py.
We have created the following views and select commands in this:
create view result as select title,concat('/article/',slug) as sl from articles
create view name as select path , count(*) as num from log Join result on result.sl like log.path group by path order by num desc limit 3
select title,num from name Join result on result.sl like name.path order by num desc
How to run?
To run this query go to git run vagrant up and then vagrant ssh.Then cd /vagrant.Then go to the solution directory which contains all the mentioned files.
Run python solution1.py and go to chrome to look for the required port.
Type localhost:8000 on browser
****************************************THE SECOND QUERY******************************************
Question:2)Who are the most popular article authors of all time?
Solution:
The html code for the first query is written in solution2.py and the queries for it are in solution2_db.py.
We have created the following views and select commands in this:
create view result1 as select author,concat('/article/',slug) as sl1 from articles
create view name as select path , count(*) as num from log Join result1 on result1.sl1 like log.path group by path order by num desc
create view name1 as select author,num from name Join result1 on result1.sl1 like name.path order by num desc
select name,sum(num) from name1 Join authors on authors.id=name1.author group by name order by sum desc
How to run?
To run this query go to git run vagrant up and then vagrant ssh.Then cd /vagrant.Then go to the solution directory which contains all the mentioned files.
Run python solution2.py and go to chrome to look for the required port.
Type localhost:8070 on browser
  ****************************************THE THIRD QUERY******************************************
Question:3)On which days did more than 1% of requests lead to errors?
Solution:
The html code for the first query is written in solution3.py and the queries for it are in solution3_db.py.
We have created the following views and select commands in this:
create view status as select date(time) as date1,count(status) as stat from log group by date(time)
create view status4 as select date(time) as date1,status from log where status like '404%'
create view status2 as select date1,count(status) as notf from status4 group by date1
create view status5 as select status2.date1 as fdate,cast(notf as float),cast(stat as float) from status join status2 on status.date1=status2.date1
select fdate,(notf*100)/stat from status5 where (notf*100)/stat > 1
How to run?
To run this query go to git run vagrant up and then vagrant ssh.Then cd /vagrant.Then go to the solution directory which contains all the mentioned files.
Run python solution3.py and go to chrome to look for the required port.
Type localhost:5000 on browser