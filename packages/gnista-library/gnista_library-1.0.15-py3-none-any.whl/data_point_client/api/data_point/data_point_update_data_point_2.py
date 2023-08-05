from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.data_point_request import DataPointRequest
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    data_point_id: str,
    tenant_name: Optional[str],
    json_body: DataPointRequest,
) -> Dict[str, Any]:
    url = "{}/DataPoint/tenant/{tenantName}/{dataPointId}".format(
        client.base_url, dataPointId=data_point_id, tenantName=tenant_name
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[None, ProblemDetails]]:
    if response.status_code == 202:
        response_202 = None

        return response_202
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[None, ProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    data_point_id: str,
    tenant_name: Optional[str],
    json_body: DataPointRequest,
) -> Response[Union[None, ProblemDetails]]:
    kwargs = _get_kwargs(
        client=client,
        data_point_id=data_point_id,
        tenant_name=tenant_name,
        json_body=json_body,
    )

    response = httpx.patch(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    data_point_id: str,
    tenant_name: Optional[str],
    json_body: DataPointRequest,
) -> Optional[Union[None, ProblemDetails]]:
    """ """

    return sync_detailed(
        client=client,
        data_point_id=data_point_id,
        tenant_name=tenant_name,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    data_point_id: str,
    tenant_name: Optional[str],
    json_body: DataPointRequest,
) -> Response[Union[None, ProblemDetails]]:
    kwargs = _get_kwargs(
        client=client,
        data_point_id=data_point_id,
        tenant_name=tenant_name,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    data_point_id: str,
    tenant_name: Optional[str],
    json_body: DataPointRequest,
) -> Optional[Union[None, ProblemDetails]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            data_point_id=data_point_id,
            tenant_name=tenant_name,
            json_body=json_body,
        )
    ).parsed
