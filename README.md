# Project-1

## Introduction

This is a web application I created as part of my course. You can access it at the following URL: https://psychic-goldfish-q777qpw94p6gf64xj-8000.app.github.dev/polls/ (exclusively while I am running the application on my VM on Codespaces)


![2023-12-07 12_47_31-Window.jpg](https://github.com/SocialEngineering90/Project-1/blob/393e52d9099daf494b4e523e8f8b5eccf5760471/2023-12-07%2012_47_31-Window.jpg)


----

# FLAW 1: Injection

**Link pinpointing flaw 1:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L11

**Description of the flaw.**
In this first flaw, I am trying to address a SQL Injection in the python code in the backend and recommend a fix using parameterized queries or prepared statements. 
The code like this is vulnerable to SQL injection because it directly includes user input in the SQL query. 

**How to fix it.**
To fix this issue, I recommend using parameterized queries or prepared statements. This helps prevent SQL injection by treating user input as data, not as part of the SQL statement. 


# FLAW 2: Broken Access Control

**Link pinpointing flaw 2:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/views.py#L13

**Description of the flaw.**
This project might have broken access control if it does not properly manage authenticated sessions or restrict access to certain views based on user roles. This flaw corresponds to A01:2021-Broken Access Control in the OWASP Top Ten.

**How to fix it.** 
To fix the "Broken Access Control" flaw, I suggest using Django's built-in authentication and authorization features. We should make sure that only authenticated users can access sensitive views. We can use the @login_required decorator to enforce authentication for specific views. For actions requiring specific permissions, like user deletion, we can use the @permission_required decorator to check if the current user has the necessary permissions. This will improve security by restricting access to privileged functionality based on the user's role and permissions.
 
# FLAW 3: Insecure Dependencies

**Link pinpointing flaw 3:** https://github.com/SocialEngineering90/Project-1/blob/main/polls/custom_script.py#L6C4-L6C4


**Description of the flaw.**
The project might be using insecure or outdated dependencies, which could include the database (SQLite3) or any libraries used in custom scripts. This flaw corresponds to A06:2021-Vulnerable and Outdated Components in the OWASP Top Ten.


**How to fix it.** 
To mitigate this flaw, it's crucial to regularly update all dependencies to their latest stable versions. You can use tools like pip list --outdated to check for outdated Python packages. For the database, consider using a more robust system like PostgreSQL or MySQL for production. Always ensure that any custom scripts follow secure coding practices. Additionally, you should update the script inside the custom_script.py with the updated library. It's also recommended to use a dependency management tool that supports lock files, like pipenv or poetry, to automatically manage your project's dependencies and their versions.


# FLAW 4: Insufficient Logging and Monitoring

**Link pinpointing flaw 4:** https://github.com/SocialEngineering90/Project-1/blob/main/manage.py#L21

**Description of the flaw.**
The project lacks a logging or monitoring setup, making it difficult to detect, escalate, and respond to active breaches. This flaw corresponds to A09:2021-Security Logging and Monitoring Failures in the OWASP Top Ten.

**How to fix it.** 
To address this flaw, implement logging in your application, especially for critical operations. You can use Django's built-in logging, or a third-party library like Loguru. For monitoring, consider using tools like Sentry, New Relic, or Datadog. Ensure that all sensitive or high-value events are logged and monitored for suspicious activity. Also, make sure that the logging system you are using is secure and has appropriate controls in place to prevent unauthorized access.


# FLAW 5: Security Misconfiguration

**Link pinpointing flaw 5:** https://github.com/SocialEngineering90/Project-1/blob/main/mysite/settings.py#L32

**Description of the flaw.**
Security misconfiguration can occur when the application is not properly configured, leading to vulnerabilities. This flaw corresponds to A05:2021-Security Misconfiguration in the OWASP Top Ten. In the given project, the settings.py file might contain insecure configurations, such as DEBUG mode enabled, weak secret keys, or improper middleware settings.

**How to fix it.** 
To fix security misconfiguration, follow best practices for configuring your Django application:
1). Ensure DEBUG mode is set to False in production environments.
2). Use strong, unique secret keys for each environment.
3). Configure middleware settings to include security-related middleware, such as 'django.middleware.security.SecurityMiddleware' and 'django.middleware.clickjacking.XContentOptionsMiddleware'.
4). Regularly review and update your application's configurations to ensure they follow security best practices.
6). Use Django's built-in security features, such as the ALLOWED_HOSTS setting, to restrict access to your application.


----
# Credits
This project was developed by myself as part of the mooc course https://cybersecuritybase.mooc.fi/

Thank you to teacher Nikolaj Tatti for clarification and assistance.
