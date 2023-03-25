import pandas as pd
import matplotlib.pyplot as plt
import argparse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

"""****************part for terminal usage****************"""
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file', type=str, help="path to file")
parser.add_argument('-c', '--chart', action='store_const', const=True, help='create chart')
args = parser.parse_args()
file = args.file
chart = args.chart

"""****************count comments****************"""
def count_com(file):
    export_data = pd.read_csv(file, delimiter=";")
    df = pd.DataFrame(export_data)
    count = df['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='counts')
    print(count)
    return count

"""****************create chart****************"""
def barh_chart(count):
    df2 = count[:50].copy().sort_values(by='counts', ascending=True)#top 50
    others = pd.DataFrame(data={'Page Name': ['Others'], 'counts': [count['counts'][50:].sum()]})#sum for others
    df2 = pd.concat([df2, others]).sort_values(by='counts', ascending=True)
    df2.plot.barh(x='Page Name', subplots=True)
    plt.show()


if __name__ == "__main__":
    count_com(file)
    if args.chart==True:
        barh_chart(count_com(file))


