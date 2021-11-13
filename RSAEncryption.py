from RSAConstants import RSAConstants
from SqrAndMultiImp import SqrAndMultiImp


class RSAEncryption:
    def divide_msg(self, message):
        divided_msg = [message[i:i+3] for i in range(0, len(message), 3)]
        msg_in_int = list()
        for chunk in divided_msg:
            msg_in_int.append(self.covert_string_to_int(chunk))
        return msg_in_int

    @staticmethod
    def covert_string_to_int(chunk):
        chunk = chunk.encode()
        chunk = chunk.hex()
        chunk = int(chunk, 16)
        return chunk

    def encrypt_msg(self, message):
        msg_in_int = self.divide_msg(message)
        enc_msg = list()
        for integer in msg_in_int:
            enc_msg.append(SqrAndMultiImp.sqr_and_mul(integer, RSAConstants.e, RSAConstants.N))
        print("Encrypted msg is :-", enc_msg)


rsa_enc = RSAEncryption()

rsa_enc.encrypt_msg(RSAConstants.msg_to_be_encrypted)
