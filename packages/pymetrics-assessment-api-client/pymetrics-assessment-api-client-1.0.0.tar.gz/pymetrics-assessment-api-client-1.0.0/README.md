# pymetrics-assessment-api-client
A client library for accessing pymetrics Assessment API

## Installation

```bash
pip install pymetrics-assessment-api-client
```

## Usage

A full set of examples can be found in the [pymetrics-assessments-api-client examples directory](https://github.com/pymetrics/pymetrics_assessment_api_client/tree/main/pymetrics_assessment_api_client/examples).

To get started, please request Client ID, Client Secret and API Key from pymetrics.

First, create a client for staging environment:

```python
from pymetrics_assessment_api_client import Client

client = Client(base_url="https://staging.pymetrics.com")
```

To get an authenticated token, you can hit the get oauth endpoint by doing the following:
```python
from pymetrics_assessment_api_client.models import OAuthTokenRequest
from pymetrics_assessment_api_client.api.default import mercury_o_auth
from pymetrics_assessment_api_client.models import OAuthTokenResponse
from pymetrics_assessment_api_client.types import Response

request = OAuthTokenRequest(client_id=client_id,
                            client_secret=client_secret,
                            grant_type="client_credentials")
auth_response: Response = mercury_o_auth.sync_detailed(client=client,
                                                       json_body=request)
auth_token_response: OAuthTokenResponse = auth_response.parsed
print(f"Access Token: {auth_token_response.access_token}")
```
To retrieve an order, you can use the token generated above and hit the get order endpoint:
```python
from pymetrics_assessment_api_client.api.default import mercury_retrieve_order
from pymetrics_assessment_api_client.models import MercuryAssessmentOrder
from pymetrics_assessment_api_client.types import Response

auth = f"Bearer {access_token}"

get_order_response: Response = mercury_retrieve_order.sync_detailed(
    client=client,
    uuid=order_uuid,
    authorization=auth,
    x_api_key=API_KEY,
    report=False
)
parsed_get_order_response: MercuryAssessmentOrder = get_order_response.parsed
print(f"Successfully retrieved order: {parsed_get_order_response.to_dict()}")
```

## Base URLs
US Production: https://www.pymetrics.com

US Staging: https://staging.pymetrics.com