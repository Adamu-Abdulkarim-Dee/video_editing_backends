# Welcome to VideoEditingApp
This is a Django application that includes essential configurations for building a robust RESTful API. It uses Django REST framework for the API functionalities and django-cors-headers for handling Cross-Origin Resource Sharing (CORS).

# Installation
To get started with VideoEditingApp, follow these steps:
1. Clone the repository:
    ```
    git clone https://github.com/Adamu-Abdulkarim-Dee/video_editing_backends
    ```

2. Create a virtual environment:
    ```
    python -m venv source
    ```

3. Activate virtual environment:
    ```
    source\scripts\activate
    ```

4. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

6. Create a super user:
    ```
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```
    python manage.py runserver
    ```

# Configuration
## Django REST Framework
[Django REST framework](https://www.django-rest-framework.org/) is used to build the API for VideoEditingApp. Basic settings are already configured in the `settings.py` file. You can customize these settings as needed.

# CORS Headers
[django-cors-headers](https://pypi.org/project/django-cors-headers/) is used to handle CORS, which allows your API to be accessed from different domains. Basic settings are included in the `settings.py` file. You can customize these settings to fit your requirements.

### Settings.py File
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    ...
]

REST_FRAMEWORK = {
    # Using Django standard `django.contrib.auth` permissions,
    # Allowing read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
}

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True

```