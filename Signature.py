from RSAConstants import RSAConstants
from RSAEncryption import RSAEncryption
from SqrAndMultiImp import SqrAndMultiImp


class Signature:
    @staticmethod
    def sign():
        msg_in_int = RSAEncryption().divide_msg(RSAConstants.my_signature)
        enc_msg = list()
        for integer in msg_in_int:
            enc_msg.append(SqrAndMultiImp.sqr_and_mul(integer, RSAConstants.d, RSAConstants.my_N))
        print("Signature is:-", enc_msg)

    @staticmethod
    def verify():
        dec_msg = ""
        for integer in RSAConstants.partners_signature:
            integer = hex(SqrAndMultiImp.sqr_and_mul(integer, RSAConstants.e, RSAConstants.N))
            integer = bytearray.fromhex(integer[2:]).decode()
            dec_msg = dec_msg + integer
        print("Verified Signature is :-", dec_msg)


