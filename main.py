import base64


def convert_hex_to_base64(hex_str):
    if not isinstance(hex_str, basestring):
        raise TypeError("should have provided str! :(")
    hex_str = hex_str.decode("hex")
    
    return base64.standard_b64encode(bytes(hex_str))


def fixed_xor(s1, s2):
    #TODO(mvv): make sure strings are of correct type!
    if not len(s1) == len(s2):
        raise ValueError("strings are of not same length :(")

    zipped_result = zip(s1, s2)

    return ''.join([
        bytes(int(a[0], 16) ^ int(b[0], 16)) for a, b in zipped_result
    ])


