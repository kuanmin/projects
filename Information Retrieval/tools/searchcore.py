import math
import pickle
import os
import numpy as np
import re

from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds

from tools import vecdoc
from tools import misc

HOME = os.getcwd()

search_core_path = os.path.join(HOME, "data/procdata/SearchCore.pkl")
isbuilt = os.path.exists(search_core_path)
abs_docpaths = misc.get_docpaths()


class SearchCore:
    """
    Parameters
    ----------
    docpaths : list
        list of absolute paths to all files from the collection
    log_weight : boolean
        whether or not the raw frequencies should be log weighted
    min_freq: integer
        minimum document frequency

    Returns
    -------
    LSICore
    
    """
    def __init__(self, abs_docpaths, log_weight, min_freq, k):

        self.abs_docpaths = abs_docpaths
        self.docs = [misc.get_fname(i) for i in abs_docpaths]
        self.log_weight = log_weight
        self.min_freq = min_freq
        self.N = len(abs_docpaths)
        self.svdk = k

        self.vecdoc_list = []
        self.vocabulary_full = {}
        self.vocabulary = {}
        self.tdmatrix = None
        self.svd = None

        self.build_vecdoc_list()
        self.build_vocabulary()
        self.build_tdmatrix()

    def build_vecdoc_list(self):
        for dp in self.abs_docpaths:
            self.vecdoc_list.append(vecdoc.VecDoc(dp, self.log_weight))
        print("vecdoc_list_ready")


    # get 'tdm_row_index', 'idf' and 'doc_indices' which for each term:
    # ['tdm_row_index, 'idf', [doc_indices]]
    def build_vocabulary(self):
        counter = 0
        for docindex, vdoc in enumerate(self.vecdoc_list):
            for term in vdoc.term_weight.keys():
                if term not in self.vocabulary_full:
                    self.vocabulary_full[term] = [counter, 1, [docindex]]
                    counter += 1
                else:
                    # if the current term is in 'vocabulary_full', increment
                    # and append the additional doc_index
                    self.vocabulary_full[term][1] += 1
                    self.vocabulary_full[term][2].append(docindex)
        # filter the term with document frequency less than 'min_freq'
        self.vocabulary = {k: v for k, v in self.vocabulary_full.items() 
                                 if v[1] > self.min_freq}

        # create new indices for the terms to remove "holes" caused by the
        # filtering
        i = 0
        for k, v in self.vocabulary.items():
            v[0] = i
            i += 1

        # convert the document frequencies to inverse document frequencies
        # the raw frequencies are still available ('len(vocabulary[2])'')
        for term, v in self.vocabulary.items():
            self.vocabulary[term][1] = math.log10(self.N / v[1])

        print("vocabulary ready")

    # build the term-document matrix, it is quite sparse so it has
    # to be stored as sparse.csr_matrix
    def build_tdmatrix(self):

        i = []
        j = []
        v = []

        if len(self.vocabulary_full) < 1:
            raise Exception("build the full vocabulary first")
        
        # loop through the list of VecDocs and through their term_weight
        # dicts to build the sparse term-document matrix
        for docindex, vdoc in enumerate(self.vecdoc_list):
            for term, weight in vdoc.term_weight.items():

                # skip the terms which were filtered
                if term not in self.vocabulary:
                    continue

                # Add the current i (the row index for the current term)
                i.append(self.vocabulary[term][0])

                # Add the current j (the column index for the current term)
                j.append(docindex)
                
                # Add the current value ()
                cv = weight * self.vocabulary[term][1]
                v.append(cv)

        self.tdmatrix = csr_matrix((v, (i, j)))

        self.tdmatrix_col_norms = np.squeeze(np.asarray(
                                  self.tdmatrix.power(2).sum(axis=0)))
        self.tdmatrix_col_norms = np.sqrt(self.tdmatrix_col_norms)
        print("term-document matrix ready")

        self.svd = svds(self.tdmatrix, k=self.svdk)
        self.u   = self.svd[0]
        self.sigmavt           = np.dot(np.diag(self.svd[1]), self.svd[2])
        self.sigmavt_col_norms = np.sqrt(np.sum(self.sigmavt ** 2, 0))
        print("svd ready")

    def export(self):
        # do not export the vecdoc_list, only wastes memory
        self.vecdoc_list = None
        self.svd = None
        if not os.path.exists(os.path.join(HOME, "data/procdata/")):
            os.makedirs(search_core_path)
        with open(search_core_path, 'wb') as out:
            pickle.dump(self, out, pickle.HIGHEST_PROTOCOL)

    def summary(self):
        print("vocabulary_full: ", len(self.vocabulary_full))
        print("vocabulary: ", len(self.vocabulary))
        print("docs: ", self.N)
        print("dimensions term-document matrix: ", self.tdmatrix.shape)
        print("entries: ", self.tdmatrix.nnz)
        print()


def getcore():
    if isbuilt:
        with open(search_core_path, 'rb') as infile:
            sc = pickle.load(infile)
        print("\nSearchCore object found at '" + search_core_path + "'\n\nProperites:")
        sc.summary()
    else:
        print("No SearchCore object found, set parameters for new one\n")
        while True:
            k = input("SVD rank (high k can be slow): ")
            if misc.is_int(k) and int(k) > 0:
                k = int(k)
                break
        while True:
            min_freq = input("Minimum document frequency for the vocabulary: ")
            if misc.is_int(min_freq):
                min_freq = int(min_freq)
                break
        while True:
            log_weight = input("Should raw frequencies be log weighted? (y / n): ")
            if log_weight in {"y", "n", "Y", "N"}:
                break

        sc = SearchCore(abs_docpaths, log_weight=log_weight, min_freq=min_freq, k=k)
        sc.export()

    return sc
