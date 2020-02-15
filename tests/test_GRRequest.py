import pytest
import time
import asyncio
import aiohttp

from pygti.auth import Auth
from pygti.gti import *
from pygti.schemas import *
from tests.payloadsForTesting import payloadsGRRequest


@pytest.mark.schema
def test_Schema_GRRequest():
    for payload in payloadsGRRequest:
        gr = GRRequest(payload)
    assert True


@pytest.mark.asyncio
@pytest.mark.usefixtures("enterCredentials")
async def test_Asyncio_GRRequest(enterCredentials):
    async with aiohttp.ClientSession() as session:
        gti_user = enterCredentials[0]
        gti_pass = enterCredentials[1]
        auth = Auth(session, gti_user, gti_pass)
        gti = GTI(auth)

        for payload in payloadsGRRequest:
            gr = await gti.getRoute(payload)
            time.sleep(1)

    assert True
