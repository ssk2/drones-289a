# coding=utf-8
from data import fetch
from data import load
from classification import features
from numpy import mean
from sklearn import svm

# Run this the first time
# load.initialise_database()

folds = 3

# Try different kernels for SVC: http://scikit-learn.org/stable/modules/svm.html#classification  'poly',  'precomputed'
kernels = ('linear', 'rbf', 'sigmoid' )  

# Use cross validation to get different subsets
cv_sets  = fetch.get_sample_indices_for_crossvalidation(folds)

train_accuracies = []
test_accuracies = []

xyz_set = [3] # X = 1, Y = 2, Z = 3... i.e. [1,3] uses X and Z of data for fv

for current_fold in range(folds):
	print "fold %d" % current_fold
	train_indices, test_indices = cv_sets[current_fold]
	train_data = fetch.get_sample_data (train_indices)
	test_data = fetch.get_sample_data (test_indices)
	X,y = features.generate_feature_vectors(train_data, xyz_set, 10, 2)
	Xtest,ytest = features.generate_feature_vectors(test_data, xyz_set, 10, 2)
	for kernel_string in kernels:
		print "trying kernel %s" % kernel_string		
		clf = svm.SVC(kernel = kernel_string)
		clf.fit(X,y)
		
		y_train_pred = clf.predict(X)
		train_accuracies.append(100*(sum(y_train_pred == y))/len(y))
		print "training set accuracy: %d" % train_accuracies[current_fold] 
		
		y_test_pred = clf.predict(Xtest)
		test_accuracies.append(100*(sum(y_test_pred == ytest))/len(ytest))
		print "test set accuracy: %d" % test_accuracies[current_fold]

print "Average training set accuracy: %d" % mean(train_accuracies)
print "Average test set accuracy: %d" % mean(test_accuracies)


# Try different methods: http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

# Try K nearest neighbours: http://scikit-learn.org/stable/modules/neighbors.html

# Try ensemble methods: http://scikit-learn.org/stable/modules/ensemble.htmlex