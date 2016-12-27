from datetime import datetime
import elasticsearch
from elasticsearch import helpers
import settings
import OracleClient
class ES(object):
	es = None
	def __init__(self,index=settings.index,doc_type=settings.doc_type):
		if ES.es is None:
			ES.es = elasticsearch.Elasticsearch(
				settings.hosts
			)
		self.index = index
		self.doc_type = doc_type

	def post(self,doc,id=None):
		if id is not None:
			res = self.es.index(index=self.index, doc_type=self.doc_type, body=doc,id=id)
		else:
			res = self.es.index(index=self.index, doc_type=self.doc_type, body=doc)
		if res['created'] is True:
			return True
		else:
			return False

	def getById(self,id):
		return self.es.get(index=self.index, doc_type=self.doc_type, id=id)['_source']

	def getBySearch(self, body):
		data = self.es.search(index=self.index, doc_type=self.doc_type, body=body, _source=True)
		return data['hits']['hits']

	def deleteIndex(self):
		self.es.delete(index=self.index,doc_type=self.doc_type)

	def postByBulk(self,data):
		actions = []
		for row in data:
			action = {
			"_index":self.index,
			"_type":self.doc_type,
			"_source":OracleClient.rowToDoc(row)
			}
			actions.append(action)
			
		if (len(actions) > 0):
			helpers.bulk(self.es, actions)
			del actions[0:len(actions)]

if __name__ == '__main__':
	es = ES()
	doc = {
	'author': 'sxiong',
	'text': 'sxiong is a sb',
	'timestamp': datetime.now(),
	}
	# print es.post(doc,1)
	print es.getById(1)


