from RSAConstants import RSAConstants
from RSADecryption import RSADecryption
from RSAEncryption import RSAEncryption
from RandomPrimeGenerator import RandomPrimeGenerator
from Signature import Signature
from SqrAndMultiImp import SqrAndMultiImp

if __name__ == '__main__':
    print("Welcome to RSA by Divyanatha Dantu. Please select an option to proceed")
    usr_input = 1
    while int(usr_input) != 0:
        print("\n0. Exit")
        print("1. Generate Random Primes p,q")
        print("2. Generate e,d for given p,q")
        print("3. Encrypt msg")
        print("4. Decrypt msg")
        print("5. Sign")
        print("6. Verify Signature\n")
        usr_input = int(input())
        if usr_input == 1:
            p, q = RandomPrimeGenerator().generate_p_q()
            n = p * q
            phiOfN = (p - 1) * (q - 1)
            print("\n n-", n, " phiOfN -", phiOfN, "for given p -", p, "and q-", q)
        elif usr_input == 2:
            p = int(input("Enter p:"))
            q = int(input("Enter q:"))
            e = RandomPrimeGenerator().generate_e(p, q)
            phiOfN = (p - 1) * (q - 1)
            d = SqrAndMultiImp.inverse_modulo(e, phiOfN)
            print("\n d for given e -", e, "is", d)
        elif usr_input == 3:
            RSAEncryption().encrypt_msg(RSAConstants.msg_to_be_encrypted)
        elif usr_input == 4:
            RSADecryption.decrypt_msg(RSAConstants.msg_to_be_decrypted)
        elif usr_input == 5:
            Signature.sign()
        elif usr_input == 6:
            Signature.verify()
        elif usr_input == 0:
            print("Thank you!")
        else:
            print("Please enter only available options")
