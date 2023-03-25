import wordcloud as w
import matplotlib.pyplot as plt
import argparse
import count_frequencies as c

"""****************part for terminal usage****************"""
parser = argparse.ArgumentParser()
parser.add_argument('export_file', metavar='export_file', type=str, help="path to export_file")
parser.add_argument('filter_file', metavar='filter_file', type=str, help="path to filter_file")
parser.add_argument('number', metavar='number', type=int, help="number of words in wordcloud element")
args = parser.parse_args()
export_file = args.export_file
filter = args.filter_file
number = args.number

"""****************part for generation wordcloud****************"""
def word_cloud(export_file, filter, number):
    r1, r2, r3 = c.count_frequencies(export_file, filter)
    if number == 1:
        result = r1
    elif number == 2:
        result = r2
    else:
        result = r3
    wordcloud = w.WordCloud(collocations=False, background_color="white", width=9000, height=6000,
                            max_words=300).generate_from_frequencies(result)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    word_cloud(export_file, filter, number)
