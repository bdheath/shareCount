# sharecount.py
# Thin wrapper for determining social shares for a URL

import urllib2
import multiprocessing
import json
import re
from shareCountSettings import API, APIs

class shareCount:
	
	def __init__(self, multithread = False):
		self._multithread = multithread
		return None
			
	def _collate(self, r):
		if r['loaded']:
			self._totalShares += r['count']
			self._shareData.update({ 'total': self._totalShares})
			self._shareData.update({ r['site'] : r['count'] })
		else:
			self._error('Could not gather data from ' + r['site'])
			
		return

	def _error(self, err):
		print ' ##### shareCount.py ERROR: ' + err + ' ##### '

	def count(self, url):
		self._totalShares = 0
		self._shareData = {}
		if url != '':
			if self._multithread and __name__ == '__main__':
				pool = multiprocessing.Pool(processes=4)
			for curAPI in APIs:
				if self._multithread and __name__ == '__main__':
					pool.apply_async(getShares, (url, curAPI ), callback=self._collate)
				else:
					getShares(url, curAPI, callback=self._collate)
			if self._multithread and __name__ == '__main__':
				pool.close()
				pool.join()
		else:
			self._error('No URL specified')
		return self._shareData

def getShares(url, site, callback = None):
	response = {}
	response['site'] = site
	try:
		dataurl = API[site].base + url
		data = urllib2.urlopen(dataurl).read()
		data = API[site].clean(data)
		js = json.loads(data)
		response['loaded'] = True
		response['count'] = js[API[site].countField]
	except:
		response['loaded'] = False
	if callback != None:
		callback(response)
	return response
	