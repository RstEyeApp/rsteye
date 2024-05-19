# rsteye
  - An App to take digital break
  - An App to remind users to take breaks and relax their eyes while working on the computer.

## General Info 

  - What is the purpose behind this project?
    
    > This project aims to explore various build systems, computer architectures, and operating systems available across the internet. Additionally, it will open a GIF with deep breathing instructions every hour, covering your entire screen.


## Use 

  - Linux 
     - download .deb file and run `sudo dpkg -i rsteye.deb`

## Development 

  - Linux 

    - run below command to create a binary file for package it as deb package 
      `pyinstaller --name RstEyeApp --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py`    
    
    - create a deb package(`dpkg-deb --build rsteye`) after copying the binary to deb_package(rsteye) usr/bin and creating a control file  

  - Mac

  - Windows


## TODO

 - [X] create deb packge for debian  
 - [ ] create dmg for mac 
 - [ ] create .exe for windows 

  Significant Enhancements:

 - [X] Convert binary into a daemon binary, possibly placing it in init.d for Linux. Research equivalent solutions for Windows and macOS.
 - [ ] Implement logging functionality and enable users to close the window. If the user closes it for over 3 hours, display a message emphasizing its  importance.
 - [ ] Consider rewriting the entire application in C++ for improved performance, especially since we'll be utilizing multithreading for logging and dealing with daemon binaries.
