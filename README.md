# 🏅 Sports Data API

**Lightweight Django + DRF API serving static data about sports and famous athletes.**

---

## 🎯 Goals

- Provide stable, cacheable sports and athlete data  
- Run easily locally or via Docker  
- Keep setup simple and reproducible  

---

## ⚙️ Tech Stack

- Python 3.10+  
- Django 3.2 + Django REST Framework  
- Poetry for dependency management  
- Docker / Docker Compose  

---

## 🚀 Quickstart

```bash
git clone https://github.com/thehecktour/sportsAPI.git
cd sportsAPI
poetry env activate
poetry install
python manage.py migrate
python manage.py loaddata fixtures/sports.json fixtures/athletes.json
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 🐳 Docker

```bash
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata fixtures/sports.json fixtures/athletes.json
```

---

## 📡 API Endpoints

| Method | Route | Description |
|--------|--------|-------------|
| GET | /api/sports/ | List all sports |
| GET | /api/athletes/ | List all athletes |

---

## 🧪 Tests

```bash
poetry add --dev pytest pytest-django
pytest
```

---

## 🤝 Contributing

1. **Fork** the repo  
2. **Create a new branch**  
   ```bash
   git checkout -b feat/add-feature
   ```
3. **Follow commit conventions**

| Type | Emoji | When to use |
|------|--------|-------------|
| feat | 🦅 | Add new feature |
| refactor | 🐝 | General improvements |
| chore | 🦁 | Structural/system changes |
| docs | 🐙 | Update documentation |

**Example:**
```bash
git commit -m "feat: 🦅 add sport endpoint"
```

4. **Push your branch & open a PR 🚀**

> 🟢 Beginners can start by checking open *issues* labeled “good first issue”.

---

## 📘 Useful Commands

```bash
poetry env activate
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

```bash
docker compose up --build
docker compose exec web python manage.py migrate
```
