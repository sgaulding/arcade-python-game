import random

import arcade as arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0

        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite('images/zombie_stand.png', 0.6)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        self.medal_list = arcade.SpriteList()
        for i in range(50):
            medal = arcade.Sprite('images/flat_medal4.png', 0.4)
            medal.center_x = random.randrange(600)
            medal.center_y = random.randrange(600)
            self.all_sprites_list.append(medal)
            self.medal_list.append(medal)

    def on_draw(self):
        arcade.start_render()
        output = f'Score: {self.score:02d}'
        arcade.draw_text(output, 100, 100, arcade.color.WHITE)
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.medal_list
        )

        for medal in hit_list:
            medal.kill()
            self.score += 1

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    MyGame(600, 600, 'My Game')
    arcade.run()


if __name__ == '__main__':
    main()
