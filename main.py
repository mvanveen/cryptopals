import base64


def convert_hex_to_base64(hex_str):
    if not isinstance(hex_str, basestring):
        raise TypeError("should have provided str! :(")

    hex_str = hex_str.decode("hex")
    return base64.standard_b64encode(bytes(hex_str))


def fixed_xor(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("srings are not of same length")

    return ''.join(
        chr(ord(a) ^ ord(b)) for (a, b) in zip(
            s1.decode('hex'),
            s2.decode('hex')
        )
    ).encode('hex')


if __name__ == '__main__':
     print fixed_xor(
         '1c0111001f010100061a024b53535009181c',
         '686974207468652062756c6c277320657965'
     )
     print fixed_xor(
         '1c0111001f010100061a024b53535009181c',
         '686974207468652062756c6c277320657965'
     ).decode('hex')
     cypher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
     
     for i in '0':
         print '---'
         print i
         cypher_2 = i * len(cypher)
         cypher_2[0] = 'a'
     
         print fixed_xor(cypher_2, cypher).decode('hex')
