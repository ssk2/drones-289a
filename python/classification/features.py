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

def std(data):
    sigma = 0
    meann = numpy.mean(data)
    for i in range(0, len(data)):
        sigma = sigma + (data[i]-meann)*(data[i]-meann)
    sigma = math.sqrt(sigma/len(data))
    return sigma


def peak_ratio(data, data_type):
    A = data[:,data_type]
    A_norm = A*1.0/sum(A)
    peak_magnitude = max(A_norm)
    mean_magnitude = data_mean(data, data_type)
    if mean_magnitude <= 0:
        return -1
    return peak_magnitude/mean_magnitude

def number_of_top_peaks(data, data_type):
    A = data[:,data_type]
    A_norm = A*1.0/sum(A)
    num_peaks = 0
    sigma = std(A_norm)
    mean = numpy.mean(A_norm)
    for i in range(0, len(A_norm)):
        if A_norm[i] > mean + sigma*3:
            num_peaks = num_peaks + 1
    return [num_peaks]

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

def feature_vector(data, data_type, hist_bins, top_freqs, centroid_bool, ratio_bool, peaks_bool):
    fv = []
    if(hist_bins > 0):
        hist_vect = histogram(data, data_type, hist_bins)
        fv = numpy.concatenate((fv, hist_vect))
    if(top_freqs > 0):
        freq_vect = top_frequencies(data, data_type, top_freqs)
        fv = numpy.concatenate((fv, freq_vect))
    if(centroid_bool > 0):
        cent_vect = centroid(data, data_type)
        fv = numpy.concatenate((fv, cent_vect))
    if(ratio_bool > 0):
        ratio_vect = peak_ratio(data, data_type)
        fv = numpy.concatenate((fv, ratio_vect))
    if(peaks_bool > 0):
        num_peaks_vect = number_of_top_peaks(data, data_type)
        fv = numpy.concatenate((fv, num_peaks_vect))
    return fv

def normalize_data(data, data_type):
    A = data[:,data_type]
    A_norm = Z*1.0/sum(Z)
    data[:,data_type] = A_norm
    return data

def generate_feature_vectors(dataset, data_types, histbins, topfreq, centroid_bool, ratio_bool, peaks_bool):
    trainlabels = []
    trainset = []
    samplesize = len(dataset)
    for i in range(0,samplesize):
        trainlabels.append(dataset[i][0])
        fullfeaturevector = []
        for j in data_types:
            vect = feature_vector(dataset[i][2], j, histbins, topfreq, centroid_bool, ratio_bool, peaks_bool)
            fullfeaturevector = numpy.concatenate((fullfeaturevector, vect))
        trainset.append(fullfeaturevector)
    return (trainset, trainlabels)