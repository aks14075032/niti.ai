import datetime
from faker import Faker

fake = Faker()


def generate_loan_payload():
    return {
        'metadata': {
            'version': fake.word(),
            'originatorOrgId': fake.uuid4(),
            'originatorParticipantId': fake.uuid4(),
            'timestamp': str(datetime.datetime.now()),
            'traceId': fake.uuid4(),
            'requestId': fake.uuid4()
        },
        'productData': {
            'productId': fake.word(),
            'productNetworkId': fake.uuid4()
        },
        'loanApplications': [
            {
                'createdDate': fake.date(),
                'loanApplicationId': fake.uuid4(),
                'loanApplicationStatus': 'CREATED',
                'pledgedDocuments': [
                    {
                        'source': 'GSTN',
                        'sourceIdentifier': fake.uuid4(),
                        'format': 'JSON',
                        'reference': fake.uuid4(),
                        'type': 'GST_PROFILE',
                        'isDataInline': True,
                        'data': fake.text()
                    }
                ],
                'borrower': {
                    'primaryId': fake.uuid4(),
                    'primaryIdType': 'PAN',
                    'name': fake.name(),
                    'category': 'ORGANIZATION',
                    'contactDetails': [
                        {
                            'type': 'PRIMARY',
                            'description': fake.word(),
                            'phone': fake.phone_number(),
                            'email': fake.email(),
                            'address': {
                                'hba': fake.word(),
                                'srl': fake.word(),
                                'landmark': fake.word(),
                                'als': fake.word(),
                                'vtc': fake.word(),
                                'pinCode': fake.zipcode(),
                                'po': fake.word(),
                                'district': fake.word(),
                                'state': fake.state(),
                                'country': fake.country(),
                                'latitude': fake.latitude(),
                                'longitude': fake.longitude(),
                            }
                        }
                    ],
                    'documents': [
                        {
                            'source': 'GSTN',
                            'sourceIdentifier': fake.uuid4(),
                            'format': 'JSON',
                            'reference': fake.uuid4(),
                            'type': 'GST_PROFILE',
                            'isDataInline': True,
                            'data': fake.text()
                        }
                    ],
                    'url': fake.url()
                },
            }
        ]
    }

