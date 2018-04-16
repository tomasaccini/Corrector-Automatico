import os

SCOPE = ["https://spreadsheets.google.com/feeds"]

SP_URL = "https://docs.google.com/spreadsheets/d/17QD8OV6EwBmKGRzIf7oRMVyVpvRkmEoplbGt57apUOg/edit?ouid=115972410932789325539&usp=sheets_home&ths=true"

ACCOUNT_CREDENTIALS = {
	  "type": "service_account",
	  "project_id": os.environ["PROJECT_ID"],
  	"private_key_id": os.environ["PRIVATE_KEY_ID"],
  	"private_key": os.environ["PRIVATE_KEY"],
  	"client_email": os.environ["CLIENT_EMAIL"],
  	"client_id": os.environ["CLIENT_ID"],
  	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
  	"token_uri": "https://accounts.google.com/o/oauth2/token",
  	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  	"client_x509_cert_url": os.environ["CLIENT_x509_CERT_URL"] 
}