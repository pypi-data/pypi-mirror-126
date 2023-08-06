import asyncio

from ...exceptions import NodeJSNotRunning
from ...exceptions import NoMtProtoClientSet
from ...scaffold import Scaffold


class PauseStream(Scaffold):
    async def pause_stream(
        self,
        chat_id: int,
    ):
        if self._app is not None:
            if self._wait_until_run is not None:
                async def internal_sender():
                    if not self._wait_until_run.done():
                        await self._wait_until_run
                    await self._binding.send({
                        'action': 'pause',
                        'chat_id': chat_id,
                    })
                active_call = self._call_holder.get_active_call(chat_id)
                asyncio.ensure_future(internal_sender())
                return active_call.status == 'playing'
            else:
                raise NodeJSNotRunning()
        else:
            raise NoMtProtoClientSet()
