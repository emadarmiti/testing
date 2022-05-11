from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_data():

    # get the data from the POST request
    data = request.get_json()

    print(data)

    # with open('./data.json', 'w') as fp:
    #     json.dump(data, fp)
    return json.dumps(data)


if __name__ == '__main__':

    # run the service, set the port
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))