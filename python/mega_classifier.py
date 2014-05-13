# coding=utf-8
from data import fetch
from data import load
from classification import features
from numpy import mean
from sklearn import svm, neighbors, tree, ensemble, mixture


# cross validation properties
folds = 5

def fit_and_predict(clf, name, cv_sets):
	print "using %s classifier" % name
	train_accuracies = []
	test_accuracies = []
	for current_fold in range(folds):
		train_indices, test_indices = cv_sets[current_fold]
		train_data = fetch.get_sample_data (train_indices)
		test_data = fetch.get_sample_data (test_indices)
		Xtest,ytest = features.generate_feature_vectors(test_data, xyz_set, bins, top_n_freq, centroid_bool, ratio_bool, num_peaks_bool)
		X,y = features.generate_feature_vectors(train_data, xyz_set, bins, top_n_freq, centroid_bool, ratio_bool, num_peaks_bool)
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
cv_sets  = fetch.get_sample_indices_for_crossvalidation(folds = folds, multiclass = "false")


# try different feature vectors
clf = svm.SVC()

# just top_n_freq
bins = 0
top_n_freq = 1
centroid_bool = 0
ratio_bool = 0
num_peaks_bool = 0
xyz_set = [3] # X = 1, Y = 2, Z = 3... i.e. [1,3] uses X and Z of data for fv

# fit_and_predict(clf, "SVM: only top_n_freq", cv_sets)

# just ratio
top_n_freq = 0
ratio_bool = 1

# fit_and_predict(clf, "SVM: only ratio", cv_sets)


# just centroid
bins = 0
centroid_bool = 1

# fit_and_predict(clf, "SVM: only centroid", cv_sets)


# just num peaks


# different bin_widths


# different axes





# Try different methods: http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

bins = 10
top_n_freq = 1
centroid_bool = 1
ratio_bool = 1
num_peaks_bool = 1
xyz_set = [1,2,3] 

### Decision Tree : http://scikit-learn.org/stable/modules/tree.html
# clf = tree.DecisionTreeClassifier()
# fit_and_predict(clf, "Decision Tree", cv_sets)


### GMM : http://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_classifier.html
# n_components=n_classes
# ,covariance_type=covar_type, init_params='wc',

# clf = mixture.GMM(n_iter=20)
# fit_and_predict(clf, "GMM", cv_sets)

### Ensemble Methods : http://scikit-learn.org/stable/modules/ensemble.html
# try different n_estimators
# clf = ensemble.RandomForestClassifier(n_estimators = 10)
# fit_and_predict(clf, "Random Forest", cv_sets)

# Adaboost
# clf = ensemble.AdaBoostClassifier(n_estimators=10)
# fit_and_predict(clf, "AdaBoost", cv_sets)

### SVM : http://scikit-learn.org/stable/modules/svm.html#classification 

# try different kernels
# 'poly', 'linear' too slow 
# 'precomputed' doesn't work
# for kernel_type in ('rbf', 'sigmoid'):
# 	clf = svm.SVC(kernel=kernel_type)
# 	name = "SVM with %s kernel" % kernel_type
# 	fit_and_predict(clf, name, cv_sets)		

# effect of different C values
# for c in range (1, 10, 1):
# 	clf = svm.SVC(C=c/10)
# 	name = "SVM with %d C hyperparameter" % c
# 	fit_and_predict(clf, name, cv_sets)


### k-NN : http://scikit-learn.org/stable/modules/neighbors.html

# try different weights
# for weight in  ('uniform', 'distance'):
# 	clf = neighbors.KNeighborsClassifier(1, weights=weight)
# 	name = "k-NN with %s weights" % weight
# 	fit_and_predict(clf, name, cv_sets)


# try different neighbors
# for n_neighbours in range(1, 10):
# 	clf = neighbors.KNeighborsClassifier(n_neighbours)
# 	name = "k-NN with %d neighbours" % n_neighbours
# 	fit_and_predict(clf, name, cv_sets)






