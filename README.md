# rsteye

  ![RstEyeApp](rsteye.png)

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

  Download the `.deb` file from one of the stable https://github.com/RstEyeApp/rsteye/releases/ 
  
  and install it by running:

  ```sh
  sudo dpkg -i rsteye.deb
  ```

### Run the Application

  After installation, you can run `RstEyeApp &` from any terminal:
  
  you can use service file as well to start it in the background 

  reload systemctl using `sudo systemctl daemon-reload` and then start the service `sudo systemctl start rsteyeapp.service` (currently not working)

  *DO WAIT FOR FEW SEC(7-8) TO START*


# Development 

  - Debian 

    - create virtual env and install dependencies 
      - python3 -m venv .venv
      - source .venv/bin/activate
      - python3 -m pip install pillow pyinstaller python-dotenv

    - run below command to create a binary file to package it as deb package 
      `pyinstaller --name RstEyeApp --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py`    
    
    - create a deb package(`dpkg-deb --build rsteye`) after copying the binary to deb_package(rsteye) usr/bin and creating DEBIAN files  

  - Mac

     - Create a Virtual Environment and Install Dependencies
       - python3 -m venv .venv
       - source .venv/bin/activate
       - python3 -m pip install pillow pyinstaller python-dotenv
  
     - run
       `pyinstaller --name RstEyeApp --windowed --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py` 
     
     - create a zip file using `zip -r RstEyeApp.zip dist/RstEyeApp.app`


  - Windows

    - Create Virtual Environment and Install Dependencies
      - python -m venv .venv
      - .\.venv\Scripts\activate
      - python -m pip install pillow pyinstaller python-dotenv

    - Build PyInstaller Application

      - Run the following command to create a binary file:
        `pyinstaller --name RstEyeApp --onefile --add-data "med.gif;." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks --icon=rsteye.ico app.py`

    - Install Inno setup(https://jrsoftware.org/isdl.php#stable) for windows and run below command to generate an installer 
      - "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup.iss
 


# TODO

 - [X] create deb packge for debian  
 - [X] create zip for mac 
 - [X] Create installer for Windows 

  Significant Enhancements:

 - [X] Convert binary into a daemon binary, and create a service file for systemd.
 - [ ] Implement logging functionality and enable users to close the window. If the user closes it for over 3 hours, display a message emphasizing its  importance.
 - [ ] Consider rewriting the entire application in C++ for improved performance, especially since we'll utilize multithreading for logging and dealing with daemon binaries.


# App Structure 

sequenceDiagram
    participant User
    participant App
    participant ImageLoader

    User->>App: Clicks to load image
    App->>User: Shows popup with new message
    User->>App: Reads breathing exercise message
    App->>ImageLoader: Requests image
    ImageLoader->>App: Loads image
    App->>User: Displays image
