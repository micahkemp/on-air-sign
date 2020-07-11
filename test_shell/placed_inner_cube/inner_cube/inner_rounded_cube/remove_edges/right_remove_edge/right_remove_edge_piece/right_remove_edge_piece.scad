// use modules
use <left_remove_edge/left_remove_edge.scad>

module right_remove_edge_piece() {
    mirror(v=[1, 0, 0]) {
        left_remove_edge();
    }
}

// call module when run directly
right_remove_edge_piece();