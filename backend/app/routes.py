from flask import Blueprint
from flask_restful import Api
from app.resources.user import UserRegister, UserLogin
from app.resources.task import TaskResource, TaskListResource

# Blueprint para a página inicial
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "<h1>Bem-vindo ao Task Manager!</h1><p>Use os endpoints da API para interagir.</p>"

# Função para registrar as rotas da API
def register_routes(app):
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # Rotas de Usuário
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    # Rotas de Tarefas
    api.add_resource(TaskListResource, '/tasks')
    api.add_resource(TaskResource, '/tasks/<int:task_id>')

    # Registrar o blueprint da API
    app.register_blueprint(api_bp, url_prefix='/api')
