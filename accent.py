from scadder.model import Model
from scadder.componenttypes import Cylinder, Translate, Rotate, Union, Circle, RotateExtrude, Mirror

class Accent(Model):
    def __init__(self, name, accent_radius, edge_radius, length, center_length, width, offset=0):
        self.accent_radius = accent_radius
        self.edge_radius = edge_radius
        self.length = length
        self.center_length = center_length
        self.width = width
        self.offset = offset

        super(Accent, self).__init__(name=name)

    @property
    def front_cylinder_height(self):
        return (self.length - self.center_length)/2

    def side_cylinder(self):
        return Cylinder(name="side_cylinder", radius=self.accent_radius, height=self.width)

    def left_cylinder_no_offset(self):
        return Rotate(name="left_cylinder_no_offset", angle=-90, vector=[1, 0, 0], children=[self.side_cylinder()])

    def left_cylinder(self):
        return Translate(name="left_cylinder", vector=[-self.offset, 0, 0], children=[self.left_cylinder_no_offset()])

    def right_cylinder_no_offset(self):
        return Translate(name="right_cylinder_no_offset", vector=[self.length, 0, 0], children=[self.left_cylinder_no_offset()])

    def right_cylinder(self):
        return Translate(name="right_cylinder", vector=[self.offset, 0, 0], children=[self.right_cylinder_no_offset()])

    def front_cylinder_upright(self):
        return Cylinder(name="front_cylinder_upright", radius=self.accent_radius, height=self.front_cylinder_height)

    def front_cylinder_left_no_offset(self):
        return Rotate(name="front_cylinder_left_no_offset", angle=90, vector=[0, 1, 0], children=[self.front_cylinder_upright()])

    def front_cylinder_left(self):
        return Translate(name="front_cylinder_left", vector=[0, -self.offset, 0], children=[self.front_cylinder_left_no_offset()])

    def front_cylinder_left_mirrored(self):
        return Mirror(name="front_cylinder_left_mirrored", vector=[1, 0, 0], children=[self.front_cylinder_left()])

    def front_cylinder_right(self):
        return Translate(name="front_cylinder_right", vector=[self.length, 0, 0], children=[self.front_cylinder_left_mirrored()])

    def curved_cylinder_circle(self):
        return Circle(name="curved_cylinder_circle", radius=self.accent_radius)

    def curved_cylinder_circle_to_extrude(self):
        return Translate(name="curved_cylinder_circle_to_extrude", vector=[-self.edge_radius-self.offset, 0, 0], children=[self.curved_cylinder_circle()])

    def edge_cylinder(self):
        return RotateExtrude(name="edge_cylinder", angle=90, children=[self.curved_cylinder_circle_to_extrude()])

    def left_edge_cylinder(self):
        return Translate(name="left_edge_cylinder", vector=[self.edge_radius, self.edge_radius, 0], children=[self.edge_cylinder()])

    def left_edge_cylinder_mirrored(self):
        return Mirror(name="left_edge_cylinder_mirrored", vector=[1, 0, 0], children=[self.left_edge_cylinder()])

    def right_edge_cylinder(self):
        return Translate(name="right_edge_cylinder", vector=[self.length, 0, 0], children=[self.left_edge_cylinder_mirrored()])

    def component(self):
        return Union(
            name=self._name,
            children=[
                self.left_cylinder(),
                self.right_cylinder(),
                self.front_cylinder_left(),
                self.front_cylinder_right(),
                self.left_edge_cylinder(),
                self.right_edge_cylinder(),
            ]
        )


if __name__ == "__main__":
    Accent(
        name="test_accent",
        accent_radius=2,
        edge_radius=5,
        length=30,
        center_length=10,
        width=20
    ).render("test_accent")

    Accent(
        name="test_accent_offset",
        accent_radius=2,
        edge_radius=5,
        length=30,
        center_length=10,
        width=20,
        offset=2,
    ).render("test_accent_offset")