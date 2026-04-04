import base64
import contextlib
import io
import os
import tempfile

from PIL import Image

from ...utils.lazy_import import lazy_import
from ..utils.computer_vision import pytesseract_get_text

# transformers = lazy_import("transformers") # Doesn't work for some reason! We import it later.


class Vision:
    def __init__(self, computer):
        self.computer = computer
        self.model = None  # Will load upon first use
        self.tokenizer = None  # Will load upon first use
        self.easyocr = None

    def load(self, load_moondream=True, load_easyocr=True):
        # print("Loading vision models (Moondream, EasyOCR)...\n")

        with contextlib.redirect_stdout(
            open(os.devnull, "w")
        ), contextlib.redirect_stderr(open(os.devnull, "w")):
            if self.easyocr == None and load_easyocr:
                import easyocr

                self.easyocr = easyocr.Reader(
                    ["en"]
                )  # this needs to run only once to load the model into memory

            if self.model == None and load_moondream:
                import transformers  # Wait until we use it. Transformers can't be lazy loaded for some reason!

                os.environ["TOKENIZERS_PARALLELISM"] = "false"

                if self.computer.debug:
                    print(
                        "Open Interpreter will use Moondream (tiny vision model) to describe images to the language model. Set `interpreter.llm.vision_renderer = None` to disable this behavior."
                    )
                    print(
                        "Alternatively, you can use a vision-supporting LLM and set `interpreter.llm.supports_vision = True`."
                    )
                model_id = "vikhyatk/moondream2"
                revision = "2024-04-02"
                print("loading model")

                self.model = transformers.AutoModelForCausalLM.from_pretrained(
                    model_id, trust_remote_code=True, revision=revision
                )
                self.tokenizer = transformers.AutoTokenizer.from_pretrained(
                    model_id, revision=revision
                )
                return True

    def ocr(
        self,
        base_64=None,
        path=None,
        lmc=None,
        pil_image=None,
    ):
        """
        Gets OCR of image.
        """
        pass

    def query(
        self,
        query="Describe this image. Also tell me what text is in the image, if any.",
        base_64=None,
        path=None,
        lmc=None,
        pil_image=None,
    ):
        """
        Uses Moondream to ask query of the image (which can be a base64, path, or lmc message)
        """
        pass
