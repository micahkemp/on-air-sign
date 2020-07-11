// use modules
use <front_cylinder_left_mirrored/front_cylinder_left_mirrored.scad>

module front_cylinder_right() {
    translate(v=[80, 0, 0]) {
        front_cylinder_left_mirrored();
    }
}

// call module when run directly
front_cylinder_right();