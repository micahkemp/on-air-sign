// use modules
use <rounding_cylinder_centered/rounding_cylinder_centered.scad>

module rounding_cylinder() {
    translate(v=[8, 8, 0]) {
        rounding_cylinder_centered();
    }
}

// call module when run directly
rounding_cylinder();