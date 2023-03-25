from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# nltk.download('punkt')


def count(text, combine=1, threshold=None):
    stop_words = stopwords.words('english')
    freq_list = []

    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]  # remove numbers and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words]
    words = [word for word in words if word not in stop_words]  # remove stopwords
    if combine == 1:
        freq_count = Counter(words)
        # return freq_count
    elif combine == 2:
        for index, word in enumerate(words):
            if index + 1 <= len(words) - 1:
                temp_v = words[index] + ' ' + words[index + 1]
                freq_list.append(temp_v)
                freq_count = Counter(freq_list)
        # return freq_count
    elif combine == 3:
        for index, word in enumerate(words):
            if 0 <= index - 1 and index + 1 <= len(words) - 1:
                temp_v = words[index - 1] + ' ' + words[index] + ' ' + words[index + 1]
                freq_list.append(temp_v)
                freq_count = Counter(freq_list)
    freq_count = dict(freq_count)
    if threshold:
        freq_count = {k: v for k, v in freq_count.items() if v > threshold}
    # print(freq_count)
    return freq_count


if __name__ == "__main__":
    text = "aaa aaa aaa bbb bbb ccc"
    # print(count(text, 3))
    # print(count(text, 2))
    # print(count(text, combine=1, threshold=2))
    print(count(text, combine=1, threshold=2))
    # print(count(text, combine=3))
