# Import the pathlib module
import pathlib

def path(file):
    # Return a Path object
    return pathlib.Path(file)

# The point of this function is to make my code cross-platform.
# When referencing a file on Windows, you would need to do:
#       C:\\folder\\file.txt
# Whereas on most other operating systems (including Mac, my primary OS):
#       folder/file.txt
# Hard coding file referencing is bound to cause some headaches later on.
# This is why I use the pathlib module. A pathlib Path object uses the
# appropiate styling for the current OS.