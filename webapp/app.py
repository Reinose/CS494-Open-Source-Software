from flask import Flask
import memcache
import MySQLdb
import redis
import datetime, time, sys, random

app = Flask(__name__)

db = MySQLdb.Connect(host='127.0.0.1', port=3306, user='reinose', passwd='password', db='cs494')
cursor = db.cursor()
nbase = redis.StrictRedis(port=6000)
arcus = memcache.Client(["127.0.0.1:11211"])


@app.route('/')
def main():
    return 'Main page'

@app.route('/init')
def init():
    cursor.execute('drop table if exists testset');
    cursor.execute('create table testset ( id int, data int );')
    for i in range(10000):
        cursor.execute('insert into testset values(%s,%s)'%(i+1,random.randint(0,100000000)))
    db.commit()
    return 'Initialization finished'

@app.route('/mysql')
def mysql():
    query = 'select * from testset where id=%s'%random.randint(1,10000)
    cursor.execute(query)
    res = cursor.fetchone()
    return str(res)

@app.route('/arcus')
def arcus_():
    i = random.randint(1,10000)
    res = arcus.get(str(i))
    if res:
        return 'Cache Hit: '+str(res)
    else:
        query = 'select * from testset where id=%s'%i
        cursor.execute(query)
        res = cursor.fetchone()
        arcus.set(str(i),res[1])
        return 'Cache Miss: '+str(res)

@app.route('/nbase')
def nbase_():
    i = random.randint(1,10000)
    res = nbase.get(i)
    if res:
        return 'Cache Hit: '+str(res)
    else:
        query = 'select * from testset where id=%s'%i
        cursor.execute(query)
        res = cursor.fetchone()
        nbase.set(i,res[1])
        return 'Cache Miss: '+str(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

