import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# This is a function that could run in AWS Lambda
def handler(event, context):

    logger.info("received request with id '{}'".format(context.aws_request_id))

    # *** INSERT MAGIC HERE ***

    return {
        "status": "success",
        "result": 42,
        "aws_request_id": context.aws_request_id
    }
