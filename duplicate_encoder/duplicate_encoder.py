def duplicate_encoder(text_to_encode: str):
    encoder_dict = {}
    for letter in text_to_encode:
        let = letter.lower()
        if encoder_dict.get(let):
            encoder_dict[let] = ")"
        else:
            encoder_dict[let] = "("

    return "".join([encoder_dict[let.lower()] for let in text_to_encode])
