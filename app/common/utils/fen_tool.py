from kink import inject
from loguru import logger
import requests
import time

from app.common.statics.fen_regex import fen_regex
from settings import Settings


class FenTool:

    @staticmethod
    @inject
    def fen2png_convert(fen_string: str, output_path: str, cfg: Settings):
        if fen_regex.match(fen_string):
            url = cfg.fen2png_base_url + "/api/"
            params = {
                "fen": fen_string,
                "raw": "true",
            }
            response = requests.get(url=url, params=params, stream=True)
            if response.status_code == 200:
                try:
                    with open(output_path, "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    logger.success(f"Convert Success: {output_path}")
                except OSError:
                    logger.error(f"Invalid Save Path: {output_path}")
            else:
                logger.error(f"API Failure: {fen_string}")
        else:
            logger.error(f"Invalid FEN string: {fen_string}")


    @staticmethod
    @inject
    def fen2png_convert_batch(fen_strings: list[str], cfg: Settings):
        logger.info("=== START CONVERTING ===")
        for index, fen_string in enumerate(fen_strings):
            output_path = cfg.outputs_path + f"/{index+1}.png"
            FenTool.fen2png_convert(fen_string=fen_string, output_path=output_path)
            time.sleep(1)
        logger.info("=== CONVERTING COMPLETE ===")
