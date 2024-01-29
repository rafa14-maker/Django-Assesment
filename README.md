# Django-Assesment

for Virtual environment Setup:
   - pip install virtualenv
   - virtualenv

Install Django
  - pip install django 

Install rest_framework :
  - pip install djangorestframework
  - paste in to settings.py -> INSTALLED_APPS -> "rest_framework"

setup .env file:
   - copy SECRET_KEY and DEBUG to .env
   - SECRET_KEY=""
     DEBUG=True

setup Postgresql:
   - pip install psycopg2
   - import all database dependencies to .env
       -> 
       DATABASE_NAME=''
       DATABASE_USER=postgres
       DATABASE_PASSWORD='Your password'
       DATABASE_HOST=localhost
       DATABASE_PORT=5432
   - goto settings.py set Database
      ->
      DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}


JWT configuration :
   - pip install djangorestframework-simpleJWT
   - import it to settings.py 
      ->  "rest_framework_simplejwt",
   - Modify REST_FRAMEWORK & create SIMPLE_JWT
      -> 
                REST_FRAMEWORK = {
                "EXCEPTION_HANDLER": "utils.custom_exception_handler.custom_exception_handler",
                "DEFAULT_AUTHENTICATION_CLASSES": (
                    "rest_framework_simplejwt.authentication.JWTAuthentication",
                ),
            }

                SIMPLE_JWT = {
                    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
                    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
                    "BLACKLIST_AFTER_ROTATION": True,
                    "AUTH_HEADER_TYPES": ("Bearer",),
                    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
                }


