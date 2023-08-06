## ColorDetector
## Project description
ColorDetector is a library for exporting colors from a photo. It supports images in .jpg, .jpeg and .png format. Colors are represented in hex and rgb format. Depending on the parameter specified by the user, it can output from 3 to 25 different colors.
## Running
`import ColorDetector`  
     
`cd = ColorDetector("filepath")`  
`cd.palete(n)`
## Functions and variables
**ColorDetector(path)** - class with one __init__ vairable, path to image: str  
**self.palete(n)** - extract n colors from image, n must be int in range <3:25>  
## Tests
`python3 -m pytest TestColorDetector.py -v`  
## Project author
Jakub Zalewski
