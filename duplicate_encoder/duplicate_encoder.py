def duplicate_encoder(text_to_encode: str):
    encoder_dict = {}
    text_to_encode = text_to_encode.lower()
    for letter in text_to_encode:
        if encoder_dict.get(letter):
            encoder_dict[letter] = ")"
        else:
            encoder_dict[letter] = "("

    return "".join([encoder_dict[letter] for letter in text_to_encode])
