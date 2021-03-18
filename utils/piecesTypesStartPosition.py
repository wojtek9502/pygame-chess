from utils.PiecesTypesEnum import PiecesTypesEnum

# x - field row
# y - field column
# syntax: (x, y)
PIECES_START_POSITIONS = {
    PiecesTypesEnum.KING: [(4, 0), (4, 7)],
    PiecesTypesEnum.QUEEN: [(3, 0), (3, 7)],
    PiecesTypesEnum.ROOK: [(0, 0), (7, 0), (0, 7), (7, 7)],
    PiecesTypesEnum.BISHOP: [(2, 0), (5, 0), (2, 7), (5, 7)],
    PiecesTypesEnum.KNIGHT: [(1, 0), (6, 0), (1, 7), (6, 7)],
    PiecesTypesEnum.PAWN: [
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
        (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
    ],
}
