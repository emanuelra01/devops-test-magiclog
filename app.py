from flask import Flask, request
from multiprocessing import Value
import json

# import datetime class from datetime module
from datetime import datetime
from dateutil import relativedelta


counter = Value('i', 0)
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    output = "Hello World!!!"
    if request.method == 'POST':
        with counter.get_lock():
            counter.value += 1
            output = '''<h1>The count value is: {}</h1>'''.format(counter.value)
    
    return output

@app.route("/birthday", methods=['POST'])
def birthday():
    data = request.get_json()
    data = dict((k.lower(), v) for k, v in data.items())
    output = {}
    if not "date" in data or not "name" in data:
        output["error"] = "Bad Request"
    else:
        try:
            datetime.fromisoformat(data["date"])
            getdate = data["date"]
            birdate = datetime.strptime(getdate, '%Y-%m-%d')
            today = datetime.now()
            diff = relativedelta.relativedelta(today, birdate)
            output["data"] = data["name"] + "'s " + str(diff.years) + " years old"
        except ValueError:
            output["error"] = "Incorrect data format, should be YYYY-MM-DD"
            #raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    return json.dumps(output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
