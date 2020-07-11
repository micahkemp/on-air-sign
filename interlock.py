from scadder.model import Model
from scadder.componenttypes import *

from math import atan2, degrees

class Interlock(Model):
    def __init__(self, name, height, thickness, depth):
        self.height = height
        self.thickness = thickness
        self.depth = depth

        super(Interlock, self).__init__(name=name)

    @property
    def interlock_cube_remove_front_bevel_angle(self):
        return -degrees(atan2(self.depth, self.thickness/2))

    def interlock_cube(self):
        return Cube(name="interlock_cube", size=[self.depth, self.thickness, self.height])

    def remove_front_bevel(self):
        return Rotate(
            name="remove_front_bevel",
            angle=self.interlock_cube_remove_front_bevel_angle,
            vector=[0, 0, 1],
            children=[
                self.interlock_cube(),
            ]
        )

    def remove_front_bevel_mirror(self):
        return Mirror(
            name="remove_front_bevel_mirror",
            vector=[0, 1, 0],
            children=[
                self.remove_front_bevel(),
            ]
        )

    def remove_back_bevel(self):
        return Translate(
            name="remove_back_bevel",
            vector=[0, self.thickness, 0],
            children=[
                self.remove_front_bevel_mirror(),
            ]
        )

    def remove_bevel(self):
        return Union(
            name="remove_bevel",
            children=[
                self.remove_front_bevel(),
                self.remove_back_bevel(),
            ]
        )

    def component(self):
        return Difference(
            name=self.name,
            children=[
                self.interlock_cube(),
                self.remove_bevel(),
            ]
        )


if __name__ == "__main__":
    Interlock(
        name="test_interlock",
        height=20,
        thickness=3,
        depth=2
    ).render("test_interlock")
