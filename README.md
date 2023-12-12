# Project-1

## Introduction

This is a web application I created as part of my course. You can access it at the following URL: https://psychic-goldfish-q777qpw94p6gf64xj-8000.app.github.dev/polls/ (exclusively while I am running the application on my VM on Codespaces)


![2023-12-07 12_47_31-Window.jpg](https://github.com/SocialEngineering90/Project-1/blob/393e52d9099daf494b4e523e8f8b5eccf5760471/2023-12-07%2012_47_31-Window.jpg)


----

# FLAW 1: Injection

**Link to flaw 1:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L11

**Description of the flaw.**
The first flaw I identified is a SQL Injection vulnerability in the Python code in the backend. This flaw makes the code susceptible to SQL injection as it directly incorporates user input into the SQL query.

**How to fix it.**
To rectify this, I suggest using parameterized queries or prepared statements. This approach treats user input as data, not as part of the SQL statement, thereby preventing SQL injection.


# FLAW 2: Broken Access Control

**Link to flaw 2:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/views.py#L13

**Description of the flaw.**
The second flaw is potential broken access control. This could occur if the project doesn't properly manage authenticated sessions or restrict access to certain views based on user roles. This flaw aligns with A01:2021-Broken Access Control in the OWASP Top Ten.

**How to fix it.** 
To address this, I recommend using Django's built-in authentication and authorization features. We should ensure that only authenticated users can access sensitive views. Django's @login_required decorator can enforce authentication for specific views. For actions requiring specific permissions, we can use the @permission_required decorator to verify if the current user has the necessary permissions.
 
# FLAW 3: Insecure Dependencies

**Link to flaw 3:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L6C4-L6C4


**Description of the flaw.**
The third flaw is the potential use of insecure or outdated dependencies, which could include the database (SQLite3) or any libraries used in custom scripts. This flaw aligns with A06:2021-Vulnerable and Outdated Components in the OWASP Top Ten.


**How to fix it.** 
To mitigate this, it's important to regularly update all dependencies to their latest stable versions. Tools like pip list --outdated can be used to check for outdated Python packages. For the database, consider using a more robust system like PostgreSQL or MySQL for production. Also, ensure that any custom scripts follow secure coding practices.


# FLAW 4: Insufficient Logging and Monitoring

**Link to flaw 4:** https://github.com/SocialEngineering90/Project-1/blob/main/manage.py#L21

**Description of the flaw.**
The fourth flaw is the lack of a logging or monitoring setup, which makes it challenging to detect, escalate, and respond to active breaches. This flaw aligns with A09:2021-Security Logging and Monitoring Failures in the OWASP Top Ten.

**How to fix it.** 
To address this, I suggest implementing logging in your application, especially for critical operations. Django's built-in logging or a third-party library like Loguru can be used. For monitoring, consider using tools like Sentry, New Relic, or Datadog.


# FLAW 5: Security Misconfiguration

**Link to flaw 5:** https://github.com/SocialEngineering90/Project-1/blob/main/mysite/settings.py#L32

**Description of the flaw.**
The fifth flaw is security misconfiguration, which can occur when the application is not properly configured, leading to vulnerabilities. This flaw aligns with A05:2021-Security Misconfiguration in the OWASP Top Ten.

**How to fix it.** 
To rectify this, follow best practices for configuring your Django application: ensure DEBUG mode is set to False in production environments, use strong, unique secret keys for each environment, configure middleware settings to include security-related middleware, and regularly review and update your application's configurations.


----
# Acknowledgements
This project was developed by me as part of the mooc course https://cybersecuritybase.mooc.fi/. Special thanks to teacher Nikolaj Tatti for his guidance and support.
