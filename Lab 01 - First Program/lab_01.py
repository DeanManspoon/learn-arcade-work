import arcade

arcade.open_window(600,600, "my first game")

arcade.set_background_color((255,0,0,0))

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(240,430,69)
arcade.finish_render()
arcade.run()

