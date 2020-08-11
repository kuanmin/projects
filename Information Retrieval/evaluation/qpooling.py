import os
import re

from tools import retdoc
HOME = os.getcwd()


queries = ["islamic banks",
           "respect the beliefs of others",
           "povray issues after upgrade",
           "nice pictures for church use",
           "programs for animation and drawing",
           "increase dos window font size",
           "write to 720 floppy disk",
           "create beep without bios",
           "cooling hot cpu using fan",
           "si clock upgrade details cpu speed time",
           "upgrade ram on powerbook 170",
           "speaker audio buzz problem",
           "dynamic window title bar",
           "specify coordinates for window in window manager",
           "compile posix message",
           "program wm window manager properties",
           "robotics modem for sale",
           "microwave convection oven for sale",
           "best cars for driving on autobahn",
           "how to drive clutchless shift",
           "toyota mr2 noisy engine",
           "why manual cars more popular than automatic in europe",
           "why buy a bmw",
           "bike riders mailing list",
           "stupid things baseball players do",
           "boston red sox winning streaks",
           "hockey team records for tie breakers",
           "key size for encryption algorithms",
           "cheap voltage converters",
           "treatment for ovarian cancer",
           "hiv aids trials",
           "inflammatory diseases",
           "mailing lists for different diseases",
           "tests on human and animal blood",
           "side effects of taking vitamins",
           "space travel competitions",
           "funding space travel",
           "gamma ray energy laws",
           "management of nasa",
           "how ancient civilisations lived",
           "arguments about christianity and the church",
           "schools promoting religion",
           "court hearings on gun lobbying",
           "religious crimes",
           "arson or accidental fire",
           "obsessive posting behaviour on internet",
           "fake news posts",
           "lifestyles of happy people",
           "relationships between european countries since world war ii",
           "politician scandals in the us"]

def pool(SearchCore, top, lsi_rank):
    """
    Builds a file for easier relevance judgements.
    
    Parameters
    ----------
    SearchCore : SearchCore object
        'tdmatrix', 'u', 'sigmavt', 'vocabulary'
    queries : list
        list of queries
    out : string/path
        where to write the annotation file
    top: integer
        how many of the top ranked results (by lsi and vsm) should
        be considered
    """
    out_path = os.path.join(HOME, "data/procdata/to_annotate.txt")

    out = open(out_path, 'a')

    for q in queries:

        r = retdoc.retrieve(SearchCore, query=q, top=top, lsi_rank=lsi_rank)
        r_union = list(set(r[0]).union(r[1]))

        for d in r_union:
            with open(d, 'r', encoding='windows-1251') as rawdoc:
                # replace special chars with space
                rd = rawdoc.read()

            rd = re.sub(r'[,"]+', ' ', rd)
            cline = d + "," + q + "," + "\"" + rd + "\"" + "\n"
            out.write(cline)

    out.flush()
    out.close()
