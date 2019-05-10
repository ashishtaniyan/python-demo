# python-demo
Used for Python demo programs

Problem Statement

You have been assigned to write filters to reduce noise in the data coming from a LIDAR sensor attached to your robot. The LIDAR generates scans at a certain rate. Each scan is an array of length N of lloat values representing distance measurements. Nis typically in a range of ~[2Dl]. 1000] measurements, and it is ﬁxed. Measured distances are typically in a range of [0.03, 5D] meters. Each time a scan is received. it will be passed on to the filters. Each ﬁlter object should have an update method, that takes a length-N array of ranges and retums a ﬁltered length-N array ot ranges.

We want you to write two different ﬁlter objects: a A range ﬁlter

The range filter crops all the values that are below range_min (resp. above range_max), and replaces them with the range_min value (resp. range_max)

. A temporal median ﬁlter The temporal median ﬁlter returns the median of the current and the previous D scans: }' Em =median(x.(r), 116— 1), . xfcx — DJ) where x and y are input and output length—N scans and i ranges from D to N—1. The number of previous scans D is a parameter that should be given when creating a new temporal median ﬁlter. Note that, although the update method will receive a single scan, the retumed arrayr depends on the values of previous scans. Note also that the for the first D scans, the ﬁlter is expected to

return the median of all the scans so far.


###Usage Instructions

Files :
1) lidar_scanner.py  // This file contains the application logic for 2 filters (Range_filter & Temporal_filter)
2) test_lidar_scanner.py // This file contains the test in pytest to verify the positive and negetive scenarios.

##Execute Test
PREREQUISITE:
1) python 2.7 or higher
2) pip libraries (numpy,pytest)

EXECUTE:
1) Unzip lidar_project.zip
2) Navigate to libdar_project.
		>cd libdar_project/
3) Execute test_lidar_scanner.py using pytest
		>pytest test_lidar_scanner.py

##Additional Notes
test_lidar_scanner.py is also provided with show_result() methood.
This method has a test data set and hooks to call the ldar_scanner filter objects.

Here is the Result show_result() method using followign test data set.

TEST DATA SET
Set 1 :: [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
				[10., 2., 4., 0., 0.]])

RESULTS
before 
[[ 0.  1.  2.  1.  3.]
 [ 1.  5.  7.  1.  3.]
 [ 2.  3.  4.  1.  0.]
 [ 3.  3.  3.  1.  3.]
 [10.  2.  4.  0.  0.]]
After Range Filter
[0.03 1.   2.   1.   3.  ]
[1. 5. 7. 1. 3.]
[2.   3.   4.   1.   0.03]
[3. 3. 3. 1. 3.]
[10.    2.    4.    0.03  0.03]
After Temporal Filter
[0. 1. 2. 1. 3.]
[0.5 3.  4.5 1.  3. ]
[1. 3. 4. 1. 3.]
[1.5 3.  3.5 1.  3. ]
[2.5 3.  4.  1.  1.5]
before 
[[ 0.  1.  2.  1.  3.]
 [ 1.  5.  7.  1.  3.]
 [ 2.  3.  4.  1.  0.]
 [ 3.  3.  3.  1.  3.]
 [10.  2.  4.  0.  0.]]
After Range Filter
[0.03 1.   2.   1.   3.  ]
[1. 5. 7. 1. 3.]
[2.   3.   4.   1.   0.03]
[3. 3. 3. 1. 3.]
[10.    2.    4.    0.03  0.03]
After Temporal Filter
[0. 1. 2. 1. 3.]
[0.5 3.  4.5 1.  3. ]
[1. 3. 4. 1. 3.]
[1.5 3.  3.5 1.  3. ]
[2.5 3.  4.  1.  1.5]
One can invoke show_result() method directly inside test_lidar_scanner by simply calling show_result() 
