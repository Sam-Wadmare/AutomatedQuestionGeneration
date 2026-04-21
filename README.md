# AutomatedQuestionGeneration

## 🤖 Smart Aptitude Question Generator

An AI-powered Flask web app that generates aptitude questions using a pretrained Hugging Face T5 model and a local CSV dataset.

## 🚀 Features

- AI-generated question text from existing aptitude prompts.
- CSV-backed options and answers.
- Flask backend with a `/generate` API endpoint.
- Minimal browser UI with loading/error states.

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Transformers (Hugging Face)
- Torch
- Pandas
- SentencePiece

## 📦 Setup

### 1) Clone

```bash
git clone https://github.com/Sam-Wadmare/smart-aptitude-generator.git
cd smart-aptitude-generator
```

### 2) Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the app

```bash
python app.py
```

Open: `http://127.0.0.1:5000`

## 🧪 Run tests

```bash
pytest
```

## 📁 Project structure

- `app.py` — Flask app factory, routes, dataset/model setup.
- `templates/index.html` — main UI template.
- `static/script.js` — frontend interaction and rendering logic.
- `clean_general_aptitude_dataset.csv` — source aptitude dataset.
- `tests/test_app.py` — route and data schema tests.

## ⚠️ Notes

- First startup can be slower because the model may download/load.
- `/generate` returns `question`, `options`, and `answer` in JSON.
