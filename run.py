from os import getenv

from application import create_app

config_name = getenv('FLASK_ENV', 'development')

app = create_app(config_name)

if __name__ == "__main__":
    app.run(port=5000)