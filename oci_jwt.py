from datetime import datetime, timezone
import oci._vendor.jwt.api_jwt as jwt
import requests
from requests.auth import HTTPBasicAuth

token_live_time = 600


def get_token(cert_alias, user_to_assert, scope, idcs_url, private_key, client_id, client_secret):

    token_issued = int(datetime.now(tz=timezone.utc).timestamp())
    token_expiry = token_issued + token_live_time

    header = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": cert_alias
    }

    user_payload = {
        "sub": user_to_assert,
        "iss": client_id,
        "aud": ["https://identity.oraclecloud.com/"],
        "iat": token_issued,
        "exp": token_expiry
    }

    encoded_user_assertion = jwt.encode(payload=user_payload, headers=header,
                                        key=private_key,
                                        algorithm="RS256")

    payload = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'scope': scope,
        'client_id': client_id,
        'assertion': encoded_user_assertion,
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(idcs_url,  headers=headers, data=payload, auth=HTTPBasicAuth(client_id, client_secret))

    return response.json()


