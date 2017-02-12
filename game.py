import arcade as arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        output = f'Score: {self.score:02d}'
        arcade.draw_text(output, 100, 100, arcade.color.WHITE)

    def animate(self, delta_time):
        self.score += 1


def main():
    MyGame(600, 600, 'My Game')
    arcade.run()


if __name__ == '__main__':
    main()
