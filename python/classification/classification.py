
import classification.features as features
reload(classification.features)

import data.load
reload(data.load)
data.load.initialise_database()

import data.fetch
reload (data.fetch)
from sklearn import svm

# PARAMETERS
bins = 10 # this currently does nothing, histogram fv commented out
top_n_freq = 2
xyz_set = [3] # X = 1, Y = 2, Z = 3... i.e. [1,3] uses X and Z of data for fv
train_sample_size = 300
# ^^^ test_sample_size = 350 - train_sample_size

train_indices, test_indices = data.fetch.get_sample_indices(train_sample_size, 50)
train_data = data.fetch.get_sample_data (train_indices)
test_data = data.fetch.get_sample_data (test_indices)

X,y = features.generate_feature_vectors(train_data, xyz_set, bins, top_n_freq)
Xtest,ytest = features.generate_feature_vectors(test_data, xyz_set, bins, top_n_freq)

clf = svm.SVC()
clf.fit(X,y)

ypred = clf.predict(Xtest)
print 100*(sum(ypred == ytest))/len(ytest)


