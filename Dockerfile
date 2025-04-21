FROM python:3.8-slim

# Install Pygame + virtual display dependencies
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    python3-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

ENV SDL_AUDIODRIVER="dummy"
ENV PULSE_SERVER="none"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create dummy ALSA config to silence errors
RUN mkdir -p /usr/share/alsa/alsa.conf.d \
    && echo "defaults.pcm.card 0" > /usr/share/alsa/alsa.conf.d/dummy.conf \
    && echo "defaults.ctl.card 0" >> /usr/share/alsa/alsa.conf.d/dummy.conf

# Use virtual display with audio/sound disabled
CMD ["xvfb-run", "-a", "python", "-u", "app.py"]
