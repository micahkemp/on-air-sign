// use modules
use <accent_number_0/accent_number_0.scad>
use <accent_number_1/accent_number_1.scad>

module inner_cube_accents() {
    union() {
        accent_number_0();
        accent_number_1();
    }
}

// call module when run directly
inner_cube_accents();