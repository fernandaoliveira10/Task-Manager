from flask import request
from flask_restful import Resource
from app.models import Task
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class TaskListResource(Resource):
    @jwt_required()
    def get(self):
        # Obter o ID do usuário autenticado
        user_id = get_jwt_identity()
        tasks = Task.query.filter_by(user_id=user_id).all()
        return [{"id": task.id, "title": task.title, "description": task.description, "done": task.done} for task in tasks]

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        print("Request Data:", data)  # Debug para verificar os dados recebidos
        print("Title:", data.get('title'))  # Debug para verificar o título

        # Validações
        if not data:
            return {"msg": "Request body must be a valid JSON object"}, 400

        if 'title' not in data or not isinstance(data['title'], str) or not data['title'].strip():
            return {"msg": "The 'title' field is required and must be a non-empty string"}, 400

        if 'description' in data and not isinstance(data['description'], str):
            return {"msg": "The 'description' field must be a string"}, 400

        # Criar nova tarefa
        new_task = Task(
            title=data['title'].strip(),
            description=data.get('description', '').strip(),
            user_id=user_id
        )
        db.session.add(new_task)
        db.session.commit()
        return {"message": "Task created successfully"}, 201


class TaskResource(Resource):
    @jwt_required()
    def put(self, task_id):
        # Obter o ID do usuário autenticado
        user_id = get_jwt_identity()
        # Buscar tarefa por ID e usuário
        task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
        data = request.get_json()

        # Validações
        if 'title' in data and (not isinstance(data['title'], str) or not data['title'].strip()):
            return {"msg": "The 'title' field must be a non-empty string"}, 400

        if 'done' in data and not isinstance(data['done'], bool):
            return {"msg": "The 'done' field must be a boolean"}, 400

        # Atualizar os campos da tarefa
        task.title = data.get('title', task.title).strip()
        task.done = data.get('done', task.done)
        db.session.commit()
        return {"message": "Task updated successfully"}, 200

    @jwt_required()
    def delete(self, task_id):
        # Obter o ID do usuário autenticado
        user_id = get_jwt_identity()
        # Buscar tarefa por ID e usuário
        task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
        # Excluir tarefa
        db.session.delete(task)
        db.session.commit()
        return {"message": "Task deleted successfully"}, 200
