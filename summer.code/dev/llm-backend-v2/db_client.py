import pymysql
from config import DATABASE_USER, DATABASE_PORT, DATABASE_HOST, DATABASE_PSW, DATABASE_NAME
class DbClient:
        def __init__(self):
                pass

        def store_messages(self, room_name, sender_name, content):
                db = pymysql.connect(
                        host=DATABASE_HOST,
                        port=DATABASE_PORT,
                        user=DATABASE_USER,
                        password=DATABASE_PSW,
                        database=DATABASE_NAME
                )
                # Create a cursor object
                try:
                        with db.cursor() as cursor:

                                sql = """
                                    INSERT INTO messages (room_name, sender_name, content, create_time) 
                                    VALUES (%s, %s, %s, NOW())
                                """
                                print(sql)
                                # Execute the query
                                cursor.execute(sql, (room_name, sender_name, content))
                                db.commit()  #
                                # Check if the table exists
                                if cursor.rowcount == 1:
                                        print("Insert successful")
                                else:
                                        print("Insert failed")
                except pymysql.Error as e:
                        print(f"Error connecting to MySQL: {e}")
                        return False
                finally:
                        if db:
                                db.close()