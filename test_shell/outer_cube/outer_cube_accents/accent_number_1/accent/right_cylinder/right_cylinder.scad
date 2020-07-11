// use modules
use <right_cylinder_no_offset/right_cylinder_no_offset.scad>

module right_cylinder() {
    translate(v=[0, 0, 0]) {
        right_cylinder_no_offset();
    }
}

// call module when run directly
right_cylinder();