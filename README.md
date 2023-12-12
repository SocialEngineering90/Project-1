# Project-1

## Introduction

Web application reacheable from my VM in codespaces after running the python manage.py runserver command. On the following url https://psychic-goldfish-q777qpw94p6gf64xj-8000.app.github.dev/polls/


![2023-12-07 12_47_31-Window.jpg](https://github.com/SocialEngineering90/Project-1/blob/393e52d9099daf494b4e523e8f8b5eccf5760471/2023-12-07%2012_47_31-Window.jpg)


----

# FLAW 1: Injection

**Link pinpointing flaw 1:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L11

**Description of the flaw.**
In this first flaw, I am trying to address a SQL Injection in the python code in the backend and recommend a fix using parameterized queries or prepared statements. 

`def get_user(user_id):`
    `cursor.execute(f"SELECT * FROM users WHERE id={user_id}")`

The code like this is vulnerable to SQL injection because it directly includes user input in the SQL query. 

**How to fix it.**

To fix this issue, it is enough to use parameterized queries or prepared statements to ensure proper data validation and sanitization. Because this helps prevent SQL injection by ensuring that user input is treated as data and not as part of the SQL statement. Like: 

`def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))`

# FLAW 2: Broken Access Control

**Link pinpointing flaw 2:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/views.py#L13

**Description of the flaw.**
This project might have broken access control if it does not properly manage authenticated sessions or restrict access to certain views based on user roles. This flaw corresponds to A01:2021-Broken Access Control in the OWASP Top Ten.

`# Broken Access Control flaw
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))`


`# Placeholder response for demonstration purposes
    return HttpResponse(f"User with ID {user_id} deleted (flawed access control).")`

**How to fix it.** 
To fix the "Broken Access Control" flaw, I can utilize Django's built-in authentication and authorization features. As far as I can see,  I should confirm that only authenticated users can access sensitive views. Using the @login_required decorator to enforce authentication for specific views. For actions requiring specific permissions, such as user deletion, I use the @permission_required decorator to check and ensure that the current user has the necessary permissions. This enhances security by restricting access to privileged functionality based on the user's role and permissions.
 
`# Fixed code with permission check
     if current_user.is_admin:
         cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
         return HttpResponse(f"User with ID {user_id} deleted.")
    else:
          raise PermissionError("Only admins can delete users.")`


# FLAW 3: Insecure Dependencies

**Link pinpointing flaw 2:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L6C4-L6C4


**Description of the flaw.**
This project might be using insecure or outdated dependencies. This could include the database (SQLite3) or any libraries used in custom scripts. This flaw corresponds to A06:2021-Vulnerable and Outdated Components in the OWASP Top Ten.

To implement this flaw in our current python script I intentionally add the following line with the respective comment. 

**How to fix it.** 
Regularly update all dependencies to their latest stable versions. Use tools like pip list --outdated to check for outdated Python packages. For the database, consider using a more robust system like PostgreSQL or MySQL for production. Always ensure that any custom scripts follow secure coding practices.

Another possible fix could be also to update the script inside the custom_script.py with the updated library. 


# FLAW 4: Insufficient Logging and Monitoring

# FLAW 5: Security Misconfiguration


----
# Credits
This project was developed by myself as part of the mooc course https://cybersecuritybase.mooc.fi/

Thank you to teacher Nikolaj Tatti for clarification and assistance.
