# test_bucketlist.py
import unittest
import os
import json
from app import create_app, db


class BucketlistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        
        # JOBS
        self.job = {"job_id": 1,
        "origin": "semarang",
        "destination": "Jakarta",
        "budget": 1000,
        "shipment_date": "2019-05-06 00:00:00",
        "distance": 1000}

        self.job1 = {"job_id": 2,
        "origin": "Surabaya",
        "destination": "Bali",
        "budget": 2000,
        "shipment_date": "2019-05-05 00:00:01",
        "distance": 3000}


        # BIDS
        self.bid = {"id": 1,
        "job_id": 1,
        "transporter_name": "James",
        "transporter_rating": 3.0,
        "price": 500,
        "vehicle_name": "Tronton"
        }

        self.bid1 = {"id": 2,
        "job_id": 1,
        "transporter_name": "james",
        "transporter_rating": 4.0,
        "price": 450,
        "vehicle_name": "Fuso"
        }
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_job_creation(self):
        # job_id has to be unique
        self.jobN = {"job_id": 1,
        "origin": "Surabaya",
        "destination": "Bali",
        "budget": 1000,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": 1000}
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/job', data=self.jobN)
        self.assertNotIn("\"origin\": \"Surabaya\"", str(res.data))
        
        # origin cannot be null
        self.jobN = {"job_id": 3,
        "origin": None,
        "destination": "Bali",
        "budget": 1000,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": 1000}
        res = self.client().post('/job',data=self.jobN)
        self.assertNotIn("\"job_id\": 3", str(res.data))
        
        # Destination cannot be null
        self.jobN = {"job_id": 3,
        "origin": "Surabaya",
        "destination": None,
        "budget": 1000,
        "shipment_date": "2019-05-05 12:00:00",
        "distance": 1000}
        res = self.client().post('/job',data=self.jobN)
        self.assertNotIn("\"job_id\": 3", str(res.data))
        
        # budget cannot be null
        self.jobN = {"job_id": 3,
        "origin": "Surabaya",
        "destination": "Bali",
        "budget": None,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": 1000}
        res = self.client().post('/job',data=self.jobN)
        self.assertNotIn("\"job_id\": 3", str(res.data))

        self.jobN = {"job_id": 3,
        "origin": "Surabaya",
        "destination": "Bali",
        "budget": 1000,
        "shipment_date": None,
        "distance": 1000}
        res = self.client().post('/job',data=self.jobN)
        self.assertIn("\"job_id\": 3", str(res.data))
        
        # distance cannot be null
        self.jobN = {"job_id": 4,
        "origin": "Surabaya",
        "destination": "Bali",
        "budget": 1000,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": None}
        res = self.client().post('/job',data=self.jobN)
        self.assertNotIn("\"job_id\": 4", str(res.data))
        
        # everything can be a duplicate except for job id
        self.jobN = {"job_id": 4,
        "origin": "Semarang",
        "destination": "Bali",
        "budget": 1000,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": 1000}
        res = self.client().post('/job',data=self.jobN)
        self.assertIn("\"job_id\": 4", str(res.data))

    def test_get_all_jobs(self):
        # EMPTY
        res = self.client().get('/getjobs')
        self.assertEqual([], [])

        # INSERTED
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/job', data=self.job1)
        print(res.data)
        res = self.client().get('/getjobs')
        self.assertEqual(res.status_code, 200)
        # print(res.data)
        self.assertIn("\"origin\": \"semarang\"", str(res.data))
        self.assertNotIn("\"origin\": \"Jakarta\"", str(res.data))

    def test_bid_creation(self):
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/bid', data=self.bid)
        self.assertIn("\"id\": 1", str(res.data))
        
        # job_id cannot be none
        self.bidN = {"id": 3,
        "job_id": None,
        "transporter_name": "james",
        "transporter_rating": 4.0,
        "price": 450,
        "vehicle_name": "Fuso"
        }
        res = self.client().post('/bid', data=self.bidN)
        self.assertIn('(psycopg2.errors.NotNullViolation)', res.data)
        
        # job_id cannot be a job that is not there
        self.bidN = {"id": 3,
        "job_id": 2,
        "transporter_name": "james",
        "transporter_rating": 4.0,
        "price": 450,
        "vehicle_name": "Fuso"
        }
        res = self.client().post('/bid', data=self.bidN)
        self.assertIn('(psycopg2.errors.ForeignKeyViolation)', res.data)

        # transpoeter name cannot be none
        self.bidN = {"id": 3,
        "job_id": 1,
        "transporter_name": None,
        "transporter_rating": 4,
        "price": 450,
        "vehicle_name": "Fuso"
        }
        res = self.client().post('/bid', data=self.bidN)
        self.assertIn('(psycopg2.errors.NotNullViolation)', res.data)

        self.bidN = {"id": 5,
        "job_id": 1,
        "transporter_name": "james",
        "transporter_rating": None,
        "price": 450,
        "vehicle_name": "Fuso"
        }
        res = self.client().post('/bid', data=self.bidN)
        self.assertIn("\"id\": 5", str(res.data))

    def test__get_job_by_id(self):
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/job', data=self.job1)

        # job is in the database
        res = self.client().get('/getjobs/1')
        self.assertIn("\"job_id\": 1", str(res.data))
        
        # job is not in the database
        res = self.client().get('/getjobs/10')
        self.assertNotIn("\"job_id\": 10", str(res.data))
    
    def test_put_job_by_id(self):
        self.job1 = {"job_id": 1,
        "origin": "Surabaya",
        "destination": "Semarang",
        "budget": 2000,
        "shipment_date": None,
        "distance": 3000}
        res = self.client().post('/job', data=self.job)
        res = self.client().put('/getjobs/1', data=self.job1)
        self.assertEqual(res.status_code, 200)
        self.assertIn("\"origin\": \"Surabaya\"", res.data)
        self.assertNotIn("Jakarta", res.data)

        res = self.client().put('/getjobs/2', data=self.job1)
        self.assertEqual(res.status_code, 404)

    def test_put_bid_by_id(self):
        self.bid1 = {"id": 1,
        "job_id": 1,
        "transporter_name": "DSP",
        "transporter_rating": 5.0,
        "price": 1000,
        "vehicle_name": "Trailer"
        }
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/bid', data=self.bid)
        res = self.client().put('/getbids/1', data=self.bid1)
        self.assertEqual(res.status_code, 200)
        self.assertNotIn("\"transporter_name\": James", str(res.data))
        self.assertNotIn("\"transporter_name\": DSP", str(res.data))


    def test__get_bids_by_job(self):
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/bid', data=self.bid)
        res = self.client().post('/bid', data=self.bid1)
        res = self.client().get('/getjobs/1/bids')
        self.assertEqual('[\n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }\n]\n',
             res.data)
        
        res = self.client().post('/job', data=self.job1)
        res = self.client().get('/getjobs/2/bids')
        self.assertEqual('[]\n', str(res.data))


    def test__del_job_by_id(self):
        res = self.client().post('/job', data=self.job)
        self.assertIn("\"job_id\": 1", str(res.data))
        res = self.client().delete('/deljob/1')
        self.assertNotIn("\"job_id\": 1", str(res.data))

        # nothing left to be deleted
        res = self.client().delete('/deljob/1')
        self.assertEqual(405, res.status_code)
    
    def test__del_bid_by_id(self):
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/bid', data=self.bid)
        self.assertIn("\"id\": 1", str(res.data))
        
        res = self.client().delete('/delbid/1')
        self.assertNotIn("\"id\": 1", str(res.data))

        res = self.client().delete('/delbid/1')
        self.assertEqual(405, res.status_code)
        
    def test_get_jobs_by_factor_odr(self):
        self.job2 = {"job_id": 3,
        "origin": "surabaya",
        "destination": "bali",
        "budget": 2001,
        "shipment_date": "2019-05-05 00:00:00",
        "distance": 3001}
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/job', data=self.job1)
        res = self.client().get('/getjobs')
        self.assertEqual('[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }\n]\n',
             res.data)

        # Descending based on origin with duplicates 
        res = self.client().post('/job', data=self.job2)
        res = self.client().get('/getjobs/origin/desc')
        self.assertEqual('[\n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }\n]\n',
         res.data)

        # Ascending based on origin with duplicates
        res = self.client().get('/getjobs/origin/asc')
        self.assertEqual('[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }\n]\n',
             res.data)
        
        # Descending based on destination
        res = self.client().get('/getjobs/origin/desc')
        self.assertEqual('[\n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Ascending based on destination
        res = self.client().get('/getjobs/origin/asc')
        self.assertEqual('[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Descending based on budget
        res = self.client().get('/getjobs/budget/desc')
        self.assertEqual('[\n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Ascending based on budget
        res = self.client().get('/getjobs/budget/asc')
        self.assertEqual( '[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Descending based on date
        res = self.client().get('/getjobs/date/desc')
        self.assertEqual('[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Ascending based on date
        res = self.client().get('/getjobs/date/asc')
        self.assertEqual('[\n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Descending based on distance
        res = self.client().get('/getjobs/dist/desc')
        self.assertEqual('[\n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)

        # Ascending based on distance
        res = self.client().get('/getjobs/dist/asc')
        self.assertEqual('[\n  {\n    "Destination": "Jakarta", \n    "budget": 1000, \n    "distance": 1000, \n    "job_id": 1, \n    "origin": "semarang", \n    "shipment_date": "Mon, 06 May 2019 00:00:00 GMT"\n  }, \n  {\n    "Destination": "Bali", \n    "budget": 2000, \n    "distance": 3000, \n    "job_id": 2, \n    "origin": "Surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:01 GMT"\n  }, \n  {\n    "Destination": "bali", \n    "budget": 2001, \n    "distance": 3001, \n    "job_id": 3, \n    "origin": "surabaya", \n    "shipment_date": "Sun, 05 May 2019 00:00:00 GMT"\n  }\n]\n',
        res.data)


    def test__get_bids_by_factor_odr(self):
        self.bid2 = {"id": 3,
        "job_id": 1,
        "transporter_name": "Jim",
        "transporter_rating": None,
        "price": 450,
        "vehicle_name": "fuso"
        }
        res = self.client().post('/job', data=self.job)
        res = self.client().post('/bid', data=self.bid)
        res = self.client().post('/bid', data=self.bid1)
        res = self.client().post('/bid', data=self.bid2)
        # Descending transporter name
        res = self.client().get('/getbids/transporter/desc')
        self.assertEqual('[\n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }\n]\n',
             res.data)

        # Ascending transporter name
        res = self.client().get('/getbids/transporter/asc')
        self.assertEqual('[\n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }\n]\n',
             res.data)

        # Descending transporter rating
        res = self.client().get('/getbids/rating/desc')
        self.assertEqual('[\n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }\n]\n',
             res.data)
        
        # Ascending transporter rating
        res = self.client().get('/getbids/rating/asc')
        self.assertEqual('[\n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }, \n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }\n]\n',
             res.data)

        # Descending price
        res = self.client().get('/getbids/price/desc')
        self.assertEqual('[\n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }\n]\n',
             res.data)

        # Ascending price
        res = self.client().get('/getbids/price/asc')
        self.assertEqual('[\n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }, \n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }\n]\n',
             res.data)

        # Descending vehicle name
        res = self.client().get('/getbids/vehicle/desc')
        self.assertEqual('[\n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }, \n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }\n]\n',
             res.data)

        # Ascending vehicle name
        res = self.client().get('/getbids/vehicle/asc')
        self.assertEqual('[\n  {\n    "id": 2, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "james", \n    "transporter_rating": 4.0, \n    "vehicle_name": "Fuso"\n  }, \n  {\n    "id": 3, \n    "job_id": 1, \n    "price": 450, \n    "transporter_name": "Jim", \n    "transporter_rating": 0.0, \n    "vehicle_name": "fuso"\n  }, \n  {\n    "id": 1, \n    "job_id": 1, \n    "price": 500, \n    "transporter_name": "James", \n    "transporter_rating": 3.0, \n    "vehicle_name": "Tronton"\n  }\n]\n',
             res.data)


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()