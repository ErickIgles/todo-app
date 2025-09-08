DESENVOLVIMENTO DE UM SISTEMA DE REGISTRO DE TAREFAS


Este é um sistema web desenvolvido com **Django**, **HTML** e **CSS**, que permite o gerenciamento de tarefas pessoais de forma simples e intuitiva. O sistema oferece autenticação de usuários, criação, listagem, edição e exclusão de tarefas, além de proteção de acesso e uma interface amigável.

---

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML5
- CSS3
- SQLite3
- Variáveis de ambiente (`.env`)

---

## 🎯 Funcionalidades

### 🔐 Autenticação de Usuários

- A tela inicial redireciona automaticamente para a página de **login**
- Possui botões para:
  - **Login** com nome de usuário e senha
  - **Cadastro** com:
    - Nome de usuário
    - E-mail
    - Senha
    - Confirmação de senha

---

### 🏠 Tela Inicial (após login)

Após autenticação, o usuário é redirecionado para a tela inicial com 3 opções principais:

1. **Home**  
   - Retorna para a tela inicial

2. **Cadastrar Tarefas**  
   - Redireciona para um formulário com os campos:
     - Título
     - Descrição
     - Estado da tarefa (Select: Pendente, Em andamento, Concluído)
   - Botões:
     - `Cadastrar`: salva a tarefa
     - `Cancelar`: retorna para a home

3. **Lista de Tarefas**  
   - Exibe todas as tarefas criadas pelo usuário autenticado
   - Cada tarefa é exibida em um card contendo:
     - Título, descrição e status
     - Botões de `Atualizar` e `Deletar`

---

### ✏️ Atualização e Exclusão de Tarefas

- **Atualizar**: leva o usuário para uma tela com os campos preenchidos (título, descrição e status)
- **Deletar**: redireciona para uma página de confirmação com a mensagem e dois botões:
  - `Deletar`: exclui a tarefa
  - `Cancelar`: retorna à lista de tarefas

---

### 🔒 Proteção de Acesso às Tarefas

- Cada tarefa é **vinculada ao usuário autenticado** no momento da criação
- É utilizado um **mixin personalizado** chamado `TaskPermissionMixin` para garantir a segurança
- Se um usuário tentar acessar uma tarefa que **não pertence a ele**, o sistema:
  - Redireciona automaticamente para a **página inicial (Home)**
  - Exibe a seguinte mensagem de erro:
    > `"Usuário não tem permissão para acessar este registro."`

Essa proteção impede acesso indevido mesmo por manipulação de URL.

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


### 2. Crie e ative um ambiente virtual

# Para criar ambiente virtual
python -m venv venv

# Para ativar

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

### 3. Instale as dependências

pip install -r requirements.txt

### 4 .Configure as variáveis de ambiente

SECRET_KEY=sua_chave_secreta

# Configurações do banco de dados
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

### 5 .Aplique as migrações

python manage.py migrate

### 6 .Crie um superusuário (opcional)

python manage.py createsuperuser

### 7 .Execute o servidor
python manage.py runserver

Acesse o sistema em: http://127.0.0.1:8000/

Acesse o admin em: http://127.0.0.1:8000/admin/
```
