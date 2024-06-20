from sqlalchemy import text
from db.mysql_db import Session

def search_user_detail_list():
    session = Session()
    sql = text('''
        SELECT
            u.user_id, u.username, u.first_name, u.last_name, u.gender, u.password, u.status
        FROM user_details u
    ''')

    cursor = session.execute(sql)
    result = cursor.fetchall()
    return result
