import base64


def convert_hex_to_base64(hex_str):
    if not isinstance(hex_str, basestring):
        raise TypeError("should have provided str! :(")
    hex_str = hex_str.decode("hex")
    
    return base64.standard_b64encode(bytes(hex_str))
