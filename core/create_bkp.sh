#!/bin/bash
host=$1
user_name=$2
password=$3
source_database=`echo $4 | sed 's/,/ /g'`
path=$5
my_cnf_path=$6

cd $path
mkdir {ddl,variables,mycnf,database}

cd $path/database

rm -rf *.sql.gz
#echo $source_database
for db in $source_database
do
echo $source_database
mysqldump --user=$user_name --host=$host --password=$password --routines --skip-opt $db |gzip> $db'_'$(date +'%Y-%m-%d').sql.gz
done

cd $path/ddl
rm -rf *.sql.gz
#echo $source_database
for db in $source_database
do
echo $source_database
mysqldump --user=$user_name --host=$host --password=$password --routines --no-data --skip-opt $db |gzip> $db'_'$(date +'%Y-%m-%d').sql.gz
done

cd $path/mycnf
#echo Please Provide complete my.cnf path
rm -rf *.cnf
cp $my_cnf_path $path/mycnf/mycnf_backup_`date +"%Y%m%d"`.cnf 

cd $path/variables
rm -rf *.sql.gz
mysqldump --user=$user_name --host=$host --password=$password performance_schema global_variables |gzip> 'global_variable_'$(date +'%Y-%m-%d').sql.gz
mysqldump --user=$user_name --host=$host --password=$password performance_schema session_variables |gzip> 'session_variable_'$(date +'%Y-%m-%d').sql.gz
