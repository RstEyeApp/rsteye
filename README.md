# rsteye
    An App to take digital break
        An App to remind users to take breaks and relax their eyes while working on the computer.
## Use 

  - Linux 
    download .deb file and run `sudo dpkg -i rsteye.deb`

## Development 

  - Linux 

    run below command to create a binary file for package it as deb package 
    pyinstaller --name RstEyeApp --onefile --add-data "med.gif:." --hidden-import=PIL.ImageTk --additional-hooks-dir=hooks app.py
    create a deb package(`dpkg-deb --build deb_package`) after copying the binary to deb_package(rsteye) usr/bin and creating a control file  

  - Mac

  - Windows


## TODO

 - [X] create deb packge for debian  
 - [] create dmg for mac 
 - [] create .exe for windows 