// use modules
use <edge_cylinder/edge_cylinder.scad>

module left_edge_cylinder() {
    translate(v=[10, 10, 0]) {
        edge_cylinder();
    }
}

// call module when run directly
left_edge_cylinder();