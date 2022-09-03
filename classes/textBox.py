import pygame
from methods import filePath

class Box:

    def __init__(self, text, color, size, game):
        self.text = text
        self.color = color
        self.game = game
        self.size = size

        self.referenceTicks = pygame.time.get_ticks()

        self.font = pygame.font.Font(str(filePath.path("fonts/PressStart2P.ttf")), self.size)

        self.wrappedLines = self.wrap_text(self.text, self.font, self.game.windowWidth)
        
        self.image = self.render_text_list(self.wrappedLines, self.font, self.color)
        
    def draw(self, surface, pos):
        surface.blit(self.image, pos)
    
    def timeDelay(self, delay):
        if self.game.now - self.referenceTicks >= delay:
            return True
        else:
            return False

    # Both the wrap_text() and render_text_list() methods 
    # were taken from https://www.reddit.com/r/pygame/comments/5j90g3/wrap_text_in_pygame/dbiv05p/?utm_source=share&utm_medium=web2x&context=3
    # by u/SotK
    def wrap_text(self, text, font, width):
        """Wrap text to fit inside a given width when rendered.
        :param text: The text to be wrapped.
        :param font: The font the text will be rendered in.
        :param width: The width to wrap to.
        """
        text_lines = text.replace('\t', '    ').split('\n')
        if width is None or width == 0:
            return text_lines

        wrapped_lines = []
        for line in text_lines:
            line = line.rstrip() + ' '
            if line == ' ':
                wrapped_lines.append(line)
                continue

            # Get the leftmost space ignoring leading whitespace
            start = len(line) - len(line.lstrip())
            start = line.index(' ', start)
            while start + 1 < len(line):
                # Get the next potential splitting point
                next = line.index(' ', start + 1)
                if font.size(line[:next])[0] <= width:
                    start = next
                else:
                    wrapped_lines.append(line[:start])
                    line = line[start+1:]
                    start = line.index(' ')
            line = line[:-1]
            if line:
                wrapped_lines.append(line)
        return wrapped_lines
    
    def render_text_list(self, lines, font, colour=(255, 255, 255)):
        """Draw multiline text to a single surface with a transparent background.
        Draw multiple lines of text in the given font onto a single surface
        with no background colour, and return the result.
        :param lines: The lines of text to render.
        :param font: The font to render in.
        :param colour: The colour to render the font in, default is white.
        """
        rendered = [font.render(line, True, colour).convert_alpha()
                    for line in lines]

        line_height = font.get_linesize()
        width = max(line.get_width() for line in rendered)
        tops = [int(round(i * line_height)) for i in range(len(rendered))]
        height = tops[-1] + font.get_height()

        surface = pygame.Surface((width, height)).convert_alpha()
        surface.fill((0, 0, 0, 0))
        for y, line in zip(tops, rendered):
            surface.blit(line, (0, y))

        return surface