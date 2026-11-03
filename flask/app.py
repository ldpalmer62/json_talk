from flask import Flask, request, jsonify, json, render_template

app=Flask(__name__)

# put variables here to be visible to all the below routes
json_data = {
        "temperature": "No data",
        "message": "No data
}

@app.route('/')
def hello_world():
    return "Hello, Flask, this is Raspberry Pi"

@app.route("/api/payload", methods=["POST"])
def receive_json():
    global json_data
    payload = request.get_json(silent=True)
    print("Received JSON", payload)
    return jsonify({"status": "success", "received":payload}), 200


    elif request.method == 'GET':
        message = payload.get('message')
        temperature = payload.get('temperature')

#    json.dumps(payload)
#    return jsonify({
#        "received": {
#            "temperature": temperature,
#            "message": message
#          #"status": "OK"
#        }
#    }), 200
    #return jsonify(payload)
    return render_template('/index.html', data=payload)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

