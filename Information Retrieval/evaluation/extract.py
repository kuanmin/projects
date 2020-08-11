import re
import os

def extract_reldocs_dict(path):
    """
    Builds a dictionary with relevant docs per query:
    {query: {doc1, doc2, ..., docX}}
    
    Parameters
    ----------
    path: path to the csv file with relevance judgements
    """
    rdd = {}
    with open(path, 'r', encoding='utf-8') as rawdoc:
        for line in rawdoc:
            fqr = line.split(",")

            if os.sep != "/":
                fqr[0] = re.sub(r'/', r'\\', fqr[0])

            if fqr[2] == "1\n":
                if fqr[1] not in rdd:
                    rdd[fqr[1]] = {fqr[0]}
                else:
                    rdd[fqr[1]].add(fqr[0])
    return rdd
