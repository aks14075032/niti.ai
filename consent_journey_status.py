from faker import Faker
import datetime

fake = Faker()


def generate_consent_journey_status():
    return {
        "metadata": {
            "version": "string",
            "originatorOrgId": fake.uuid4(),
            "originatorParticipantId": fake.uuid4(),
            "timestamp": str(datetime.datetime.now()),
            "traceId": fake.uuid4(),
            "requestId": fake.uuid4()
        },
        "productData": {
            "productId": fake.random_number(digits=4),  # Example: 1231
            "productNetworkId": fake.random_number(digits=3)  # Example: 101
        },
        "loanApplicationIds": [fake.uuid4()],
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
        }
    }
