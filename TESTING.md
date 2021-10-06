

## Testing

### Setting up testing environment to point to local development environment after dployment of skelton project

As we were encouraged to have deploy empty project first approach to avoid last minute deployment issue, the testing environment needed to be setup for Django to refer the local Sqlite database..
This procedure was kindly shared by a cohort student group member, Elaine.

1. Following lines were added in setting.py and env.py

    **In setting.py**
        if development:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }

            
            
        development = os.environ.get('DEVELOPMENT', False)

        if development:
            ALLOWED_HOSTS = ['localhost']
        else:
            ALLOWED_HOSTS = ['blog.herokuapp.com']
            
    **In env.py**
      os.environ["DEVELOPMENT"] = "True"

2. After setting up the developmet setting run migrate in command line as follows:
    python3 manage.py migrate