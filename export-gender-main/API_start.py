from flask import Flask, request
from flask_restful import Api
import determinate_gender
import json

determinate_gender.load_data()
app = Flask(__name__)
api = Api()


@app.route('/')
def get_name():
    name = request.args.get('name')
    if name:
        return determinate_gender.get_gender(name)
    else:
        return json.dumps({'error':'missing name parameter'})



#api.init_app(app)

if __name__=='__main__':

    app.run(debug=False,port=3001, host="0.0.0.0")