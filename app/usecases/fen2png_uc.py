from kink import inject
from app.common.structure.usecase import BaseUseCase
from app.common.utils.fen_tool import FenTool
from settings import Settings


class FEN2PngExecUseCase(BaseUseCase):
    @inject
    def execute(self, cfg: Settings) -> None:
        fen_strings = []
        with open(cfg.inputs_path, "r") as file:
            for line in file:
                fen_string = line.strip()
                fen_strings.append(fen_string)
        FenTool.fen2png_convert_batch(fen_strings=fen_strings)
