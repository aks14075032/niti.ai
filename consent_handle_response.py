from faker import Faker
import datetime

fake = Faker()


def generate_consent_handle_response():
    return {
        "metadata": {
            "version": "string",
            "originatorOrgId": fake.uuid4(),  # Use a Faker method to generate a UUID
            "originatorParticipantId": fake.uuid4(),
            "timestamp": str(datetime.datetime.now()),
            "traceId": fake.uuid4(),
            "requestId": fake.uuid4()
        },
        "productData": {
            "productId": fake.uuid4(),
            "productNetworkId": fake.uuid4()
        },
        "loanApplicationIds": [fake.uuid4()],  # Use a Faker method to generate a UUID
        "consent": {
            "consentFetchType": "ONETIME",
            "vua": fake.uuid4(),
            "description": fake.text(),
            "isAggregationEnabled": True,
            "consentAggregationId": fake.uuid4(),
            "consentHandle": fake.uuid4(),
            "consentStatus": "READY",
            "url": fake.url(),
            "extensibleData": {}
        },
        "response": {
            "status": "SUCCESS",
            "responseDetail": fake.text()
        }
    }
