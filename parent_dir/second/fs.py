class FirstClass(object):

	class_data = "this is first class data"

	@property
	def get_context(self, **kwargs):
		data_1 = kwargs.get('data_1',"")
		return data_1 + self.class_data

	def get_qs(self, **kwargs):
		data_2 = kwargs.get("data_2")
		return data_2

	def __unicode__(self):

		return "this is is FirstClass"

class SecondInherit(FirstClass):
	class_data = "this is second class inherited data"

	def __str__(self):

		return "this is an instance of SecondInherit"


if __name__ == '__main__':

	s_obj = SecondInherit()

	print s_obj.get_context(data_1="first python class \n")

	print s_obj.get_qs()