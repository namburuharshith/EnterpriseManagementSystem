from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'
<<<<<<< HEAD
from app import routes,models
bootstrap = Bootstrap(app)
=======
from app import routes,models
>>>>>>> cdf0f5e4a09221c6397f0bef4127cad0391e5676
