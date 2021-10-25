

## Testing

### Setting up testing environment to point to local development environment after dployment of skelton project

I have taken deploy empty project first approach as it was encouraged in Code Institute's Blog walkthrough. The main reason for this is to avoid last minute deployment issue. However testign in deployed project throw errors connecting databse. In order to resolve this to accomdate testing I needed to setup of the testing environment for Django to refer the local Sqlite database.
The procedure for this was kindly shared by a cohort student group member, Elaine.
Here is the steps taken to enable testing in the development environment.

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



  [<<< Back to README](../../README.md)