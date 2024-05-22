# Stage 1: Build the binary with PyInstaller
FROM ubuntu:20.04 as builder

# Set environment variables to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt-get update && \
    apt-get install -y tzdata python3 python3-pip python3-venv build-essential python3-tk

# Set the time zone
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

# Set up Python environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages
RUN pip install pillow pyinstaller python-dotenv

# Copy application source code
COPY . /app
WORKDIR /app

# Build the binary
RUN pyinstaller --name RstEyeApp --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py
