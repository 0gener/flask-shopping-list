from os import getenv
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from application import db, create_app

config_name = getenv('FLASK_ENV', 'default')
app = create_app(config=config_name)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()