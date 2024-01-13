from flask import Flask

def create_app():
    app = Flask(__name__) #used to initialize flask

    from .views import views #import the blueprint 
    from .auth import auth

#register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
