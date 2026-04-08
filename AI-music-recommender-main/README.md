---
title: PLM Devs AI Music Recommender
emoji: 🎵
colorFrom: green
colorTo: gray
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: true
license: mit
---

# 🎵 Mood-Based AI Music Recommender

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)
![AI](https://img.shields.io/badge/AI-Q--Learning-green?style=for-the-badge)
![Songs](https://img.shields.io/badge/Songs-168+-purple?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-5-orange?style=for-the-badge)

**Built by PLM Devs 🚀**

*An industry-level AI-powered music recommendation system that learns from you.*

</div>

---

## 🧠 What Makes This Special?

Most music apps use static algorithms. This app uses **Reinforcement Learning (Q-Learning)** — meaning the AI literally gets smarter every time you give feedback. Like a song? The AI remembers. Skip it? It learns that too. Every user gets their own personal AI brain that evolves over time.

---

## ✨ Features

### 🎧 Core Recommendation Engine
- **Q-Learning RL Agent** — personalized per user, learns from Like / Listen / Skip feedback
- **NLP Mood Detection** — type how you feel, AI detects mood using VaderSentiment
- **Voice Input** — speak your mood, AI transcribes and detects it
- **Dropdown Selection** — quick manual mood pick
- **Auto Time Detection** — suggests time-of-day based on your system clock
- **🎲 Surprise Me!** — random mood + genre + language combo for discovery

### 🌍 Multi-Language Support
| Language | Songs |
|----------|-------|
| Hindi    | 67    |
| English  | 67    |
| Punjabi  | 14    |
| Tamil    | 10    |
| Telugu   | 10    |
| **Total**| **168** |

### 🤖 AI Chatbot
Natural language song requests — just type what you want:
- `"sad hindi songs do"`
- `"party punjabi chahiye"`
- `"lofi focus music"`
- `"surprise me"`

### 📊 Weekly Music Report
- Sessions, Likes, Listens, Skips breakdown
- Mood & Genre charts
- Daily activity graph
- Top songs of the week
- Personalized insight message
- Download as `.txt`

### 🏆 Gamification System
- **XP Points** — Like = +10, Listen = +2, Skip = -2
- **6 Levels** — Newbie → Listener → Music Fan → Enthusiast → Audiophile → Legend
- **11 Badges** — First Beat, Music Lover, On Fire, 3/7-Day Streak, Mood Explorer, Genre Master, Power User, Century, Chill Master, Focus Champion
- **Daily Streak Tracker**
- **Badge unlock toast notifications**

### 🌐 Social Features
- **Community Playlists** — share your playlist with a note, others can like it
- **AI Friend Match** — compare Q-Tables with friends, get a match % with gauge chart
- **Favourites** — heart any song, saved permanently
- **Export Playlist** — download favourites as `.txt`

### ⏱️ Productivity Tools
- **Real Pomodoro Timer** — actual countdown with presets (25 min, 50 min, 5/10 min break)
- **Sleep Timer** — music stops after set time
- **Session counter** — tracks completed Pomodoro sessions

### 📓 Mood Journal
- Write daily mood entries with notes
- Mood distribution pie chart
- Timeline of past entries

### 📈 Analytics Dashboard
- Q-Value Heatmap (State × Genre matrix)
- Raw Q-Table data
- Mood trend over time (line chart)

### 🔐 Authentication
- Secure login / signup with SHA-256 hashed passwords
- Per-user data isolation
- Change password from profile
- Logout from sidebar

### 🛡️ Admin God Mode
Login with `admin_plm` / `admin123` to access:
- View all users' Q-Tables
- Delete user profiles
- Inject new songs into the database
- View all users' listening history

### 🔔 Streak Reminders
- In-app warning banner if streak is about to break
- Browser notification support (click "Enable Streak Reminders" in Chatbot tab)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit + Custom CSS (Glassmorphism) |
| AI/ML | Q-Learning (Reinforcement Learning) |
| NLP | VaderSentiment |
| Speech | SpeechRecognition (Google API) |
| Data | Pandas, NumPy |
| Charts | Plotly Express + Graph Objects |
| Auth | SHA-256 hashing, JSON storage |
| Storage | JSON files (per-user) |

---

## 🚀 How to Run

**1. Clone / download the project**

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the app:**
```bash
streamlit run app.py
```

**4. Open browser:** `http://localhost:8501`

---

## 📂 Project Structure

```
AI-music-recommender-main/
│
├── app.py              # Main Streamlit app — all UI & tab logic
├── agent.py            # Q-Learning RL agent
├── env.py              # RL environment (states, actions, rewards)
├── recommend.py        # Song filtering & recommendation engine
├── nlp_engine.py       # Mood detection (NLP) + voice transcription
├── dashboard.py        # Analytics / Q-table heatmap rendering
├── auth.py             # Login, signup, history, mood journal
├── gamification.py     # XP, levels, badges, streaks
├── social.py           # Community playlists, favourites, export
├── chatbot.py          # Rule-based AI chatbot
├── weekly_report.py    # Weekly stats & report generation
├── pomodoro.py         # Pomodoro + sleep timer
│
├── data/
│   └── songs.csv       # 168 songs (Hindi, English, Punjabi, Tamil, Telugu)
│
├── .streamlit/
│   └── config.toml     # Streamlit theme config
│
├── requirements.txt
└── README.md
```

> **Runtime files** (auto-generated per user):
> - `q_table_{username}.json` — RL agent memory
> - `history_{username}.json` — listening history
> - `stats_{username}.json` — XP, badges, streak
> - `favourites_{username}.json` — saved songs
> - `journal_{username}.json` — mood journal
> - `users.json` — hashed credentials
> - `shared_playlists.json` — community playlists

---

## 🎯 How the AI Works

```
User gives feedback (Like / Listen / Skip)
           ↓
    Reward assigned (+10 / +2 / -5)
           ↓
  Q-Learning formula updates Q-Table:
  Q(s,a) = Q(s,a) + α × (r + γ × max Q(s') - Q(s,a))
           ↓
  Next recommendation uses updated Q-values
  (epsilon-greedy: 80% exploit, 20% explore)
```

**State** = `Mood_TimeOfDay_LastGenre`  
**Action** = Genre (Pop, Lo-fi, Rock, Instrumental, Classical)  
**Reward** = Based on user feedback

---

## 🔑 Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin_plm` | `admin123` |
| User | *(sign up)* | *(your choice)* |

---

## 📦 Requirements

```
streamlit
pandas
numpy
vaderSentiment
SpeechRecognition
plotly
```

Install all: `pip install -r requirements.txt`

---

<div align="center">

Made with ❤️ by **PLM Devs**

🚀 Designed & Developed by **Pranav Chakravorty**

*"Turning mood into music, one algorithm at a time."*

</div>
