
def connectToSQL (): 

            #Import Modules
            import pandas as pd
            import mysql.connector
            import sqlalchemy 
            from sqlalchemy import create_engine, types, sql
            
                                 
            conn = mysql.connector.connect(user='Test', password='Test', host='127.0.0.1', Port=11, database='AutoAusschreibung')
            print("Connection successfully ")
            cur = conn.cursor()
            

            