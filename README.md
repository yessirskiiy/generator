1. pip install -r requirements.txt
2. python manage.py migrate
3. После запуска localhost прописать две команды в разных терминалах чтобы запустить celery
celery --app=generator worker -l INFO
celery -A generator beat
