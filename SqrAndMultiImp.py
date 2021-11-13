class SqrAndMultiImp:
    @staticmethod
    def inverse_modulo(base, mod):
        prev_res = 0
        res = 1
        reminder = mod
        prev_reminder = base
        while prev_reminder != 1:
            cur_prev_rem = prev_reminder
            prev_reminder = reminder % prev_reminder
            cur_prev_res = res
            res = prev_res - res * int(reminder / cur_prev_rem)
            prev_res = cur_prev_res
            reminder = cur_prev_rem
        return res % mod

    @staticmethod
    def sqr_and_mul(base, exp, mod):
        exp_in_binary = bin(exp)
        squares = list()
        squares.append(base)
        powers = 2
        while powers <= exp:
            squares.append(squares[-1] ** 2 % mod)
            powers *= 2
        inc = 0
        res = 1
        for bit in exp_in_binary[2:][::-1]:
            if int(bit) == 1:
                res *= squares[inc]
                res %= mod
            inc += 1
        return res
