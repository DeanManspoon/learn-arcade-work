import arcade
import random


SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
TILE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 200




class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.wall_list = None
        self.shrooms_list = None
        self.player_sprite = None


        self.physics_engine = None


        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        platforms_layer_name = 'Platforms'

        coins_layer_name = 'Coins'

        foreground_layer_name = 'Foreground'

        background_layer_name = 'Background'

        dont_touch_layer_name = "Don't Touch"


        map_name = f"maps\level1.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        self.end_of_map = my_map.map_size.width * SPRITE_SCALING_BOX

        self.background_list = arcade.tilemap.process_layer(my_map,
                                                           background_layer_name,
                                                           TILE_SCALING)

        self.foreground_list = arcade.tilemap.process_layer(my_map,
                                                            foreground_layer_name,
                                                            TILE_SCALING)


        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name, 
                                                     scaling=TILE_SCALING,
                                                      use_spatial_hash=True)


        self.tinyshroom_list = arcade.tilemap.process_layer(my_map,                               
                                                      coins_layer_name,
                                                     TILE_SCALING,
                                                     use_spatial_hash=True)

        self.dont_touch_list = arcade.tilemap.process_layer(my_map,
                                                           dont_touch_layer_name,
                                                           TILE_SCALING,
                                                           use_spatial_hash=True)
        arcade.set_background_color(arcade.color.BANANA_YELLOW)

        self.view_left = 0
        self.view_bottom = 0


        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.score = 0
        self.shrooms_list = arcade.SpriteList()
        for x in range(20):
            shrooms = arcade.Sprite("images/tinyShroom_red.png", SPRITE_SCALING_BOX)
            shrooms.center_x = random.randint(1, SCREEN_WIDTH)
            shrooms.center_y = random.randint(1, SCREEN_HEIGHT)
            self.shrooms_list.append(shrooms)

    
        coordinate_list = [[300, 300],
                           [370, 300],
                           [200, 370],
                           [270, 370]]

    
        for coordinate in coordinate_list:
            shrooms = arcade.Sprite("images/tinyShroom_red.png", SPRITE_SCALING_BOX)
            shrooms.center_x = coordinate[0]
            shrooms.center_y = coordinate[1]
            self.shrooms_list.append(shrooms)

        self.player_sprite = arcade.Sprite("images\zombie_cheer2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)


        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        for x in range(173, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)


        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

 
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.shrooms_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        self.physics_engine.update()
        changed = False
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True


        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True


        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True


        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)


        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

        touching = arcade.check_for_collision_with_list(self.player_sprite, self.shrooms_list)
        for shroom in touching:
            shroom.kill()
            self.score += 1
        self.player_sprite.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D: 
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:   
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        if key == arcade.key.W or key == arcade.key.S:   
            self.player_sprite.change_y = 0

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        arcade.draw_text(str(self.score), SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK)                                                                   
        self.shrooms_list.draw()

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()