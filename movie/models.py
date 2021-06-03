from django.db import models
import cx_Oracle
# Create your models here.

def getConnection():
    try:
         conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
        print(e)
    return conn

def movie_detail(mno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT mno,title,poster,regdate,genre,grade,story,key
            FROM daum_movie 
            WHERE mno={mno}
          """
    cursor.execute(sql)
    movie_data=cursor.fetchone()
    md=(movie_data[0],movie_data[1],movie_data[2],movie_data[3],movie_data[4],movie_data[5],movie_data[6].read(),movie_data[7])
    cursor.close()
    conn.close()
    return md

