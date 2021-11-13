from SqrAndMultiImp import SqrAndMultiImp


class RSAConstants:
    """Values for Decryption"""
    p = 41141
    q = 64499
    my_N = p * q
    phiOfN = (p - 1) * (q - 1)
    my_e = 2438696627
    d = SqrAndMultiImp.inverse_modulo(my_e, phiOfN)

    """Values for Encryption (partner's values)"""
    N = 2566387231
    e = 1985

    """ Messages """
    msg_to_be_encrypted = "Hi this is divyanath, hope this message reaches you in good health and hale !"
    msg_to_be_decrypted = [963174423, 349833966, 2305336595, 987881663, 1658138511, 1946382762, 2192380799, 428669900,
                           1810620741, 1022134689, 1118928640, 394727798, 1898002562, 862292826, 1051295317, 2546765952,
                           2154768182, 772553931, 1094503398, 673325513, 772553931, 2302755166]

