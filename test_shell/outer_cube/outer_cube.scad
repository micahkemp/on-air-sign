// use modules
use <outer_rounded_cube/outer_rounded_cube.scad>
use <outer_cube_accents/outer_cube_accents.scad>

module outer_cube() {
    difference() {
        outer_rounded_cube();
        outer_cube_accents();
    }
}

// call module when run directly
outer_cube();