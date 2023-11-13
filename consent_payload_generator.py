from decimal import Decimal
import random
from faker import Faker
import datetime
fake = Faker()


def generate_random_string(length=10):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))


def generate_random_decimal():
    return Decimal(random.uniform(100, 1000))


def generate_consent_payload():
    return {
        "metadata": {
            "version": "base",
            "originatorOrgId": fake.uuid4(),
            "originatorParticipantId": fake.uuid4(),
            "timestamp": str(datetime.datetime.now()),
            "traceId": fake.uuid4(),
            "requestId": fake.uuid4()
        },
        "productData": {
            "productId": "show",
            "productNetworkId": fake.uuid4()
        },
        "loanApplicationIds": [fake.uuid4()],
        "consent": {
            "consentFetchType": "ONETIME",
            "vua": generate_random_string(),
            "description": fake.text(),
            "isAggregationEnabled": True,
            "consentAggregationId": fake.uuid4(),
            "consentHandle": generate_random_string(),
            "consentStatus": "READY",
            "url": fake.url(),
            "extensibleData": {}
        }
    }

