from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
PORT = 3000

lender_url = 'http://localhost:4000/v4.0.0alpha/loanApplications/createLenderLoanRequest'
lender_consent_url = 'http://localhost:4000/v4.0.0alpha/loanApplications/createLenderLoanRequest'
consent_status_url = 'http://localhost:4000/v4.0.0alpha/consent/lenderStatusRequest'
lender_offer_request_url = 'http://localhost:4000/v4.0.0alpha/offers/lenderGenerateOffersRequest'
lender_responses = {}


def forward_request(url, payload):
    response = requests.post(url, json=payload)
    return response.json()


@app.route('/v4.0.0alpha/loanApplications/createLoanRequest', methods=['POST'])
def create_loan_request():
    print("\n" + "-" * 20, 'Loan Agent Request Got called', "-" * 20)
    loan_application = json.loads(request.data)
    trace_id = loan_application['metadata']['traceId']
    timestamp = loan_application['metadata']['timestamp']

    # Forward loan application to the lender
    response_payload = {'traceId': trace_id, 'timestamp': timestamp, 'loanApplication': loan_application}
    response = forward_request(lender_url, response_payload)

    return response


@app.route('/v4.0.0alpha/loanApplications/createLoanResponse', methods=['POST'])
def create_loan_response():
    print("\n" + "-" * 20, "Loan agent processing response", "-" * 20)
    response_data = request.json

    trace_id = response_data['traceId']

    # Store lender response
    lender_responses[trace_id] = response_data

    print(response_data)
    return jsonify({'ack': 'received', 'trace_id': trace_id})


@app.route('/v4.0.0alpha/consent/createConsentHandleRequest', methods=['POST'])
def create_consent_handle_request():
    print("\n" + "-" * 20, 'Loan Agent consent handle Got called', "-" * 20)
    loan_application = json.loads(request.data)
    trace_id = loan_application['metadata']['traceId']
    timestamp = loan_application['metadata']['timestamp']

    # Forward consent to the lender
    response_payload = {'traceId': trace_id, 'timestamp': timestamp, 'loanApplication': loan_application}
    response = forward_request(lender_consent_url, response_payload)

    return response


@app.route('/v4.0.0alpha/consent/consentHandleResponse', methods=['POST'])
def consent_handle_response():
    print("\n" + "-" * 20, 'Loan Agent consent handle response Got called', "-" * 20)
    data = json.loads(request.data)
    trace_id = data['metadata']['traceId']
    print(data)
    return jsonify({'ack': 'received', 'trace_id': trace_id})


@app.route('/v4.0.0alpha/consent/statusRequest', methods=['POST'])
def consent_status_request():
    print("\n" + "-" * 20, 'Loan Agent consent status request Got called', "-" * 20)
    data = json.loads(request.data)
    trace_id = data['metadata']['traceId']
    # Forward loan application to the lender
    response_payload = {'traceId': trace_id, 'data': data}
    response = forward_request(consent_status_url, response_payload)

    return response


@app.route('/v4.0.0alpha/consent/statusResponse', methods=['POST'])
def consent_status_response():
    print("\n" + "-" * 20, 'Loan Agent consent status response Got called', "-" * 20)
    data = request.json
    trace_id = data['metadata']['traceId']
    timestamp = data['metadata']['timestamp']

    print("\n" + "-" * 20, 'Consent status', data, "-" * 20)

    # Send acknowledgment
    acknowledgment = {'error': '0.0000', 'traceId': trace_id, 'timestamp': timestamp}

    # Here Call Account Aggregator

    return jsonify(acknowledgment)


@app.route('/v4.0.0alpha/offers/generateOffersRequest', methods=['POST'])
def generate_offer_request():
    print("\n" + "-" * 20, 'Loan Agent generate offer Request Got called', "-" * 20)
    offer_request = json.loads(request.data)
    trace_id = offer_request['metadata']['traceId']
    timestamp = offer_request['metadata']['timestamp']

    # Forward loan application to the lender
    response_payload = {'traceId': trace_id, 'timestamp': timestamp, 'data': offer_request}
    response = forward_request(lender_offer_request_url, response_payload)

    return response


@app.route('/v4.0.0alpha/offers/generateOffersResponse', methods=['POST'])
def generate_offer_response():
    print("\n" + "-" * 20, "Loan agent generate offer processing response", "-" * 20)
    response_data = request.json

    trace_id = response_data['traceId']

    print(response_data)
    return jsonify({'ack': 'received', 'trace_id': trace_id})


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
