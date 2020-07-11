from scadder.model import Model
from scadder.componenttypes import *
from interlock import Interlock


class Window(Model):
    def __init__(self, name, length, height, thickness, interlock_depth):
        self.length = length
        self.height = height
        self.thickness = thickness
        self.interlock_depth = interlock_depth

        super(Window, self).__init__(name=name)

    def window_cube(self):
        return Cube(name="window_cube", size=[self.length, self.thickness, self.height])

    def vertical_interlock(self):
        return Interlock(
            name="side_interlock",
            height=self.height,
            thickness=self.thickness,
            depth=self.interlock_depth,
        ).component()

    def horizontal_interlock_vertical_oriented(self):
        return Interlock(
            name="horizontal_interlock_vertical_oriented",
            height=self.length,
            thickness=self.thickness,
            depth=self.interlock_depth,
        ).component()

    def bottom_interlock(self):
        return Rotate(
            name="bottom_interlock",
            angle=90,
            vector=[0, 1, 0],
            children=[
                self.horizontal_interlock_vertical_oriented(),
            ]
        )

    def left_interlock(self):
        return Mirror(
            name="left_interlock",
            vector=[1, 0, 0],
            children=[
                self.vertical_interlock(),
            ]
        )

    def right_interlock(self):
        return Translate(
            name="right_interlock",
            vector=[self.length, 0, 0],
            children=[self.vertical_interlock()],
        )

    def left_interlock_for_corner(self):
        return Translate(
            name="left_interlock_for_corner",
            vector=[0, 0, -self.interlock_depth],
            children=[
                self.left_interlock(),
            ]
        )

    def bottom_interlock_for_corner(self):
        return Translate(
            name="bottom_interlock_for_corner",
            vector=[-self.interlock_depth, 0, 0],
            children=[
                self.bottom_interlock(),
            ]
        )

    def bottom_left_interlock_corner(self):
        return Intersection(
            name="bottom_left_interlock_corner",
            children=[
                self.left_interlock_for_corner(),
                self.bottom_interlock_for_corner(),
            ]
        )

    def bottom_left_interlock_corner_mirror(self):
        return Mirror(
            name="bottom_left_interlock_corner_mirror",
            vector=[1, 0, 0],
            children=[
                self.bottom_left_interlock_corner(),
            ]
        )

    def bottom_right_interlock_corner(self):
        return Translate(
            name="bottom_right_interlock_corner",
            vector=[self.length, 0, 0],
            children=[
                self.bottom_left_interlock_corner_mirror(),
            ]
        )

    def window_origin_bottom_left(self):
        return Union(
            name="window_origin_bottom_left",
            children=[
                self.window_cube(),
                self.left_interlock(),
                self.right_interlock(),
                self.bottom_interlock(),
                self.bottom_left_interlock_corner(),
                self.bottom_right_interlock_corner(),
            ],
        )

    def component(self):
        return Translate(
            name=self.name,
            vector=[-self.length/2, 0, -self.height],
            children=[
                self.window_origin_bottom_left(),
            ],
        )


if __name__ == "__main__":
    Window(
        name="test_window",
        length=50,
        height=50,
        thickness=5,
        interlock_depth=3,
    ).render("test_window")
