# Project-1

## Introduction





----

# FLAW 1: Injection

**Link pinpointing flaw 1: ** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L11

**Description of the flaw. **
In this first flaw, I am trying to address a SQL Injection in the python code in the backend and recommend a fix using parameterized queries or prepared statements. 

`def get_user(user_id):`
    `cursor.execute(f"SELECT * FROM users WHERE id={user_id}")`

The code like this is vulnerable to SQL injection because it directly includes user input in the SQL query. 

**How to fix it.**

To fix this issue, it is enough to use parameterized queries or prepared statements to ensure proper data validation and sanitization. Because this helps prevent SQL injection by ensuring that user input is treated as data and not as part of the SQL statement. Like: 

`def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))`

# FLAW 2: Broken Access Control

# FLAW 3: Insecure Dependencies

# FLAW 4: Insufficient Logging and Monitoring

# FLAW 5: Security Misconfiguration


----
# Credits
This project was developed by myself as part of the mooc course https://cybersecuritybase.mooc.fi/

Thank you to teacher Nikolaj Tatti for clarification and assistance.
