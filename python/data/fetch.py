import sqlite3 as lite
import data.database as db
import random as rnd
import numpy as np

def get_number_of_samples (data_dir):
    cur, con = db.connect(data_dir)
    select_statement = 'SELECT COUNT(*) FROM test_samples;'
    cur.execute(select_statement)
    max_index = cur.fetchone()[0]
    db.disconnect()
    return max_index;

def get_sample_indices (training_samples, data_dir = "../data/"):
    number_of_samples = get_number_of_samples(data_dir) # assume sample IDs are contiguous
    training_indices = rnd.sample(range(number_of_samples), training_samples)
    test_indices = [ i for i in range(number_of_samples) if i not in training_indices ]
    return (training_indices, test_indices)

def get_sample_data (sample_ids, data_dir = "../data/"):
    cur, con = db.connect(data_dir)
    sample_data = []
    for sample_id in sample_ids:
        class_statement = 'SELECT issue > 0, pulse_width FROM test_samples JOIN tests ON test_samples.test_id = tests.test_id WHERE sample_id = %s;' % str(sample_id)
        cur.execute(class_statement)
        row = cur.fetchone();
        sample_class = row[0]
        sample_pulse_width = row[1]
        sample_statement = 'SELECT freq, x, y, z FROM samples WHERE sample_id = %s;' % str(sample_id)
        cur.execute(sample_statement)
        rows = cur.fetchall()
        data = np.zeros((len(rows),4))
        row_index = 0
        for row in rows:
            data[row_index] = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
            row_index += 1
        sample_data.append((sample_class, sample_pulse_width, data))
    db.disconnect()
    return sorted(sample_data, key=lambda sample: str(sample[0]) + str(sample[1]))

def get_sample_indices_by_issue (data_dir, issue="> -1"):
    cur, con = db.connect(data_dir)
    select_statement = 'SELECT sample_id FROM test_samples JOIN tests ON test_samples.test_id = tests.test_id WHERE tests.issue %s GROUP BY sample_id;' % issue 
    cur.execute(select_statement)
    sample_ids = []
    for row in cur.fetchall():
        sample_ids.append(row[0])
    db.disconnect()
    return sample_ids;

def get_sample_indices_for_crossvalidation (folds, data_dir = "../data/"): 
    number_of_samples = get_number_of_samples(data_dir) 
    fold_size = number_of_samples / folds

    class_0_sample_ids = get_sample_indices_by_issue(data_dir, "= 0")
    class_1_sample_ids = get_sample_indices_by_issue(data_dir, "!= 0")

    class_0_fold_size = len(class_0_sample_ids) / folds
    class_1_fold_size = len(class_1_sample_ids) / folds

    rnd.shuffle (class_0_sample_ids)
    rnd.shuffle (class_1_sample_ids)

    fold_ids = []

    for i in range(folds):
        fold_test_ids = class_0_sample_ids[i*class_0_fold_size : (i+1) * class_0_fold_size] + class_1_sample_ids[i*class_1_fold_size : (i+1) * class_1_fold_size]
        fold_train_ids = [ i for i in class_0_sample_ids if i not in fold_test_ids]
        fold_train_ids = fold_train_ids + [ i for i in class_1_sample_ids if i not in fold_test_ids]
        fold_ids.append((fold_train_ids, fold_test_ids))
    return fold_ids