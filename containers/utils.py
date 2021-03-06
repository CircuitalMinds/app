def str_decode(strs):
    strs = strs.strip()
    decoders = dict({
        "&nbsp": '\\xc2\\xa0', "¡": '\\xc2\\xa1', "¢": '\\xc2\\xa2', "£": '\\xc2\\xa3',
        "¤": '\\xc2\\xa4', "¥": '\\xc2\\xa5', "¦": '\\xc2\\xa6', "§": '\\xc2\\xa7',
        "¨": '\\xc2\\xa8', "©": '\\xc2\\xa9', "ª": '\\xc2\\xaa', "«": '\\xc2\\xab',
        "¬": '\\xc2\\xac', "&shy": '\\xc2\\xad', "®": '\\xc2\\xae', "¯": '\\xc2\\xaf',
        "°": '\\xc2\\xb0', "±": '\\xc2\\xb1', "²": '\\xc2\\xb2', "³": '\\xc2\\xb3',
        "´": '\\xc2\\xb4', "µ": '\\xc2\\xb5', "¶": '\\xc2\\xb6', "·": '\\xc2\\xb7',
        "¸": '\\xc2\\xb8', "¹": '\\xc2\\xb9', "º": '\\xc2\\xba', "»": '\\xc2\\xbb',
        "¼": '\\xc2\\xbc', "½": '\\xc2\\xbd', "¾": '\\xc2\\xbe', "¿": '\\xc2\\xbf',
        "À": '\\xc3\\x80', "Á": '\\xc3\\x81', "Â": '\\xc3\\x82', "Ã": '\\xc3\\x83',
        "Ä": '\\xc3\\x84', "Å": '\\xc3\\x85', "Æ": '\\xc3\\x86', "Ç": '\\xc3\\x87',
        "È": '\\xc3\\x88', "É": '\\xc3\\x89', "Ê": '\\xc3\\x8a', "Ë": '\\xc3\\x8b',
        "Ì": '\\xc3\\x8c', "Í": '\\xc3\\x8d', "Î": '\\xc3\\x8e', "Ï": '\\xc3\\x8f',
        "Ð": '\\xc3\\x90', "Ñ": '\\xc3\\x91', "Ò": '\\xc3\\x92', "Ó": '\\xc3\\x93',
        "Ô": '\\xc3\\x94', "Õ": '\\xc3\\x95', "Ö": '\\xc3\\x96', "×": '\\xc3\\x97',
        "Ø": '\\xc3\\x98', "Ù": '\\xc3\\x99', "Ú": '\\xc3\\x9a', "Û": '\\xc3\\x9b',
        "Ü": '\\xc3\\x9c', "Ý": '\\xc3\\x9d', "Þ": '\\xc3\\x9e', "ß": '\\xc3\\x9f',
        "à": '\\xc3\\xa0', "á": '\\xc3\\xa1', "â": '\\xc3\\xa2', "ã": '\\xc3\\xa3',
        "ä": '\\xc3\\xa4', "å": '\\xc3\\xa5', "æ": '\\xc3\\xa6', "ç": '\\xc3\\xa7',
        "è": '\\xc3\\xa8', "é": '\\xc3\\xa9', "ê": '\\xc3\\xaa', "ë": '\\xc3\\xab',
        "ì": '\\xc3\\xac', "í": '\\xc3\\xad', "î": '\\xc3\\xae', "ï": '\\xc3\\xaf',
        "ð": '\\xc3\\xb0', "ñ": '\\xc3\\xb1', "ò": '\\xc3\\xb2', "ó": '\\xc3\\xb3',
        "ô": '\\xc3\\xb4', "õ": '\\xc3\\xb5', "ö": '\\xc3\\xb6', "÷": '\\xc3\\xb7',
        "ø": '\\xc3\\xb8', "ù": '\\xc3\\xb9', "ú": '\\xc3\\xba', "û": '\\xc3\\xbb',
        "ü": '\\xc3\\xbc', "ý": '\\xc3\\xbd', "þ": '\\xc3\\xbe', "ÿ": '\\xc3\\xbf',
    })
    for k, v in decoders.items():
        strs = strs.replace(v, k)
    return strs
