# polls/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def delete_user(request, user_id):
    # Assuming you have a User model with an is_admin attribute
    current_user = request.user

    # Broken Access Control flaw
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    # Placeholder response for demonstration purposes
    return HttpResponse(f"User with ID {user_id} deleted (flawed access control).")

   # Fixed code with permission check
    #if current_user.is_admin:
     #   cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
      #  return HttpResponse(f"User with ID {user_id} deleted.")
   # else:
    #    raise PermissionError("Only admins can delete users.")
