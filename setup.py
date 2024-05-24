from setuptools import setup

APP = ['app.py']
DATA_FILES = ['med.gif']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL'],
    'includes': ['PIL', 'PIL.Image', 'PIL.ImageTk', 'PIL.ImageSequence'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)