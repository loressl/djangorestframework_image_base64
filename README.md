# Api teste para salvar imagens em base64.

---

# Ambiente virtual

Criação

    python -m venv nome_venv

Ativação
  
    WINDOWS: nome_venv\Scripts\activate
    LINUX: source nome_venv\Scripts\activate

Instalação do pip
  
    python -m pip install --upgrade pip

OBS: Fora da pasta project

---

# Instalação

    python -m pip install -r requirements.txt

OBS: Dentro da pasta project

---

# Criação do banco

    python manage.py makemigrations image64
    python manage.py migrate
    
---

# Criação do usuário admin

    python manage.py createsuperuser
    
---

# Rodar o servidor

    python manage.py runserver
    
---

# Rotas

    GET: http://127.0.0.1:8000/base64/
    
      - Pega todas as imagens salvas no banco.
    
    GET: http://127.0.0.1:8000/base64/<int:id>
    
      - Pega uma imagem específica no banco.
      
    POST: http://127.0.0.1:8000/save_base64/
    
      - Salva a imagem no banco. Para isso pode usar o postman passando no body:
      
      {
          "image":"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS...."
      }
      
      -Ou pode usar o próprio site do admin e salvar apenas o dado copiado.
      
      
 -Site utilizado para pegar converte a imagem: https://www.base64-image.de/
 
 -Referência : https://dev.to/ageumatheus/creating-image-from-dataurl-base64-with-pyhton-django-454g
    
