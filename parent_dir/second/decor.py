
class DecorClass(object):


	def decor_func(self, func):
		def inner_wrap():
			import time
			t1 = time.time()
			print func()
			t2 = time.time()
			ttl = t2- t1

			return ttl
		return inner_wrap