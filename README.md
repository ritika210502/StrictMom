# StrictMommy – A Digital “Mom-Like” Companion 👩‍🏫📱

StrictMommy is a productivity and emotional wellness assistant designed primarily for students. It simulates the role of a strict but caring guardian, helping users stick to routines, track moods, limit screen time, and stay accountable — just like a real mom would.

---

## 🚀 Features

- ✅ User authentication (Signup, Login, Password Reset)
- 📅 Routine & goal setup with automated daily scheduling
- 😃 Mood tracking and emotion-driven schedule personalization
- ⏳ Screen time monitoring and recovery enforcement
- 📣 Notifications for reminders and motivation
- ⚖️ Punishments for rule violations, Rewards for achievements
- 👨‍👩‍👧 Guardian mode to oversee student progress
- 📊 Dashboard with weekly summaries and performance stats

---

## 🛠️ Tech Stack

| Layer              | Tech Used                         |
|-------------------|-----------------------------------|
| Backend            | Python, Django, Django REST       |
| Database           | PostgreSQL                        |
| Auth               | JWT (JSON Web Tokens)             |
| Data Science and ML| NumPy, pandas, scikit-learn, Matplotlib, Seaborn |
| Deployment         | Docker-ready (future plan)        |

---

## 📁 Project Structure

strictmommy/
├── accounts/ # Auth and Profile Management
├── routine/ # Daily study/break management
├── goals/ # Goal & roadmap setup
├── scheduler/ # Auto schedule generator
├── mood/ # Mood tracker
├── screenmonitor/ # App usage logging
├── notifications/ # Reminders & motivational quotes
├── punishments/ # Trigger warning & consequences
├── dashboard/ # Weekly summary for users/guardians
├── rewards/ # Points & badge system
├── strictmommy/ # Project root (settings, urls)
├── manage.py

---

## ⚙️ Installation Guide

### Prerequisites

- Python 3.10+
- PostgreSQL
- Virtualenv (optional but recommended)
- Git

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/strictmommy.git
cd strictmommy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup PostgreSQL DB and update `settings.py` with credentials

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

🔌 API Endpoints
Auth (/auth/)
POST /signup

POST /login

POST /logout

POST /password-reset

User
GET/PUT /user/profile

Routine & Goals
GET/POST/PUT /user/routine

GET/POST/PUT /user/goals

GET/POST /user/daily-goals

Tasks & Scheduling
GET/POST /api/tasks

GET/POST/PUT /api/schedule

Monitoring & Motivation
GET/POST /api/screentime

GET/POST /api/notify

Punishment & Rewards
GET /api/warnings

POST /api/punishments

GET /api/points

GET /api/awards

Guardian & Dashboard
POST /api/invite-guardian

GET /api/dashboard

📊 Planned ML Features
📈 Mood inference via passive signals (keyboard speed, schedule adherence, etc.)

🤖 Smart scheduler using historical productivity patterns

⚠️ Real-time anomaly detection in mood/screen time

🧠 Models built using: scikit-learn, pandas, NumPy, joblib

🧪 Testing

# Run unit tests
python manage.py test
Use Postman to explore and test REST APIs.

🌍 Deployment (Planned)
Docker containerization

CI/CD via GitHub Actions

Hosting: AWS

👨‍👩‍👧 Target Users
Students: Seek productivity, discipline, emotional balance

Guardians: Want to track student progress and engagement

💡 Contribution
Feel free to fork and contribute:

git checkout -b feature/your-feature-name
Pull requests and issue suggestions are welcome!

📄 License
This project is licensed under the MIT License.



