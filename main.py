from fastapi import FastAPI
import spacy
from pydantic import BaseModel


en_core_web = spacy.load("en_core_web_lg")
app = FastAPI(tags=['sentence'])

class Input(BaseModel):
    sentence: str

@app.post("/analyze_text")
def get_text_characteristics(sentence_input: Input):
    document = en_core_web(sentence_input.sentence)
    output_array = []
    for token in document:
        output = {
            "Index": token.i, "Token": token.text, "Tag": token.tag_, "POS": token.pos_,
            "Dependency": token.dep_, "Lemma": token.lemma_, "Shape": token.shape_,
            "Alpha": token.is_alpha, "Is Stop Word": token.is_stop
        }
        output_array.append(output)
    return {"output": output_array}

@app.post("/entity_recognition")
def get_entity(sentence_input: Input):
    document = en_core_web(sentence_input.sentence)
    output_array = []
    for token in document.ents:
        output = {
            "Text": token.text, "Start Char": token.start_char,
            "End Char": token.end_char, "Label": token.label_
        }
        output_array.append(output)
    return {"output": output_array}