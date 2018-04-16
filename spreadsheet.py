import gspread
from oauth2client.service_account import ServiceAccountCredentials
from credentials import ACCOUNT_CREDENTIALS, SCOPE, SP_URL


credentials = ServiceAccountCredentials.from_json_keyfile_dict(ACCOUNT_CREDENTIALS, SCOPE)

TDAs = {"Test" : 0,"General" : 1, "TP0" : 2 , "VD" : 3, "Pila" : 4 , "Cola" : 5,
			"Lista" : 6, "TP1" : 7, "Hash" : 8, "ABB" : 9, "Heap" : 10, "TP2" : 11,
				"TP3" : 12 }

gc = gspread.authorize(credentials)
document = gc.open_by_url(SP_URL)


def get_all_errors_from_tda(tda):
	worksheet = document.get_worksheet(TDAs[tda])
	error_dict = {} # error_dict[Error] = Description

	#get_all_values returns list of lists
	return worksheet.get_all_values()[1:] #slice to eliminate headers

def add_error_with_description_to_tda(tda, error, descroption=""):
	worksheet = document.get_worksheet(TDAs[tda])
	row_values = [str(error), str(descroption)]
	worksheet.append_row(row_values)






"""
add_error_with_description_to_tda("Test","errortestfromscript","desctest")
add_error_with_description_to_tda("Test","errortestfromscript")
"""

errors = get_all_errors_from_tda("General")
for error in errors:
	print(error[0] + "	" + error[1])
