import pygame, sys


class Missile:
    def __init__(self, screen, x, y):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        self.screen = screen
        self.x = x
        self.y = y
        self.has_exploded = False

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        self.y -= 5

    def draw(self):
        # Draw a vertical, 4 pixels thick, 8 pixels long, red (or green) line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (0, 255, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("fighter.png")
        # Note that self.x and self.y refer to the (x,y) position of the upper left corner of the image
        self.x = screen.get_width() // 2 - self.image.get_width() // 2
        self.y = screen.get_height() - self.image.get_height()
        self.missiles = []
        # Set the colorkey to white (it has a white background that needs removed)
        self.image.set_colorkey((255, 255, 255))

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        new_missile = Missile(self.screen, self.x + self.image.get_width() // 2,
                              self.screen.get_height() - self.image.get_height() + 1)
        self.missiles.append(new_missile)

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same name.
        # Set   is_dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.original_x = x
        self.y = y
        self.speed = speed * 1.5  # Can change speed here (will affect both downward and left/right movement of enemies)
        self.is_dead = False
        self.image = pygame.image.load("badguy.png")

    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        self.x += self.speed
        if abs(self.x - self.original_x) > 100:
            self.speed = -self.speed
            self.y += 4* abs(self.speed)  # Can change speed here (downward movement of enemies)

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        pass


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        pass

    def move(self):
        # Make each badguy in this EnemyFleet move.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # DONE 9: Set    enemy_rows    to an initial value of 3.
    # DONE 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    enemy_rows = 3  # Number of rows of enemies for level one (we will increase later)
    enemy_fleet = EnemyFleet(screen, enemy_rows)

    # DONE 1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # DONE 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            # NOTE: if we took out "event.type == pygame.KEYDOWN" in the code below, users could "rapid fire" the
            #       missiles by holding down the space bar and jiggling the mouse (mouse movement creates new events).
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # DONE 3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        # DONE 4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[pygame.K_LEFT] and fighter.x > -fighter.image.get_width() / 2:
            fighter.x -= 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < screen.get_width() - fighter.image.get_width() / 2:
            fighter.x += 5
        # DONE 2: Draw the fighter
        fighter.draw()

        # DONE 11: Move the enemy_fleet
        # DONE 12: Draw the enemy_fleet
        enemy_fleet.move()
        enemy_fleet.draw()

        # DONE 6: For each missile in the fighter missiles
        #   DONE 7: Move the missile
        #   DONE 8: Draw the missile
        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        # TODO 12: For each badguy in the enemy_fleet.badguys list
        #     TODO 13: For each missile in the fighter missiles
        #         TODO 14: If the badguy is hit by the missile
        #             TODO 15: Mark the badguy is_dead = True
        #             TODO 16: Mark the missile has_exploded = True

        # TODO 17: Use the fighter to remove exploded missiles
        # TODO 18: Use the enemy_fleet to remove dead badguys

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows

        # TODO 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
