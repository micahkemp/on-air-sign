// use modules
use <curved_cylinder_circle/curved_cylinder_circle.scad>

module curved_cylinder_circle_to_extrude() {
    translate(v=[-10, 0, 0]) {
        curved_cylinder_circle();
    }
}

// call module when run directly
curved_cylinder_circle_to_extrude();