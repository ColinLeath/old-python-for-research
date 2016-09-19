# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  """Print a message in a box in the middle of the screen
  2002-10-24-1133 we're moving box to upper half of screen so it should show in one eye in 
  stereo mode.
  """
  fontobject = pygame.font.Font(None,30)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 150,
                    (screen.get_height() / 3) - 15,
                    300,30), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 152,
                    (screen.get_height() / 3) - 17,
                    304,34), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 150, (screen.get_height() / 3) - 15))
  pygame.display.flip()

def ask(screen, question, default=''):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = default
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    #elif inkey == K_MINUS:
    #  current_string.append("_")
    elif inkey <= 127:
      #current_string.append(chr(inkey))
      #string.join([current_string,chr(inkey)],'')
      current_string = current_string + chr(inkey)
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((320,240))
  print ask(screen, "Name", 'default') + " was entered"

if __name__ == '__main__': main()
