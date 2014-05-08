import sqlite3 as lite
import data.database as db
import random as rnd
import numpy as np

def get_number_of_samples (data_dir):
    cur, con = db.connect(data_dir)
    cur.execute('SELECT COUNT(*) FROM test_samples;')
    max_index = cur.fetchone()[0]
    db.disconnect()
    return max_index;

def get_sample_indices (training_samples, testing_samples, data_dir = "../data/"):
    number_of_samples = get_number_of_samples(data_dir) # assume sample IDs are contiguous
    training_indices = rnd.sample(range(number_of_samples), training_samples)
    test_indices = [ i for i in range(number_of_samples) if i not in training_indices ]
    return (training_indices, test_indices)

def get_sample_data (sample_ids, data_dir = "../data/"):
    cur, con = db.connect(data_dir)
    sample_data = []
    for sample_id in sample_ids:
        class_statement = 'SELECT issue  FROM test_samples JOIN tests on test_samples.test_id = tests.test_id WHERE sample_id = %s;' % str(sample_id)
        cur.execute(class_statement)
        sample_class = cur.fetchone()[0]
        sample_statement = 'SELECT freq, x, y, z FROM samples WHERE sample_id = %s;' % str(sample_id)
        cur.execute(sample_statement)
        rows = cur.fetchall()
        data = np.zeros((len(rows),4))
        row_index = 0
        for row in rows:
            data[row_index] = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
            row_index += 1
        sample_data.append((sample_class, data))
    db.disconnect()
    return sample_data
