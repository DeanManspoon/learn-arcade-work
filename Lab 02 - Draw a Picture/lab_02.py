import arcade

arcade.open_window(600,600, "my first game")

arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.color.GO_GREEN)
arcade.draw_circle_filled(150, 525, 85, arcade.color.GRAY_BLUE)
arcade.draw_rectangle_filled(600, 300, 100, 300, arcade.color.BURLYWOOD)
arcade.draw_circle_filled(600, 450, 115, arcade.color.GUPPIE_GREEN)
arcade.draw_circle_filled(525, 500, 60, arcade.color.GUPPIE_GREEN)
arcade.draw_polygon_filled(((300, 301), (350, 301), (475, 0), (175, 0)), arcade.color.BLACK)

arcade.finish_render()

arcade.run()

