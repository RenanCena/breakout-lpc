import pygame

pygame.init()
pygame.mixer.init()

# All colors
black_color = (0, 0, 0)
white_color = (255, 255, 255)
grey_color = (215, 215, 215)
blue_color = (0, 97, 148)
red_color = (162, 8, 0)
orange_color = (183, 119, 0)
green_color = (0, 127, 33)
yellow_color = (197, 199, 37)

# All sounds
brick_sound = pygame.mixer.Sound('sounds_brick.wav')
paddle_sound = pygame.mixer.Sound('sounds_paddle.wav')
wall_sound = pygame.mixer.Sound('sounds_wall.wav')

# Window specs
window_width = 670
window_height = 700
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
font_theme = "EightBit Atari-Block.ttf"

# Game specs
score = 0
balls = 1
velocity = 3
paddle_width = 50
paddle_height = 15.5
sprites_list = pygame.sprite.Group()


# Creating Bricks
class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


all_bricks = pygame.sprite.Group()
brick_width = 40
brick_height = 10
x_gap = 7
y_gap = 5
wall_width = 10


# Making paddle movements
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > window_width - wall_width - paddle_width:
            self.rect.x = window_width - wall_width - paddle_width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


paddle = Paddle(blue_color, paddle_width, paddle_height)
paddle.rect.x = window_width // 2 - paddle_width // 2
paddle.rect.y = window_height - 50


# Creating Ball
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


ball = Ball(white_color, 10, 10)
ball.rect.x = window_width // 2 - 5
ball.rect.y = window_height // 2 - 5


# Positioning bricks
def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(red_color, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(red_color, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(orange_color, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(orange_color, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(green_color, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(green_color, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(yellow_color, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(yellow_color, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 120 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)


def main(score_0, balls_0):
    frames_per_sec = 60
    step = 0
    global font_theme
    run = True

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # Controls
        if keys[pygame.K_LEFT]:
            paddle.move_left(10)

        if keys[pygame.K_RIGHT]:
            paddle.move_right(10)

        sprites_list.update()

        # Physics
        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]
            wall_sound.play()

        if ball.rect.x >= window_width - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.y > window_height:
            ball.rect.x = window_width // 2 - 5
            ball.rect.y = window_height // 2 - 5
            ball.velocity[1] = ball.velocity[1]
            balls_0 += 1

            # End Game
            if balls_0 == 4:
                font = pygame.font.Font(font_theme, 40)
                text = font.render("GAME OVER", True, white_color)
                text_rect = text.get_rect(center=(window_width / 2, window_height / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x += ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
            paddle_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()

            if len(brick_collision_list) > 0:
                step += 1

                for i in range(0, 448, 28):

                    if step == i:
                        ball.velocity[0] += 1
                        ball.velocity[1] += 1

            # Adjusting score according to the bricks
            if 238 > brick.rect.y > 198.5:
                score_0 += 1
                brick.kill()

            elif 198.5 > brick.rect.y > 168:
                score_0 += 3
                brick.kill()

            elif 168 > brick.rect.y > 139:
                score_0 += 5
                brick.kill()

            else:
                score_0 += 7
                brick.kill()

            if len(all_bricks) == 0:
                font = pygame.font.Font(font_theme, 40)
                text = font.render("SCREEN CLEARED", True, white_color)
                text_rect = text.get_rect(center=(window_width / 2, window_height / 2))
                sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        # Making Interface
        screen.fill(black_color)

        pygame.draw.line(screen, grey_color, [0, 19], [window_width, 19], 40)

        pygame.draw.line(screen, grey_color, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, window_height],
                         wall_width)

        pygame.draw.line(screen, grey_color, [(window_width - wall_width / 2) - 1, 0],
                         [(window_width - wall_width / 2) - 1, window_height], wall_width)

        pygame.draw.line(screen, blue_color, [(wall_width / 2) - 1, window_height - 50 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, window_height - 50 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, blue_color,
                         [(window_width - wall_width / 2) - 1, window_height - 50 + paddle_height / 2 - 54 / 2],
                         [(window_width - wall_width / 2) - 1, window_height - 50 + paddle_height / 2 - 54 / 2 + 54],
                         wall_width)

        pygame.draw.line(screen, red_color, [(wall_width / 2) - 1, 115.5],
                         [(wall_width / 2) - 1, 115.5 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, red_color, [(window_width - wall_width / 2) - 1, 115.5],
                         [(window_width - wall_width / 2) - 1, 115.5 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, orange_color, [(wall_width / 2) - 1, 115.5 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 115.5 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, orange_color,
                         [(window_width - wall_width / 2) - 1, 115.5 + 2 * brick_height + 2 * y_gap],
                         [(window_width - wall_width / 2) - 1, 115.5 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, green_color, [(wall_width / 2) - 1, 115.5 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 115.5 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, green_color,
                         [(window_width - wall_width / 2) - 1, 115.5 + 4 * brick_height + 4 * y_gap],
                         [(window_width - wall_width / 2) - 1, 115.5 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, yellow_color, [(wall_width / 2) - 1, 115.5 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 115.5 + 8 * brick_height + 8 * y_gap], wall_width)

        pygame.draw.line(screen, yellow_color,
                         [(window_width - wall_width / 2) - 1, 115.5 + 6 * brick_height + 6 * y_gap],
                         [(window_width - wall_width / 2) - 1, 115.5 + 8 * brick_height + 8 * y_gap], wall_width)

        # Score text
        font = pygame.font.Font(font_theme, 40)
        text = font.render(str(f"{score_0:03}"), True, white_color)
        screen.blit(text, (65, 75))
        text = font.render(str(balls_0), True, white_color)
        screen.blit(text, (320, 35))
        text = font.render('000', True, white_color)
        screen.blit(text, (360, 75))
        text = font.render('1', True, white_color)
        screen.blit(text, (20, 35))

        sprites_list.draw(screen)
        pygame.display.update()
        clock.tick(frames_per_sec)

    pygame.quit()

# Calling all functions
bricks()
sprites_list.add(paddle)
sprites_list.add(ball)
main(score, balls)
