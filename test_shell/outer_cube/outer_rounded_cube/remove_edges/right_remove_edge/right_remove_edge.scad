// use modules
use <right_remove_edge_piece/right_remove_edge_piece.scad>

module right_remove_edge() {
    translate(v=[80, 0, 0]) {
        right_remove_edge_piece();
    }
}

// call module when run directly
right_remove_edge();