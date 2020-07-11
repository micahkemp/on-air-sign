// use modules
use <front_cylinder_upright/front_cylinder_upright.scad>

module front_cylinder_left_no_offset() {
    rotate(a=90, v=[0, 1, 0]) {
        front_cylinder_upright();
    }
}

// call module when run directly
front_cylinder_left_no_offset();