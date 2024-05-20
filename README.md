# rsteye
  - An App to take digital break
  - An App to remind users to take breaks and relax their eyes while working on the computer.

## General Info 

  - What is the purpose behind this project?
    
    > This project aims to explore various build systems, computer architectures, and operating systems available across the internet. Additionally, it will open a GIF with deep breathing instructions every hour, covering your entire screen.


# Usage Instructions

## Debian

### Set Environment Variables

  - `POPUP_DURATION`: This variable sets the duration for which you want the popup to appear. The default value is 60 seconds (1 minute). You must provide this value in seconds.

  - `POPUP_INTERVAL`: This variable sets the interval after which you want the popup to appear. The default value is 60 minutes. You must provide this value in minutes.

### Configure Environment Variables

  Set these environment variables in your shell configuration files (e.g., `.bashrc` or `.zshrc`). For example:

  ```sh
  export POPUP_DURATION=30
  export POPUP_INTERVAL=120
  ```

### Download and Install

  Download the `.deb` file and install it by running:

  ```sh
  sudo dpkg -i rsteye.deb
  ```

### Run the Application

  After installation, you can run `RstEyeApp` from any terminal:
  
  you can use service file as well to start it in the background 

  reload systemctl using `sudo systemctl daemon-reload` and then start the service `sudo systemctl start rsteyeapp.service`


# Development 

  - Debian 

    - create virtual env and install dependencies 
      - python3 -m venv .venv
      - source .venv/bin/activate
      - python3 -m pip install pillow pyinstaller python-dotenv

    - run below command to create a binary file to package it as deb package 
      `pyinstaller --name RstEyeApp --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py`    
    
    - create a deb package(`dpkg-deb --build rsteye`) after copying the binary to deb_package(rsteye) usr/bin and creating a DEBIAN files  

  - Mac

  - Windows


# TODO

 - [X] create deb packge for debian  
 - [ ] create dmg for mac 
 - [ ] create .exe for windows 

  Significant Enhancements:

 - [X] Convert binary into a daemon binary, create service file for systemd. Research equivalent solutions for Windows and macOS.
 - [ ] Implement logging functionality and enable users to close the window. If the user closes it for over 3 hours, display a message emphasizing its  importance.
 - [ ] Consider rewriting the entire application in C++ for improved performance, especially since we'll be utilizing multithreading for logging and dealing with daemon binaries.
