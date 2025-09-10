# Sports Data API

**A lightweight Django + Django REST Framework API that serves mostly static (non-ephemeral) information about sports and famous athletes.**

This repository provides a simple, well-documented API intended to host canonical data about sports (categories, Olympic status, etc.) and notable athletes. The project is designed to be reproducible with **Poetry** for dependency management and packaged with **Docker** for easy deployment.

---

## Table of Contents

* [Project goals](#project-goals)
* [Tech stack](#tech-stack)
* [Key concepts / models](#key-concepts--models)
* [Quickstart (development)](#quickstart-development)
* [Docker / Production quickstart](#docker--production-quickstart)
* [Database migrations & fixtures](#database-migrations--fixtures)
* [API endpoints & examples](#api-endpoints--examples)
* [Schema & Documentation (OpenAPI / Swagger / Redoc)](#schema--documentation-openapi--swagger--redoc)
* [Filtering, pagination and ordering](#filtering-pagination-and-ordering)
* [Testing](#testing)
* [Project structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

---

## Project goals

* Provide authoritative, mostly static data about sports and famous athletes.
* Make the project easy to run locally and in containers (Docker).
* Keep the API stable and versionable so downstream clients can cache data long-term.
* Offer clear documentation so the README can be used as the canonical setup + usage guide.

---

## Tech stack

* Python 3.10+ (adjust in `pyproject.toml`)
* Django 3.2.x (LTS in the example)
* Django REST Framework
* Poetry for dependency management
* Docker + Docker Compose for containerized development / deployment

---

## Key concepts / models

This project exposes two primary models (already included in `models.py`):

* **Sport**

  * `name` (string)
  * `category` (string, optional) — e.g., "Team", "Individual"
  * `olympic_sport` (boolean)

* **FamousAthlete**

  * `name` (string)
  * `country` (string)
  * `sport` (ForeignKey -> `Sport`)
  * `titles` (integer)

These map directly to serializers and DRF viewsets (list/retrieve/create/update/destroy). For a mostly static dataset you will typically only use `list` and `retrieve`.

---

## Quickstart (development)

> The project is configured to use Poetry. If you don't have Poetry installed, follow: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)

1. Clone the repo

```bash
git clone https://github.com/thehecktour/sportsAPI>
cd sportsAPI
```

2. Install dependencies

```bash
poetry shell
poetry install
```

3. Create `.env` (if your project expects it). Example minimal `.env`:

```env
DJANGO_SECRET_KEY=replace_this_with_a_real_secret
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

If you use `django-environ` the `DATABASE_URL` pattern will work with Postgres, MySQL, or SQLite.

4. Apply migrations

```bash
python manage.py migrate
```

5. (Optional) Load fixtures (static seed data). Example:

```bash
python manage.py loaddata fixtures/sports.json
python manage.py loaddata fixtures/athletes.json
```

6. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` (or your API root) in your browser.

---

## Docker / Production quickstart

A minimal `Dockerfile` and `docker-compose.yml` make running in containers straightforward. Example commands below assume you have Docker installed.

1. Build and run (development)

```bash
docker compose up --build
```

2. Run migrations inside the running container

```bash
# If your web service is named 'web' in docker-compose
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata fixtures/sports.json
docker compose exec web python manage.py loaddata fixtures/athletes.json
```

3. To run in detached mode

```bash
docker compose up --build -d
```

**Notes for production:**

* Use a production-grade database (Postgres), set `DJANGO_DEBUG=False`, and configure `ALLOWED_HOSTS`.
* Use a process manager / WSGI server such as Gunicorn, and place the app behind a reverse proxy like Nginx.
* Use an environment secret manager for `SECRET_KEY` and DB credentials.

---

## Database migrations & fixtures

Because your data is mostly static, seed data should be managed carefully so it remains reproducible.

Options:

1. **Fixtures** (`fixtures/*.json`) — simple and portable. Load with `loaddata` as shown above.
2. **Data migrations** — Django data migrations (inside `migrations/`) let you programmatically insert records during migration.
3. **Admin import script** — a management command that idempotently imports or updates records.

**Example fixture snippet** (this repo includes sample fixtures):

```json
// fixtures/sports.json
[
  {
    "model": "sports.sport",
    "pk": 1,
    "fields": {"name": "Tennis", "category": "Individual", "olympic_sport": true}
  },
  {
    "model": "sports.sport",
    "pk": 2,
    "fields": {"name": "Basketball", "category": "Team", "olympic_sport": true}
  }
]
```

```json
// fixtures/athletes.json
[
  {
    "model": "sports.famousathlete",
    "pk": 1,
    "fields": {"name": "Roger Federer", "country": "Switzerland", "sport": 1, "titles": 103}
  },
  {
    "model": "sports.famousathlete",
    "pk": 2,
    "fields": {"name": "Serena Williams", "country": "USA", "sport": 1, "titles": 73}
  }
]
```

Load with `python manage.py loaddata fixtures/sports.json fixtures/athletes.json`.

---

## API endpoints & examples

This project uses DRF `ModelViewSet` for `Sport` and `FamousAthlete`, so standard endpoints are available if routed with a `DefaultRouter`.

**Common routes (example)**

* `GET  /api/sports/` — list sports
* `GET  /api/sports/{id}/` — retrieve a sport
* `POST /api/sports/` — create (if you allow writes)
* `GET  /api/athletes/` — list athletes
* `GET  /api/athletes/{id}/` — retrieve an athlete

### Example: list sports

```bash
curl http://127.0.0.1:8000/api/sports/
```

**Sample response**

```json
[
  {"id":1,"name":"Tennis","category":"Individual","olympic_sport":true},
  {"id":2,"name":"Basketball","category":"Team","olympic_sport":true}
]
```

### Example: list athletes

```bash
curl http://127.0.0.1:8000/api/athletes/
```

**Sample response**

```json
[
  {"id":1,"name":"Roger Federer","country":"Switzerland","sport":"Tennis","titles":103},
  {"id":2,"name":"Serena Williams","country":"USA","sport":"Tennis","titles":73}
]
```

> Note: The `FamousAthleteSerializer` in this repo uses `sport = serializers.StringRelatedField()` so the sport is returned as the sport's `__str__()` (name). If you prefer nested objects or ids, change the serializer to `PrimaryKeyRelatedField` or nest a `SportSerializer`.

---

## Schema & Documentation (OpenAPI / Swagger / Redoc)

DRF can auto-generate an OpenAPI schema. Two popular options to expose it:

* `drf-yasg` — provides Swagger UI and Redoc easily.
* `drf-spectacular` — alternative with opinionated schema generation.

Basic example using DRF's built-in schema view (no external package):

```py
# urls.py
from rest_framework import routers
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'sports', SportViewSet)
router.register(r'athletes', FamousAthleteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('schema/', get_schema_view(title="Sports API"), name='openapi-schema'),
    path('docs/', include_docs_urls(title='Sports API')),
]
```

If you install `drf-yasg`, add a Swagger UI route for interactive docs.

---

## Filtering, pagination and ordering

* **Pagination**: Use DRF's pagination classes in `settings.py` (e.g. `PageNumberPagination`) to limit result size for large datasets.
* **Filtering**: Add `django-filter` and configure `DjangoFilterBackend` to filter by fields (e.g., `category`, `olympic_sport`, `country`).
* **Ordering**: Use `OrderingFilter` to allow `?ordering=-titles` or `?ordering=name`.

Example viewset augmentation:

```py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class FamousAthleteViewSet(viewsets.ModelViewSet):
    queryset = FamousAthlete.objects.all()
    serializer_class = FamousAthleteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['country', 'sport__name']
    search_fields = ['name', 'country']
    ordering_fields = ['titles', 'name']
```

---

## Testing

Add unit tests for serializers, views, and management commands. Example pytest matrix:

```bash
poetry add --dev pytest pytest-django factory-boy
```

Run tests:

```bash
pytest
```

---

## Project structure (suggested)

```
├── README.md
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── .env
├── manage.py
├── app_name/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── sports/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── fixtures/
│       ├── sports.json
│       └── athletes.json
└── requirements.txt (optional, produced by poetry export)
```

---

## Contributing

* Keep the canonical data accurate and sourced. When adding or updating entries, document the source (URL or reference) in the commit message.
* Prefer `fixtures/` or data migrations for static content so deployments are reproducible.
* Run `python manage.py test` before opening pull requests.


---

## Appendix — Helpful commands

```bash
# Poetry
poetry install
poetry run python manage.py migrate
poetry run python manage.py loaddata fixtures/sports.json fixtures/athletes.json
poetry run python manage.py runserver

# Docker
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata fixtures/sports.json
```

---

If you'd like, I can also:

* produce a `Dockerfile` + `docker-compose.yml` example tuned for this project,
* add DRF swagger configuration (`drf-yasg`) example,
* convert fixtures into a data migration,
* or translate this README into Portuguese.

Tell me which of those you'd like next.
