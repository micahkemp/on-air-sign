// use modules
use <left_cylinder_no_offset/left_cylinder_no_offset.scad>

module left_cylinder() {
    translate(v=[0, 0, 0]) {
        left_cylinder_no_offset();
    }
}

// call module when run directly
left_cylinder();