// use modules
use <inner_rounded_cube/inner_rounded_cube.scad>
use <inner_cube_accents/inner_cube_accents.scad>

module inner_cube() {
    difference() {
        inner_rounded_cube();
        inner_cube_accents();
    }
}

// call module when run directly
inner_cube();