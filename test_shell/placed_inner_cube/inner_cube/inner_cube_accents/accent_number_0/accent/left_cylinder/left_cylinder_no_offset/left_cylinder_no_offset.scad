// use modules
use <side_cylinder/side_cylinder.scad>

module left_cylinder_no_offset() {
    rotate(a=-90, v=[1, 0, 0]) {
        side_cylinder();
    }
}

// call module when run directly
left_cylinder_no_offset();