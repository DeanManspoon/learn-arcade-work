import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 2


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius


        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        
        super().__init__(width, height, title)

        
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0

 

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()