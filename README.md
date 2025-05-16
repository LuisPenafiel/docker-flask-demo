# Snake Game 🐍

A classic Snake game built with Flask, JavaScript, and Docker. The game features a retro arcade style with background music, a scoring system, and responsive controls. It is deployed on Render for public access.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Deployment on Render](#deployment-on-render)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project is a modern take on the classic Snake game, where players control a snake to eat food, grow in length, and avoid colliding with themselves. The game includes 8-bit arcade background music that plays in a loop, triggered by the first user interaction. It is built as a web application using Flask for the backend, JavaScript for the game logic, and Docker for containerization. The game is deployed on Render, making it accessible online.

## Features

- **Classic Snake Gameplay**: Control the snake to eat food and grow, avoiding self-collisions.
- **Scoring System**: Keep track of your score as you eat food.
- **Retro Background Music**: Enjoy an 8-bit arcade soundtrack that loops after the first click.
- **Responsive Controls**: Use arrow keys to navigate the snake.
- **Reset Functionality**: Restart the game with a single button.
- **Dockerized Application**: Run the game in a containerized environment for consistency.
- **Deployed on Render**: Play the game online via a public URL.

## Technologies Used

- **Flask**: A lightweight Python web framework for serving the game.
- **JavaScript/HTML5 Canvas**: Used for the game logic and rendering.
- **Docker**: Containerization for consistent development and deployment.
- **Render**: Hosting platform for deploying the web application.
- **GitHub**: Version control and repository hosting.

## Installation

To run the Snake game locally, follow these steps:

### Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **Docker**: Install Docker to run the application in a container.
- **Git**: Required to clone the repository.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/penafiel2004/docker-flask-demo.git
   cd docker-flask-demo
   ```

2. **Set Up the Environment**:
   - If you prefer running without Docker, create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
   - Alternatively, proceed with Docker in the next step.

3. **Build and Run with Docker**:
   - Build the Docker image:
     ```bash
     docker build -t snake-game .
     ```
   - Run the container:
     ```bash
     docker run -p 8080:8080 snake-game
     ```

4. **Access the Game**:
   - Open your browser and go to `http://localhost:8080`.
   - Click anywhere on the page to start the background music and play the game.

## How to Play

- **Controls**: Use the **arrow keys** (↑, ↓, ←, →) to move the snake.
- **Objective**: Eat the green food to grow the snake and increase your score.
- **Game Over**: The game resets if the snake collides with itself.
- **Reset**: Click the "Reset Game" button to start over.
- **Music**: The background music starts playing after your first click and loops continuously.

## Deployment on Render

The game is deployed on Render and accessible online. Follow these steps to deploy your own instance:

1. **Create a Render Account**:
   - Sign up at [Render](https://render.com).

2. **Set Up a New Web Service**:
   - Click "New" → "Web Service".
   - Connect your GitHub account and select the `docker-flask-demo` repository.
   - Configure the service:
     - **Name**: `snake-game`
     - **Environment**: Docker
     - **Region**: Choose the region closest to you (e.g., Oregon)
     - **Branch**: `main`
     - **Build Command**: Leave blank (Render uses the `Dockerfile`)
     - **Start Command**: Leave blank (defined in `Dockerfile`)
     - **Instance Type**: Free
   - Click "Create Web Service".

3. **Access the Deployed Game**:
   - Once deployed, Render will provide a URL (e.g., `https://snake-game.onrender.com`).
   - Open the URL, click on the page, and enjoy the game with background music.

### Note on Render Deployment
- The free tier of Render may suspend the service after inactivity, causing a delay on the first load.
- For better performance, the project uses `gunicorn` as the WSGI server in production (see `requirements.txt` and `Dockerfile`).

## Project Structure

```
docker-flask-demo/
├── Dockerfile              # Docker configuration for building the image
├── README.md               # Project documentation (this file)
├── app.py                  # Flask application to serve the game
├── requirements.txt        # Python dependencies
├── static/                 # Static files (music, favicon)
│   ├── arcade-8bit.mp3    # Background music
│   └── favicon.ico         # Favicon for the browser tab
└── templates/              # HTML templates
    └── game.html           # Main game page with JavaScript logic
```

## Future Improvements

- Add difficulty levels (e.g., adjustable speed).
- Implement a "Game Over" screen with the final score.
- Add sound effects for eating food or game over events.
- Include a high score system with local storage.
- Enhance the UI with more styling and animations.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request on GitHub.

Please ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **xAI**: For providing Grok, which assisted in the development and debugging of this project.
- **Render**: For hosting the deployed game.
- **Flask**: For making web development with Python simple and fun.
- **The Open Source Community**: For providing resources like 8-bit music and tutorials.

---

Happy gaming! 🐍