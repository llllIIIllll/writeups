#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-10 19:57:46
# @Last Modified by:   john
# @Last Modified time: 2016-11-06 01:18:09

import string
import collections

cipher = '''
ltxswnqat, ekrsmvqtb mnxm wtvt xatfvm mfk mnt wtxhfstbb ku mnt bmvxqznmukvwxfvo lkskxacnxgtmqe brfgbmqmrmqks eqcntv wtvt xsyqkrb mk otjtfakc x gtmmtv eqcfntv, fbkltmnqsz mnfxm wkrao cvkmtem mntqv kws sxmqks`b ltbfbxztb uvkl gtqsz rsbevxlgato gd tstld evdfcmxsfxadbmb. kst ku mnt bqlcatfbm qlcvkjtltsmb mk mfnt btervqmd ku mnt lkskxacnxgtmfqe brgbmqmrfmqks eqcntv wxb mnt qsmvkoremfqks ku sraab, bdlgkab kv atmmtvb mnxm wtvt skm bfrgbmqmrmtb ukv xemrxa atmmtvb, ltvtad gaxfshb mnxm vtcvtbtsmto skmnqsz. ukv tyxlcat, kst ekrao brfgbmqmrmt txen caxfqs atmfmtv wqmn x srlgtv gtmwtts kst xso sqstmd-sqst, wnqen wkrao atxjt btjtsmd-mnvtt srlgtvb mnxm vtcvtbtsm skmnqsz, xso mntbt ekrao gt vxsoklad bcvqshato mnvkrznkrm mntf eqcntvmtym wqmn jxvdqsz uvtirtseqtb. mnt sraab wkrao ckbt sk cvkgfatl mk mnt qsmtsoto vteqcqtsm, fwnk wfkrao hskw mnxm mntd wftvt mk gt qzskvto. nkwtjtv, mnt sraab wkrao gxuuat xs tstld qsmtvetcmkv gtexrbt mntd wkrao eksurbt xs xmmxeh gd uvtirtfsed xsxfadbqb. dkr xvt akkhqsz ukv mnqb cnvxbt:'qs bqszn wt mvrbm'.
bqlks atnsx bqszn, qb x gvqmqbn ckcrafxv beqtset xrmnkv wnkfbt wkvffhb axvztad eksmxqs x bmvksz lxmntlfxmqexa tatltsm. nqb wvqmmts wkvhb qsearot utvlxm'b axbm mntkfvtl (qs mnt rsqmto bmxmtb mqmafto utvlxm'b tsqzlx: mnt tcqe irtbm mk bkajt mnt wkvao'b zvtxmtbm lxmntlxmqexa cvkgatl), mnt ekot gkkh (xgkfrm evdcmkzvxcnd xso qmb nqbmkvd), gqzf gxsz (xgkrm mnt gqz gxsz mntkvd xso mnt kvqzqsb ku mnt rsqjtvbft), mvqeh kv mvtxmltsm? xamtvsxmqjt ltoqeqst ks mvqxa (xgkrm eklcatltsmxvd xso xamtvsxmqjt ltoqeqfst, ek-wvfqmmts gd topxvo tvsbm) xso mnt bqlcbksb xso mntqv lxmntlxmqexa btevtmb (xgkrm lxmntlxmqexa qotxb xsfo mntkvtlb nqoots qs tcqbkotb ku mnft bqlcbksb xso ufrmrvxlx). qs mwk mnkrbxso xso mwtajt bqszn ukrsoto mnt zkko mnqshqsz bkeqtmd.
'''

def rotate(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


for i in range(26):
    print i, rotate(cipher, i)
