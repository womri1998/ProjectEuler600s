from math import ceil
from modulo import mod, modulo


JUMP = 1504170715041707
MOD = 4503599627370517


def next_coin(last_coin: modulo) -> modulo:
    multiplicand = last_coin.modulus // last_coin.residue + 1
    return last_coin * multiplicand


def sum_of_coins(coin: modulo = mod(JUMP, MOD)) -> int:
    total = coin.residue
    last_coin = coin.residue
    while coin.residue != 1:
        coin = next_coin(coin)
        print(last_coin > coin.residue)
        total += coin.residue
    return total


if __name__ == "__main__":
    print(sum_of_coins())
