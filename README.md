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

# :dizzy:Visualização do Projeto
**01.  Página Inicial**

   
<img width="1000" height="610" alt="image" src="https://github.com/user-attachments/assets/c8d8dde3-4c9f-4e2b-a239-ad85af829435" />

**02. Cadastro e Login**

   
![cadastro-login](https://github.com/user-attachments/assets/7b37f1a1-55bc-4942-a149-ab315792c07c)

**03. Adicionando Tópicos**

   
![add-topicos](https://github.com/user-attachments/assets/206ca612-5ff8-4546-ba4e-fcc1181c7295)

**04. Funções CRUD**

   
![CRUD](https://github.com/user-attachments/assets/fb7afc8d-bbba-4001-a82b-14648d7f52f5)


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
