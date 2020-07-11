from scadder.model import Model
from scadder.componenttypes import *
from interlock import Interlock


class Window(Model):
    def __init__(self, name, length, height, thickness, interlock_depth, tolerance=None):
        self.length = length
        self.height = height
        self.thickness = thickness
        self.interlock_depth = interlock_depth
        self.tolerance = tolerance

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

    def cutout_window(self):
        if self.tolerance:
            return Window(
                name="cutout_window",
                length=self.length+self.tolerance*2,
                height=self.height+self.tolerance,
                thickness=self.thickness,
                interlock_depth=self.interlock_depth,
            ).component()

        return None

    def cutout(self):
        # force cutout_window to be a module, though there's really nothing to union here
        return Union(
            name="cutout",
            children=[
                self.cutout_window(),
            ]
        )

    def cutout_margin(self):
        return Difference(
            name="cutout_margin",
            children=[
                self.cutout_window(),
                self.component(),
            ]
        )

    @property
    def frame_length(self):
        return self.length + self.thickness*2

    @property
    def frame_thickness(self):
        # the frame should be exactly the thickness of the window so the faces align
        return self.thickness

    @property
    def frame_height(self):
        return self.height + self.thickness

    def frame_cube(self):
        return Cube(
            name="frame_cube",
            size=[self.frame_length, self.frame_thickness, self.frame_height],
        )

    def frame_cube_positioned(self):
        return Translate(
            name="frame_cube_positioned",
            vector=[-self.frame_length/2, 0, -self.frame_height],
            children=[
                self.frame_cube(),
            ]
        )


if __name__ == "__main__":
    window = Window(
        name="test_window",
        length=50,
        height=50,
        thickness=5,
        interlock_depth=3,
        tolerance=0.5,
    )

    window.render("test_window")
    window.cutout_margin().render("test_window")
    window.frame_cube_positioned().render("test_window")

