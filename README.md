# Django Project Setup Guide 🚀

## Prerequisites
<div class="prereq-container">
  <button class="prereq-btn python">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" />
    Python 3.12
  </button>
  <button class="prereq-btn pip">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" alt="pip" />
    pip
  </button>
  <button class="prereq-btn poetry">
    <img src="https://python-poetry.org/images/logo-origami.svg" alt="Poetry" />
    Poetry
  </button>
  <button class="prereq-btn git">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" />
    Git
  </button>
  <button class="prereq-btn postgres">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" />
    PostgreSQL
  </button>
  <button class="prereq-btn aws">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS" />
    AWS
  </button>
  <button class="prereq-btn stripe">
    <img src="https://cdn.worldvectorlogo.com/logos/stripe-3.svg" alt="Stripe" />
    Stripe
  </button>
  <button class="prereq-btn tailwind">
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" alt="Tailwind" />
    Tailwind
  </button>
  <button class="prereq-btn flowbite">
    <img src="https://flowbite.com/docs/images/logo.svg" alt="Flowbite" />
    Flowbite
  </button>
</div>

<style>
.prereq-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0.75rem;
  border-radius: 4px;
}

.prereq-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0.5rem;
  border: none;
  border-radius: 3px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  color: white;
}

.prereq-btn img {
  width: 16px;
  height: 16px;
}

.prereq-btn.python { background: #3776AB; }
.prereq-btn.pip { background: #0066B3; }
.prereq-btn.poetry { background: #4B5563; }
.prereq-btn.git { background: #171515; }
.prereq-btn.postgres { background: #32648C; }
.prereq-btn.aws { background: white; color: black; }
.prereq-btn.stripe { background: #a4b6ff; color: black; }
.prereq-btn.tailwind { background: white; color: black; }
.prereq-btn.flowbite { background: #8BBFFF; color: black; }

.prereq-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.15);
  filter: brightness(110%);
}

.prereq-btn:active {
  transform: translateY(0);
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}
</style>

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