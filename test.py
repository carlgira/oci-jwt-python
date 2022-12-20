from oci_jwt import get_token

if __name__ == '__main__':
    cert_alias = '<certificate-alias>'
    user_to_assert = '<username>'
    scope = 'https://<app-idcs>:443urn:opc:resource:consumer::all'
    idcs_url = 'https://<idcs-url>/oauth2/v1/token'

    private_key = open('private.pem', 'r').read() # for local testing
    # private_key = get_secret('private.pem') Read from secret in OCI vault

    client_id = '<client-id>'
    client_secret = '<client-secret>'

    response = get_token(cert_alias, user_to_assert, scope, idcs_url, private_key, client_id, client_secret)
    access_token = response['access_token']
    print(access_token)