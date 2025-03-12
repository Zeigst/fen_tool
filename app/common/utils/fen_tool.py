import os
from kink import inject
from loguru import logger
import requests
import time

from app.common.statics.fen_regex import fen_regex
from settings import Settings


class FenTool:

    @staticmethod
    @inject
    def get_current_turn(fen_string: str) -> str:
        if not fen_regex.match(fen_string):
            raise ValueError(f"Invalid FEN string: {fen_string}")
        return fen_string.split()[1]

    @staticmethod
    @inject
    def fen2png_convert(fen_string: str, output_path: str, cfg: Settings) -> None:
        if not fen_regex.match(fen_string):
            logger.error(f"Invalid FEN string: {fen_string}")
            return
        try:
            url = cfg.fen2png_base_url + "/api/"
            params = {
                "fen": fen_string,
                "raw": "true",
            }
            response = requests.get(url=url, params=params, stream=True)
            if response.status_code == 200:
                with open(output_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                logger.success(f"Convert Success: {output_path}")
            else:
                logger.error(f"API Failure: {fen_string}")
        except Exception as e:
            logger.error(e)

    @staticmethod
    @inject
    def fen2png_convert_batch(fen_strings: list[str], cfg: Settings) -> None:
        if not os.path.exists(cfg.outputs_path):
            logger.error(f"Invalid outputs_path: {cfg.outputs_path}")
            return
        logger.info("=== START CONVERTING USING FEN2PNG ===")
        for index, fen_string in enumerate(fen_strings):
            output_path = cfg.outputs_path + f"/fen2png_{index+1}.png"
            FenTool.fen2png_convert(fen_string=fen_string, output_path=output_path)
            time.sleep(cfg.sleep_time)
        logger.info("=== CONVERTING COMPLETE ===")


    @staticmethod
    @inject
    def chessvision_convert(fen_string: str, output_path: str, cfg: Settings, turn_display: bool = False, pov: str = "white") -> None:
        if not fen_regex.match(fen_string):
            logger.error(f"Invalid FEN string: {fen_string}")
            return
        try:
            url = cfg.chessvision_base_url + "/" + fen_string
            params = {
                "pov": pov
            }

            if turn_display:
                turn = FenTool.get_current_turn(fen_string=fen_string)
                if turn == "w":
                    params["turn"] = "white"
                elif turn == "b":
                    params["turn"] = "black"

            response = requests.get(url=url, params=params, stream=True)
            if response.status_code == 200:
                with open(output_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                logger.success(f"Convert Success: {output_path}")
            else:
                logger.error(f"API Failure: {fen_string}")
        except Exception as e:
            logger.error(e)

    @staticmethod
    @inject
    def chessvision_convert_batch(fen_strings: list[str], cfg: Settings, turn_display: bool = False) -> None:
        if not os.path.exists(cfg.outputs_path):
            logger.error(f"Invalid outputs_path: {cfg.outputs_path}")
            return
        logger.info("=== START CONVERTING USING CHESSVISION ===")
        for index, fen_string in enumerate(fen_strings):
            output_path = cfg.outputs_path + f"/chessvision_{index+1}.png"
            FenTool.chessvision_convert(fen_string=fen_string, output_path=output_path, turn_display=turn_display)
            time.sleep(cfg.sleep_time)
        logger.info("=== CONVERTING COMPLETE ===")
