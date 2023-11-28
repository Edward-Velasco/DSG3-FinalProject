# Infinity Deadpool

## Execution
Executing this project can be easily done by running it using Python:
```
python.exe -m pip install -U pygame --user
python.exe -m pip install -U unicode --user
python.exe .\main.py
```

## Executable Creation
To create an executable from the game, so you don't need to have Python installed run the following commands:
```
pip install pyinstaller
pip install --upgrade pyinstaller
pyinstaller --onefile -w main.py
```
Make sure to add the `./assets` directory to the same folder as the executable to ensure assets are available!