import arcade
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 6











class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.player = arcade.Sprite("./zombie_cheer2.png", 0.5)
    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D: 
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:   
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
        if key == arcade.key.W or key == arcade.key.S:   
            self.player.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print(x, y)

def main():

    
    window = MyGame(600, 480, "Yeah boi")
    arcade.run()
main()
