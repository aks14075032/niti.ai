import datetime
from faker import Faker

fake = Faker()


def generate_consent_status_response():
    return {
        "metadata": {
            "version": fake.word(),
            "originatorOrgId": fake.uuid4(),
            "originatorParticipantId": fake.uuid4(),
            "timestamp": str(datetime.datetime.now()),
            "traceId": fake.uuid4(),
            "requestId": fake.uuid4()
        },
        "productData": {
            "productId": fake.word(),
            "productNetworkId": fake.word()
        },
        "loanApplicationIds": [fake.uuid4()],
        "consent": {
            "consentFetchType": "ONETIME",
            "vua": fake.word(),
            "description": fake.word(),
            "isAggregationEnabled": fake.boolean(),
            "consentAggregationId": fake.uuid4(),
            "consentHandle": fake.uuid4(),
            "consentStatus": "READY",
            "url": fake.url(),
            "extensibleData": {}
        },
        "response": {
            "status": "SUCCESS",
            "responseDetail": fake.word()
        }
    }
