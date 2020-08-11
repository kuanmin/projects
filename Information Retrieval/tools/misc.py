import os
import glob
HOME = os.getcwd()

def get_docpaths():
    """
    Filters out the directories returned by 'glob'.
    
    Parameters
    ----------
    col_path : path to the collection ('~/data/rawdata/20news-18828/')
        absolute path to the '20news-18828' folder
    
    Returns
        list of absolute file paths to the documents
    """
    col_path = os.path.join(HOME, "data/rawdata/20news-18828/**/*")

    file_paths = glob.glob(col_path, recursive=True)
    return [i for i in file_paths if os.path.isfile(i)]

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_fname(path):
    split = path.split(os.sep)
    return split[-2] + os.sep + split[-1]
