import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, x, y, color, radius, speed_x, speed_y):
        """ Creates a ball that will bounce around the screen. Speed CANNOT be zero."""
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        """ Draws ball onto the screen."""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        """ Controls the movement of the ball."""
        if self.speed_x > 0:
            if self.x + self.speed_x <= self.screen.get_width() - self.radius:
                self.x += self.speed_x
            else:
                self.x = self.screen.get_width() - self.radius
                self.speed_x = -self.speed_x
        else:
            if self.x + self.speed_x >= self.radius:
                self.x += self.speed_x
            else:
                self.x = self.radius
                self.speed_x = -self.speed_x

        if self.speed_y > 0:
            if self.y + self.speed_y <= self.screen.get_height() - self.radius:
                self.y += self.speed_y
            else:
                self.y = self.screen.get_height() - self.radius
                self.speed_y = -self.speed_y
        else:
            if self.y + self.speed_y >= self.radius:
                self.y += self.speed_y
            else:
                self.y = self.radius
                self.speed_y = -self.speed_y



def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # DONE: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, 20, 20, (0, 0, 0), 10, 3, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        ball1.move()
        # TODO: Draw the ball
        ball1.draw()
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
