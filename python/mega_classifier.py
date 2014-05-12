# coding=utf-8
from data import fetch
from data import load
from classification import features
from numpy import mean
from sklearn import svm, neighbors


# cross validation properties
folds = 5

# feature vector properties
bin_width = 50
top_freqs = 1
xyz_set = [3] # X = 1, Y = 2, Z = 3... i.e. [1,3] uses X and Z of data for fv

def fit_and_predict(clf, name, cv_sets):
	print "using %s classifier" % name
	train_accuracies = []
	test_accuracies = []
	for current_fold in range(folds):
		train_indices, test_indices = cv_sets[current_fold]
		train_data = fetch.get_sample_data (train_indices)
		test_data = fetch.get_sample_data (test_indices)
		Xtest,ytest = features.generate_feature_vectors(test_data, xyz_set, bin_width, top_freqs)
		X,y = features.generate_feature_vectors(train_data, xyz_set, bin_width, top_freqs)
		clf.fit(X,y)
		y_train_pred = clf.predict(X)
		train_accuracies.append(100*(sum(y_train_pred == y))/len(y))
		y_test_pred = clf.predict(Xtest)
		test_accuracies.append(100*(sum(y_test_pred == ytest))/len(ytest))

	print "%.1f \t average training set accuracy" % mean(train_accuracies)
	print "%.1f \t average test set accuracy" % mean(test_accuracies)


# Run this the first time
# load.initialise_database()

# svm properties

# Use cross validation to get different subsets pulse_width = pulse_width, unloaded = unloaded
cv_sets  = fetch.get_sample_indices_for_crossvalidation(folds = folds)

# Try different methods: http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

# Try ensemble methods: http://scikit-learn.org/stable/modules/ensemble.htmlex

# try different feature vectors

# try different training methods

### SVM : http://scikit-learn.org/stable/modules/svm.html#classification 

# try different kernels
# 'poly' too slow
for kernel_type in ('precomputed', 'linear', 'rbf', 'sigmoid'):
	clf = svm.SVC(kernel=kernel_type)
	name = "SVM with %s kernel" % kernel_type
	fit_and_predict(clf, name, cv_sets)		

# effect of different C values
for c in range (0, 1, 0.1):
	clf = svm.SVC(C=c)
	name = "SVM with %d C hyperparameter" % c
	fit_and_predict(clf, name, cv_sets)


### k-NN : http://scikit-learn.org/stable/modules/neighbors.html

# try different weights
for weight in  ('uniform' 'distance'):
	clf = neighbors.KNeighborsClassifier(1, weights=weight)
	name = "k-NN with %s weights" % weight
	fit_and_predict(clf, name, cv_sets)


# try different neighbors
for n_neighbours in  range(10):
	clf = neighbors.KNeighborsClassifier(n_neighbours)
	name = "k-NN with %d neighbours" % n_neighbours
	fit_and_predict(clf, name, cv_sets)






