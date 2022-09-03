class Dialogue():

    def __init__(self, text):
        self.boxPath = filePath.path("art/GUI/dialogueBox.png")

        self.boxImage = pygame.image.load(str(self.boxPath))