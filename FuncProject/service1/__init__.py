import logging
import random
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    num=requests.get('https://serverlesspaul.azurewebsites.net/api/service2?code=9bcyqmQKp7EIc0jaW7gZZBHZNiiSpK01e3aytfL3jhSp/IfkiVRn1A==').text
    let=requests.get('https://serverlesspaul.azurewebsites.net/api/service3?code=G4cn6gVNC1/rMv/9ZVuKrnWsmho5zqdKTz03XraIk51aO0aK9zFRFw==').text
    username=""
    for i in range(5):
        username += let[i]
        username += num[i]
    
    key = "xK02sprQ1EFRd00KVRAfgH1aAwqk0qHOFoUuZArj2O7Fnvja7p08r3VU6TRimpCCGPteOPqAslGHADDQrtiiyw=="
    endpoint = "https://paulcosmos94.documents.azure.com:443/"

    client=CosmosClient(endpoint, key)

    database_name="Usernames"
    database=client.create_database_if_not_exists(id=database_name)
    
    container_name="UsernameContainer"
    container=database.create_container_if_not_exists(
            id=container_name,
            partition_key=PartitionKey(path="/username")
    )

    username_to_add={
            "id": username
    }
    container.create_item(body=username_to_add)
      
    return username 
