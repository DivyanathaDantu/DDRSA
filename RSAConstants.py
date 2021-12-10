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
    N = 76602983
    e = 44944441

    """ Messages """
    msg_to_be_encrypted = "Hi this is divyanath, hope this message reaches you in good health and hale !"
    msg_to_be_decrypted = [987881663, 1658138511, 1946382762, 114993941, 2067727052, 280669318, 1204057221, 2101752276]
    """ Signatures """
    my_signature = "Divyanatha Reddy Dantu"
    partners_signature = [55647728, 17491099, 27997253, 74547410, 21382997]
