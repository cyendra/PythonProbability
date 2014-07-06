import survey
import first
import sys
import Pmf

def Mode(hist):
    mode = 0
    ans = 0
    for val, freq in hist.Items():
        if freq > mode:
            mode = freq
            ans = val
    return (ans, mode)

if __name__ == '__main__':
    hist = Pmf.MakeHistFromList([1,2,2,3,5]);
    print Mode(hist)
    vals, freqs = hist.Render()
