# genotickautomation
genotickautomation

This is still very raw and whenever I've had a chance to change things up I did. Rather than using Java I'm using python, Rather than storing the information in files I'm using a database and rather than using a YYYYMMDD dateformat I'm using YYYY-MM-DD ;)<p>
Here's the setup<p>
<h1>Step 1</h1>
Install mariadb or mysql - we're storing a lot of the metadata in that database<p>
Create a user genotick with password mypassword (you can change all that) in that database, here's the syntax I used<p>
<b>GRANT ALL PRIVILEGES ON *.* TO 'genotick'@'localhost' IDENTIFIED BY 'mypassword';</b>
<h1>Step 2</h1>
within mysql create a database called genotick<p>
<b>create database genotick;</b>
then import the genotick.sql file to lay down the table structure<p>
from the command line run<p>
<b>mysql -u root/youruser -p genotick < genotick.sql </b>
Then go into the genotick folder and adjust the w2.ksh file
I've included 3 stocks in the dataset, you can load your own and test it that way on more symbols.

This is my first public github project to be gentle on things :)
