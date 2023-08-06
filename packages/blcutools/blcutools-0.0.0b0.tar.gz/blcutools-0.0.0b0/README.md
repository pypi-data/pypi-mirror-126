# BLCUtools

BLCUtools

## Python

```python
pip install blcutools
```

分句

```python
from blcutools.nlp.preprocess import SplitSentenceWithPuncs

text = "北京语言大学（Beijing Language and Culture University），简称“北语”，中华人民共和国教育部直属高等学校，入选国家建设高水平大学公派研究生项目、特色重点学科项目、教育部来华留学示范基地、中国政府奖学金来华留学生接收院校，是在周恩来总理的亲自关怀下建立的，创办于1962年，时名为“外国留学生高等预备学校”；1964年6月由国务院批准定名为“北京语言学院”；1974年毛泽东主席为学校题写校名；1996年6月更名为“北京语言文化大学”；2002年校名简化为“北京语言大学”。"
SplitSentenceWithPuncs.split(text)
```