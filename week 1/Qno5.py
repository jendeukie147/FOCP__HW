l=24
d,e,f=113,175,12
def numned(labgrp,a,b,c):
    sub=0
    sub+=a%labgrp
    sub+=b%labgrp
    sub+=c%labgrp

    print(a//labgrp)                                        k
    print(b//labgrp)
    print(c//labgrp)
    print((sub+c)//labgrp)
numned(l,d,e,f)