# -*- coding: utf-8 -*-

import syllab


def word2pieces(word):
    return '|'.join(syllab.split_word(word))


def test_split_word():
    assert(word2pieces(u'кошка') == u'кош|ка')


if __name__ == '__main__':
    test_split_word()
