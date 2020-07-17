
import logging
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
        num_list=list()
        for i in range(5):
            num_list.append(str(random.randint(1, 9)))
        return "".join(num_list)
