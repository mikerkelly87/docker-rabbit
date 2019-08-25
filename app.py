from flask import Flask
from flask import jsonify
import pymysql

app = Flask(__name__)


@app.route('/')
def hello():
    #return "Hello World!"

    mydb = pymysql.connect(
      "172.25.0.201",
      "rabbitmq",
      "S3cur3",
      "rabbitmq"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM messages;")

    messages = cursor.fetchall()
    #return jsonify(messages=cursor.fetchall())
    return jsonify(messages)
    mydb.close



if __name__ == '__main__':
    app.run(host= '0.0.0.0')