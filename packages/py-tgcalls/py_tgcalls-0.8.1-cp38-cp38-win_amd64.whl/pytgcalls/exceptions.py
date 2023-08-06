class NodeJSNotInstalled(Exception):
    def __init__(
        self,
        version_needed: str,
    ):
        super().__init__(
            f'Please install node ({version_needed}+)',
        )


class TooOldNodeJSVersion(Exception):
    def __init__(
        self,
        version_needed: str,
        node_version: str,
    ):
        super().__init__(
            f'Needed node {version_needed}+, '
            'actually installed is '
            f'{node_version}',
        )


class TooOldPyrogramVersion(Exception):
    def __init__(
            self,
            version_needed: str,
            pyrogram_version: str,
    ):
        super().__init__(
            f'Needed pyrogram {version_needed}+, '
            'actually installed is '
            f'{pyrogram_version}',
        )


class TooOldTelethonVersion(Exception):
    def __init__(
        self,
        version_needed: str,
        telethon_version: str,
    ):
        super().__init__(
            f'Needed telethon {version_needed}+, '
            'actually installed is '
            f'{telethon_version}',
        )


class InvalidStreamMode(Exception):
    def __init__(self):
        super().__init__(
            'Invalid stream mode',
        )


class NoMtProtoClientSet(Exception):
    def __init__(self):
        super().__init__(
            'No MtProto client set',
        )


class NodeJSNotRunning(Exception):
    def __init__(self):
        super().__init__(
            'Node.js not running',
        )


class NoActiveGroupCall(Exception):
    def __init__(self):
        super().__init__(
            'No active group call',
        )


class PyTgCallsAlreadyRunning(Exception):
    def __init__(self):
        super().__init__(
            'PyTgCalls client is already running',
        )


class TooManyCustomApiDecorators(Exception):
    def __init__(self):
        super().__init__(
            'Too Many Custom Api Decorators',
        )


class GroupCallNotFound(Exception):
    def __init__(
        self,
        chat_id: int,
    ):
        super().__init__(
            f'Group call not found with the chat id {chat_id}',
        )


class InvalidMtProtoClient(Exception):
    def __init__(self):
        super().__init__(
            'Invalid MtProto Client',
        )


class NoVideoSourceFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'No video source found on {path}',
        )


class InvalidVideoProportion(Exception):
    def __init__(self, message: str):
        super().__init__(
            message,
        )


class NoAudioSourceFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'No audio source found on {path}',
        )


class FFmpegNotInstalled(Exception):
    def __init__(self, path: str):
        super().__init__(
            'FFmpeg ins\'t installed on your server',
        )
