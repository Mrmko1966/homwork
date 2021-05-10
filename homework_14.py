# 1. Write a Python class which should contain
# a constructor to create a dictionary from a string.
#  Sample string : ‘python’
#  Expected output: {‘p’: 1, ‘y’: 1, ‘t’: 2, ‘h’: 1, ‘o’: 1, ‘n’:1}
#  a method which returns a version of the dictionary without duplicate values.
#  a method which returns the highest 3 values in a dictionary
# a method which presents the dictionary
#from collections import defaultdict, Counter
# class Dict_from_string:
# 	def __init__(self, name):
		
# 		self.name = name
# 		print(self.name)
# 	# def hh(self):

# 	# 	my_dict = {}	
# 	# 	for key in self.name:
# 	# 		my_dict[key] = my_dict.get(key, 0) + 1
# 	# def my_dict_duplicate_values():


# 	# 	return my_dict
# 	# def my_dict_highest_3_values():
# 	# 	pass
# 	# 	return
# print(Dict_from_string("Pythons"))
import random
class Str_dict:
	"""docstring for Str_dict"""
	def __init__(self, name):
		self.my_dict = {}
		for key in name:
			self.my_dict[key] = random.randint(1,4)
	def my_dict_duplicate(self):
		print(self.my_dict)
		self.temp = []
		self.res =dict()
		for i,k in self.my_dict.items():
			if k not in self.temp:
				self.temp.append(k)
				self.res[i] = k 
		return self.res
	def my_dict_3_max(self):
		key = sorted(self.my_dict, key=self.my_dict.get, reverse=True)[:3]
		return key
	def my_dict_print(self):
		my_dict_print = self.my_dict
		return my_dict_print
dict_ = Str_dict("Python")
print(dict_.__dict__)
print(Str_dict.my_dict_duplicate(dict_))			
print(Str_dict.my_dict_3_max(dict_))
print(Str_dict.my_dict_print(dict_))

# 2 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
# class Circle:
# 	"""docstring for ClassName"""
	
# 	def __init__(self, radius):
# 		self.r1 = radius
# 		self.pi = 3.14
# 	def perimeter_calc(self):
# 		perimeter = 2 * self.pi * self.r1
		
# 		return F"This is your circle perimeter {perimeter}"
# 	def area_calc(self):
# 		area = self.pi * (self.r1 ** 2) 
		
# 		return F"This is your circle area {area}"

# circle_ = Circle(5)

# print(Circle.perimeter_calc(circle_))
# print(Circle.area_calc(circle_))
		