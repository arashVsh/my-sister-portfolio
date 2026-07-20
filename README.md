# Yasmin Vashagh Portfolio

A personal portfolio website for **Yasmin Vashagh**, built with **Python, Django, HTML, CSS, and JavaScript**.

The website presents her academic background, publication, science education work, paintings, violin performances, awards, and competitive swimming achievements.

## Live Website

[Visit yasminvashagh.com](https://yasminvashagh.com)

## About Yasmin

Yasmin Vashagh is a graduate of Farzanegan Amin 2 High School in Isfahan, Iran, part of Iran’s National Organization for Development of Exceptional Talents.

Her interests include:

- Biology and biotechnology
- Biomedical research
- Science education
- Painting
- Violin performance
- Competitive swimming

She is also a published co-author in the field of medical artificial intelligence.

## Website Sections

The portfolio includes:

- **About** — introduction and academic interests
- **Education** — high school background, GPA, and selected grades
- **Research** — publication on deep learning for brain tumor detection
- **Teaching** — biology and science education through YouTube
- **Art** — selected paintings
- **Music** — selected violin performances
- **Awards** — achievements in painting, violin, swimming, and academic activities
- **Contact** — email and social media links

## Main Links

- Portfolio: [yasminvashagh.com](https://yasminvashagh.com)
- YouTube: [Yasmin Vashagh](https://www.youtube.com/@YasminVashagh)
- Instagram: [@yasmin_vashagh](https://www.instagram.com/yasmin_vashagh/)
- Publication: [CIVILICA](https://en.civilica.com/doc/2042459/)
- Email: [yasmin.vashagh@gmail.com](mailto:yasmin.vashagh@gmail.com)

## Features

- Responsive design for desktop and mobile devices
- Sticky navigation menu
- Artwork gallery with image preview
- Locally hosted violin performance videos
- Downloadable résumé
- Publication and social media links
- Fast static asset delivery with WhiteNoise
- Django production deployment support

## Technologies

- Python
- Django
- HTML
- CSS
- JavaScript
- WhiteNoise
- Gunicorn

## Local Development

Clone the repository:

```bash
git clone https://github.com/arashVsh/my-sister-portfolio.git
cd my-sister-portfolio
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
my-sister-portfolio/
├── manage.py
├── requirements.txt
├── build.sh
├── yasmin_portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── portfolio/
    ├── templates/
    │   └── portfolio/
    │       └── home.html
    ├── static/
    │   └── portfolio/
    │       ├── css/
    │       ├── js/
    │       ├── images/
    │       ├── videos/
    │       └── documents/
    ├── views.py
    └── urls.py
```

## Deployment

The project is configured for deployment with:

- Gunicorn
- WhiteNoise
- Environment-based Django settings
- Static file collection through `collectstatic`

Required production environment variables:

```text
SECRET_KEY=your-secure-secret-key
DEBUG=False
```

The production start command is:

```bash
gunicorn yasmin_portfolio.wsgi:application
```

## Licence

This repository contains personal photographs, artwork, videos, résumé content, and other media belonging to Yasmin Vashagh.

The source code may be viewed for educational purposes, but the personal media and portfolio content may not be reused, reproduced, or redistributed without permission.
