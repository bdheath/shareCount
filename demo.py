import shareCount

url = 'http://www.usatoday.com/story/news/nation/2014/07/20/atf-stash-house-stings-racial-profiling/12800195/'

counter = shareCount.shareCount()
d = counter.count(url)
print d['total']