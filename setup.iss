[Setup]
AppName=RstEyeApp
AppVersion=1.0
DefaultDirName={pf}\RstEyeApp
DefaultGroupName=RstEyeApp
OutputDir=dist
OutputBaseFilename=RstEyeAppInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\RstEyeApp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "med.gif"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\RstEyeApp"; Filename: "{app}\RstEyeApp.exe"

[Run]
Filename: "{app}\RstEyeApp.exe"; Description: "{cm:LaunchProgram,RstEyeApp}"; Flags: nowait postinstall skipifsilent
