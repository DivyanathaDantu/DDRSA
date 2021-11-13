from SqrAndMultiImp import SqrAndMultiImp


class RSAConstants:
    """Values for Decryption"""
    p = 41141
    q = 64499
    my_N = p * q
    phiOfN = (p - 1) * (q - 1)
    my_e = 40487
    d = SqrAndMultiImp.inverse_modulo(my_e, phiOfN)

    """Values for Encryption (partner's values)"""
    N = 4014785717
    e = 12611

    """ Messages """
    msg_to_be_encrypted = "Hi this is divyanath, hope this message reaches you in good health and hale !"
    msg_to_be_decrypted = [1252269483, 1776399758, 221327816]
