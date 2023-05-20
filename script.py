import snowflake.connector
import logging
import os
import time
from snowflake.connector import SnowflakeConnection
from snowflake.connector.cursor import SnowflakeCursor
class SnowflakeIntegration:
    def displayData(self, data:list[dict]):
        for item in data:
            print(item)
    def run(self):
        user:str=os.getenv("SNOWFLAKE_USER")
        password:str=os.getenv("SNOWFLAKE_PASSWORD")
        account:str=os.getenv("SNOWFLAKE_ACCOUNT")
        role:str = os.getenv("SNOWFLAKE_USER_ROLE","USERADMIN")
        warehouse:str="COMPUTE_WH"
        database:str="SNOWFLAKE_SAMPLE_DATA"
        schema:str="TPCH_SF1"
        page_size: int = 10
        log_file_name:str="snowflake_connector.log"

        logging.basicConfig(
            filename=log_file_name,
            level=logging.ERROR)

        try:
            conn:SnowflakeConnection = snowflake.connector.connect(
                user=user,
                password=password,
                account=account,
                warehouse=warehouse,
                database=database,
                schema=schema,
            )
            cursor:SnowflakeCursor = conn.cursor().execute("USE ROLE "+role)
            sql_query:str = '''
            SELECT * FROM CUSTOMER LIMIT 25
            '''
            cursor.execute_async(sql_query)
            query_id:str = cursor.sfqid
            print('*******************************************************************************')
            while conn.is_still_running(conn.get_query_status(query_id)):
                print("{} query still running".format(query_id))
                time.sleep(1)
            logging.info(conn.get_query_status(query_id))
            cursor.get_results_from_sfqid(query_id)
            data:list[dict] = cursor.fetchmany(page_size)
            print('*******************************************************************************')
            self.displayData(data)
            while(len(data)>0):
                data:list[dict] = cursor.fetchmany(page_size)
                self.displayData(data)
        except ValueError as e:
            logging.error(e)
        except snowflake.connector.errors.ProgrammingError as e:
            logging.error(e)
        except Exception as e:
            logging.critical(e)
        finally:
            conn.close()

snow:SnowflakeIntegration = SnowflakeIntegration()
snow.run()