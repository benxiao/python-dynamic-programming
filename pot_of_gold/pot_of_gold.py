"""
In Pots of gold game, there are two players A & B and pots of gold
arranged in a line, each containing gold coins. The players can see
how many coins are there in each gold pot and each player gets alternating
turns in which the player can pick a pot from one of the ends of the line.
The winner is the player which has a higher number of coins at the end.
The objective is to "maximize" the numbe of coins collected by A, assuming
B also plays optimally and A starts the game.

"""

from functools import lru_cache

@lru_cache(maxsize=None)
def pot_of_gold(game, i, j, k):
    # k is used to flip between two players
    if i == j:
        if k:
            return game[i], 0, [game[i]]
        else:
            return 0, game[i], [game[i]]

    lp0, lp1, lpath = pot_of_gold(game, i + 1, j, not k)
    rp0, rp1, rpath = pot_of_gold(game, i, j-1, not k)

    if k:
        if lp0 + game[i] > rp0 + game[j]:
            return lp0 + game[i], lp1, [game[i]] + lpath
        else:
            return rp0 + game[j], rp1, [game[j]] + rpath

    else:
        if lp1 + game[i] > rp1 + game[j]:
            return lp0, lp1 + game[i], [game[i]] + lpath
        else:
            return rp0, rp1 + game[j], [game[j]] + rpath








if __name__ == '__main__':
    print(pot_of_gold(game, 0, 3, True))
    print(pot_of_gold([6,1,4,9,8,5], 0, 5, False))