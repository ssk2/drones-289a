
# coding: utf-8

# In[ ]:

import numpy
import operator
import random
import matplotlib.pyplot as plt

def histogram(data, bins):
    freq = data[:,0]
    Z = data[:,3]
    H = numpy.asarray(plt.hist(Z,bins,(freq[0],freq[-1])))
    H[0] = 1.0*H[0]/sum(H[0])
    return H[0]

def top_frequencies(data, N):
    sorted_data = sorted(data, key=operator.itemgetter(3))
    top_freqs = numpy.asarray(sorted_data[-N:])
    return top_freqs[:,0]

def centroid(data):
    Z = data[:,3]
    Z_norm = Z*1.0/sum(Z)
    return numpy.mean(Z_norm)

def feature_vector(data, hist_bins, top_freqs):
    hist_vect = histogram(data, hist_bins)
    freq_vect = top_frequencies(data, top_freqs)
    cent_vect = centroid(data)
    return numpy.concatenate((hist_vect, freq_vect, [cent_vect]))

def normalize_data(data):
    Z = data[:,3]
    Z_norm = Z*1.0/sum(Z)
    data[:,3] = Z_norm
    return data

def generate_training_set(dataset, histbins, topfreq):
    trainlabels = []
    trainset = []
    samplesize = len(dataset)
    for i in range(0,samplesize):
        trainlabels.append(dataset[i][0])
        trainset.append(feature_vector(dataset[i][1], histbins, topfreq))
    return (trainset, trainlabels)

