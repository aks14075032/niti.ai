import datetime
from faker import Faker

fake = Faker()


def generate_offers_request():
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
        "loanApplicationIds": [fake.uuid4()]
    }
