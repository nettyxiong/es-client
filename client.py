#coding=utf-8
import OracleClient
from EsClient import ES
import datetime
from optparse import OptionParser
def _load(kind="daily"):
	if kind=="daily":
		data = OracleClient.getDailyRows()
	else:
		data = OracleClient.getAllRows()

	es = ES()
	for row in data:
		doc = OracleClient.rowToDoc(row)
		es.post(doc)


def loadAll():
	data = OracleClient.getAllRows()
	es = ES()
	es.postByBulk(data)

def loadDaily():
	# _load()
	data = OracleClient.getDailyRows()
	es = ES()
	es.postByBulk(data)

if __name__ == '__main__':
	# loadAll()
	loadDaily()
