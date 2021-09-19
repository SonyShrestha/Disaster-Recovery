1) dags folder contains Dag program with required config. This code should be added inside dags folder. 

2) core folder contains shell script to create database backup. This code should be placed in some location location of which should be provided in config.

3) Make required changes in configuration file inside dags/Create_Backup/config/config.json.
Specify the connection url, location of backup script and comma seperated list of databases for which backup needs to be created.

4) Execute create_backup dag either from command line or UI.
 