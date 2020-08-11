import os

import numpy as np

from tools import retdoc
from evaluation import extract

HOME = os.getcwd()
annfile = os.path.join(HOME, "data/procdata/ready_joined_rj_k500_N10.csv")

def avprec(ranking, rel_set):
    nrel = 0
    precisions = np.zeros(len(rel_set))
    for i, d in enumerate(ranking):
        if d in rel_set:
            nrel += 1
            precisions[nrel-1] = nrel / (i + 1)
    return precisions.mean()


def patk(ranking, rel_set, k):
    if k < 0:
        raise Exception("no '0' or negative position in the ranking")
    nrel = 0
    for d in ranking[:k]:
        if d in rel_set:
            nrel += 1
    
    return nrel / min(len(ranking), k)

def rprec(ranking, rel_set):
    return patk(ranking, rel_set, k=len(rel_set))


def map(SearchCore, top, lsi_rank, verbose):

    avprecs_vsm = np.array([])
    avprecs_lsi = np.array([])
    if verbose:
        print("\n VSM_AP   LSI_AP  query")

    for q, rel_set in rdd.items():
        r = retdoc.retrieve(SearchCore, query=q,
                            top=top, lsi_rank=lsi_rank)
        cap_vsm = avprec(r[0], rel_set)
        cap_lsi = avprec(r[1], rel_set)
        if verbose:
            print("%4f %4f %s" % (cap_vsm, cap_lsi, q))
        avprecs_vsm = np.append(avprecs_vsm, cap_vsm)
        avprecs_lsi = np.append(avprecs_lsi, cap_lsi)

    return [avprecs_vsm, avprecs_lsi]

rdd = extract.extract_reldocs_dict(annfile)
