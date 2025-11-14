## Usage

### Quick Start (Docker)
```bash
cp .env.example .env
docker-compose up -d
docker-compose exec chatbot-api python manage.py migrate
open http://localhost:8000
```

### Development (Local)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### API
Swagger docs: `http://localhost:8000/api/docs/`