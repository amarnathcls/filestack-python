from filestack import __version__

ACCEPTED_SECURITY_TYPES = {'expiry': int, 'call': list,
                           'handle': str, 'url': str,
                           'maxSize': int, 'minSize': int,
                           'path': str, 'container': str}

API_URL = 'https://www.filestackapi.com/api'
CDN_URL = 'https://cdn.filestackcontent.com'
PROCESS_URL = 'https://process.filestackapi.com'

MULTIPART_START_URL = 'https://upload.filestackapi.com/multipart/start'

HEADERS = {
    'User-Agent': 'filestack-python {}'.format(__version__),
    'Filestack-Source': 'Python-{}'.format(__version__)
}

DEFAULT_CHUNK_SIZE = 5 * 1024 ** 2
DEFAULT_UPLOAD_MIMETYPE = 'application/octet-stream'

STORE_PATH = 'store'
FILE_PATH = 'file'
METADATA_PATH = 'metadata'
