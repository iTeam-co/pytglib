from pytglib.api.functions import AddProxy, RemoveProxy, PingProxy, EnableProxy, DisableProxy, GetProxies, GetProxyLink
from pytglib.api.types import Proxies, Proxy, ProxyTypeHttp, ProxyTypeMtproto, ProxyTypeSocks5, Ok, Seconds, Text


class ProxyManager:
    def __init__(self, client):
        self.client = client
        self.send = client.send
        self.execute = client.execute

    def add_http_proxy(self, server, port, username=None, password=None, http_only=True, enable=False):
        """
            Adds a proxy server for network requests.
            Can be called before authorization

            Args:
                server (:obj:`str`):
                    Proxy server IP address
                port (:obj:`int`):
                    Proxy server port
                username (:obj:`str`):
                    Username for logging in; may be empty
                password (:obj:`str`):
                    Password for logging in; may be empty
                http_only (:obj:`bool`):
                    Pass true, if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method
                enable (:obj:`bool`):
                    True, if the proxy should be enabled

            Returns:
                Proxy
            """
        res = self.send(AddProxy(server, port, enable, ProxyTypeHttp(username, password, http_only)))
        res.wait()
        return res.update  # type: Proxy

    def add_socks5_proxy(self, server, port, username=None, password=None, enable=False):
        """
            Adds a proxy server for network requests.
            Can be called before authorization

            Args:
                server (:obj:`str`):
                    Proxy server IP address
                port (:obj:`int`):
                    Proxy server port
                username (:obj:`str`):
                    Username for logging in; may be empty
                password (:obj:`str`):
                    Password for logging in; may be empty
                enable (:obj:`bool`):
                    True, if the proxy should be enabled

            Returns:
                Proxy
            """
        res = self.send(AddProxy(server, port, enable, ProxyTypeSocks5(username, password)))
        res.wait()
        return res.update  # type: Proxy

    def add_mtproto_proxy(self, server, port, secret, enable=False):
        """
            Adds a proxy server for network requests.
            Can be called before authorization

            Args:
                server (:obj:`str`):
                    Proxy server IP address
                port (:obj:`int`):
                    Proxy server port
                secret (:obj:`str`):
                    The proxy's secret in hexadecimal encoding
                enable (:obj:`bool`):
                    True, if the proxy should be enabled

            Returns:
                Proxy
            """
        res = self.send(AddProxy(server, port, enable, ProxyTypeMtproto(secret)))
        res.wait()
        return res.update  # type: Proxy

    def remove_proxy(self, proxy_id):
        """
            Removes a proxy server.
            Can be called before authorization

            Args:
                proxy_id (:obj:`int`):
                    Proxy identifier

            Returns:
                bool
        """
        res = self.send(RemoveProxy(proxy_id))
        res.wait()
        return isinstance(res.update, Ok)

    def ping_proxy(self, proxy_id):
        """
            Computes time needed to receive a response from a Telegram server through a proxy.
            Can be called before authorization

            Args:
                proxy_id (:obj:`int`):
                    Proxy identifier
                    Use 0 to ping a Telegram server without a proxy

            Returns:
                float
        """
        res = self.send(PingProxy(proxy_id))
        res.wait()
        ping = res.update  # type: Seconds
        return ping.seconds

    def enable_proxy(self, proxy_id):
        """
            Enables a proxy. Only one proxy can be enabled at a time.
            Can be called before authorization

            Args:
                proxy_id (:obj:`int`):
                    Proxy identifier

            Returns:
                bool
        """
        res = self.send(EnableProxy(proxy_id))
        res.wait()
        return isinstance(res.update, Ok)

    def disable_proxy(self):
        """
            Disables the currently enabled proxy.
            Can be called before authorization

            Returns:
                bool
        """
        res = self.send(DisableProxy())
        res.wait()
        return isinstance(res.update, Ok)

    def get_proxy_link(self, proxy_id):
        """
        Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies.
        Can be called before authorization

        Args:
            proxy_id (:obj:`int`):
                Proxy identifier

            Returns:
                str
        """
        res = self.send(GetProxyLink(proxy_id))
        res.wait()
        link = res.update  # type: Text
        return link.text

    def get_proxies(self):
        """
            Returns list of proxies that are currently set up.
            Can be called before authorization

            Returns:
                List of Proxy
        """
        res = self.send(GetProxies())
        res.wait()
        proxies = res.update  # type: Proxies
        return proxies.proxies










