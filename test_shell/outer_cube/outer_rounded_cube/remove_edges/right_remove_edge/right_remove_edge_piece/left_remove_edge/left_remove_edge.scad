// use modules
use <remove_cube/remove_cube.scad>
use <rounding_cylinder/rounding_cylinder.scad>

module left_remove_edge() {
    difference() {
        remove_cube();
        rounding_cylinder();
    }
}

// call module when run directly
left_remove_edge();