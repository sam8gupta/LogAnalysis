## LogAnalysis
### An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Installation
Before you start, you need to following softwares installed in your computer.
If not, download them from the given links:

<a href="https://www.vagrantup.com/">Vagrant</a> -- Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.

<a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1">VirtualBox</a> -- VirtualBox is the software that actually runs the virtual machine.

From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

<a href="https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip">VirtualMachine</a> -- This will give you a directory called FSND-Virtual-Machine.

<a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">Data</a> -- The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To use the reporting tool, you'll need to load the site's data into your local database.

To load the data, login to the VM, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

Now download the project zip files, extract them to a folder which is shared with your virtual machine.

To run the project on mac, open `Terminal` and login to the VM, cd into the vagrant directory and use the command `python answers.py`

## Conclusion

Here is the description of the files in the project:

`answers.py` file contains a Python program using the psycopg2 module to connect to the database prints out reports (in plain text) based on the data in the database.

`answers.txt` file contains the output of the project.

## Note
Followings views must be created before using the reporting tool.

`create view vw_ArticleDetails as 
 select concat('/article/',slug) as location, title, author
 from articles;`
 
 
 `create view vw_ArticleRequests as 
 select path, status 
 from log where path in (select location from vw_ArticleDetails);`
 
 
 `create view vw_Requests 
 as select count(*), status, TO_CHAR(cast(time as date) :: DATE, 'Mon dd, yyyy') as date 
 from log 
 group by date, status;`

To create a view in the database:
1. Open `Terminal`.
2. Login to the VM by running `vagrant up` followed by `vagrant ssh`.
3. Connect to the news database by running `psql news`.
4. Run the create view queries and you are done.
