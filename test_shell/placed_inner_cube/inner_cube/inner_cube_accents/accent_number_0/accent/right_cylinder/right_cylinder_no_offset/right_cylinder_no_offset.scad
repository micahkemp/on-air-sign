// use modules
use <left_cylinder_no_offset/left_cylinder_no_offset.scad>

module right_cylinder_no_offset() {
    translate(v=[76, 0, 0]) {
        left_cylinder_no_offset();
    }
}

// call module when run directly
right_cylinder_no_offset();