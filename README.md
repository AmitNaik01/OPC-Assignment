Here’s a revised README.md file without the PostgreSQL section:

markdown

# OPC Server with Web-Based SCADA HMI

This project implements an OPC UA server that simulates a life sciences process and provides a web-based SCADA HMI to visualize real-time process data.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Clone and Setup](#clone-and-setup)
3. [Install Dependencies](#install-dependencies)
4. [Running the OPC Server](#running-the-opc-server)
5. [Running the Web-Based SCADA UI](#running-the-web-based-scada-ui)
6. [Validating Data Consistency with OPC Client](#validating-data-consistency-with-opc-client)
7. [Screenshots](#screenshots)

## Prerequisites

- Python 3.x
- `pip` for installing Python packages
- An OPC client like [UaExpert](https://www.unified-automation.com/products/development-tools/uaexpert.html) or [Kepware](https://www.kepware.com/en-us/products/kepserverex/) for testing

## Clone and Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

Install Dependencies

    Create and activate a virtual environment (recommended):

    bash

python -m venv opc_scada_venv
source opc_scada_venv/bin/activate   # On Windows use `opc_scada_venv\Scripts\activate`

Install the required Python packages:

bash

    pip install flask opcua

Running the OPC Server

    Navigate to the directory where your OPC server script is located (e.g., server.py), and run the server:

    bash

python server.py

You should see a message indicating that the OPC UA server has started:

arduino

    OPC UA Server started at opc.tcp://localhost:4840

Running the Web-Based SCADA UI

    In a new terminal (with the virtual environment activated), navigate to the directory where your Flask app script is located (e.g., app.py), and run the Flask application:

    bash

python app.py

You should see a message indicating that the server is running:

csharp

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    Open your web browser and navigate to http://127.0.0.1:5000/ to access the SCADA HMI.

Validating Data Consistency with OPC Client

    Using UaExpert:
        Download and install UaExpert.
        Open UaExpert and create a new connection using the endpoint opc.tcp://localhost:4840.
        Once connected, browse the data model to find the variables for temperature, pressure, and humidity.
        Compare the values displayed in UaExpert with those shown in your SCADA UI.

Screenshots

Include screenshots of the SCADA HMI UI below:
