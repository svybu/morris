import pandas as pd
import texthero as hero
from collections import Counter

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_rows', None)


"""**************** work with text ****************"""


def count_frequencies(export_file, filter):
    # prepare comments
    export_data = pd.read_excel(export_file)  # """, delimiter=';', encoding='ANSI'""")
    df = pd.DataFrame(export_data)
    df['Comment Text'] = hero.clean(df['Comment Text'])
    comment = df['Comment Text']
    comments_list = []
    list_1 = []
    list_2 = []
    list_3 = []
    # total_list = []
    ar = []  # array for words from filter
    comment = comment.tolist()
    for i in comment:
        comments_list.append(i.split())
    comments_list = [item for sublist in comments_list for item in sublist]
    # prepare filter
    with open(filter) as filt:
        for item in filt:
            n = item.lower().split('\n')[0]
            if n != '':
                ar.append(n)
        # create list with one, two and three-word elements
        for index, word in enumerate(comments_list):
            if word in ar:
                temp_v = comments_list[index]
                list_1.append(temp_v)
                if index == 0:
                    temp_v = comments_list[index] + ' ' + comments_list[index + 1]
                    list_2.append(temp_v)
                elif index == len(comments_list) - 1:
                    temp_v = comments_list[index - 1] + ' ' + comments_list[index]
                    list_2.append(temp_v)
                else:
                    temp_v = comments_list[index] + ' ' + comments_list[index + 1]
                    list_2.append(temp_v)
                    temp_v = comments_list[index - 1] + ' ' + comments_list[index]
                    list_2.append(temp_v)
                    temp_v = comments_list[index - 1] + ' ' + comments_list[index] + ' ' + comments_list[index + 1]
                    list_3.append(temp_v)

    return dict(Counter(list_1)), dict(Counter(list_2)), dict(Counter(list_3))


if __name__ == '__main__':
    count_frequencies('china.csv', 'filter_EN.txt')
