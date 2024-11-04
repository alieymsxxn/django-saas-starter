# Django Project Setup Guide 🚀

## Tools & Dependencies
<div align="left">

### Core Tools
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-171515?style=flat&logo=git&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-32648C?style=flat&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonwebservices&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-38B2AC?style=flat&logo=tailwindcss&logoColor=white)
![Flowbite](https://img.shields.io/badge/Flowbite-1A56DB?style=flat&logo=flowbite&logoColor=white)

### Backend Dependencies
![Django](https://img.shields.io/badge/Django%20|%20v5.0.9-092E20?style=flat&logo=django&logoColor=white)
![gunicorn](https://img.shields.io/badge/gunicorn%20|%20v23.0.0-499848?style=flat&logo=gunicorn&logoColor=white)
![python-decouple](https://img.shields.io/badge/python--decouple%20|%20v3.8-3776AB?style=flat&logo=python&logoColor=white)
![psycopg](https://img.shields.io/badge/psycopg%20|%20v3.2.3-336791?style=flat&logo=postgresql&logoColor=white)
![dj-database-url](https://img.shields.io/badge/dj--database--url%20|%20v2.3.0-003545?style=flat&logo=django&logoColor=white)
![requests](https://img.shields.io/badge/requests%20|%20v2.32.3-3776AB?style=flat&logo=python&logoColor=white)
![whitenoise](https://img.shields.io/badge/whitenoise%20|%20v6.8.2-000000?style=flat&logo=python&logoColor=white)

### Authentication & UI
![django-allauth](https://img.shields.io/badge/django--allauth%20|%20v65.1.0-092E20?style=flat&logo=django&logoColor=white)
![django-allauth-ui](https://img.shields.io/badge/django--allauth--ui%20|%20v1.5.1-092E20?style=flat&logo=django&logoColor=white)
![django-widget-tweaks](https://img.shields.io/badge/django--widget--tweaks%20|%20v1.5.0-092E20?style=flat&logo=django&logoColor=white)

### Storage & Payment
![Stripe](https://img.shields.io/badge/Stripe%20|%20v11.2.0-008CDD?style=flat&logo=stripe&logoColor=white)
![django-storages](https://img.shields.io/badge/django--storages%20|%20v1.14.4-092E20?style=flat&logo=django&logoColor=white)
![boto3](https://img.shields.io/badge/boto3%20|%20v1.35.54-FF9900?style=flat&logo=amazonwebservices&logoColor=white)

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