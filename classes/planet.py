# Import the 'pygame' module
import pygame
# Import the 'random' module
import random
# From the 'os' module, import 'listdir'
from os import listdir
# From the 'os.path' module, import 'isfile' and 'join'
from os.path import isfile, join

from methods import filePath

# Create a new class called 'Planet'
class Planet:

    
    # The constructor function
    def __init__(self, game):

        # Dictionary to convert the numerical size of the planet (by what scale factor it's image is scaled by) to an alphabetical size (to use for displaying)
        self.sizeDict = {
        0.25:"Extremely small",
        0.50:"Very small",
        0.75:"Small",
        1.00:"Average",
        1.25:"Large",
        1.50:"Very large",
        1.75:"Extremely large"
    }
        # !-- The following was copied from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
        # Create a list of all files in the art/planets folder
        planetList = ['PlanetXVIII@0.50.png', 'PlanetIII@1.75.png', 'PlanetVIII@0.75.png', 'PlanetXX@0.50.png', 'PlanetXV@1.25.png', 'PlanetXI@0.75.png', 'PlanetXXI@1.50.png', 'PlanetVII@1.25.png', 'PlanetXIX@1.25.png', 'PlanetIV@1.75.png', 'PlanetXIV@0.50.png', 'PlanetI@1.50.png', 'PlanetXII@1.00.png', 'PlanetII@0.25.png', 'PlanetX@1.75.png', 'PlanetXXII@0.25.png', 'PlanetXXIV@1.75.png', 'PlanetXIII@0.50.png', 'PlanetXXIII@0.75.png', 'PlanetXVI@0.25.png', 'PlanetVI@1.00.png', 'PlanetXIII@1.00.png', 'PlanetVI@0.50.png', 'PlanetXVI@1.75.png', 'PlanetXXIII@1.25.png', 'PlanetXVII@1.50.png', 'PlanetXXIV@0.25.png', 'PlanetXXII@1.75.png', 'PlanetVII@0.75.png', 'PlanetV@1.50.png', 'PlanetX@0.25.png', 'PlanetII@1.75.png', 'PlanetXII@0.50.png', 'PlanetIX@1.50.png', 'PlanetXIV@1.00.png', 'PlanetIV@0.25.png', 'PlanetXIX@0.75.png', 'PlanetIII@0.25.png', 'PlanetXVIII@1.00.png', 'PlanetXI@1.25.png', 'PlanetXV@0.75.png', 'PlanetXXV@1.50.png', 'PlanetXX@1.00.png', 'PlanetVIII@1.25.png', 'PlanetVI@1.75.png', 'PlanetXVI@0.50.png', 'PlanetXIII@0.25.png', 'PlanetXXIV@1.00.png', 'PlanetXXII@0.50.png', 'PlanetXVII@0.75.png', 'PlanetV@0.75.png', 'PlanetX@1.00.png', 'PlanetII@0.50.png', 'PlanetXII@1.75.png', 'PlanetI@1.25.png', 'PlanetIX@0.75.png', 'PlanetXIV@0.25.png', 'PlanetIV@1.00.png', 'PlanetXIX@1.50.png', 'PlanetVII@1.50.png', 'PlanetXXI@1.25.png', 'PlanetXV@1.50.png', 'PlanetXXV@0.75.png', 'PlanetXX@0.25.png', 'PlanetIII@1.00.png', 'PlanetXVIII@0.25.png', 'PlanetVIII@1.50.png', 'PlanetXX@1.75.png', 'PlanetXXV@1.25.png', 'PlanetXI@1.50.png', 'PlanetXXI@0.75.png', 'PlanetXVIII@1.75.png', 'PlanetIII@0.50.png', 'PlanetIV@0.50.png', 'PlanetXIV@1.75.png', 'PlanetIX@1.25.png', 'PlanetI@0.75.png', 'PlanetXII@0.25.png', 'PlanetII@1.00.png', 'PlanetX@0.50.png', 'PlanetV@1.25.png', 'PlanetXXII@1.00.png', 'PlanetXXIV@0.50.png', 'PlanetXVII@1.25.png', 'PlanetXXIII@1.50.png', 'PlanetXVI@1.00.png', 'PlanetVI@0.25.png', 'PlanetXIII@1.75.png', 'PlanetXIII@1.50.png', 'PlanetXVI@1.25.png', 'PlanetXXIII@1.75.png', 'PlanetXVII@1.00.png', 'PlanetXXIV@0.75.png', 'PlanetXXII@1.25.png', 'PlanetVII@0.25.png', 'PlanetX@0.75.png', 'PlanetV@1.00.png', 'PlanetII@1.25.png', 'PlanetI@0.50.png', 'PlanetIV@0.75.png', 'PlanetXIX@0.25.png', 'PlanetIX@1.00.png', 'PlanetXIV@1.50.png', 'PlanetIII@0.75.png', 'PlanetXVIII@1.50.png', 'PlanetXI@1.75.png', 'PlanetXXI@0.50.png', 'PlanetXXV@1.00.png', 'PlanetXX@1.50.png', 'PlanetXV@0.25.png', 'PlanetVIII@1.75.png', 'PlanetIII@1.25.png', 'PlanetVIII@0.25.png', 'PlanetXV@1.75.png', 'PlanetXXV@0.50.png', 'PlanetXXI@1.00.png', 'PlanetXI@0.25.png', 'PlanetVII@1.75.png', 'PlanetIX@0.50.png', 'PlanetXIX@1.75.png', 'PlanetIV@1.25.png', 'PlanetI@1.00.png', 'PlanetII@0.75.png', 'PlanetXII@1.50.png', 'PlanetV@0.50.png', 'PlanetX@1.25.png', 'PlanetXVII@0.50.png', 'PlanetXXII@0.75.png', 'PlanetXXIV@1.25.png', 'PlanetXXIII@0.25.png', 'PlanetVI@1.50.png', 'PlanetXVI@0.75.png', 'PlanetVIII@1.00.png', 'PlanetXV@0.50.png', 'PlanetXX@1.25.png', 'PlanetXXV@1.75.png', 'PlanetXXI@0.25.png', 'PlanetXI@1.00.png', 'PlanetXVIII@1.25.png', 'PlanetXIV@1.25.png', 'PlanetIX@1.75.png', 'PlanetXIX@0.50.png', 'PlanetI@0.25.png', 'PlanetII@1.50.png', 'PlanetXII@0.75.png', 'PlanetV@1.75.png', 'PlanetVII@0.50.png', 'PlanetXXII@1.50.png', 'PlanetXVII@1.75.png', 'PlanetXXIII@1.00.png', 'PlanetVI@0.75.png', 'PlanetXVI@1.50.png', 'PlanetXIII@1.25.png', 'PlanetVI@1.25.png', 'PlanetXXIII@0.50.png', 'PlanetXIII@0.75.png', 'PlanetXXIV@1.50.png', 'PlanetXVII@0.25.png', 'PlanetX@1.50.png', 'PlanetV@0.25.png', 'PlanetXII@1.25.png', 'PlanetI@1.75.png', 'PlanetIV@1.50.png', 'PlanetXIX@1.00.png', 'PlanetIX@0.25.png', 'PlanetXIV@0.75.png', 'PlanetVII@1.00.png', 'PlanetXI@0.50.png', 'PlanetXXI@1.75.png', 'PlanetXXV@0.25.png', 'PlanetXX@0.75.png', 'PlanetXV@1.00.png', 'PlanetVIII@0.50.png', 'PlanetIII@1.50.png', 'PlanetXVIII@0.75.png']
        
        self.name = random.choice(['Devone', 'Zehines', 'Lugetov', 'Llibutera', 'Grypso NY6', 'Mara 3K', 'Digrueter', 'Ulvuaphus', 'Azoth', 'Lonrora', 'Lailia', 'Vagawa', 'Llechunides', 'Zalilea', 'Biri 5J', 'Biri 5J', 'Streshan ZD24', 'Nebroria', 'Ucheulara', 'Tunonoe', 'Ilarvis', 'Reacarro', 'Theunides', 'Crabonus', 'Cienope', 'Geron GO3', 'Garth FV', 'Malneulara', 'Utrioruta', 'Yellade', 'Hulleshan', 'Xarilia', 'Vuihines', 'Mayumia', 'Zasibos', 'Crore ZQ', 'Trorth T9U', 'Yonuhines', 'Dozuiliv', 'Munkoth', 'Komeshan', 'Yatania', 'Outer', 'Cronenerth', 'Stritotis', 'Strao 4EIR', 'Durn 674', 'Xachiyama', 'Tistrazuno', 'Dosore', 'Tennilia', 'Heogantu', 'Xanope', 'Luenus', 'Biutis', 'Thuna 8J4', 'Gides BQ6', 'Vustriorus', 'Ilrewei', 'Xuphides', 'Gemerth', 'Sonia', 'Kuhiri', 'Dochoter', 'Sukinerth', 'Drorix 70', 'Grorix XREK', 'Taloatov', 'Ostraeter', 'Osoria', 'Gachov', 'Zutis', 'Xaobos', 'Zadocury', 'Trotitune', 'Zeon 3F16', 'Cilia 70', 'Xezeoria', 'Laborilia', 'Melmilles', 'Polroria', 'Hoilia', 'Munus', 'Gnucuyama', 'Grozezuno', 'Gomia MIWV', 'Gara O6E', 'Xezeoria', 'Laborilia', 'Melmilles', 'Polroria', 'Hoilia', 'Munus', 'Gnucuyama', 'Grozezuno', 'Gomia MIWV', 'Gara O6E'])
        # Random choice for the scale factor that the planet image will be scaled by
        self.resize = random.choice([0.25,0.50,0.75,1.00,1.25,1.50,1.75])
        # Convert that scale factor into a text size
        self.size = self.sizeDict[self.resize]
        # Choose a random item in the list planetList and create a path to that file
        self.imagePath = "art/planets/"+random.choice(planetList)
        # Load that path using pygame
        self.image = pygame.image.load(str(filePath.path(self.imagePath)))
        self.image = pygame.transform.scale(self.image, (int((game.scaleFactor/60)*self.image.get_width()), int((game.scaleFactor/60)*self.image.get_height())))
        # Scale the image by the scale factor previously determined
        self.climate = "CLIMATE"
        # Get the pygame rect object of the image
        self.rect = self.image.get_rect()
        # Set the X co ordinate of the image to be a random number between 0 and the maximum X value
        self.rect.x = random.randint(0,game.windowWidth - self.image.get_width())
        # Set the Y co ordinate of the image to be a random number between 0 and the maximum Y value
        self.rect.y = random.randint(0,game.windowHeight - self.image.get_height())