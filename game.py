import arcade as arcade


def main():
    arcade.open_window('Prune Game', 600, 600)
    arcade.start_render()
    arcade.draw_text('Hello', 100, 100, arcade.color.WHITE)
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()
