import logging
import random
import azure.functions as func
from string import ascii_lowercase

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    let_list=list()
    for i in range(5):
        let_list.append(random.choice(ascii_lowercase))
    return "".join(let_list)
