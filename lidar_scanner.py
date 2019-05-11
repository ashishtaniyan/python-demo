"""
Title: Range filter and Temporal median filter for LIDAR generated scans
Created on May 9th 2019
@author: Ashish Aniyan

"""

import numpy as np


class Range_filter:
#	min_range = 0
#	max_range = 0
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
