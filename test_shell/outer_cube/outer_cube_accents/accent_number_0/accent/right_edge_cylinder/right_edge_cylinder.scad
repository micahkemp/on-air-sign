// use modules
use <left_edge_cylinder_mirrored/left_edge_cylinder_mirrored.scad>

module right_edge_cylinder() {
    translate(v=[80, 0, 0]) {
        left_edge_cylinder_mirrored();
    }
}

// call module when run directly
right_edge_cylinder();