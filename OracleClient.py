import os 
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

import cx_Oracle
import settings
import logging
import datetime

pool = cx_Oracle.SessionPool(user=settings.user, password=settings.password, dsn=settings.dsn, min=settings.min, max=settings.max, increment=settings.increment)

class Client:
	@classmethod
	def execute(cls, sql):
		try:
			global pool
			conn = pool.acquire()
			cur = conn.cursor()
			cur.execute(sql)
			return True
		except Exception, e:
			logging.exception(e)
			return False
		finally:
			cur.close()
			pool.release(conn)

	@classmethod
	def query(cls, sql):
		try:
			global pool
			conn = pool.acquire()
			cur = conn.cursor()
			cur.execute(sql)
			return cur.fetchall()
		except Exception, e:
			print e
			logging.exception(e)
			return None
		finally:
			cur.close()
			pool.release(conn)

def rowToDoc(row):
	keys = ['clicknum', 'commentnum', 'videodateupload', 'videoid', 'videoname', 'videoorigin', 'videotime']
	values = list(row)
	doc = dict(zip(keys,values))
	return doc

def getAllRows():
	sql = 'select clicknum, commentnum, videodateupload, snooker_video_dynamic.videoid, videoname, videoorigin, round (totalduration/1000) as videotime from snooker_video inner join snooker_video_dynamic on snooker_video.videoid = snooker_video_dynamic.videoid'
	return Client.query(sql)

def getDailyRows():
	now_time_str=datetime.datetime.today().strftime('%Y%m%d')
	# now_time_str="20161220"
	daily_sql = '''select clicknum, commentnum, videodateupload, d.videoid, 
	 		videoname, videoorigin, round (totalduration/1000) as videotime 
	 		from snooker_video v, snooker_video_dynamic d
	 		where v.videoid = d.videoid and to_char(v.videodatecome,'yyyymmdd')=%s
	 		''' % now_time_str
	return Client.query(daily_sql)

if __name__ == '__main__':
	# print getAllRows()
	print len(getDailyRows())



