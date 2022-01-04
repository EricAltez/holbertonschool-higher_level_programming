#!/usr/bin/python3
def multiple_returns(sentence):
    sentl = len(sentence)
    if sentl > 0:
        tuple_a = (sentl, sentence[0])
        return (tuple_a)
    else:
        tuple_a = (sentl, None)
        return (tuple_a)
