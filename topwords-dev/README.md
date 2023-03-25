# topwords

Python library to extract the most common word combinations from a text.

## Usage

```python
>> > import topwords_main
>> > text = "aaa aaa aaa bbb bbb ccc"

>> > topwords.count(text, combine=1)
{'aaa': 3, 'bbb': 2, 'ccc': 1}

>> > topwords.count(text, combine=1, threshold=2)
{'aaa': 3, 'bbb': 2}

>> > topwords.count(text, combine=2)
{'aaa aaa': 2, 'bbb bbb': 1}

>> > topwords.count(text, combine=3)
{'aaa aaa aaa': 1}
```
