import pygame, sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Image, Text, and Sound")

    # Load the music and the image
    # DONE 1: Create an image with the 2dogs.JPG image
    image1 = pygame.image.load("2dogs.JPG")

    # DONE 4: Create a font object with a size 28 font.
    font1 = pygame.font.Font(None, 28)
    font2 = pygame.font.Font(None, 55)
    # print(pygame.font.get_fonts())
    # I tried to change the font, but I don't really want to go downloading fonts right now, so I'm going to hold off
    # and try to figure it out later if it becomes relevant to my game :)

    # TODO 8: Create a Sound object from the "bark.wav" file.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # DONE 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        # NOTE: This is slower & more inefficient than resizing the image in an image editing program.
        image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
        # DONE 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image1, (0,0))

        # Draw the text onto the screen
        # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        caption1 = font1.render("Two Dogs", True, BLACK)

        # DONE 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption1, ((image1.get_width() // 2) - (caption1.get_width() // 2), image1.get_height() + 5))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        caption2 = font2.render("BOOP!", True, WHITE)
        screen.blit(caption2, ((image1.get_width() // 2) - (caption2.get_width() // 2), 2))

        # Update the screen
        pygame.display.update()


main()
