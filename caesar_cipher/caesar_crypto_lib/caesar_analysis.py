#! /usr/bin/python

from caesar_cipher.caesar_crypto_lib import CaesarDecrypt


def count_letters(tokens, out):
    for i in tokens:
        out[i] += 1


def parse_prob_matrix(prob_mat):
    count = sum(prob_mat[0])
    for r in prob_mat:
        for i, v in enumerate(r):
            r[i] = v / count

    return prob_mat


def dist(a, b):

    out = 0
    for j, k in zip(a, b):
        out += (j - k) ** 2

    return out


def find_min(mat, prob_vect):

    dv = [0] * len(mat)
    for i, v in enumerate(mat):
        d = dist(v, prob_vect)
        dv[i] = d

    I = 0
    m = dv[I]
    for i in range(1, len(mat)):
        if dv[i] < m:
            m = dv[i]
            I = i

    # index 0 contains data from key 1
    return I + 1, dv


def prob_analysis(cipher, prob_vect, lc=26):

    prob_mat = [None] * lc
    caesar_decrypt = CaesarDecrypt(cipher)

    for i, tv in enumerate(caesar_decrypt):
        tmp = [0] * lc
        tv.analyze(lambda x: count_letters(x, tmp))
        prob_mat[i] = tmp

    prob_mat = parse_prob_matrix(prob_mat)

    return find_min(prob_mat, prob_vect)









