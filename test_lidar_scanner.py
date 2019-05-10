"""
Title: Pytest baed test cases to verify Range filter and Temporal median filter
Created on May 9th 2019
@author: Ashish Aniyan

"""

from lidar_scanner import *
import pytest

def test_range_filter():
	a = [0., 1., 2., 1., 3.]
	first_filter = Range_filter()
		#x = first_filter.update(a)
	processed_data = first_filter.update(a)
	b = [0.03, 1.0, 2.0, 1.0, 3.0]
	assert  processed_data == b, "Array did not match. "

def test_range_filter_max():
	a = [51, 1., 2., 1., 3.]
	first_filter = Range_filter()
		#x = first_filter.update(a)
	processed_data = first_filter.update(a)
	b = [50, 1.0, 2.0, 1.0, 3.0]
	assert  processed_data == b, "Array did not match. "

def test_range_filter_supermax():
	a = [51, 1., 2., 1., 3.,3000,9999]
	first_filter = Range_filter()
		#x = first_filter.update(a)
	processed_data = first_filter.update(a)
	b = [50, 1.0, 2.0, 1.0, 3.0, 50, 50]
	assert  processed_data == b, "Array did not match. "

def test_temporal_filter_positive():
	a = [0., 1., 2., 1., 3.]
	second_filter = Temporal_filter(3)
	processed_data = second_filter.update(a)
	b = [0., 1., 2., 1., 3.]
	print(processed_data)
	assert np.all(processed_data == b), "Array did not match."

def test_temporal_filter_negetive():
	a = [0., 1., 2., 1., 3.]
	second_filter = Temporal_filter(3)
	processed_data = second_filter.update(a)
	b = [0., 1., 2., 1., 3.5]
	print(processed_data)
	assert not np.all(processed_data == b), "Array did not match."

def show_result():
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