from lidar_scanner import *
import pytest

def test_range_filter():
	a = np.array([[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]])
	first_filter = Range_filter()
	for i in a :
		x = first_filter.update(i)
	b = [[0.03, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 5, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 0.03], [3.0, 3.0, 3.0, 1.0, 3.0], [5, 2.0, 4.0, 0.03, 0.03]]
	assert first_filter.update(a) == b, "Array did not match. Test failed"

def test_temporal_filter():
	a = np.array([[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]])
	second_filter = Temporal_filter(3)
	for i in b :
		y = second_filter.update(i)
	b = [[0, 1, 2, 1, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0], [1.0, 3.0, 4.0, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 3.0], [3.0, 3.0, 4.0, 1.0, 0.0]]
	assert b == y, "Array did not match. Test failed"
