from accent import Accent
from scadder.model import Model
from scadder.componenttypes import Translate, Union

class Accents(Model):
    def __init__(self, name, accent_radius, edge_radius, length, center_length, width, height, vertical_margin, count, offset=0):
        self.accent_radius = accent_radius
        self.edge_radius = edge_radius
        self.length = length
        self.center_length = center_length
        self.width = width
        self.height = height
        self.vertical_margin = vertical_margin
        self.count = count
        self.offset = offset

        super(Accents, self).__init__(name=name)

    def accent(self):
        return Accent(
            name="accent",
            accent_radius=self.accent_radius,
            edge_radius=self.edge_radius,
            length=self.length,
            center_length=self.center_length,
            width=self.width,
            offset=self.offset
        ).component()

    @property
    def vertical_spacing(self):
        return (self.height - 2*self.vertical_margin) / (self.count-1)

    def accent_number(self, number):
        return Translate(
            name=f"accent_number_{number}",
            vector=[0, 0, self.vertical_margin + number*self.vertical_spacing],
            children=[self.accent()],
        )

    def accents(self):
        return [self.accent_number(i) for i in range(0, self.count)]

    def component(self):
        return Union(
            name=self._name,
            children=self.accents(),
        )



if __name__ == "__main__":
    Accents(
        name="test_accents",
        accent_radius=2,
        edge_radius=5,
        length=30,
        center_length=10,
        width=20,
        height=20,
        vertical_margin=5,
        count=3,
    ).render("test_accents")
