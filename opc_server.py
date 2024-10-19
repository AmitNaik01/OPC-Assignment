from opcua import Server
import time
import random

# Initialize the server
server = Server()
server.set_endpoint("opc.tcp://localhost:4840")

# Add a namespace to organize the structure
uri = "http://examples.opcua/"
idx = server.register_namespace(uri)

# Create a folder for the simulation process
objects = server.get_objects_node()
simulation_folder = objects.add_folder(idx, "Simulations")

# Add variables for temperature, pressure, and humidity
temperature = simulation_folder.add_variable(idx, "Temperature", 20.0)
pressure = simulation_folder.add_variable(idx, "Pressure", 1.0)
humidity = simulation_folder.add_variable(idx, "Humidity", 50.0)

# Set variables to be writable by the client
temperature.set_writable()
pressure.set_writable()
humidity.set_writable()

# Start the OPC UA server
server.start()
print("OPC UA Server started at opc.tcp://localhost:4840")

try:
    while True:
        # Simulate changing values for the variables
        temp_value = 20.0 + random.uniform(-0.5, 0.5)
        pressure_value = 1.0 + random.uniform(-0.05, 0.05)
        humidity_value = 50.0 + random.uniform(-1, 1)

        # Write new values to the variables
        temperature.set_value(temp_value)
        pressure.set_value(pressure_value)
        humidity.set_value(humidity_value)

        print(f"Temperature: {temp_value}, Pressure: {pressure_value}, Humidity: {humidity_value}")
        time.sleep(1)
finally:
    # Close the server when exiting
    server.stop()
