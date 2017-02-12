from unittest import TestCase


class TestMyGame(TestCase):
    def test_on_start_motion_stopped(self):
        from game import MyGame
        game = MyGame(100, 100, 'Test')
        assert game.is_motion_stopped is True

    def test_on_draw_motion_will_stop(self):
        from game import MyGame
        game = MyGame(100, 100, 'Test')
        game.is_motion_stopped = False
        game.on_draw()
        assert game.is_motion_stopped is True

    def test_on_draw_when_motion_stopped_will_stayed_stop(self):
        from game import MyGame
        game = MyGame(100, 100, 'Test')
        game.is_motion_stopped = True
        game.on_draw()
        assert game.is_motion_stopped is True

    def test_on_mouse_motion_motion_will_start(self):
        from game import MyGame
        game = MyGame(100, 100, 'Test')
        game.is_motion_stopped = True
        game.on_mouse_motion(50, 50, 50, 50)
        assert game.is_motion_stopped is False

    def test_when_player_collides_with_metal_then_score_increased(self):
        from game import MyGame
        game = MyGame(100, 100, 'Test')
        game_score_start = game.score
        first_medal = game.medal_list[0]
        game.on_mouse_motion(first_medal.center_x, first_medal.center_y, first_medal.center_x, first_medal.center_y)
        game.animate(0.1)
        assert game.score > game_score_start


