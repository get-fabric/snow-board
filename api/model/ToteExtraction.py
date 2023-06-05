from pydantic import BaseModel


class ToteExtraction(BaseModel):
    def __init__(self, clean: int, new_sticker: int, damaged: int, prepping: int):
        super().__init__()
        self.clean = clean
        self.new_sticker = new_sticker
        self.damaged = damaged
        self.prepping = prepping

    clean: int
    new_sticker: int
    damaged: int
    # TODO what is that?
    prepping: int
