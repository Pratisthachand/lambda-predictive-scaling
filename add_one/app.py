import json
import time

print("Initializing the lambda function")

#simulating time taken to complete a large task
#will be replaced with more extensive functions later

time.sleep(1)

print("Initialization complete!")

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    try:
        body = json.loads(event.get('body','{}'))
        number = body.get('number',0)

        result = number + 1

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"The result is {result}",
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"An error occurred",
                "error": str(e),
            }),
        }

    
