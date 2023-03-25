import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

#path_to_result = '2_result.csv'


def apple_pie(file):
    df = pd.DataFrame(pd.read_table(file, delimiter=";"))  # open  file and create dataframe
    gender = df['gender'].value_counts()  # count gender values
    gender.plot.pie(autopct='%.2f')  # create  pie chart with % inside
    plt.show()  # create new window with  pie chart


if __name__ == "__main__":
    try:
        path_to_original = argv[1]
        apple_pie(path_to_original)
    except:
        print('Seems, there is no right path to original file')
