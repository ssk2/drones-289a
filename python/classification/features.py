
# coding: utf-8

# In[ ]:

import numpy
import operator
import random
import matplotlib.pyplot as plt
import math


def histogram(data, data_type, bins):
    A = data[:,data_type]
    binlength = int(math.floor(len(data)/bins))
    binned_data = numpy.zeros(bins)
    for i in range(0, bins):
        summ = 0
        for j in range(0,binlength):
            summ = summ + A[j+i*binlength]
        binned_data[i] = summ
    normalized_data = binned_data*1.0/numpy.sum(binned_data)
    return normalized_data

def top_frequencies(data, data_type, N):
    sorted_data = sorted(data, key=operator.itemgetter(data_type))
    top_freqs = numpy.asarray(sorted_data[-N:])
    return top_freqs[:,0]

def data_mean(data, data_type):
    A = data[:,data_type]
    A_norm = A*1.0/sum(A)
    A_mean = numpy.mean(A_norm)
    return [A_mean]

def peak_ratio(data, data_type):
    A = data[:,data_type]
    A_norm = A*1.0/sum(A)
    peak_magnitude = max(A_norm)
    mean_magnitude = data_mean(data, data_type)
    if mean_magnitude <= 0:
        return -1
    return peak_magnitude/mean_magnitude

def centroid(data, data_type):
    freq = data[:,0]
    A = data[:,data_type]
    A_norm = A*1.0/sum(A)
    n = len(A)
    summ = 0
    for i in range(0,n):
        if(summ + A_norm[i] > 0.5):
            return [freq[i]]
        summ = summ + A_norm[i]
    return [-1]

def feature_vector(data, data_type, hist_bins, top_freqs):
    hist_vect = histogram(data, data_type, hist_bins)
    freq_vect = top_frequencies(data, data_type, top_freqs)
    cent_vect = centroid(data, data_type)
    ratio_vect = peak_ratio(data, data_type)
    return numpy.concatenate((freq_vect, cent_vect, ratio_vect))

def normalize_data(data, data_type):
    A = data[:,data_type]
    A_norm = Z*1.0/sum(Z)
    data[:,data_type] = A_norm
    return data

def generate_feature_vectors(dataset, data_types, histbins, topfreq):
    trainlabels = []
    trainset = []
    samplesize = len(dataset)
    num_types = len(data_types)
    for i in range(0,samplesize):
        trainlabels.append(dataset[i][0])
        fullfeaturevector = []
        for j in data_types:
            vect = feature_vector(dataset[i][2], j, histbins, topfreq)
            fullfeaturevector = numpy.concatenate((fullfeaturevector, vect))
        trainset.append(fullfeaturevector)
    return (trainset, trainlabels)

