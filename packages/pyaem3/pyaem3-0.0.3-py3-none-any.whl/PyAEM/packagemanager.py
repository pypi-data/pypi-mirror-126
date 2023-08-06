from . import handlers
from . import httprequest as bag
from . import result as res


class PackageManager(object):

    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.handlers = {
            401: handlers.auth_fail,
            405: handlers.method_not_allowed
        }

    def update_package(self, group_name, package_name, package_version, **kwargs):
        def _handler_ok_update(response):
            message = 'Package updated'
            result = res.PyAemResult(response)
            result.success(message)
            return result

        _handlers = {
            200: _handler_ok_update
        }

        params = {
            'groupName': group_name,
            'packageName': package_name,
            'version': package_version,
            'path': '/etc/packages/{0}/{1}-{2}.zip'.format(group_name, package_name, package_version),
            '_charset_': 'utf-8'
        }

        method = 'get'
        url = '{0}/crx/packmgr/update.jsp'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def download_package(self, group_name, package_name, package_version, file_path, **kwargs):
        def _handler_ok_download(response, **org_kwargs):
            message = '{0} downloaded'.format(org_kwargs['file'])
            result = res.PyAemResult(response)
            result.success(message)
            return result

        _handlers = {
            200: _handler_ok_download
        }

        opts = {
            'file': '{0}/{1}-{2}.zip'.format(file_path, package_name, package_version)
        }

        url = '{0}/etc/packages/{1}/{2}-{3}.zip'.format(self.url, group_name, package_name, package_version)
        params = kwargs
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = dict(self.kwargs.items() | opts.items())

        return bag.download_file(url, params, _handlers, **opts)
