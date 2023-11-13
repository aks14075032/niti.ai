import requests
from create_loan_payload import generate_loan_payload
from decimal import Decimal
import json
from consent_payload_generator import generate_consent_payload
from generate_offer_payload import generate_offers_request
from lender import send_consent_handle_response, send_consent_status_response
from consent_journey_status import generate_consent_journey_status
from consent_status_request import generate_consent_status_request


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class Borrower:
    def __init__(self):
        # Initialize any required variables or settings here

        # Call the functions you need
        self.create_loan()
        self.consent_handle()
        send_consent_handle_response()
        self.send_consent_journey_status()
        self.send_consent_status_request()
        send_consent_status_response()
        self.generate_offer()

    # Convert Decimal to float for JSON serialization
    @staticmethod
    def convert_to_serializable(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return obj

    def create_loan(self):
        url = "http://localhost:3000/v4.0.0alpha/loanApplications/createLoanRequest"

        loan_payload = generate_loan_payload()

        # Use json.dumps to serialize the payload
        payload = json.dumps(loan_payload, default=self.convert_to_serializable)

        # Use data instead of json, since we've already serialized the payload
        response = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})

        print(response.text)

    def consent_handle(self):
        url = "http://localhost:3000/v4.0.0alpha/consent/createConsentHandleRequest"

        consent_payload = generate_consent_payload()
        payload = json.dumps(consent_payload, default=self.convert_to_serializable)

        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=payload)

        print(response.text)

    def send_consent_journey_status(self):
        url = "http://localhost:4000/v4.0.0alpha/consent/journeyNotify"

        consent_journey_status_payload = generate_consent_journey_status()
        payload = json.dumps(consent_journey_status_payload, default=self.convert_to_serializable)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def send_consent_status_request(self):
        url = "http://localhost:3000/v4.0.0alpha/consent/statusRequest"

        consent_status_request_payload = generate_consent_status_request()
        payload = json.dumps(consent_status_request_payload)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def generate_offer(self):
        url = 'http://localhost:3000/v4.0.0alpha/offers/generateOffersRequest'

        offer_payload = generate_offers_request()

        # Use json.dumps to serialize the payload
        payload = json.dumps(offer_payload, default=self.convert_to_serializable)

        # Use data instead of json, since we've already serialized the payload
        response = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})

        print(response.text)


if __name__ == "__main__":
    borrower = Borrower()
