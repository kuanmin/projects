########################
# ICD code analysis applying LSI
########################

import collections
import csv
import math
import numpy
import pandas
import re
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load the input file and create some top-level variables
file = r"ICD_10.xlsx"
icd_full = pandas.read_excel(file, encoding=sys.getfilesystemencoding())
count_row_i = icd_full.shape[0]
count_col_i = icd_full.shape[1]
icd_full_arr = numpy.empty((count_row_i, count_col_i), np.byte)

## Why do you rename icd_full_arr to icd_full_arr_o??
icd_full_arr_o = icd_full_arr

char = {}
char_list = []
menu = {}

########################
# Part A
########################
# read in the ICD 10 code
# remove the stop words
# lemmatize words
# remove tokens with lenght less than (or equal) 2
# (assume these tokens provide not enough informations)
########################

# We want to scan the whole array based on the first column
# to see if we can group descriptions based on the "detailness"
# of the ICD code. This means, that we can group descriptions of
# "child" codes into "parent" codes. Codes are stripped of the
# last
#
# Example:
# A0221                Salmonella meningitis
# A0222                Salmonella pneumonia
# A0223                Salmonella arthritis
# A0224                Salmonella osteomyelitis
# A0225                Salmonella pyelonephritis
# A0229                Salmonella with other localized infection
#
# Would become:
# A02 Salmonella meningitis pneumonia arthritis osteomyelitis pyelonephritis (lemmatized)

# This are middlestep variables
mid_code = icd_full_arr[0][0]
mid_desc_pre_0 = icd_full_arr[0][1]
mid_desc_pre_1 = re.sub(r"[^\w]", " ", mid_desc_pre_0)
mid_desc_pre_2 = re.sub(r"[0-9]+", "", mid_desc_pre_1)
mid_desc_pre_3 = mid_desc_pre_2.replace("  ", " ", 5)
mid_desc_pre_4 = mid_desc_pre_3.lower()
mid_desc_pre_5 = mid_desc_pre_4.strip()
mid_desc_pre_6 = mid_desc_pre_5.split()
mid_desc_pre_7 = []

# Loop on the cleaned words from the description, remove stop words,
# lemmatize them and store them in the mid_desc_pre_7 list
for w1 in mid_desc_pre_6:
    if w1 not in stop_words:
        temp_word = lemmatizer.lemmatize(w1)
        if len(temp_word) > 2:
            if temp_word not in stop_words:
                mid_desc_pre_7.append(temp_word)

s = " "

## Why to variables with the same data?
mid_desc = s.join(mid_desc_pre_7)
mid_desc_text = s.join(mid_desc_pre_7)
menu_text = [mid_desc]

# Iterate the whole array, row by row
# We have a temporary variable holding the initial
# code and description values mid_code, mid_desc
#
# Iterate every row;
# If the row code is equal to the mid_code; then
#             add the description of the row to mid_desc
# if the code is different then store the code along
# with the joined descriptions into the other array
# icd_full_arr_o

row_n = 0
for i in range(1, count_row_i):
                # Check if it is the same code as the previous row.
                if icd_full_arr[i][0] != mid_code:
                                icd_full_arr_o[row_n][0] = mid_code
                                icd_full_arr_o[row_n][1] = mid_desc
                                menu_text.append(mid_desc_text)
                                mid_code = icd_full_arr[i + 1][0]
                                mid_desc_pre_0 = icd_full_arr[i + 1][1]
                                mid_desc_pre_1 = re.sub(r"[^\w]", " ", mid_desc_pre_0)
                                mid_desc_pre_2 = re.sub(r"[0-9]+", "", mid_desc_pre_1)
                                mid_desc_pre_3 = mid_desc_pre_2.replace("  ", " ", 5)
                                mid_desc_pre_4 = mid_desc_pre_3.lower()
                                mid_desc_pre_5 = mid_desc_pre_4.strip()
                                mid_desc_pre_6 = mid_desc_pre_5.split()
                                mid_desc_pre_7 = []
                                for w2 in mid_desc_pre_6:
                                                if w2 not in stop_words:
                                                                temp_word = lemmatizer.lemmatize(w2)
                                                                if len(temp_word) > 2:
                                                                                if temp_word not in stop_words:
                                                                                                mid_desc_pre_7.append(temp_word)
                                s = " "
                                mid_desc = s.join(mid_desc_pre_7)
                                row_n += 1

                else:
                                mid_desc_pre_0 = icd_full_arr[i][1]
                                mid_desc_pre_1 = re.sub(r"[^\w]", " ", mid_desc_pre_0)
                                mid_desc_pre_2 = re.sub(r"[0-9]+", "", mid_desc_pre_1)
                                mid_desc_pre_3 = mid_desc_pre_2.replace("  ", " ", 5)
                                mid_desc_pre_4 = mid_desc_pre_3.lower()
                                mid_desc_pre_5 = mid_desc_pre_4.strip()
                                mid_desc_pre_6 = mid_desc_pre_5.split()
                                mid_desc_pre_7 = []
                                for w1 in mid_desc_pre_6:
                                                if w1 not in stop_words:
                                                                temp_word = lemmatizer.lemmatize(w1)
                                                                if len(temp_word) > 2:
                                                                                if temp_word not in stop_words:
                                                                                                mid_desc_pre_7.append(temp_word)

                                s = " "
                                mid_desc += " " + s.join(mid_desc_pre_7)
                                mid_desc_text += "; " + s.join(mid_desc_pre_7)

                                if i == count_row_i - 1:
                                                icd_full_arr_o[row_n][0] = mid_code
                                                icd_full_arr_o[row_n][1] = mid_desc
                                                menu_text.append(mid_desc_text)
                                               
# ALLES SEHR GUT

########################
# Part B - apply simplified LSI
# ( here index the token and present the documents in vectors)
########################
# build dictionary for ICD 10 as "MENU"
# ex. menu = { 1 : {'code':'A06', 'text': 'Spontaneous bacterial peritonitis',
#                   'word': ['Spontaneous', 'bacterial', 'peritonitis'],
#                   'word_c': {'Spontaneous': 1, 'bacterial': 1, 'peritonitis': 1},
#                   'length': 3},
#              2 : {'code':'H58', 'text': 'Other specified disorders of peritoneum',
#                   'word': ['Other', 'specified', 'disorders', 'peritoneum'],
#                   'word_c': {'Other': 1, 'specified': 1, 'disorders': 1, 'peritoneum': 1},
#                   'length': 4},
#              ...,
#              ...}
#
# build dictionary for words
# ex. char = { 'Spontaneous': {'doc_fq': 78, 'ind': [1,25,179]},
#              'peritoneum': {'doc_fq': 14, 'ind': [50,52,88,310]},
#              ...,
#              ...}
#
# build character list where collects all the words
# ex. char_list = [ 'Spontaneous', 'bacterial', 'peritonitis', 'Other', 'specified', ...]
#
########################

char_list = []
char = {}
menu = {}

# Prepare a list with the word of the diagnosis description
mid_split = icd_full_arr_o[0][1].split()

# Fancy python. Create an empty dictionary using the mid_split words as keys.
# Note: could be changed to set
mid_word = list(dict.fromkeys(mid_split))

# Then we have create a dictionary with the frequencies of each word.
# Warning: Pablo may have broken this because he removed the outer dictionary transformation
mid_collect = collections.Counter(mid_split)

# Build the dictionary for words. "ind" means index here.
for w in mid_word:
    if w in char_list:
        char[w]["doc_fq"] = char[w]["doc_fq"] + 1
        char[w]["ind"].append(0)
    else:
        char.update({w: {"doc_fq": 1, "ind": [0]}})

menu_words = icd_full_arr_o[0][1].split()
menu.update(
    {
        0: {
            "code": icd_full_arr_o[0][0],
            "text": menu_text[0],
            "word": mid_word,
            "word_c": mid_collect,
            "len": len(menu_words),
        }
    }
)

menu_list = [icd_full_arr_o[0][0]]
char_list += mid_word

# Here row_n is the size of the array icd_full_arr_o in its Y axis
for code_num in range(row_n + 1):
    if code_num > 0:

        mid_split = icd_full_arr_o[code_num][1].split()

        mid_word = list(dict.fromkeys(mid_split))
        mid_collect = dict(collections.Counter(mid_split))
                               
                                # Append the diagnosis code to menu list
        menu_list.append(icd_full_arr_o[code_num][0])

        for w in mid_word:
            if w in char_list:
                char[w]["doc_fq"] = char[w]["doc_fq"] + 1
                char[w]["ind"].append(code_num)
            else:
                char.update({w: {"doc_fq": 1, "ind": [code_num]}})

        menu_words = icd_full_arr_o[code_num][1].split()
        menu.update(
            {
                code_num: {
                    "code": icd_full_arr_o[code_num][0],
                    "text": menu_text[code_num],
                    "word": mid_word,
                    "word_c": mid_collect,
                    "len": len(menu_words),
                }
            }
        )
        char_list = char_list + mid_word
        char_list = list(dict.fromkeys(char_list))

########################
# Part C
########################
# read in the train data
# for each iteration:
# 1. read in new row and build a dictionary for items
#    ex. query = {'code':'A06', 'text': 'Spontaneous bacterial peritonitis',
#                'word': ['Spontaneous', 'bacterial', 'peritonitis'],
#                'word_c': {'Spontaneous': 1, 'bacterial': 1, 'peritonitis': 1},
#                'length': 3}
# 2. calculate TF-IDF vector of the query.
# 3. calcualte TF-IDF vectors for each ICD code where includes the token (word) from the query.
# 4. calcualte cosine between the query and each document.
# 5. rank.
########################

file = r"test_SVD.xlsx"
array_svd_ori = pandas.read_excel(file, encoding=sys.getfilesystemencoding())
count_row_svd = array_svd_ori.shape[0]
count_col_svd = array_svd_ori.shape[1]
array_svd = numpy.asarray(array_svd_ori)
svd_output = []

for b in range(count_row_svd):

    query_ori = array_svd[b][2]

    mid_code = query_ori
    mid_desc_pre_0 = mid_code
    mid_desc_pre_1 = re.sub(r"[^\w]", " ", mid_desc_pre_0)
    mid_desc_pre_2 = re.sub(r"[0-9]+", "", mid_desc_pre_1)
   mid_desc_pre_3 = mid_desc_pre_2.replace("  ", " ", 5)
    mid_desc_pre_4 = mid_desc_pre_3.lower()
    mid_desc_pre_5 = mid_desc_pre_4.strip()
    mid_desc_pre_6 = mid_desc_pre_5.split()
    mid_desc_pre_7 = []
    for w1 in mid_desc_pre_6:
        if w1 not in stop_words:
            temp_word = lemmatizer.lemmatize(w1)
            if len(temp_word) > 2:
                if temp_word not in stop_words:
                    mid_desc_pre_7.append(temp_word)

    s = " "
                # The following might be able to be ommited
    query_desc_pri = s.join(mid_desc_pre_7)
    query_split_pri = query_desc_pri.split()
    query_word_pri = list(dict.fromkeys(query_split_pri))
    query_collect_pri = dict(collections.Counter(query_split_pri))

                # Build the query
                # If the word is not in the char_list it is not the descriptions
                # so there's no point in using it.
    query_word = []
    for w in query_word_pri:
        if w in char_list:
            query_word.append(w)

    if len(query_word) < 1:

                                # Why is this needed here?
        svd_output.append(
            (
                array_svd[i][0],
                array_svd[i][1],
                array_svd[i][2],
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            )
        )

    else:
        top = 10
        s = " "
                                # The following line can be omitted?
        query_desc = s.join(query_word)
        query_split = query_desc.split()
        query_word = list(dict.fromkeys(query_split))
        query_collect = dict(collections.Counter(query_split))

        query_words = query_desc.split()
        query = {
            "text": query_desc,
            "word": query_word,
            "word_c": query_collect,
            "len": len(query_words),
        }

        vec = []

        for i in range(query["len"]):
            value_in_2 = (
                query["word_c"][query["word"][i]]
                                                                # This is the TF-IDF formula
                * numpy.log(
                    float(len(char_list) + 1) / (char[query["word"][i]]["doc_fq"] + 1)
                )
                / float(query["len"])
            )
            vec.append(value_in_2)

        menu_look = []
        for i in query_word:
            menu_look += char[i]["ind"]

                                # Get the unique indexes
        menu_look_cl = list(dict.fromkeys(menu_look))

                                # What are this 'tag' variables?
        code_tag = []
        desc_tag = []
        cal = []
        for i in menu_look_cl:
            code_tag.append(menu[i]["code"])
            desc_tag.append(menu[i]["text"])
            temp_in = []
            for j in range(query["len"]):
                if i in char[query["word"][j]]["ind"]:
                    value_in_1 = (
                        menu[i]["word_c"][query["word"][j]]
                        * numpy.log(
                            (float(len(char_list) + 1))
                            / (char[query["word"][j]]["doc_fq"] + 1)
                        )
                        / float(menu[i]["len"])
                    )
                    temp_in.append(value_in_1)
                else:
                    temp_in.append(0)
            cal.append(temp_in)

        results = []
        for i in range(len(menu_look_cl)):
            vec1 = numpy.array([vec])
            vec2 = numpy.array([cal[i]])
            cos = cosine_similarity(vec1, vec2)
            results.append((cos, code_tag[i]))

        output = sorted(results, key=lambda t: t[0], reverse=True)

        sim_code = []

        if len(menu_look_cl) > (top - 1):
            for i in range(top):
                sim_code.append(output[i][1])
                sim_code.append(output[i][0][0][0])
        else:
            for i in range(len(menu_look_cl)):
                sim_code.append(output[i][1])
                sim_code.append(output[i][0][0][0])
            for i in range(top - len(menu_look_cl)):
                sim_code.append("")
                sim_code.append("")

        svd_output.append(
            (
                array_svd[b][0],
                array_svd[b][1],
                array_svd[b][2],
                sim_code[0],
                sim_code[1],
                sim_code[2],
                sim_code[3],
                sim_code[4],
                sim_code[5],
                sim_code[6],
                sim_code[7],
                sim_code[8],
                sim_code[9],
                sim_code[10],
                sim_code[11],
                sim_code[12],
                sim_code[13],
                sim_code[14],
                sim_code[15],
                sim_code[16],
                sim_code[17],
                sim_code[18],
                sim_code[19],
            )
        )

with open("test_svd_out.csv", "w", encoding="utf-8", newline="") as csvfile:
    csvfile = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    for vn in range(count_row_svd):
        csvfile.writerow(
            [
                svd_output[vn][0],
                svd_output[vn][1],
                svd_output[vn][2],
                svd_output[vn][3],
                svd_output[vn][4],
                svd_output[vn][5],
                svd_output[vn][6],
                svd_output[vn][7],
                svd_output[vn][8],
                svd_output[vn][9],
                svd_output[vn][10],
                svd_output[vn][11],
                svd_output[vn][12],
                svd_output[vn][13],
                svd_output[vn][14],
                svd_output[vn][15],
                svd_output[vn][16],
                svd_output[vn][17],
                svd_output[vn][18],
                svd_output[vn][19],
                svd_output[vn][20],
                svd_output[vn][21],
                svd_output[vn][22],
            ]
        )
