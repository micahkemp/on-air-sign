// use modules
use <inner_cube/inner_cube.scad>

module placed_inner_cube() {
    translate(v=[2, 2, 0]) {
        inner_cube();
    }
}

// call module when run directly
placed_inner_cube();