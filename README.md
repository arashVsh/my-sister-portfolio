# Yasmin Vashagh Portfolio — Django

A responsive English-language portfolio website for Yasmin Vashagh, built with Python and Django.

## Features

- Sticky section navigation
- Responsive desktop and mobile design
- Local portrait, artwork, and video loading
- Artwork lightbox gallery
- Local violin video playback
- Downloadable résumé
- Publication, YouTube, Instagram, and email links
- Sections for education, research, teaching, art, music, awards, and contact
- WhiteNoise support for static-file deployment

## 1. Add Yasmin's files

Copy the files into these exact locations:

```text
portfolio/static/portfolio/images/Vashagh_Yasmin_Photo.jpg

portfolio/static/portfolio/images/gallery/1.jpg
portfolio/static/portfolio/images/gallery/2.jpg
portfolio/static/portfolio/images/gallery/3.jpg
portfolio/static/portfolio/images/gallery/4.jpg
portfolio/static/portfolio/images/gallery/5.jpg
portfolio/static/portfolio/images/gallery/6.jpg
portfolio/static/portfolio/images/gallery/7.jpg
portfolio/static/portfolio/images/gallery/8.jpg

portfolio/static/portfolio/videos/1.mp4
portfolio/static/portfolio/videos/2.mp4
portfolio/static/portfolio/videos/3.mp4

portfolio/static/portfolio/documents/Yasmin_Vashagh_Resume.pdf
```

The résumé should be exported from LaTeX as `Yasmin_Vashagh_Resume.pdf`.

## 1. Install and run

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 3. Production notes

Before deployment:

1. Change `SECRET_KEY` in `yasmin_portfolio/settings.py`.
2. Set `DEBUG = False`.
3. Add the production domain to `ALLOWED_HOSTS`.
4. Run:

```bash
python manage.py collectstatic
```

A typical start command is:

```bash
gunicorn yasmin_portfolio.wsgi:application
```

## Main links included

- Email: yasmin.vashagh@gmail.com
- YouTube: https://www.youtube.com/@YasminVashagh
- Instagram: https://www.instagram.com/yasmin_vashagh/?hl=en
- Publication: https://en.civilica.com/doc/2042459/

## Content updates

Most visible content is in:

```text
portfolio/templates/portfolio/home.html
```

Styles are in:

```text
portfolio/static/portfolio/css/style.css
```
