
import classification.features as features
reload(classification.features)

import data.load
reload(data.load)
data.load.initialise_database()

import data.fetch
reload (data.fetch)
from sklearn import svm

# PARAMETERS
bins = 0
top_n_freq = 1
centroid_bool = 0
ratio_bool = 0
num_peaks_bool = 0

xyz_set = [1] # X = 1, Y = 2, Z = 3... i.e. [1,3] uses X and Z of data for fv
train_sample_size = 300
# ^^^ test_sample_size = 350 - train_sample_size


train_indices, test_indices = data.fetch.get_sample_indices(train_sample_size, 50)
train_data = data.fetch.get_sample_data (train_indices)
test_data = data.fetch.get_sample_data (test_indices)

X,y = generate_feature_vectors(train_data, xyz_set, bins, top_n_freq, centroid_bool, ratio_bool, num_peaks_bool)
Xtest,ytest = generate_feature_vectors(test_data, xyz_set, bins, top_n_freq, centroid_bool, ratio_bool, num_peaks_bool)

clf = svm.SVC().fit(X,y)
clf.score(Xtest,ytest)

