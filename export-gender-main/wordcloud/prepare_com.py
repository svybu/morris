import pandas as pd
import argparse
import texthero as hero

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

"""****************part for terminal usage****************"""
parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file', type=str, help="path to file")
parser.add_argument('result_file', metavar='result_file', type=str, help="path to file")
args = parser.parse_args()
file = args.file
result_file = args.result_file

"""**************** work with text ****************"""
def comments(file, result_file):
    export_data = pd.read_csv(file, delimiter=";")
    df = pd.DataFrame(export_data)
    df['Comment Text'] = hero.clean(df['Comment Text'])
    df.to_csv(result_file, index=False, sep=';')


if __name__ == "__main__":
    comments(file, result_file)