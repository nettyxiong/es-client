import bottle
from bottle import get, post, delete
from bottle import request, response

import settings
from EsClient import ES
import json

import logging
logging.basicConfig(
	level=logging.INFO,
	format="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s:%(funcName)s] %(message)s",
	datefmt='%Y-%m-%d %H:%M:%S',   
)

# GET /dml/snooker/_search?q=videoname:snooker
@get('/<index>/<doc_type>/_search')
def search_by_get(index,doc_type):
	es = ES(index,doc_type)
	query = dict(request.query)
	key = query['q'].split(":")[0]
	value = query['q'].split(":")[1]
	queryDict = {key:value}
	body = {
		"query": {
			"match": queryDict
		}
	}
	logging.info(body)
	data = es.getBySearch(body)
	response.status = 200
	response.content_type='application/json'
	return json.dumps(data)
	
# POST /dml/snooker/_search
# {
# 	"query": {
# 		"match": {
# 			"videoname": "奥利沙文"
# 		}
# 	}
# }
@post('/<index>/<doc_type>/_search')
def search_by_post(index,doc_type):
	es = ES(index,doc_type)
	body = request.json
	logging.info(body)
	data = es.getBySearch(body)
	response.status = 200
	response.content_type='application/json'
	return json.dumps(data)


if __name__ == '__main__':
	bottle.run(host = settings.api_host, port = settings.api_port)
	# bottle.run(server='gunicorn', host = settings.api_host, port = settings.api_port)
else:
	app = application = bottle.default_app()