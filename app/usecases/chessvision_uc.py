import os
from kink import inject
from loguru import logger
import time
from app.common.structure.usecase import BaseUseCase
from app.common.utils.fen_tool import FenTool
from app.common.utils.image_tool import ImageTool
from settings import Settings


class ChessvisionUseCase(BaseUseCase):
    @inject
    def execute(self, cfg: Settings) -> None:
        if not os.path.exists(cfg.inputs_path):
            logger.error(f"Invalid inputs_path: {cfg.inputs_path}")
            return
        fen_strings = []
        with open(cfg.inputs_path, "r") as file:
            for line in file:
                fen_string = line.strip()
                fen_strings.append(fen_string)
        
        logger.info("=== START CONVERTING USING CHESSVISION ===")
        for index, fen_string in enumerate(fen_strings):
            output_path = cfg.outputs_path + f"/chessvision_{index+1}.png"
            FenTool.chessvision_convert(fen_string=fen_string, output_path=output_path)
            if os.path.exists(output_path):
                ImageTool.image_crop(image_path=output_path)
                turn = FenTool.get_current_turn(fen_string)
                ImageTool.turn_caption(image_path=output_path, turn=turn)
            time.sleep(cfg.sleep_time)
        logger.info("=== CONVERTING COMPLETE ===")
