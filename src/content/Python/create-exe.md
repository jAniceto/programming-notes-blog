Title: Create a standalone executable (.exe) from a Python script
Date: 2018-08-27 18:13 
Authors: José Aniceto


## Using pyinstaller

To install pyinstaller on your pc (more details can be found here: https://www.pyinstaller.org/)

`pip install pyinstaller`

Use cmd to go to your program directory and to turn it into a exe folder

`pyinstaller yourprogram.py`

What I run:

`pyinstaller -F --windowed --icon=myapp.ico SumExcel.py`

This makes it a single exe (without the folders with all dependables) but is slightly slower, minimizes the console window sine I have a GUI, and gives it a snazzy icon that I had saved (you have to copy over the icon, or have an exception incase it isn't found)