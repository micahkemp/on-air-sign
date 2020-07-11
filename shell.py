from scadder.model import Model
from roundedcube import RoundedCube
from accents import Accents
from scadder.componenttypes import Difference, Translate

class Shell(Model):
    def __init__(self, name, length, width, height, edge_radius, thickness, accent_radius, accent_count, accent_vertical_margin, accent_center_length):
        self.length = length
        self.width = width
        self.height = height
        self.edge_radius = edge_radius
        self.thickness = thickness
        self.accent_radius = accent_radius
        self.accent_count = accent_count
        self.accent_vertical_margin = accent_vertical_margin
        self.accent_center_length = accent_center_length

        super(Shell, self).__init__(name=name)

    def component(self):
        return Difference(name="shell", children=[self.outer_cube(), self.placed_inner_cube()])

    @property
    def inner_length(self):
        return self.length - self.thickness*2

    @property
    def inner_width(self):
        return self.width - self.thickness*2

    @property
    def inner_height(self):
        # inner height same as outer height, so accents can line up
        return self.height

    @property
    def inner_offset_length(self):
        return self.thickness

    @property
    def inner_offset_width(self):
        return self.thickness

    @property
    def inner_offset_height(self):
        # height not offset, so accents can line up
        return 0

    @property
    def inner_edge_radius(self):
        return self.edge_radius - self.thickness

    def outer_rounded_cube(self):
        return RoundedCube(
            name="outer_rounded_cube",
            length=self.length,
            width=self.width,
            height=self.height,
            edge_radius=self.edge_radius
        ).component()

    def outer_cube_accents(self):
        return Accents(
            name="outer_cube_accents",
            accent_radius=self.accent_radius,
            edge_radius=self.edge_radius,
            length=self.length,
            center_length=self.accent_center_length,
            width=self.width,
            height=self.height,
            vertical_margin=self.accent_vertical_margin,
            count=self.accent_count,
        ).component()

    def outer_cube(self):
        return Difference(
            name="outer_cube",
            children=[
                self.outer_rounded_cube(),
                self.outer_cube_accents(),
            ]
        )

    @property
    def inner_accent_radius(self):
        return self.accent_radius + self.thickness

    @property
    def inner_accent_offset(self):
        return self.thickness

    @property
    def inner_accent_center_length(self):
        return self.accent_center_length - 2*self.thickness

    @property
    def inner_accent_vertical_margin(self):
        return self.accent_vertical_margin

    def inner_cube_accents(self):
        return Accents(
            name="inner_cube_accents",
            accent_radius=self.inner_accent_radius,
            edge_radius=self.inner_edge_radius,
            length=self.inner_length,
            center_length=self.inner_accent_center_length,
            width=self.inner_width,
            height=self.inner_height,
            vertical_margin=self.inner_accent_vertical_margin,
            count=self.accent_count,
            offset=self.inner_accent_offset
        ).component()

    def inner_rounded_cube(self):
        return RoundedCube(
            name="inner_rounded_cube",
            length=self.inner_length,
            width=self.inner_width,
            height=self.inner_height,
            edge_radius=self.inner_edge_radius
        ).component()

    def inner_cube(self):
        return Difference(
            name="inner_cube",
            children=[
                self.inner_rounded_cube(),
                self.inner_cube_accents(),
            ]
        )

    def placed_inner_cube(self):
        return Translate(
            name="placed_inner_cube",
            vector=[
                self.inner_offset_length,
                self.inner_offset_width,
                self.inner_offset_height
            ],
            children=[self.inner_cube()]
        )


if __name__ == "__main__":
    Shell(
        name="test_shell",
        length=80,
        width=20,
        height=40,
        edge_radius=10,
        thickness=2,
        accent_radius=2,
        accent_center_length=28,
        accent_vertical_margin=13,
        accent_count=2
    ).render("test_shell")
