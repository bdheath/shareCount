import re

class APISetting:

	def __init__(self, base = '', name = '', countField = '', helperRegexp = None,
				helperRegexpReplace = ''):
		self.base = base
		self.name = name
		self.countField = countField
		self.helperRegexp = helperRegexp
		self.helperRegexpReplace = helperRegexpReplace
		return
		
	def clean(self, d):
		if self.helperRegexp != None:
			d = re.sub(self.helperRegexp, self.helperRegexpReplace, d)
		return d

API = {}

API['Twitter'] = APISetting( base = 'http://cdn.api.twitter.com/1/urls/count.json?url=',
									name = 'Twitter',
									countField = 'count' )
API['Facebook'] = APISetting ( base = 'http://graph.facebook.com/?id=',
									name = 'Facebook',
									countField = 'shares' )
API['Pintrest'] = APISetting ( base = 'http://api.pinterest.com/v1/urls/count.json?url=',
									name = 'Pintrest',
									countField = 'count',
									helperRegexp = 'receiveCount\((.*)\)',
									helperRegexpReplace = '\g<1>'
									)
API['LinkedIn'] = APISetting ( base = 'http://www.linkedin.com/countserv/count/share?url=',
									name = 'LinkedIn',
									countField = 'count',
									helperRegexp = 'IN\.Tags\.Share\.handleCount\((.*)\);',
									helperRegexpReplace = '\g<1>'
									)
APIs = [ 'Twitter', 'Facebook', 'Pintrest', 'LinkedIn' ]

