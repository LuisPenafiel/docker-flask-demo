# 🐍 docker-flask-demo + Snake Game (Flask + Docker)

Simple Snake game with web interface

## ▶️ Run It
```bash
# With Docker:
docker build -t snake-game . && docker run -p 5000:5000 snake-game

# Without Docker:
pip install -r requirements.txt
python app.py
```
## 🌐 Access
Open http://localhost:5000 in your browser

## 📦 Files
.
├── devcontainer.json         
├── app.py                 
├── Dockerfile             
├── requirements.txt
└── templates/
    └── game.html 

## 🛠️  Troubleshooting    

No game window? Expected in Docker - use the web interface

502 Error? Wait a few seconds for Flask to start
