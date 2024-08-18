from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app=Flask(__name__)
bcrypt = Bcrypt(app)


if app.config['ENV']=='production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV']=='testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db=SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model.model import Users,Contact
from app.views import admin_views,views
from app.forms.forms import LoginForm, RegisterForm,ContactForm,SearchForm,ProductForm
