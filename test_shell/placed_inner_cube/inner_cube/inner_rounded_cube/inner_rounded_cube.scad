// use modules
use <main_cube/main_cube.scad>
use <remove_edges/remove_edges.scad>

module inner_rounded_cube() {
    difference() {
        main_cube();
        remove_edges();
    }
}

// call module when run directly
inner_rounded_cube();