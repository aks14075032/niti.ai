import time
import requests
from flask import Flask, request, jsonify
from threading import Thread
from consent_handle_response import generate_consent_handle_response
import json

from consent_status_response import generate_consent_status_response

app = Flask(__name__)
PORT = 4000

loan_agent_url = 'http://localhost:3000/v4.0.0alpha/loanApplications/createLoanResponse'
loan_agent_offer_response_url = 'http://localhost:3000/v4.0.0alpha/offers/generateOffersResponse'


def send_response_to_la(trace_id, lender_name, data, response_url):
    # Additional processing time (e.g., 5 seconds)
    time.sleep(5)
    print("\n" + "-" * 20, f"Lender Sending response to {response_url}", "-" * 20)
    # Assume validation is done, send response to Loan Agent
    response_payload = {'traceId': trace_id, 'status': 'Approved', 'lender': lender_name, 'data': data}
    requests.post(response_url, json=response_payload)


@app.route('/v4.0.0alpha/loanApplications/createLenderLoanRequest', methods=['POST'])
def create_loan_request():
    print("\n" + "-" * 20, "Lender is called for loan request", "-" * 20)
    return process_request(request, loan_agent_url)


@app.route('/v4.0.0alpha/offers/lenderGenerateOffersRequest', methods=['POST'])
def generate_offer_request():
    print("\n" + "-" * 20, "Lender is called for offer request", "-" * 20)
    return process_request(request, loan_agent_offer_response_url)


def process_request(request_obj, response_url):
    loan_application_data = request_obj.json

    trace_id = loan_application_data['traceId']
    timestamp = loan_application_data['timestamp']
    data = loan_application_data.get('loanApplication', loan_application_data.get('data'))

    # Perform initial checks on the loan application...

    # Send acknowledgment
    acknowledgment = {'error': '0.0000', 'traceId': trace_id, 'timestamp': timestamp, 'status': 'Acknowledged'}

    # Simulate multiple lenders by using threads
    lenders_threads = []
    num_lenders = 2  # Change this number based on the desired number of lenders

    for i in range(num_lenders):
        lender_name = f'lender{i + 1}'
        t = Thread(target=send_response_to_la, args=(trace_id, lender_name, data, response_url))
        lenders_threads.append(t)
        t.start()

    # Wait for all lender threads to finish
    for t in lenders_threads:
        t.join()

    return jsonify(acknowledgment)


def send_response(response_url, payload):
    response = requests.post(response_url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
    print("\n" + "-" * 20, response.text, "-" * 20)


@app.route('/v4.0.0alpha/loanApplications/createConsenTHandleRequest', methods=['POST'])
def create_consent_handle_request():
    print("\n" + "-" * 20, "Lender is called for consent handle request", "-" * 20)
    loan_application_data = request.json

    trace_id = loan_application_data['traceId']
    timestamp = loan_application_data['timestamp']
    data = loan_application_data['loanApplication']

    # Perform initial checks on the loan application...

    # Send acknowledgment
    acknowledgment = {'error': '0.0000', 'traceId': trace_id, 'timestamp': timestamp, 'status': 'Sent'}

    # Here Call Account Aggregator
    send_consent_handle_response()

    return jsonify(acknowledgment)


def send_consent_handle_response():
    print("\n" + "-" * 20, "Lender is called for consent handle response", "-" * 20)
    url = "http://localhost:3000/v4.0.0alpha/consent/consentHandleResponse"

    consent_handle_response_payload = generate_consent_handle_response()  # Assuming this function is defined somewhere
    send_response(url, consent_handle_response_payload)


@app.route('/v4.0.0alpha/consent/journeyNotify', methods=['POST'])
def consent_journey_notification():
    print("\n" + "-" * 20, "Lender is called for consent journey notification", "-" * 20)
    data = request.json
    trace_id = data['metadata']['traceId']
    timestamp = data['metadata']['timestamp']

    print("\n" + "-" * 20, data, "-" * 20)
    # Send acknowledgment
    acknowledgment = {'error': '0.0000', 'traceId': trace_id, 'timestamp': timestamp}

    # Here Call Account Aggregator
    # ...

    return jsonify(acknowledgment)


@app.route('/v4.0.0alpha/consent/lenderStatusRequest', methods=['POST'])
def consent_status_request():
    print("\n" + "-" * 20, "Lender is called for consent status request", "-" * 20)
    data = request.json['data']
    trace_id = data['metadata']['traceId']
    timestamp = data['metadata']['timestamp']
    consent = data['consentHandle']

    print("\n" + "-" * 20, 'Consent Handle', consent, "-" * 20)

    # Send acknowledgment
    acknowledgment = {'error': '0.0000', 'traceId': trace_id, 'timestamp': timestamp}

    # Here Call Account Aggregator
    # ...

    return jsonify(acknowledgment)


@app.route('/v4.0.0alpha/consent/statusResponse', methods=['POST'])
def send_consent_status_response():
    print("\n" + "-" * 20, "Lender is called for consent status response", "-" * 20)
    url = "http://localhost:3000/v4.0.0alpha/consent/statusResponse"

    consent_status_response_payload = generate_consent_status_response()  # Assuming this function is defined somewhere
    send_response(url, consent_status_response_payload)


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
