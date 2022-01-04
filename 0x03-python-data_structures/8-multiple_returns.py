#!/usr/bin/python3
def multiple_returns(sentence):
    sentl = len(sentence)
    if sentl > 0:
        return (tuple_a = (sentl, sentence[0]))
    else:
        return (tuple_a = (lsen, None))
