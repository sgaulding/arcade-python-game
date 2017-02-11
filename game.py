import arcade as arcade


class MyGame(arcade.Window):
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Hello', 100, 100, arcade.color.WHITE)


def main():
    MyGame(600, 600, 'My Game')
    arcade.run()


if __name__ == '__main__':
    main()
