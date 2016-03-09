#/usr/bin/env python
#coding:utf-8

from time import ctime
from string import lowercase
from random import randint, choice
from sys import maxint

doms = ['com','gov','net','edu','org','cn','net']

with open('redata.txt','ab+') as f:
    for i in range(randint(5,10)):
        dtint = randint(0,maxint)
        dtstr = ctime(dtint)

        prefixint = randint(4,7)
        em = ''
        for j in range(prefixint):
            em += choice(lowercase)

        suffixint = randint(prefixint,12)
        do = ''
        for j in range(suffixint):
            do += choice(lowercase)

        f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,
                em, do, choice(doms), dtint,
                prefixint, suffixint))
