import os
import re

from lib.rules.enums import DBMS

def Read(name):
    # 定义一个空列表
    lines = []

    # 打开文件并读取内容
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            # 去掉每行的换行符并添加到列表中
            lines.append(line.strip())

    # 输出结果
    print(lines)

    return lines

current_dir = os.path.dirname(os.path.abspath(__file__))
def GetSqlErr():
    errors = []
    sqlerror=current_dir+'/../../resources/sql_errors.txt'
    RData=Read(sqlerror)
    for line in RData:
        errors.append((line, DBMS.MSSQL))

    return errors
def Get_sql_errors():
    errors = []
    # ASP / MSSQL
    errors.append(('System\.Data\.OleDb\.OleDbException', DBMS.MSSQL))
    errors.append(('\[SQL Server\]', DBMS.MSSQL))
    errors.append(('\[Microsoft\]\[ODBC SQL Server Driver\]', DBMS.MSSQL))
    errors.append(('\[SQLServer JDBC Driver\]', DBMS.MSSQL))
    errors.append(('\[SqlException', DBMS.MSSQL))
    errors.append(('System.Data.SqlClient.SqlException', DBMS.MSSQL))
    errors.append(('Unclosed quotation mark after the character string', DBMS.MSSQL))
    errors.append(('mssql_query\(\)', DBMS.MSSQL))
    errors.append(('odbc_exec\(\)', DBMS.MSSQL))
    errors.append(('Microsoft OLE DB Provider for ODBC Drivers', DBMS.MSSQL))
    errors.append(('Microsoft OLE DB Provider for SQL Server', DBMS.MSSQL))
    errors.append(('Incorrect syntax near', DBMS.MSSQL))
    errors.append(('Sintaxis incorrecta cerca de', DBMS.MSSQL))
    errors.append(('Syntax error in string in query expression', DBMS.MSSQL))
    errors.append(('ADODB\.Field \(0x800A0BCD\)<br>', DBMS.MSSQL))
    errors.append(("Procedure '[^']+' requires parameter '[^']+'", DBMS.MSSQL))
    errors.append(("ADODB\.Recordset'", DBMS.MSSQL))
    errors.append(("Unclosed quotation mark before the character string", DBMS.MSSQL))

    # DB2
    errors.append(('DB2 SQL error:', DBMS.DB2))
    errors.append(('internal error \[IBM\]\[CLI Driver\]\[DB2/6000\]', DBMS.DB2))
    errors.append(('SQLSTATE=\d+', DBMS.DB2))
    errors.append(('\[CLI Driver\]', DBMS.DB2))

    # Sybase
    errors.append(("Sybase message:", DBMS.SYBASE))

    # Access
    errors.append(('Syntax error in query expression', DBMS.ACCESS))
    errors.append(('Data type mismatch in criteria expression.', DBMS.ACCESS))
    errors.append(('Microsoft JET Database Engine', DBMS.ACCESS))
    errors.append(('\[Microsoft\]\[ODBC Microsoft Access Driver\]', DBMS.ACCESS))

    # ORACLE
    errors.append(('(PLS|ORA)-[0-9][0-9][0-9][0-9]', DBMS.ORACLE))

    # POSTGRE
    errors.append(('PostgreSQL query failed:', DBMS.POSTGRE))
    errors.append(('supplied argument is not a valid PostgreSQL result', DBMS.POSTGRE))
    errors.append(('pg_query\(\) \[:', DBMS.POSTGRE))
    errors.append(('pg_exec\(\) \[:', DBMS.POSTGRE))

    # MYSQL
    errors.append(('supplied argument is not a valid MySQL', DBMS.MYSQL))
    errors.append(('Column count doesn\'t match value count at row', DBMS.MYSQL))
    errors.append(('mysql_fetch_array\(\)', DBMS.MYSQL))
    #errors.append(('mysql_', DBMS.MYSQL))
    errors.append(('on MySQL result index', DBMS.MYSQL))
    errors.append(('You have an error in your SQL syntax;', DBMS.MYSQL))
    errors.append(('You have an error in your SQL syntax near', DBMS.MYSQL))
    errors.append(('MySQL server version for the right syntax to use', DBMS.MYSQL))
    errors.append(('\[MySQL\]\[ODBC', DBMS.MYSQL))
    errors.append(("Column count doesn't match", DBMS.MYSQL))
    errors.append(("the used select statements have different number of columns", DBMS.MYSQL))
    errors.append(("Table '[^']+' doesn't exist", DBMS.MYSQL))

    # Informix
    errors.append(('com\.informix\.jdbc', DBMS.INFORMIX))
    errors.append(('Dynamic Page Generation Error:', DBMS.INFORMIX))
    errors.append(('An illegal character has been found in the statement', DBMS.INFORMIX))

    errors.append(('<b>Warning</b>:  ibase_', DBMS.INTERBASE))
    errors.append(('Dynamic SQL Error', DBMS.INTERBASE))

    # DML
    errors.append(('\[DM_QUERY_E_SYNTAX\]', DBMS.DMLDATABASE))
    errors.append(('has occurred in the vicinity of:', DBMS.DMLDATABASE))
    errors.append(('A Parser Error \(syntax error\)', DBMS.DMLDATABASE))

    # Java
    errors.append(('java\.sql\.SQLException', DBMS.JAVA))
    errors.append(('Unexpected end of command in statement', DBMS.JAVA))

    # Coldfusion
    errors.append(('\[Macromedia\]\[SQLServer JDBC Driver\]', DBMS.MSSQL))

    # Generic errors..
    errors.append(('SELECT .*? FROM .*?', DBMS.UNKNOWN))
    errors.append(('UPDATE .*? SET .*?', DBMS.UNKNOWN))
    errors.append(('INSERT INTO .*?', DBMS.UNKNOWN))
    errors.append(('Unknown column', DBMS.UNKNOWN))
    errors.append(('where clause', DBMS.UNKNOWN))
    #errors.append(('SqlServer', DBMS.UNKNOWN))

    Getlist_key=GetSqlErr()
    merged_errors = errors + Getlist_key
    # 去重并保持顺序
    unique_errors = []
    seen = set()

    for error in merged_errors:
        if error not in seen:
            seen.add(error)
            unique_errors.append(error)

    sql_errors = []
    for re_string, DBMS_type in unique_errors:
        sql_errors.append((re.compile(re_string, re.IGNORECASE), DBMS_type))
    return sql_errors
