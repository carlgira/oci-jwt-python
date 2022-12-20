# OCI JWT Python
Script to use python to generate a JWT for OCI confidential applications.

## Prerequisites
- Python 

- Clone the repo
```bash
git clone https://github.com/carlgira/oci-jwt-python.git
```
- Create virtualenv, activate the environment, and install the requirements. 
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Instructions
Read the instructions in the official documentation to create the confidential application and to configure the app protected with JWT token.

Section *Prerequisites for JWT User Assertion* 
- https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-adapter/authentication-support.html#GUID-33BDEC15-CEC5-4535-8C71-FBA1A37BD7A3
```bash
python test.py
```

## Run
The script has one single function (get_token) with all the parameters required to generate the JWT token.
- idcs_url: The URL of the Identity Cloud Service (IDCS) instance.
- client_id: The client ID of the application.
- client_secret: The client secret of the application.
- cert_alias: The alias of the certificate used.
- scope: The scope configured in the confidential application.
- private_key: The private key used to sign the JWT token. (This can be read from a file, or you can get it from a secret in an OCI vault)

## Test
Open the test.py file, add the parameters required. Run the script to generate the JWT token.
```bash
python test.py
```

## References
- Confidential app configuration: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-adapter/authentication-support.html#GUID-33BDEC15-CEC5-4535-8C71-FBA1A37BD7A3
- Shell script doing the same: https://blogs.oracle.com/integration/post/oic-oauth-using-jwt-user-assertion