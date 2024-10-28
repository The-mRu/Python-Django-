# Day 9: [Django Authentication](https://docs.djangoproject.com/en/5.1/topics/auth/) ( Authorization,   Authentication, Login & Registration )

**users** app created, then add login.html and registration.html in the templates folder

## Task 1 & 2: Login System & Registration System 


### Create the Login Template :
Add login.html in the users/templates/ folder

```bash
#users/templates/login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <!-- Include Tailwind CSS -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white rounded-lg shadow-md">
        <h2 class="mb-6 text-2xl font-bold text-center text-gray-800">Login</h2>
        <form method="post">
            {% csrf_token %}
            <div class="mb-4">
                {{ form.as_p }}
            </div>
            <button type="submit" class="w-full px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300">
                Login
            </button>
        </form>
    </div>
</body>
</html>

```

### Create the Registration Template :
Add registration.html in the users/templates/ folder:

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">

    <div class="w-full max-w-md">
        <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <h2 class="text-2xl font-bold mb-6 text-center">Register</h2>

            <form method="post" class="space-y-4">
                {% csrf_token %}
                {{ form.as_p }}

                <div class="flex items-center justify-between">
                    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                        Register
                    </button>
                </div>
            </form>
        </div>
    </div>

</body>
</html>
```





### Create Registration View : 
In users/views.py:

```bash
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful registration
```

### In users/urls.py, add the login,registration path:
users/urls.py
```bash
from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

# Login and Logout paths
urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  # Register page
]
```