# Task Manager API

## **Descrição**
O **Task Manager API** é uma aplicação backend construída com Flask para gerenciar tarefas. Ele oferece recursos como autenticação de usuários, criação, listagem, atualização e exclusão de tarefas. O sistema utiliza JWT para autenticação e um banco de dados SQLite para armazenar as informações.

---

## **Recursos do Projeto**
- **Autenticação**:
  - Registro de usuários (`POST /api/register`).
  - Login para obter token JWT (`POST /api/login`).

- **Gestão de Tarefas**:
  - Criar tarefas (`POST /api/tasks`).
  - Listar tarefas (`GET /api/tasks`).
  - Atualizar tarefas (`PUT /api/tasks/<task_id>`).
  - Deletar tarefas (`DELETE /api/tasks/<task_id>`).

- **Segurança**:
  - Todas as rotas, exceto registro e login, exigem autenticação via JWT.

---

## **Configuração do Projeto**

### **1. Pré-requisitos**
Certifique-se de ter instalado:
- Python 3.8 ou superior
- `pip` para gerenciar pacotes Python

### **2. Clonar o Repositório**
```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd Task-Manager
```

### **3. Criar e Ativar o Ambiente Virtual**
```bash
# Criar o ambiente virtual
python -m venv env

# Ativar o ambiente virtual
# Windows:
.\env\Scripts\activate
# Mac/Linux:
source env/bin/activate
```

### **4. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **5. Configurar o Banco de Dados**
```bash
python
from app import create_app
from app.extensions import db
app = create_app()
with app.app_context():
    db.create_all()
exit()
```

### **6. Executar o Servidor**
```bash
python run.py
```
O servidor estará disponível em: `http://127.0.0.1:5000`.

---

## **Endpoints da API**

### **1. Autenticação**
#### **1.1 Registro de Usuário**
- **Endpoint**: `POST /api/register`
- **Body**:
  ```json
  {
      "username": "usuario",
      "password": "senha123"
  }
  ```
- **Resposta**:
  ```json
  {
      "message": "User created successfully"
  }
  ```

#### **1.2 Login**
- **Endpoint**: `POST /api/login`
- **Body**:
  ```json
  {
      "username": "usuario",
      "password": "senha123"
  }
  ```
- **Resposta**:
  ```json
  {
      "access_token": "TOKEN_JWT"
  }
  ```

---

### **2. Gestão de Tarefas**
#### **2.1 Criar Tarefa**
- **Endpoint**: `POST /api/tasks`
- **Headers**:
  ```
  Authorization: Bearer <TOKEN_JWT>
  Content-Type: application/json
  ```
- **Body**:
  ```json
  {
      "title": "Estudar Flask",
      "description": "Aprender validações no backend"
  }
  ```
- **Resposta**:
  ```json
  {
      "message": "Task created successfully"
  }
  ```

#### **2.2 Listar Tarefas**
- **Endpoint**: `GET /api/tasks`
- **Headers**:
  ```
  Authorization: Bearer <TOKEN_JWT>
  ```
- **Resposta**:
  ```json
  [
      {
          "id": 1,
          "title": "Estudar Flask",
          "description": "Aprender validações no backend",
          "done": false
      }
  ]
  ```

#### **2.3 Atualizar Tarefa**
- **Endpoint**: `PUT /api/tasks/<task_id>`
- **Headers**:
  ```
  Authorization: Bearer <TOKEN_JWT>
  Content-Type: application/json
  ```
- **Body**:
  ```json
  {
      "title": "Estudar Flask Avançado",
      "done": true
  }
  ```
- **Resposta**:
  ```json
  {
      "message": "Task updated successfully"
  }
  ```

#### **2.4 Deletar Tarefa**
- **Endpoint**: `DELETE /api/tasks/<task_id>`
- **Headers**:
  ```
  Authorization: Bearer <TOKEN_JWT>
  ```
- **Resposta**:
  ```json
  {
      "message": "Task deleted successfully"
  }
  ```

---

## **Estrutura do Projeto**
```
Task-Manager/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── extensions.py
│   │   └── resources/
│   │       ├── user.py
│   │       └── task.py
│   ├── run.py
│   └── requirements.txt
└── README.md
```

---

## **Dicas**
- Use ferramentas como Postman ou cURL para testar os endpoints.
- Para alterar a URL do banco de dados, edite `SQLALCHEMY_DATABASE_URI` em `app/__init__.py`.
- Configure variáveis de ambiente para armazenar informações sensíveis, como a chave secreta do JWT.

---

## **Melhorias Futuras**
- Adicionar paginação na listagem de tarefas.
- Implementar categorias para organizar tarefas.
- Adicionar integração com um frontend (React, Vue.js ou Angular).

---

## **Contribuição**
Sinta-se à vontade para contribuir com este projeto. Faça um fork, implemente suas melhorias e abra um pull request!

