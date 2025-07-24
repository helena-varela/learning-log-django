# 📖 Learning Log
Aplicação web simples de diário de aprendizagem feito com Django que permite registrar e organizar o que você está aprendendo e observar seu progresso ao longo do tempo.

## 🚀 Funcionalidades
- Autenticação de usuários (login, logout, cadastro)
- Criar, ler, editar e excluir tópicos de estudo
- Também permite adiconar, editar e deletar entradas (anotações) relativas a cada tópico
- Interface intuitiva com navegação simples para usuários autenticados

## 🛠️ Tecnologias utilizadas
- Python 3
- Django
- Bootstrap 5
- SQLite

## ⚙️ Instalação do Projeto
01. **Clone o repositório**

      ```git clone https://github.com/helena-varela/learning-log-django.git ```

02. **Crie um ambiente virtual**
   
       ``` python -m venv venv ```

03. **Ative o ambiente virtual**
   
   - Windows: ``` .venv\Scripts\activate ```
   - Linux/MacOs: ``` source venv/bin/activate ```

04. **Instale as dependências**
   
     ``` pip install -r requirements.txt ```

05. **Realize as migrações do banco de dados**
  
     ``` python manage.py migrate ```

06. **Inicie o servidor**
   
    ```python manage.py runserver```
