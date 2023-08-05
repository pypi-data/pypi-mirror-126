from http import HTTPStatus
from typing import Union, Dict, Optional

import aiohttp

from .peas import AsyncPeaClient
from .mixin import AsyncToSyncMixin
from ..helper import if_alive, error_msg_from
from ..models.id import DaemonID, daemonize
from ..models.enums import UpdateOperation


class AsyncPodClient(AsyncPeaClient):
    """Async Client to create/update/delete Peods on remote JinaD"""

    _kind = 'pod'
    _endpoint = '/pods'

    @if_alive
    async def update(
        self,
        id: Union[str, 'DaemonID'],
        dump_path: Optional[str] = None,
        *,
        uses_with: Optional[Dict] = None,
    ) -> str:
        """Update a Flow on remote JinaD (only rolling_update supported)

        :param id: flow id
        :param dump_path: path of dump from other flow
        :param uses_with: the uses_with to update the Executor
        :return: flow id
        """
        if dump_path is not None:
            if uses_with is not None:
                uses_with['dump_path'] = dump_path
            else:
                uses_with = {'dump_path': dump_path}
        async with aiohttp.request(
            method='PUT',
            url=f'{self.store_api}/{daemonize(id, self._kind)}',
            params={
                'kind': UpdateOperation.ROLLING_UPDATE.value,
            },
            json={'uses_with': uses_with},
            timeout=self.timeout,
        ) as response:
            response_json = await response.json()
            if response.status != HTTPStatus.OK:
                error_msg = error_msg_from(response_json)
                self._logger.error(
                    f'{self._kind.title()} update failed as: {error_msg}'
                )
                return error_msg
            return response_json


class PodClient(AsyncToSyncMixin, AsyncPodClient):
    """Client to create/update/delete Pods on remote JinaD"""
