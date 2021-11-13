from RSAConstants import RSAConstants
from SqrAndMultiImp import SqrAndMultiImp


class RSADecryption:
    @staticmethod
    def decrypt_msg(encrypted_msg):
        dec_msg = ""
        for integer in encrypted_msg:
            integer = hex(SqrAndMultiImp.sqr_and_mul(integer, RSAConstants.d, RSAConstants.my_N))
            integer = bytearray.fromhex(integer[2:]).decode()
            dec_msg = dec_msg + integer
        print("Decrypted msg is :-", dec_msg)


rsa_dec = RSADecryption()
rsa_dec.decrypt_msg(RSAConstants.msg_to_be_decrypted)
