from . import FB_2_1
from . import FB_2_2
from . import FB_2_0

fb_modules = {
    '2.1': FB_2_1,
    '2.2': FB_2_2,
    '2.0': FB_2_0,
}


DEFAULT_TIMEOUT = 15.0
DEFAULT_RETRIES = 5


def Client(target, version="2.2", id_token=None, private_key_file=None, private_key_password=None,
           username=None, client_id=None, key_id=None, issuer=None, api_token=None,
           retries=DEFAULT_RETRIES, timeout=DEFAULT_TIMEOUT, ssl_cert=None, user_agent=None):
    """
    Initialize a FlashBlade Client.

    Keyword args:
        target (str, required):
            The target array's IP or hostname.
        version (str, optional):
            REST API version to use. Defaults to the most recent version.
        id_token (str, optional):
            The security token that represents the identity of the party on
            behalf of whom the request is being made, issued by an enabled
            API client on the array. Overrides given private key.
        private_key_file (str, optional):
            The path of the private key to use. Defaults to None.
        private_key_password (str, optional):
            The password of the private key. Defaults to None.
        username (str, optional):
            Username of the user the token should be issued for. This must
            be a valid user in the system.
        client_id (str, optional):
            ID of API client that issued the identity token.
        key_id (str, optional):
            Key ID of API client that issued the identity token.
        issuer (str, optional):
            API client's trusted identity issuer on the array.
        api_token (str, optional):
                API token for the user.
        retries (int, optional):
            The number of times to retry an API call if it fails for a
            non-blocking reason. Defaults to 5.
        timeout (float or (float, float), optional):
            The timeout duration in seconds, either in total time or
            (connect and read) times. Defaults to 15.0 total.
        ssl_cert (str, optional):
            SSL certificate to use. Defaults to None.
        user_agent (str, optional):
            User-Agent request header to use.

    Raises:
        PureError: If it could not create an ID or access token
    """
    fb_module = version_to_module(version)
    client = fb_module.Client(target=target, id_token=id_token, private_key_file=private_key_file,
                              private_key_password=private_key_password, username=username, client_id=client_id,
                              key_id=key_id, issuer=issuer, api_token=api_token, retries=retries, timeout=timeout,
                              ssl_cert=ssl_cert, user_agent=user_agent)
    return client


def version_to_module(version):
    fb_module = fb_modules.get(version, None)
    if fb_module is None:
        msg = "version {} not supported".format(version)
        raise ValueError(msg.format(version))
    return fb_module
