// use modules
use <left_edge_cylinder/left_edge_cylinder.scad>

module left_edge_cylinder_mirrored() {
    mirror(v=[1, 0, 0]) {
        left_edge_cylinder();
    }
}

// call module when run directly
left_edge_cylinder_mirrored();