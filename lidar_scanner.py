import numpy as np


class Range_filter:
	min_range = 0
	max_range = 0
	def __init__(self):
		self.min_range = 0.03
		self.max_range = 50
	
	def update(self,data):
		for i in range(len(data)) :
			if data[i] < self.min_range:
				data[i] = self.min_range
			elif data[i] > self.max_range:
				data[i] = self.max_range
		return data


class Temporal_filter:
	def __init__(self,d):
		self.scan_data = []
		self.d = d + 1 # +1 for current scanned data set.

	def update(self,data):
		self.scan_data.append(data)
		self.scan_data = self.scan_data[-self.d:]
		result_data = np.median(self.scan_data,axis = 0)
		return result_data

#Test Data Set	
a = np.array([[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]])

b = np.array([[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]])

first_filter = Range_filter()
second_filter = Temporal_filter(3)
print("before ")
print(a)
print("After Range Filter")

for i in a :
	x = first_filter.update(i)
	print(x)

print("After Temporal Filter")
for i in b :
	y = second_filter.update(i)
	print(y)

