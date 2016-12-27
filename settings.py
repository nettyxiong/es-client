# elaticsearch config
hosts=[ {"host": "202.114.18.78","port":"9200"},
		{"host": "202.114.18.78","port":"9201"},
		{"host": "202.114.18.78","port":"9202"} ]

index="dml"
doc_type="snooker"

# oracle config
user="snooker"
password="snooker"
dsn='202.114.18.96/orcl'
min=1
max=10
increment=1

# api config
api_host = "0.0.0.0"
api_port = 8003