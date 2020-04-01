from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def apitest():
    resp = "[url]--->" + request.url + "\n[method]--->" + str(request.method) + "\n[Content-Type]--->" + str(
        request.headers.get('Content-Type')) + "\n[json]--->" + str(request.json) + "\n[query_string]--->" + str(
        request.query_string) + "\n[form]-->" + str(request.form)
    print(resp)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=6666)