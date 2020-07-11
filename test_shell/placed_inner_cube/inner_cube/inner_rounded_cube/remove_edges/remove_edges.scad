// use modules
use <left_remove_edge/left_remove_edge.scad>
use <right_remove_edge/right_remove_edge.scad>

module remove_edges() {
    union() {
        left_remove_edge();
        right_remove_edge();
    }
}

// call module when run directly
remove_edges();