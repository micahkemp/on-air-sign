// use modules
use <accent/accent.scad>

module accent_number_0() {
    translate(v=[0, 0, 13.0]) {
        accent();
    }
}

// call module when run directly
accent_number_0();