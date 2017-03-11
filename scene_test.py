from scene import *

class MyScene (Scene):
    def setup(self):
        self.background_color = 'midnightblue'
        self.ship = SpriteNode('spc:PlayerShip1Orange')
        self.ship.position = self.size / 2
        self.add_child(self.ship)

    def touch_began(self, touch):
        x, y = touch.location
        move_action = Action.move_to(x, y, 0.7, TIMING_SINODIAL)
        self.ship.run_action(move_action)

run(MyScene())
