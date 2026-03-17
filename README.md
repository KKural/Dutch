# Dutch B1 Part 2 — Interactive Learning App

An interactive Flask web app for learning Dutch at the B1.2 level.  
Built for Tamil-speaking researchers at UGent, Ghent.

## Features
- 25 structured sessions covering grammar, vocabulary & exercises
- 375 interactive exercises (fill-in, multiple choice, true/false, translate, reorder)
- Progress tracking with scores
- Ghent-specific context & CVO Canvas / Nedbox-style exercises

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy on Render (free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Settings: **Build Command** = `pip install -r requirements.txt` | **Start Command** = `gunicorn app:app`
5. Click Deploy — done!

## Tech Stack
- Python 3.13 + Flask 3.1
- Vanilla JS (no frontend framework)
- JSON-based progress storage
