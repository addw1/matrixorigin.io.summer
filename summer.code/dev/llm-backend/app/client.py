import pymysql
from .config import Config

class DbClient:
        def __init__(self):
                pass

        def check_table_exists(self, db_name,table_name):
                config = Config()
                db = pymysql.connect(
                        host=config.DATABASE_HOST,
                        port=config.DATABASE_PORT,
                        user=config.DATABASE_USER,
                        password=config.DATABASE_PSW,
                )
                # Create a cursor object
                try:
                        with db.cursor() as cursor:
                                # SQL query to check if the table exists
                                sql = f"""
                                    SELECT COUNT(*)
                                    FROM information_schema.tables
                                    WHERE table_schema = %s
                                    AND table_name = %s
                                    """
                                # Execute the query
                                cursor.execute(sql, (db_name, table_name))
                                # Fetch the result
                                result = cursor.fetchone()
                                # Check if the table exists
                                if result[0] == 1:
                                        return True
                                else:
                                        return False
                except pymysql.Error as e:
                        print(f"Error connecting to MySQL: {e}")
                        return False
                finally:
                        if db:
                                db.close()

        def store_messages(self, room_name, sender_name, content):
                config = Config()
                db = pymysql.connect(
                        host=config.DATABASE_HOST,
                        port=config.DATABASE_PORT,
                        user=config.DATABASE_USER,
                        password=config.DATABASE_PSW,
                )
                # Create a cursor object
                try:
                        with db.cursor() as cursor:

                                sql = """
                                    INSERT INTO messages (room_name, sender_name, content, create_time) 
                                    VALUES (%s, %s, %s, NOW())
                                """
                                # Execute the query
                                cursor.execute(sql, (room_name, sender_name, content))
                                # Fetch the result
                                result = cursor.fetchone()
                                # Check if the table exists
                                if result[0] == 1:
                                        return True
                                else:
                                        return False
                except pymysql.Error as e:
                        print(f"Error connecting to MySQL: {e}")
                        return False
                finally:
                        if db:
                                db.close()