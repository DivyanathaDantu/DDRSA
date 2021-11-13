from RSAConstants import RSAConstants
from RSADecryption import RSADecryption
from RSAEncryption import RSAEncryption
from RandomPrimeGenerator import RandomPrimeGenerator

if __name__ == '__main__':
    print("Welcome to RSA by Divyanatha Dantu. Please select an option to proceed")
    usr_input = 1
    while int(usr_input) != 0:
        print("\n0. Exit")
        print("1. Generate Random Primes p,q")
        print("2. Generate e for given p,q")
        print("3. Encrypt msg")
        print("4. Decrypt msg")
        print("5. Check signature \n")
        usr_input = int(input())
        if usr_input == 1:
            RandomPrimeGenerator().generate_p_q()
        elif usr_input == 2:
            p = int(input("Enter p:"))
            q = int(input("Enter q:"))
            RandomPrimeGenerator().generate_e(p, q)
        elif usr_input == 3:
            RSAEncryption().encrypt_msg(RSAConstants.msg_to_be_encrypted)
        elif usr_input == 4:
            RSADecryption.decrypt_msg(RSAConstants.msg_to_be_decrypted)
        elif usr_input == 0:
            print("Thank you!")
        else:
            print("Please enter only available options")
