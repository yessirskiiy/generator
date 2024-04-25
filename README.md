1. pip install -r requirements.txt
2. python manage.py migrate
3. После запуска python manage.py runserver прописать две команды в разных терминалах чтобы запустить celery
4. celery --app=generator worker -l INFO
5. celery -A generator beat
