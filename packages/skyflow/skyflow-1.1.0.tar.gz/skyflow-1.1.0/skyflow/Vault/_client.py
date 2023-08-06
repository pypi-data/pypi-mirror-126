import types
import requests
from ._insert import getInsertRequestBody, processResponse, convertResponse
from ._config import Configuration
from ._config import InsertOptions, ConnectionConfig
from ._connection import createRequest
from ._detokenize import sendDetokenizeRequests, createDetokenizeResponseBody
from ._getById import sendGetByIdRequests, createGetByIdResponseBody
import asyncio
from skyflow.Errors._skyflowErrors import SkyflowError, SkyflowErrorCodes, SkyflowErrorMessages   

class Client:
    def __init__(self, config: Configuration):
        if not isinstance(config.vaultID, str):
            raise SkyflowError(SkyflowErrorCodes.INVALID_INPUT, SkyflowErrorMessages.VAULT_ID_INVALID_TYPE.value%(str(type(config.vaultID))))
        if not isinstance(config.vaultURL, str):
            raise SkyflowError(SkyflowErrorCodes.INVALID_INPUT, SkyflowErrorMessages.VAULT_URL_INVALID_TYPE.value%(str(type(config.vaultURL))))

        if not isinstance(config.tokenProvider, types.FunctionType):
            raise SkyflowError(SkyflowErrorCodes.INVALID_INPUT, SkyflowErrorMessages.TOKEN_PROVIDER_ERROR.value%(str(type(config.tokenProvider))))

        self.vaultID = config.vaultID
        self.vaultURL = config.vaultURL.rstrip('/')
        self.tokenProvider = config.tokenProvider

    def insert(self, records: dict, options: InsertOptions = InsertOptions()):
        jsonBody = getInsertRequestBody(records, options.tokens)
        requestURL = self.vaultURL + "/v1/vaults/" + self.vaultID
        token = self.tokenProvider()
        headers = {
            "Authorization": "Bearer " + token
        }
        response = requests.post(requestURL, data=jsonBody, headers=headers)
        processedResponse = processResponse(response)
        return convertResponse(records, processedResponse, options.tokens)

    def invokeConnection(self, config: ConnectionConfig):
        session = requests.Session()
        token = self.tokenProvider()
        request = createRequest(config)
        request.headers['X-Skyflow-Authorization'] = token
        response = session.send(request)
        session.close()
        return processResponse(response)

    def detokenize(self, records):
        token = self.tokenProvider()
        url = self.vaultURL + "/v1/vaults/" + self.vaultID + "/detokenize"
        responses = asyncio.run(sendDetokenizeRequests(records, url, token))
        result, partial = createDetokenizeResponseBody(responses)
        if partial:
            raise SkyflowError(SkyflowErrorCodes.PARTIAL_SUCCESS ,SkyflowErrorMessages.PARTIAL_SUCCESS, result)
        else:
            return result
    
    def getById(self, records):
        token = self.tokenProvider()
        url = self.vaultURL + "/v1/vaults/" + self.vaultID
        responses = asyncio.run(sendGetByIdRequests(records, url, token))
        result, partial = createGetByIdResponseBody(responses)
        if partial:
            raise SkyflowError(SkyflowErrorCodes.PARTIAL_SUCCESS ,SkyflowErrorMessages.PARTIAL_SUCCESS, result)
        else:
            return result
        


