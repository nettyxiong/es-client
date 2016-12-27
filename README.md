# es-client
dml搜球网基于Elasticsearch的存储服务
# settings.py

```python
# elaticsearch config
hosts=[ {"host": "127.0.0.1","port":"9200"},
		{"host": "127.0.0.1","port":"9201"},
		{"host": "127.0.0.1","port":"9202"} ]

index="dml"
doc_type="snooker"

# oracle config
user="snooker"
password="snooker"
dsn='127.0.0.1/orcl'
min=1
max=10
increment=1

# api config
api_host = "0.0.0.0"
api_port = 8003
```
