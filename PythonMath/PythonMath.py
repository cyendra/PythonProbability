import survey
import first
import sys
import Pmf
import matplotlib.pyplot as pyplot
import myplot
import descriptive

def Mode(hist):
    mode = 0
    ans = 0
    for val, freq in hist.Items():
        if freq > mode:
            mode = freq
            ans = val
    return (ans, mode)

if __name__ == '__main__':
    descriptive.main(*sys.argv)