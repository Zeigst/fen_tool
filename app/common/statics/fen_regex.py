import re

fen_regex = re.compile(
    r"^(([pnbrqkPNBRQK1-8]+/){7}[pnbrqkPNBRQK1-8]+)"  # Piece placement
    r" [wb]"  # Active color
    r" (K?Q?k?q?|[-])"  # Castling availability
    r" ([a-h][36]|-)"  # En passant target square
    r" (\d+)"  # Halfmove clock
    r" (\d+)$"  # Fullmove number
)