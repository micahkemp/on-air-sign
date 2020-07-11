// use modules
use <left_cylinder/left_cylinder.scad>
use <right_cylinder/right_cylinder.scad>
use <front_cylinder_left/front_cylinder_left.scad>
use <front_cylinder_right/front_cylinder_right.scad>
use <left_edge_cylinder/left_edge_cylinder.scad>
use <right_edge_cylinder/right_edge_cylinder.scad>

module accent() {
    union() {
        left_cylinder();
        right_cylinder();
        front_cylinder_left();
        front_cylinder_right();
        left_edge_cylinder();
        right_edge_cylinder();
    }
}

// call module when run directly
accent();