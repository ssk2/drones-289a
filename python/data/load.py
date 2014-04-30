import sqlite3 as lite
import csv
import data.database as db

def initialise_database(data_dir = "../data/"):
    # issue:
    #    0 = ok
    #    1 = loosemotor
    #    2 = loosepylon
    #    3 = broken_prop

    # Load CSV files into database
    issues = {0: "", 1:"loosemotor_", 2:"loosepylon_", 3:"broken_prop_"}
    loaded = {0:"unloaded", 1:"loaded"}
    stem = "fft_gs_mar24_"
    stem2 = "us_"

    cur, con = db.connect(data_dir)

    cur.executescript("""
    DROP TABLE IF EXISTS samples;
    DROP TABLE IF EXISTS test_samples;
    DROP TABLE IF EXISTS tests;
    CREATE TABLE samples (sample_id INTEGER, freq REAL, x REAL, y REAL, z REAL, UNIQUE(sample_id, freq) ON CONFLICT REPLACE);
    CREATE TABLE test_samples (sample_id INTEGER PRIMARY KEY, test_id INTEGER, part INTEGER);
    CREATE TABLE tests (test_id INTEGER PRIMARY KEY ASC, unloaded INTEGER, issue INTEGER, pulse_width TEXT);
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 1, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "1600us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "1700us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "1700us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "1700us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "1700us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "1700us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "2200us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "2200us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "2200us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "2200us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "2200us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "2300us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "2300us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "2300us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "2300us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "2300us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 1, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 3, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "800us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 0, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 1, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 2, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (1, 3, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 0, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 1, "900us");
    INSERT INTO tests (unloaded, issue, pulse_width) VALUES (0, 2, "900us");
    """)

    con.commit()

    cur.execute('SELECT pulse_width, unloaded, issue, test_id FROM tests')
    tests = cur.fetchall()

    for test in tests:
        pulse_width_string = test[0]
        unloaded_string = loaded[test[1]]
        issue_string = issues[test[2]]
        test_id = test[3]
        for part in range(0, 10):
            filename = data_dir + "fft/" + stem + pulse_width_string + "_" + unloaded_string + "_" + issue_string + str(part) + ".csv"
            sample_id = (test_id - 1) * 10 + part
            insert_statement = 'INSERT INTO test_samples (sample_id, test_id, part) VALUES (%s, %s, %s);' % (sample_id, test_id, part)
            cur.execute(insert_statement)
            with open (filename, 'r') as fftfile:
                fftreader = csv.reader(fftfile)
                fftreader.next()
                for row in fftreader:                
                    insert_statement = 'INSERT INTO samples (sample_id, freq, x, y, z) VALUES (%s, %s, %s, %s, %s);' % (sample_id, row[0], float(row[1]), float(row[2]), float(row[3]))
                    cur.execute(insert_statement)

    con.commit()                
    db.disconnect()
