import easyocr
from googletrans import Translator


def translation(target):
    has = target
    print(has)

    reader = easyocr.Reader(["en", "hi"], gpu=False)
    # Returns list having coordinate,string,confidence
    results = reader.readtext(has)
    text = ""

    for result in results:
        text += result[1]+' '
    print(text)
    print()

    translator = Translator()

    # returns key value output
    out = translator.translate(text, dest="hi")
    print(out.text)
