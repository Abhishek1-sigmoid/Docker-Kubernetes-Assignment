import psycopg2

def insert_entry_to_table():

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()
        add_data = "CREATE TABLE if not exists dag_execution_table(DAG_ID varchar(250), Execution_Date TIMESTAMPTZ);"
        cursor.execute(add_data)
        insert = """insert into dag_execution_table(DAG_ID, Execution_Date) 
        select DAG_ID, Execution_Date from dag_run order by Execution_Date desc limit 1;"""
        cursor.execute(insert)
        conn.commit()

        print("data added to a new table Successfully")
    except Exception as e:
        print("Error in connection", e)
    finally:
        conn.close()
