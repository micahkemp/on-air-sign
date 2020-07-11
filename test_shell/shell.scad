// use modules
use <outer_cube/outer_cube.scad>
use <placed_inner_cube/placed_inner_cube.scad>

module shell() {
    difference() {
        outer_cube();
        placed_inner_cube();
    }
}

// call module when run directly
shell();