# Django Project Setup Guide 🚀

## Prerequisites
<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0.75rem; border-radius: 4px;">
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: white; background: #3776AB;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" style="width: 16px; height: 16px;" />
    Python 3.12
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: white; background: #0066B3;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" alt="pip" style="width: 16px; height: 16px;" />
    pip
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: white; background: #4B5563;">
    <img src="https://python-poetry.org/images/logo-origami.svg" alt="Poetry" style="width: 16px; height: 16px;" />
    Poetry
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: white; background: #171515;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" style="width: 16px; height: 16px;" />
    Git
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: white; background: #32648C;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" style="width: 16px; height: 16px;" />
    PostgreSQL
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: black; background: white;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS" style="width: 16px; height: 16px;" />
    AWS
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: black; background: #a4b6ff;">
    <img src="https://cdn.worldvectorlogo.com/logos/stripe-3.svg" alt="Stripe" style="width: 16px; height: 16px;" />
    Stripe
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: black; background: white;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" alt="Tailwind" style="width: 16px; height: 16px;" />
    Tailwind
  </button>
  <button style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.5rem; border: none; border-radius: 3px; font-size: 0.85rem; font-weight: 500; cursor: pointer; transition: all 0.2s ease; color: black; background: #8BBFFF;">
    <img src="https://flowbite.com/docs/images/logo.svg" alt="Flowbite" style="width: 16px; height: 16px;" />
    Flowbite
  </button>
</div>

## Dependencies:
<div align="center">

<div style="width: 50%; margin: 0 auto;">

| Dependency | Use Case |
|:----------|:---------|
| ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) | Web framework |
| ![gunicorn](https://img.shields.io/badge/gunicorn-499848?style=flat&logo=gunicorn&logoColor=white) | Production web server |
| ![python-decouple](https://img.shields.io/badge/python--decouple-3776AB?style=flat&logo=python&logoColor=white) | Environment configuration |
| ![psycopg](https://img.shields.io/badge/psycopg-336791?style=flat&logo=postgresql&logoColor=white) | PostgreSQL adapter |
| ![dj-database-url](https://img.shields.io/badge/dj--database--url-003545?style=flat&logo=django&logoColor=white) | Database URL configuration |
| ![requests](https://img.shields.io/badge/requests-3776AB?style=flat&logo=python&logoColor=white) | HTTP library |
| ![whitenoise](https://img.shields.io/badge/whitenoise-000000?style=flat&logo=python&logoColor=white) | Static file serving |
| ![django-allauth](https://img.shields.io/badge/django--allauth-092E20?style=flat&logo=django&logoColor=white) | Authentication |
| ![django-allauth-ui](https://img.shields.io/badge/django--allauth--ui-092E20?style=flat&logo=django&logoColor=white) | Auth UI components |
| ![django-widget-tweaks](https://img.shields.io/badge/django--widget--tweaks-092E20?style=flat&logo=django&logoColor=white) | Form rendering |
| ![stripe](https://img.shields.io/badge/stripe-008CDD?style=flat&logo=stripe&logoColor=white) | Payment processing |

</div>

</div>

## Setup Instructions

### 1. Virtual Environment Setup 🔧
- Create virtual environment:
  ```bash
  python3 -m venv .venv
  ```
- Activate environment:
  ```bash
  source .venv/bin/activate
  ```
- Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
- Upgrade pip:
  ```bash
  pip install pip --upgrade
  ```

### 2. Run Development Server
- Run development server:
  ```bash
  cd src
  python manage.py runserver
  ```