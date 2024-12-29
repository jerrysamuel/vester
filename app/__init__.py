import os
from flask import Flask
from app.db import db
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'uploads'

    db.init_app(app)

    from app.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.cli.command("init-db")
    def init_db():
        """Initialize the database."""
        with app.app_context():
            db.create_all()
            print("Initialized the database.")


    return app