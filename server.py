# app.py

from flask import Flask, jsonify, render_template
from opcua import Client

app = Flask(__name__)

# Connect to the OPC UA server
client = Client("opc.tcp://localhost:4840")
client.connect()

# Serve the index.html file from the 'templates' directory
@app.route("/")
def serve_hmi():
    return render_template("index.html")

# API route to get process data from the OPC UA server
@app.route("/api/process-data", methods=["GET"])
def get_process_data():
    # Read values from OPC UA server
    temperature = client.get_node("ns=2;i=2").get_value()
    pressure = client.get_node("ns=2;i=3").get_value()
    humidity = client.get_node("ns=2;i=4").get_value()

    # Return values as JSON
    return jsonify({
        "temperature": temperature,
        "pressure": pressure,
        "humidity": humidity
    })

if __name__ == "__main__":
    app.run(debug=True)
