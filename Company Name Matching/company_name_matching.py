import sys
import csv
import numpy
import pandas
import textdistance

sim_list = ["jaccard", "jaro winkler", "hamming", "levenshtein", "ratcliff obershelp"]
# sim_list = ["jaccard"]
sim_threshold = 0.9
sim_diff = 0.1
# table = sorted(table_in, key=lambda t: t[0], reverse=True)


def sim(input_a, input_b, func_v):
    if func_v == "jaccard":
        sim_out = textdistance.jaccard(input_a.lower(), input_b.lower())
    elif func_v == "jaro winkler":
        sim_out = textdistance.jaro_winkler(input_a.lower(), input_b.lower())
    elif func_v == "hamming":
        sim_out = textdistance.hamming.normalized_similarity(
            input_a.lower(), input_b.lower()
        )
    elif func_v == "levenshtein":
        sim_out = textdistance.levenshtein.normalized_similarity(
            input_a.lower(), input_b.lower()
        )
    else:
        sim_out = textdistance.ratcliff_obershelp(input_a.lower(), input_b.lower())

    return sim_out

file = r"comp_list.xlsx"
# icd_full = pandas.read_excel(file, encoding=sys.getfilesystemencoding())
# count_row_i = icd_full.shape[0]
# count_col_i = icd_full.shape[1]
comp_list = numpy.asarray(pandas.read_excel(file, encoding=sys.getfilesystemencoding()))

file = r"check_list.xlsx"
check_list = numpy.asarray(
    pandas.read_excel(file, encoding=sys.getfilesystemencoding())
)

dict_comp = {}
for i in range(len(comp_list)):
    if dict_comp.get(comp_list[i][0]) is not None:
        dict_comp.get(comp_list[i][0]).extend([comp_list[i][1]])
    else:
        dict_comp.update({comp_list[i][0]: [comp_list[i][1]]})

# print(dict_comp)


match_rate = {}
match_list = {}
for i in sim_list:
    match_list.update({i: []})

count_correct = {}
for i in sim_list:
    count_correct.update({i: 0})


divided_by = {}
for i in sim_list:
    divided_by.update({i: 0})


# num_sim = 5
for i in range(len(check_list)):
    for ns in sim_list:
        # match_list.append(sim_list[ns])
        match_list.get(ns).append(
            [check_list[i][0], check_list[i][1], check_list[i][2]]
        )
    if dict_comp.get(check_list[i][0]) is not None:
        # matched_1st = "1st"
        # matched_2nd = "2nd"
        # sim_1st = 0
        # sim_2nd = 0
        if len(dict_comp.get(check_list[i][0])) < 2:
            for ns in sim_list:
                match_list.get(ns)[i].extend(
                    [dict_comp.get(check_list[i][0]), "2nd", "single source"]
                )
        else:
            for ns in sim_list:

                matched_1st = "1st"
                matched_2nd = "2nd"
                sim_1st = 0
                sim_2nd = 0
                for j in dict_comp.get(check_list[i][0]):
                    matched_temp = j
                    sim_temp = sim(j, match_list[ns][i][1], ns)
                    if sim_temp > sim_1st:
                        matched_2nd = matched_1st
                        matched_1st = matched_temp
                        sim_2nd = sim_1st
                        sim_1st = sim_temp
                    elif sim_temp > sim_2nd:
                        matched_2nd = matched_temp
                        sim_2nd = sim_temp
                match_list.get(ns)[i].extend([matched_1st, matched_2nd])
                diff = sim_1st - sim_2nd
                if sim_1st >= sim_threshold:
                    if diff >= sim_diff:
                        if matched_1st == match_list.get(ns)[i][2]:
                            match_list.get(ns)[i].extend(["matched"])
                            add_a = count_correct.get(ns)
                            count_correct.update({ns: add_a + 1})
                            add_b = divided_by.get(ns)
                            divided_by.update({ns: add_b + 1})
                        else:
                            match_list.get(ns)[i].extend(["qualified"])
                            add_b = divided_by.get(ns)
                            divided_by.update({ns: add_b + 1})
                    else:
                        match_list.get(ns)[i].extend(["low diff"])
                        add_b = divided_by.get(ns)
                        divided_by.update({ns: add_b + 1})
                else:
                    match_list.get(ns)[i].extend(["low sim"])
                    add_b = divided_by.get(ns)
                    divided_by.update({ns: add_b + 1})
            # match_rate.update({ns: int(count_correct / divided_by)})
            # if ns == "jaccard":
            #     ns = 1
    else:
        for ns in sim_list:
            match_list.get(ns)[i].extend(["none", "none", "not in dict"])


for ns in sim_list:
    with open("ikea_" + ns + ".csv", "w", encoding="utf-8", newline="") as csvfile:
        csvfile = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        csvfile.writerow(
            ["country", "DWH name", "correct match", "sim 1st", "sim 2nd", "result"]
        )
        for vn in range(len(match_list.get(ns))):
            csvfile.writerow(match_list.get(ns)[vn])


match_rate_list = []

for kk in sim_list:
    match_rate_list.append(count_correct.get(kk) / divided_by.get(kk))

with open("ikea_compare.csv", "w", encoding="utf-8", newline="") as csvfile:
    csvfile = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    csvfile.writerow(sim_list)
    csvfile.writerow(match_rate_list)

print("done")