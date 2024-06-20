import requests
import datetime
import json
import hashlib
import os
import logging



######### DATE TIME #########
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


######### PATH SETTINGS #########
if not __name__ == "__main__":
    # LOGGING PATH
    os.makedirs("./logs/", exist_ok=True)

    path_python_log = os.path.join(os.curdir, "logs/DataExtractor.py.log")

    with open(path_python_log, "a") as writer:
        writer.write(f"[{current_datetime}] Started Python file from path {os.path.curdir}\n")

    logging.basicConfig(filename=path_python_log, level=logging.ERROR)

    # TEMPORARY FOLDER PATH
    path_femp_folder = os.path.join(os.curdir, ".TempFolder")

    # HASH FILE PATH
    file_path = os.path.join(path_femp_folder, "hashfile.txt")


######### HASH FUNCTION #########
def hash_adder(extracted_data: str):
    try:
        file_hash = hashlib.md5(extracted_data.encode('utf-8')).hexdigest()
        # Check if the folder exists, create it if it doesn't
        os.makedirs(path_femp_folder, exist_ok=True)

        # Append a string to the file
        string_to_append = f"{file_hash},\n"
        with open(file_path, "a") as file:
            file.write(string_to_append)

        return str(file_hash)
    
    except Exception as e:
        logging.error(f"An errror occurred while writing to the file: {e}")
 
######### JSON TEST #########
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        print(f"ValueError: {e}")
        print(myjson)
        return False
    return True

######### PROMPT TEMPLATE #########
template =  """    'Invoicenumber': Invoicenumber (Format: String),
    'FirstName': First Name (Invoicereceiver) (Format: String),
    'LastName': Last Name (Invoicereceiver) (Format: String),
    'Address': {
                'street': Street (Invoicereceiver) (Format: String),
                'city': City (Invoicereceiver) (Format: String),
                'PLZ': Postcode (Invoicereceiver) (Format: String),
                },
    'Amount': Invoice Amount (Total) (Format: Decimal),
    'Company': Company Name (Format: String),""" + f"""
    
    'createDate': '{formatted_datetime}',
    'modifiedDate': '{formatted_datetime}'""" + """
    }

Do not change anything on the structure and only return the JSON without explanation or starting/ending sentences!\n\nHere is the Data:\n""" 

######### MAIN FUNCTION FOR UI PATH #########
def process_with_olama(extracted_data):
    try:
        chain = "Return a JSON-Object with the following Form and Values:\n" + "{\n" + f"    Id: '{hash_adder(extracted_data)}',\n" + template + extracted_data
        print(chain)
        headers = {
                    "Content-Type": "application/json"
                    }

        jsondata = {
                        "model": "mistral:latest",
                        "prompt": f"{chain}",
                        "stream": False
                    }
        response = requests.post("http://localhost:11434/api/generate",
                                headers = headers,
                                json = jsondata
                                )
        
        response_text = response.json()['response']

        if is_json(f"{response_text}"):
            return response_text
        else:
            empty_json = {
                "invoiceNr": "",
                "firstName": "",
                "lastName":  "" ,
                "amount": "",
                "currency": "",
                "company": "",
                "address":
                    {
                    "street": "",
                    "city": "",
                    "PLZ": ""
                    },
                "createDate": f"{formatted_datetime}",
                "modifiedDate": f"{formatted_datetime}",
                "Extraction Failed": "True"
            }
            return str(empty_json)
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        return f"Following error has occured:\n{e}"
    


if __name__ == "__main__":
    ######### TESTING #########

    data = """
    Raffi Testing AG
    Versuchsstrasse 5
    7310 Bad Ragaz
    Grosse Rechnung
    Lieferadresse:
    Pascal Federico
    Hochschulstrasse 8
    7000 Chur
    Rechnungsadresse:
    Pascal Federico
    Hochschulstrasse 12
    7000 Chur
    Rechnungsdatum:  01.06.2024
    Rechnungsnummer:  111991
    Kundennummer:  187
    Rechnungsdetails
    Serviceleistung   Währung Betrag
    1x diskrete Testing-Services CHF  1000.00
    1x Spezial-Testing-Services  CHF  2450.05
    1x Beratungsgebühren «Testing» CHF  12.00
    Gesamttotal    CHF  3462.05
    Zahlbar bis: 10.07.2024
    Bei nicht-erfolgter Zahlung werden Sie durch unseren Debitorenverwalter - «Happy Hells
    Angels» - kontaktiert.
    Merci!
    Bei Fragen wenden Sie sich bitte nicht an uns.
    ___________________
    Raffi
    CEO Raffi Testing AG
    Seite 1/1"""


    ######### PATH SETTINGS #########
    
    # LOGGING PATH
    os.makedirs("./../logs/", exist_ok=True)

    path_python_log = os.path.join(os.curdir, "../logs/DataExtractor.py.log")
  
    with open(path_python_log, "a") as writer:
        writer.write(f"[{current_datetime}] Started Python file from path {os.path}\n")

    logging.basicConfig(filename=path_python_log, level=logging.ERROR)

    # TEMPORARY FOLDER PATH
    path_femp_folder = os.path.join(os.curdir, "../.TempFolder")

    # HASH FILE PATH
    file_path = os.path.join(path_femp_folder, "hashfile.txt")

    ######### FUNCTION CALL #########
    result = process_with_olama(data)
    print(result)