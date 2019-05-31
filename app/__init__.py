import os, json
import sorter
from flask import Flask, request, jsonify, abort
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
	from app.models import Jobs, Bids
	
	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)
	
	@app.route("/job", methods=['GET','POST'])
	def add_job():
		job_id=request.data.get('job_id')
		origin=request.data.get('origin')
		destination=request.data.get('destination')
		budget=request.data.get('budget')
		shipment_date=request.data.get('shipment_date')
		distance=request.data.get('distance')
		try:
			job=Jobs(
				job_id=job_id,
				origin=origin,
				destination=destination,
				budget=budget,
				shipment_date=shipment_date,
				distance=distance
			)
			db.session.add(job)
			db.session.commit()
			return jsonify({
				'job_id':job.job_id,
				'origin':job.origin,
				'destination':job.destination,
				'budget':job.budget,
				'shipment_date':job.shipment_date,
				'distance':job.distance
			})
		except Exception as e:
			return(str(e))
	
	@app.route("/bid", methods=['GET','POST'])
	def add_bid():
		id=request.data.get('id')
		job_id=request.data.get('job_id')
		transporter_name=request.data.get('transporter_name')
		transporter_rating=request.data.get('transporter_rating', 0.0)
		price=request.data.get('price')
		vehicle_name=request.data.get('vehicle_name')
		try:
			bid = Bids(id= id,
        	job_id= job_id,
        	transporter_name=transporter_name,
        	transporter_rating= transporter_rating,
        	price=price,
        	vehicle_name=vehicle_name
			)
			db.session.add(bid)
			db.session.commit()
			return jsonify({
				'id':bid.id,
				'job_id':bid.job_id,
				'transporter_name':bid.transporter_name,
				'transporter_rating':bid.transporter_rating,
				'price':bid.price,
				'vehicle_name':bid.vehicle_name
			})
		except Exception as e:
			return(str(e))

	@app.route("/getjobs", methods=['GET'])
	def get_all_jobs():
		try:
			jobs=Jobs.query.all()
			return  jsonify([e.serialize() for e in jobs])
		except Exception as e:
			return(str(e))

	@app.route("/getbids", methods=['GET'])
	def get_all_bids():
		try:
			bids=Bids.query.all()
			return  jsonify([e.serialize() for e in bids])
		except Exception as e:
			return(str(e))

	# Get_by_id
	@app.route("/getjobs/<id_>", methods=['GET'])
	def get__job_by_id(id_):
		try:
			job=Jobs.query.filter_by(job_id=id_).first()
			return jsonify(job.serialize())
		except Exception as e:
			return(str(e))

	@app.route("/getbids/<id_>", methods=['GET'])
	def get__bid_by_id(id_):
		try:
			bid=Bids.query.filter_by(id=id_).first()
			return jsonify(bid.serialize())
		except Exception as e:
			return(str(e))

	# PUT
	@app.route("/getjobs/<id_>", methods=['PUT'])
	def put__job_by_id(id_):
		job = Jobs.query.filter_by(job_id=id_).first()
		if not job:
			abort(404)
		origin=request.data.get('origin', job.origin)
		destination=request.data.get('destination', job.destination)
		budget=request.data.get('budget', job.budget)
		shipment_date=request.data.get('shipment_date', job.shipment_date)
		distance=request.data.get('distance',job.distance)
		
		job.origin=origin
		job.destination=destination
		job.budget=budget
		job.shipment_date=shipment_date
		job.distance=distance
		
		# print(job.origin)
		db.session.commit()

		return jsonify({
				'job_id':job.job_id,
				'origin':job.origin,
				'destination':job.destination,
				'budget':job.budget,
				'shipment_date':job.shipment_date,
				'distance':job.distance
			})
	
	@app.route("/getbids/<id_>", methods=['PUT'])
	def put__bid_by_id(id_):
		bid = Bids.query.filter_by(id=id_).first()
		if not bid:
			abort(404)
		job_id=request.data.get('job_id', bid.job_id)
		transporter_name=request.data.get('transporter_name', bid.transporter_name)
		transporter_rating=request.data.get('transporter_rating', bid.transporter_rating)
		price=request.data.get('price', bid.price)
		vehicle_name=request.data.get('vehicle_name', bid.vehicle_name)
		
		bid.job_id=job_id
		bid.transporter_name=transporter_name
		bid.transporter_rating=transporter_rating
		bid.price=price
		bid.vehicle_name=vehicle_name
		
		# print(job.origin)
		db.session.commit()

		return jsonify({
			'id':bid.id,
			'job_id':bid.job_id,
			'transporter_name':bid.transporter_name,
			'transporter_rating':bid.transporter_rating,
			'price':bid.price,
			'vehicle_name':bid.vehicle_name
		})
		
	# Get bids for certain jobs
	@app.route("/getjobs/<id_>/bids", methods=['GET'])
	def get__bids_by_job(id_):
		try:
			bids = Bids.query.filter_by(job_id=id_).all()
			return jsonify([e.serialize() for e in bids])
		except Exception as e:
			return (str(e))

	# Delete
	@app.route("/deljob/<id_>")
	def del__job_by_id(id_):
		job = Jobs.query.filter_by(job_id=id_).delete()
		db.session.commit()
		try:
			job1 = Jobs.query.all()
			return jsonify([e.serialize() for e in job1])
		except Exception as e:
			return (str(e))

	@app.route("/delbid/<id_>")
	def del__bid_by_id(id_):
		bid = Bids.query.filter_by(id=id_).delete()
		db.session.commit()
		try:
			bid1 = Bids.query.all()
			return jsonify([e.serialize() for e in bid1])
		except Exception as e:
			return (str(e))

	@app.route("/getjobs/<factor>/<odr>", methods=['GET'])
	def get__jobs_by_factor_odr(factor, odr):
		try:
			jobs=Jobs.query.all()

			#Origin 
			if(factor == "origin"):
				if(odr == "asc"):
					sorter.quickSort_jobs_by_origin_asc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
				elif(odr == "desc"):
					sorter.quickSort_jobs_by_origin_desc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
			
			#Destination
			elif(factor == "dest"):
				if(odr == "asc"):
					sorter.quickSort_jobs_by_destination_asc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
				elif(odr == "desc"):
					sorter.quickSort_jobs_by_destination_desc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])

			#Budget
			elif(factor == "budget"):
				if(odr == "asc"):
					sorter.quickSort_jobs_by_budget_asc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
				else:
					sorter.quickSort_jobs_by_budget_desc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])

			#Shipment_date
			elif(factor == "date"):
				if(odr == "asc"):
					sorter.quickSort_jobs_by_shipment_date_asc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
				else:
					sorter.quickSort_jobs_by_shipment_date_desc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])

			#Distance
			elif(factor == "dist"):
				if(odr == "asc"):
					sorter.quickSort_jobs_by_distance_asc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
				else:
					sorter.quickSort_jobs_by_distance_desc(jobs, 0, len(jobs)-1)
					return  jsonify([e.serialize() for e in jobs])
			
			else:
				return jsonify([e.serialize() for e in jobs])
		except Exception as e:
				return(str(e))

	@app.route("/getbids/<factor>/<odr>", methods=['GET'])
	def get__bids_factor_odr(factor,odr):
		try:
			bids = Bids.query.all()

			#Transporter name
			if(factor == "transporter"):
				if(odr == "asc"):
					sorter.quickSort_bids_by_transporter_asc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])
				else:
					sorter.quickSort_bids_by_transporter_desc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])

			#Transporter rating
			elif(factor == "rating"):
				if(odr == "asc"):
					sorter.quickSort_bids_by_rating_asc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])
				else:
					sorter.quickSort_bids_by_rating_desc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])

			#Price
			elif(factor == "price"):
				if(odr == "asc"):
					sorter.quickSort_bids_by_price_asc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])
				else:
					sorter.quickSort_bids_by_price_desc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])

			#Vehicle name
			elif(factor == "vehicle"):
				if(odr == "asc"):
					sorter.quickSort_bids_by_vehicle_asc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])
				else:
					sorter.quickSort_bids_by_vehicle_desc(bids, 0, len(bids)-1)
					return  jsonify([e.serialize() for e in bids])
			else:
				return jsonify([e.serialize() for e in bids])
		except Exception as e:
				return(str(e))

	return app