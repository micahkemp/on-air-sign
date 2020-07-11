// use modules
use <front_cylinder_left/front_cylinder_left.scad>

module front_cylinder_left_mirrored() {
    mirror(v=[1, 0, 0]) {
        front_cylinder_left();
    }
}

// call module when run directly
front_cylinder_left_mirrored();