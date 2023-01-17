import json
import mercadopago
import os


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    body = json.loads(event["body"])

    

    # Crear pago
    payment_data = {
        "transaction_amount": float(body["transaction_amount"]),
        "token": body["token"],
        "installments": int(body["installments"]),
        "payment_method_id": body["payment_method_id"],
        "issuer_id": body["issuer_id"],
        "payer": {
            "email": body["payer"]["email"],
            "identification": {
                "type": body["payer"]["identification"]["type"],
                "number": body["payer"]["identification"]["number"]
            }
        }
    }
    # print(payment_data)
    payment_response = sdk.payment().create(payment_data)
    print("payment response")
    print(payment_response)

    payment=payment_response["response"]
    print("payment")
    print(type(payment))
    response={
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Headers" : "Content-Type",
                "Access-Control-Allow-Origin": "*", 
                "Access-Control-Allow-Methods": "GET"
            },
            "body": json.dumps(payment)
    }
    print("respuesta json")
    print(response)
    return response

    