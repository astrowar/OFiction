from shlex import split as sp
from SVar import Svar

__author__ = 'astrowar'

def sp_var(Q):
    if Q[0] == ":":
        return Svar(Q[1:])
    return Q

def sp_q(L):
    Ls = sp(L)
    return [ sp_var(x)  for x in Ls]


def rsplit(xa , tail = False ):
    # return stack , reminder
    x= xa +""
    b = ""
    rr = []

    j= 0


    while j < len(x) :

        if x[j] == ']':
            if b != "":
                rr =  rr + sp_q(b)
            if not tail  : return rr
            return rr, x[j+1:]

        if x[j] == '[':

            if b != "":
                rr  = rr + sp_q(b)
            b=""
            sk , xn = rsplit(x[j+1:],True )

            rr = rr + [sk]
            x = xn + ""
            j=0

            continue


        b = b + x[j]
        j+=1

    if b != "":
        rr = rr+ sp_q(b)
    if tail :
        return rr ,""
    return rr
