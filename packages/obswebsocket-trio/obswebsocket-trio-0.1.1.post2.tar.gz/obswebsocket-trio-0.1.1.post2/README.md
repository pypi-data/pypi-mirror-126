![PyPI - License](https://img.shields.io/pypi/l/obswebsocket_trio)
![PyPI](https://img.shields.io/pypi/v/obswebsocket_trio)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/obswebsocket_trio)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mkdryden/obs-websocket-py-trio)

# obs-websocket-py
Python library to communicate with an [obs-websocket](https://github.com/Palakis/obs-websocket) server.
This is a fork of [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py) using the trio async library.

_Licensed under the MIT License_

## Project pages

GitHub project: https://github.com/mkdryden/obs-websocket-py-trio

PyPI package: https://pypi.org/project/obs-websocket-py-trio/

## Installation

Just run `pip install obswebsocket-trio` in your Python venv or directly on your system.

For development, `poetry install` from the source directory will generate a venv with all the dependencies

For manual install, git clone the github repo and copy the directory **obswebsocket_trio** in your python project root.


## Usage

See python scripts in the [samples](https://github.com/mkdryden/obs-websocket-py-trio/tree/master/samples) directory.

The big change from the original obs-websocket-py is the use of the trio async library.
This means that most methods of `ObsWS` must be called with `await` from inside a trio event loop.
A new convenience function `open_obs_websocket` acts as an asynchronous context manager yielding an `ObsWs` instance,
automatically connecting and starting a trio `Nursery` to manage the background tasks required for the websocket
connection and to handle events from OBS.


A simple example to print the names of all scenes:
```python
from obswebsocket_trio import open_obs_websocket, requests
import trio

async def main(host: str = 'localhost', port: int = 4444, password: str = 'secret'):
    async with open_obs_websocket(host, port, password) as ws:
        scenes = await ws.call(requests.GetSceneList())
        for scene in scenes.getScenes():
            print(scene['name'])

trio.run(main)
```

Or take a look at the documentation below:

_Output of `pydoc obswebsocket.core.ObsWS`:_

```
Help on class ObsWS in obswebsocket.core:

obswebsocket.core.ObsWS = class ObsWS(trio.abc.AsyncResource)
 |  obswebsocket.core.ObsWS(nursery: trio.Nursery, host='localhost', port=4444, password='')
 |
 |  Core class for using obs-websocket-py
 |
 |  Simple usage:
 |      >>> import obswebsocket_trio, obswebsocket_trio.requests as obsrequests
 |      >>> async with obswebsocket_trio.open_obs_websocket("localhost", 4444, "secret") as client:
 |      >>>     await client.call(obsrequests.GetVersion()).getObsWebsocketVersion()
 |      '4.1.0'
 |
 |  For advanced usage, including events callback, see the 'samples' directory.
 |
 |  Method resolution order:
 |      ObsWS
 |      trio.abc.AsyncResource
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, nursery: trio.Nursery, host='localhost', port=4444, password='')
 |      Construct a new obsws wrapper
 |
 |      :param nursery: A trio Nursery to run background tasks
 |      :param host: Hostname to connect to
 |      :param port: TCP Port to connect to (Default is 4444)
 |      :param password: Password for the websocket server (Leave this field
 |          empty if no auth enabled on the server)
 |
 |  async aclose(self)
 |      Close this resource, possibly blocking.
 |
 |      IMPORTANT: This method may block in order to perform a "graceful"
 |      shutdown. But, if this fails, then it still *must* close any
 |      underlying resources before returning. An error from this method
 |      indicates a failure to achieve grace, *not* a failure to close the
 |      connection.
 |
 |      For example, suppose we call :meth:`aclose` on a TLS-encrypted
 |      connection. This requires sending a "goodbye" message; but if the peer
 |      has become non-responsive, then our attempt to send this message might
 |      block forever, and eventually time out and be cancelled. In this case
 |      the :meth:`aclose` method on :class:`~trio.SSLStream` will
 |      immediately close the underlying transport stream using
 |      :func:`trio.aclose_forcefully` before raising :exc:`~trio.Cancelled`.
 |
 |      If the resource is already closed, then this method should silently
 |      succeed.
 |
 |      Once this method completes, any other pending or future operations on
 |      this resource should generally raise :exc:`~trio.ClosedResourceError`,
 |      unless there's a good reason to do otherwise.
 |
 |      See also: :func:`trio.aclose_forcefully`.
 |
 |  async call(self, obj) -> obswebsocket.base_classes.Baserequests
 |      Make a call to the OBS server through the Websocket.
 |
 |      :param obj: Request (class from obswebsocket.requests module) to send
 |          to the server.
 |      :return: Request object populated with response data.
 |
 |  async connect(self, autoreconnect: bool = True)
 |      Connect to the websocket server
 |      :param autoreconnect: If True, tries to reconnect every 2 seconds if disconnected.
 |
 |      :return: Nothing
 |
 |  async disconnect(self)
 |      Disconnect from websocket server
 |
 |      :return: Nothing
 |
 |  async reconnect(self)
 |      Restart the connection to the websocket server
 |
 |      :return: Nothing
 |
 |  register(self, func, event=None)
 |      Register a new hook in the websocket client
 |
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) to trigger
 |          the hook on. Default is None, which means trigger on all events.
 |      :return: Nothing
 |
 |  async send(self, data: dict) -> dict
 |      Make a raw json call to the OBS server through the Websocket.
 |
 |      :param data: Request (python dict) to send to the server. Do not
 |          include field "message-id".
 |      :return: Response (python dict) from the server.
 |
 |  unregister(self, func, event=None)
 |      Unregister a new hook in the websocket client
 |
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) which
 |          triggered the hook on. Default is None, which means unregister this
 |          function for all events.
 |      :return: Nothing
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  build_event(data)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from trio.abc.AsyncResource:
 |
 |  async __aenter__(self)
 |
 |  async __aexit__(self, *args)
```

