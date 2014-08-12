shareCount
==========

A Python class for counting social shares of a given URL. shareCount gathers total social counts for any URL. It supports optional multithreading for speed.

shareCount currently gathers shares from Facebook, Twitter, LinkedIn and Pintrest. Others to come soon. 

usage
=====

For a working demo, see '''demo.py'''

```
import shareCount

url = 'http://www.usatoday.com/story/news/nation/2014/07/20/atf-stash-house-stings-racial-profiling/12800195/'

counter = shareCount.shareCount()

data = counter.count(url)
print data['total']
