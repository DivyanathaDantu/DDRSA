from RSAConstants import RSAConstants
from SqrAndMultiImp import SqrAndMultiImp


class RSADecryption:
    @staticmethod
    def decrypt_msg(encrypted_msg):
        dec_msg = ""
        dec_chunks = []
        for integer in encrypted_msg:
            integer = hex(SqrAndMultiImp.sqr_and_mul(integer, RSAConstants.d, RSAConstants.my_N))
            dec_string = bytearray.fromhex(integer[2:]).decode()
            dec_chunks.append(dec_string)
            dec_msg = dec_msg + dec_string
        print("chunks :-", dec_chunks)
        print("Decrypted msg is :-", dec_msg)


# rsa_dec = RSADecryption()
# rsa_dec.decrypt_msg(RSAConstants.msg_to_be_decrypted)
