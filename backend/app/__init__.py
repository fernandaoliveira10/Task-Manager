from flask import Flask
from app.extensions import db, ma, jwt
from app.routes import register_routes, main_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'

    # Inicializar extensões
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Registrar rotas principais e da API
    app.register_blueprint(main_bp)  # Página inicial
    register_routes(app)  # Rotas da API

    return app
