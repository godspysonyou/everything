import skimage.data
import numpy
import matplotlib
import numpy_cnn

'''
Convolutional neural implementation using Numpy.
'''

# Reading the image
img = skimage.data.chelsea()

# Converting the image into gray
img = skimage.color.rgb2gray(img)

# First conv layer
# l1_filter = numpy.random.rand(2,7,7)*20 # Preparing the filters randomly.
l1_filter = numpy.zeros((2, 3, 3))
l1_filter[0, :, :] = numpy.array([[[-1, 0, 1],
                                   [-1, 0, 1],
                                   [-1, 0, 1]]])
l1_filter[1, :, :] = numpy.array([[[1, 1, 1],
                                   [0, 0, 0],
                                   [-1, -1, -1]]])

print("\n**Working with conv layer 1**")
l1_feature_map = numpycnn.conv()