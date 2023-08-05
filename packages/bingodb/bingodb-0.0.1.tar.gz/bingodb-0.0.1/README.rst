Aquesa Bingo DB is a lightweight postgresql adapter written on top of psycopg2 module for flask developers to facilitate postgresql database connectivity in not less then 1 line, i.e., connecting to database is now only 1 line of code. In future versions, multiple databases connectivity possibility will be added.

# Connection Example

```
import bingodb

bingodb.BingoDB().db_connect(database="database_name", credentials={"USER":'your username here', "PASSWORD":'your password here'})
```

# Operation Example
```
bingodb.BingoDB().db_operation(operationName="insert", tablename="your tablename here", columns=["your column name(s) here (only string(s))"], values=["your column value(s) here (only string(s))"])
```

# Command Example
```
bingodb.BingoDB().db_operation(command="truncate table your_table_name;")
```