// use modules
use <front_cylinder_left_no_offset/front_cylinder_left_no_offset.scad>

module front_cylinder_left() {
    translate(v=[0, 0, 0]) {
        front_cylinder_left_no_offset();
    }
}

// call module when run directly
front_cylinder_left();