// use modules
use <curved_cylinder_circle_to_extrude/curved_cylinder_circle_to_extrude.scad>

module edge_cylinder() {
    rotate_extrude(angle=90) {
        curved_cylinder_circle_to_extrude();
    }
}

// call module when run directly
edge_cylinder();