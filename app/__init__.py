from flask import Flask
from app.routes import main_routes
from app.models import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    init_db()
    app.register_blueprint(main_routes)
    return app
