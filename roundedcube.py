from scadder.model import Model
from scadder.componenttypes import Union, Translate, Difference, Mirror
from scadder.componenttypes import Cube, Cylinder


class RoundedCube(Model):
    def __init__(self, name, length, width, height, edge_radius):
        self._length = length
        self._width = width
        self._height = height
        self._edge_radius = edge_radius

        super(RoundedCube, self).__init__(name=name)

    def component(self):
        return Difference(
            name=self.name,
            children=[
                self.main_cube(),
                self.remove_edges(),
            ]
        )

    def main_cube(self):
        return Cube(name="main_cube", size=[self._length, self._width, self._height])

    def left_remove_edge(self):
        rounding_cylinder_centered = Cylinder(name="rounding_cylinder_centered", radius=self._edge_radius, height=self._height)
        rounding_cylinder = Translate(name="rounding_cylinder", children=[rounding_cylinder_centered], vector=[self._edge_radius, self._edge_radius, 0])
        remove_cube = Cube(name="remove_cube", size=[self._edge_radius, self._edge_radius, self._height])

        return Difference(name="left_remove_edge", children=[remove_cube, rounding_cylinder])

    def right_remove_edge(self):
        right_remove_edge_piece = Mirror(name="right_remove_edge_piece", vector=[1, 0, 0], children=[self.left_remove_edge()])
        return Translate(name="right_remove_edge", vector=[self._length, 0, 0], children=[right_remove_edge_piece])

    def remove_edges(self):
        return Union(name="remove_edges", children=[self.left_remove_edge(), self.right_remove_edge()])


if __name__ == "__main__":
    RoundedCube("test_rounded_cube", 30, 20, 20, 5).render("test_rounded_cube")
