from sys import argv
from determinate_gender import get_gender


if __name__ == "__main__":
    try:
        path_to_original = argv[1]
        path_to_result = argv[2]
        get_gender(path_to_original, path_to_result)
    except:
        print('Seems, there is no right path to original or result .csv files')