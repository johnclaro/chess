import collections

from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster('local').setAppName('RatingsHistogram')
sc = SparkContext(conf=conf)

lines = sc.textFile('fk/datasets/ratings/u.data')
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

results = collections.OrderedDict(sorted(result.items()))
for key, value in results.items():
    print(f'{key} {value}')