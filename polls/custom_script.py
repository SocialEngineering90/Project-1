# custom_script.py
import sqlite3

#The fixing of this issue is to have no outdated library like this
#from updated_library import secure_function
from outdated_library import outdated_function  # Introduced an outdated or insecure library intentionally

#Fix of FLAW 1: Injection
#def get_user(user_id):
#    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))

def get_user(user_id):
    connection = sqlite3.connect('/workspaces/codespaces-blank/project1-cyber-security-base-2023/mysite/db.sqlite3')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    result = cursor.fetchall()
    connection.close()
    return result
