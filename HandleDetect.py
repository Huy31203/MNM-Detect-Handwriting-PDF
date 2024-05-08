import cv2
from PIL import Image
import enchant

from enchant.checker import SpellChecker
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

import os

def convertToString(segments, language = "vi_VN"):
    os.environ['KMP_DUPLICATE_LIB_OK']='True'

    config = Cfg.load_config_from_file('venv/Include/Models/config.yml')

    detector = Predictor(config)

    
    result = ""
    
    for segment in segments:
        # chuyển đổi ảnh đen trắng để dự đoán (vì dễ đọc)
        segment_pil = Image.fromarray(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
        segment_pil_gray = segment_pil.convert('L')

        text = detector.predict(segment_pil_gray)
        result += " " + text # type: ignore
    
    # dùng thư viện enchant để chỉnh sửa chính tả
    vi_dict = enchant.Dict(language)
    chkr = SpellChecker(vi_dict)
    chkr.set_text(result)

    
    for err in chkr:
        sug = err.suggest()
        if sug:
            err.replace(sug[0])
            result = chkr.get_text()

    return result