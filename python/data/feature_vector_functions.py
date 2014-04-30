
# coding: utf-8

# In[ ]:

import numpy
import operator

def histogram_feature_vector(data, bins):
    freq = data[:,0]
    Z = data[:,3]
    H = asarray(hist(Z,bins,(freq[0],freq[-1])))
    H[0] = 1.0*H[0]/sum(H[0])
    return H[0]

def top_frequencies(data, N):
    sorted_data = sorted(data, key=operator.itemgetter(3))
    top_freqs = asarray(sorted_data[-N:])
    return top_freqs[:,0]

def centroid(data):
    Z = data[:,3]
    Z_norm = Z*1.0/sum(Z)
    return mean(Z_norm)

def full_feature_vector(data, hist_bins, top_freqs):
    hist_vect = histogram_feature_vector(data, hist_bins)
    freq_vect = top_frequencies(data, top_freqs)
    cent_vect = centroid(data)
    return concatenate((hist_vect, freq_vect, [cent_vect]))

def normalize_data(data):
    Z = data[:,3]
    Z_norm = Z*1.0/sum(Z)
    data[:,3] = Z_norm
    return data

