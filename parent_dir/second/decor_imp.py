from decor import DecorClass

dec_obj = DecorClass()

@dec_obj.decor_func
def check_func():

	k = [i for i in range(1,100)]

	return k

if __name__ == '__main__':

	print check_func()