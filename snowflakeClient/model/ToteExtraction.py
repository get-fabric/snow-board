from pydantic import BaseModel
class ToteExtraction(BaseModel):
    clean: int
    newSticker: int
    damaged: int
    # TODO what is that?
    prepping: int