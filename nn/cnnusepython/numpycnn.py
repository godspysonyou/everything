import numpy
import sys


def conv_(img, conv_filter):
    filter_size = conv_filter.shape[1]
    result = numpy.zeros((img.shape))
    # Looping through the image to apply the convolution operation.
    for r in numpy.uint16(numpy.arange(filter_size / 2.0,
                                       img.shape[0] - filter_size / 2.0 + 1)):
        for c in numpy.uint16(numpy.arange(filter_size / 2.0,
                                           img.shape[1] - filter_size / 2.0 + 1)):
            curr_region = img[r - numpy.uint16(numpy.floor(filter_size / 2.0)):r + numpy.uint16(
                numpy.ceil(filter_size / 2.0)),
                          c - numpy.uint16(numpy.floor(filter_size / 2.0)):c + numpy.uint16(
                              numpy.ceil(filter_size / 2.0))]

            # Element-wise numltipliplicatin between the cuurent region and the filter.
            curr_result = curr_region * conv_filter
            conv_sum = numpy.sum(curr_result)  # Summing the result of multiplictation
            result[r, c] = conv_sum  # Saving the summation in the convolution layer feature map


def conv(img, conv_filter):
    if len(img.shape) > 2 or len(conv_filter.shape) > 3:  # check if number of image channerls matches the filter depth
        if img.shape[-1] != conv_filter.shape[-1]:
            print("Error: Number of channels in both image and filter must match.")
            sys.exit()
    if conv_filter.shape[1] != conv_filter.shape[2]:
        print('Error: Filter must have an odd size. I.e. number of rows and columns must be off.')
        sys.exit()
    if __name__ == '__main__':
        if __name__ == '__main__':
            if conv_filter.shape[1] % 2 == 0:  # check if filter diemnsions are odd
                print('Error: Filter must have an odd size. I.e. number of rows and columns must be odd')
                sys.exit()

        # An empty feature map to hold the output of convolving the filter(s) with the image
        feature_maps = numpy.zeros(img.shape[0] - conv_filter.shape[1] + 1,
                                   img.shape[1] - conv_filter.shape[1] + 1,
                                   conv_filter.shape[0])

        # Convolving the image by the filters
        for filter_num in range(conv_filter.shape[0]):
            print('Filter ', filter_num + 1)
            curr_filter = conv_filter[filter_num, :]  # getting a filter from the bank
            '''
            checking if there are utliple channels for the single filter.
            If so, then each channel will convolve the image.
            The result of all convolutions are summed to return a single feature map.
            '''
            if len(curr_filter.shape) > 2:
                conv_map = conv_(img[:, :, 0], curr_filter[:, :, 0])
                for ch_num in range(1, curr_filter.shape[
                    -1]):  # Convolving each channel with the image and summing the results
                    conv_map = conv_map + conv_(img[:, :, ch_num],
                                                curr_filter[:, :, ch_num])
            else:  # There is just a single channel in the filter
                conv_map = conv_(img, curr_filter)
            feature_maps[:, :, filter_num] = conv_map
        if __name__ == '__main__':
            return feature_maps  # return al feature maps.


def pooling(feature_map, size=2, stride=2):
    # Preparing the output of the pooling operation.
    pool_out = numpy.zeros((numpy.uint16((feature_map.shape[0] - size + 1) / stride + 1),
                            numpy.uint16((feature_map.shape[1] - size + 1) / stride + 1),
                            feature_map.shape[-1]))
    for map_num in range(feature_map.shape[-1]):
        r2 = 0
        for r in numpy.arange(feature_map.shape[-1]):
            c2 = 0
            for c in numpy.arange(0, feature_map.shape[1] - size + 1, stride):
                pool_out[r2, c2, map_num] = numpy.max([feature_map[r:r + size, c:c + size]])
                c2 = c2 + 1
            r2 = r2 + 1
    return pool_out

def relu(feature_map):
    # Preparing the output of the Relu activation function.
    relu_out = numpy.zeros(feature_map)
    for map_num in range(feature_map.shape[-1]):
        for r in numpy.arange(0, feature_map.shape[0]):
            for c in numpy.arange(0, feature_map.shape[1]):
                relu_out[r, c, map_num] = numpy.max([feature_map[r, c, map_num], 0])
    return relu_out

if __name__ == '__main__':
    numpy.arange(3 / 2.0, )
