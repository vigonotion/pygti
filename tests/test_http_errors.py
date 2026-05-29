import pytest
import pytest_asyncio
from aiohttp import ClientSession
from aioresponses import aioresponses

from pygti import (
    GTIBadRequestError,
    GTIError,
    GTIForbiddenError,
    GTIHTTPError,
    GTIInternalServerError,
    GTIServiceUnavailableError,
    GTITooManyRequestsError,
    GTIUnauthorizedError,
)
from pygti.auth import Auth
from pygti.models import InitRequest

_INIT_URL = "https://gti.geofox.de/gti/public/init"


@pytest_asyncio.fixture
async def auth():
    async with ClientSession() as session:
        yield Auth(session, "user", "pass")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "status,exc_type",
    [
        (400, GTIBadRequestError),
        (401, GTIUnauthorizedError),
        (403, GTIForbiddenError),
        (429, GTITooManyRequestsError),
        (500, GTIInternalServerError),
        (503, GTIServiceUnavailableError),
    ],
)
async def test_http_error_raises_correct_exception(
    auth: Auth, status: int, exc_type: type[GTIHTTPError]
) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=status)
        with pytest.raises(exc_type) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.status_code == status
        assert isinstance(exc_info.value, GTIHTTPError)
        assert isinstance(exc_info.value, GTIError)


@pytest.mark.asyncio
async def test_http_error_captures_dev_info(auth: Auth) -> None:
    with aioresponses() as m:
        m.post(
            _INIT_URL,
            status=500,
            payload={"errorDevInfo": "NullPointerException at line 42"},
        )
        with pytest.raises(GTIInternalServerError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.error_dev_info == "NullPointerException at line 42"


@pytest.mark.asyncio
async def test_http_error_no_body(auth: Auth) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=401, body=b"")
        with pytest.raises(GTIUnauthorizedError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.error_dev_info is None


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [404, 408, 422, 502, 504])
async def test_unmapped_http_error_raises_gti_http_error(
    auth: Auth, status: int
) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=status)
        with pytest.raises(GTIHTTPError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.status_code == status
        assert type(exc_info.value) is GTIHTTPError


@pytest.mark.asyncio
async def test_http_error_str_contains_status_code(auth: Auth) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=500)
        with pytest.raises(GTIInternalServerError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert "500" in str(exc_info.value)


@pytest.mark.asyncio
async def test_http_error_captures_message_fallback(auth: Auth) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=503, payload={"message": "Backend down"})
        with pytest.raises(GTIServiceUnavailableError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.error_dev_info == "Backend down"


@pytest.mark.asyncio
async def test_http_error_empty_string_error_dev_info_not_overridden(
    auth: Auth,
) -> None:
    with aioresponses() as m:
        m.post(
            _INIT_URL,
            status=400,
            payload={"errorDevInfo": "", "message": "should not appear"},
        )
        with pytest.raises(GTIBadRequestError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.error_dev_info == ""


@pytest.mark.asyncio
async def test_http_error_non_dict_json_body(auth: Auth) -> None:
    with aioresponses() as m:
        m.post(_INIT_URL, status=500, payload=["error"])
        with pytest.raises(GTIInternalServerError) as exc_info:
            await auth.request("post", "/gti/public/init", InitRequest())
        assert exc_info.value.error_dev_info is None


@pytest.mark.asyncio
async def test_ok_response_does_not_raise(auth: Auth) -> None:
    payload = {
        "returnCode": "OK",
        "beginOfService": "2024-01-01",
        "endOfService": "2024-12-31",
        "id": "1",
        "dataId": "d1",
        "buildDate": "2024-01-01",
        "buildTime": "00:00",
        "buildText": "test",
    }
    with aioresponses() as m:
        m.post(_INIT_URL, status=200, payload=payload)
        result = await auth.request("post", "/gti/public/init", InitRequest())
    assert result["returnCode"] == "OK"
