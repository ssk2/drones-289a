
# coding: utf-8

# In[6]:

import classification.features as features
reload(classification.features)

import data.load
reload(data.load)
data.load.initialise_database()

import data.fetch
reload (data.fetch)
from sklearn import svm

train_indices, test_indices = data.fetch.get_sample_indices(50, 300)
train_data = data.fetch.get_sample_data (train_indices)
test_data = data.fetch.get_sample_data (test_indices)

X,y = features.generate_training_set(train_data, 10, 5)
Xtest,ytest = features.generate_training_set(test_data, 10, 5)

clf = svm.SVC()
clf.fit(X,y)

ypred = clf.predict(Xtest)
print 100*(sum(ypred == ytest))/len(ytest)


# In[ ]:



