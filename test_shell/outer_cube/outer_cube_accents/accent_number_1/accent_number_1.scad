// use modules
use <accent/accent.scad>

module accent_number_1() {
    translate(v=[0, 0, 27.0]) {
        accent();
    }
}

// call module when run directly
accent_number_1();