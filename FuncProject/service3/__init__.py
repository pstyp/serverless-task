import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    let_list=list()
    for i in range(4):
        let_list.append(random.choice(string.ascii_lowercase))
    return "".join(let_list)

