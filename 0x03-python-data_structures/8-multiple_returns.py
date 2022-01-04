#!/usr/bin/python3
def multiple_returns(sentence):
    sentl = len(sentence)
    if sentl > 0:
        return (sentl, sentence[0])
    elif sentl == 0:
        return (lsen, None)
