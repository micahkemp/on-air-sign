// use modules
use <main_cube/main_cube.scad>
use <remove_edges/remove_edges.scad>

module outer_rounded_cube() {
    difference() {
        main_cube();
        remove_edges();
    }
}

// call module when run directly
outer_rounded_cube();