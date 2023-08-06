import re

from bs4 import BeautifulSoup

from . import handlers
from . import httprequest as bag
from . import result as res

HEX_MASSAGE = [(re.compile('&#x([^;]+);'), lambda m: '&#%d;' % int(m.group(1), 16))]


class ContentRepo(object):

    def __init__(self, url, **kwargs):

        self.url = url
        self.kwargs = kwargs
        self.handlers = {
            401: handlers.auth_fail,
            405: handlers.method_not_allowed
        }

    def create_path(self, path, **kwargs):

        def _handler_exist(response):
            message = 'Path {0} already exists'.format(path)
            result = res.PyAemResult(response)
            result.warning(message)
            return result

        def _handler_ok(response):
            message = 'Path {0} created'.format(path)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        _handlers = {
            200: _handler_exist,
            201: _handler_ok
        }

        method = 'post'
        url = '{0}/{1}'.format(self.url, path.lstrip('/'))
        params = kwargs
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def delete_path(self, path, **kwargs):

        def _handler_ok(response):
            message = 'Path {0} deleted'.format(path)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_not_found(response):
            message = 'Path {0} not found'.format(path)
            result = res.PyAemResult(response)
            result.warning(message)
            return result

        _handlers = {
            204: _handler_ok,
            404: _handler_not_found
        }

        method = 'delete'
        url = '{0}/{1}'.format(self.url, path.lstrip('/'))
        params = kwargs
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def activate_path(self, path, **kwargs):

        def _handler_ok(response):

            soup = BeautifulSoup(response['body'],
                                 convertEntities=BeautifulSoup.HTML_ENTITIES,
                                 markupMassage=HEX_MASSAGE
                                 )
            errors = soup.findAll(attrs={'class': 'error'})

            result = res.PyAemResult(response)
            if len(errors) == 0:
                message = 'Path {0} activated'.format(path)
                result.success(message)
            else:
                message = errors[0].string
                result.failure(message)
            return result

        params = {
            'cmd': 'activate',
            'path': path
        }

        _handlers = {
            200: _handler_ok
        }

        method = 'post'
        url = '{0}/etc/replication/treeactivation.html'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def does_user_exist(self, user_path, user_name, **kwargs):

        node_path = '{0}/{1}'.format(user_path.rstrip('/'), user_name.lstrip('/'))
        return self._does_node_exist(node_path, 'User', **kwargs)

    def create_user(self, user_path, user_name, password, **kwargs):

        def _handler_ok(response):

            message = 'User {0}/{1} created'.format(user_path.rstrip('/'), user_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_exist_or_error(response):

            message = ""
            soup = BeautifulSoup(response['body'],
                                 convertEntities=BeautifulSoup.HTML_ENTITIES,
                                 markupMassage=HEX_MASSAGE
                                 )
            message_elem = soup.find('div', {'id': 'Message'})
            if message_elem is not None:
                message = message_elem.contents[0]

            exist_message = ('org.apache.jackrabbit.api.security.user.AuthorizableExistsException: ' +
                             'User or Group for \'{0}\' already exists'.format(user_name))

            result = res.PyAemResult(response)
            if message == exist_message:
                result.warning('User {0}/{1} already exists'.format(user_path.rstrip('/'), user_name))
            else:
                result.failure(message)
            return result

        params = {
            'createUser': '',
            'authorizableId': user_name,
            'rep:password': password,
            'intermediatePath': user_path
        }

        _handlers = {
            201: _handler_ok,
            500: _handler_exist_or_error
        }

        method = 'post'
        url = '{0}/libs/granite/security/post/authorizables'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def add_user_to_group(self, user_name, group_path, group_name, **kwargs):

        def _handler_ok(response):
            message = 'User {0} added to group {1}/{2}'.format(user_name, group_path.rstrip('/'), group_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        params = {
            'addMembers': user_name
        }

        _handlers = {
            200: _handler_ok
        }

        method = 'post'
        url = '{0}/{1}/{2}.rw.html'.format(self.url, group_path.strip('/'), group_name)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def does_group_exist(self, group_path, group_name, **kwargs):

        node_path = '{0}/{1}'.format(group_path.rstrip('/'), group_name.lstrip('/'))
        return self._does_node_exist(node_path, 'Group', **kwargs)

    def create_group(self, group_path, group_name, **kwargs):

        def _handler_ok(response):

            message = 'Group {0}/{1} created'.format(group_path.rstrip('/'), group_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_exist_or_error(response):

            message = ""
            soup = BeautifulSoup(response['body'],
                                 convertEntities=BeautifulSoup.HTML_ENTITIES,
                                 markupMassage=HEX_MASSAGE
                                 )
            message_elem = soup.find('div', {'id': 'Message'})
            if message_elem is not None:
                message = message_elem.contents[0]

            exist_message = ('org.apache.jackrabbit.api.security.user.AuthorizableExistsException: ' +
                             'User or Group for \'{0}\' already exists'.format(group_name))

            result = res.PyAemResult(response)
            if message == exist_message:
                result.warning('Group {0}/{1} already exists'.format(group_path.rstrip('/'), group_name))
            else:
                result.failure(message)
            return result

        params = {
            'createGroup': '',
            'authorizableId': group_name,
            'profile/givenName': group_name,
            'intermediatePath': group_path
        }

        _handlers = {
            201: _handler_ok,
            500: _handler_exist_or_error
        }

        method = 'post'
        url = '{0}/libs/granite/security/post/authorizables'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def change_password(self, user_path, user_name, old_password, new_password, **kwargs):

        def _handler_ok(response):
            message = 'User {0}/{1} password changed'.format(user_path.rstrip('/'), user_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        params = {
            ':currentPassword': old_password,
            'rep:password': new_password
        }

        _handlers = {
            200: _handler_ok
        }

        method = 'post'
        url = '{0}/{1}/{2}.rw.html'.format(self.url, user_path.strip('/'), user_name)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def set_permission(self, user_or_group_name, path, permissions, **kwargs):

        def _handler_ok(response):
            message = 'Permissions {0} set on path {1} for user/group {2}'.format(permissions, path, user_or_group_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_not_found(response):
            soup = BeautifulSoup(response['body'],
                                 convertEntities=BeautifulSoup.HTML_ENTITIES,
                                 markupMassage=HEX_MASSAGE
                                 )
            message_elem = soup.find('div', {'id': 'Message'})
            message = message_elem.contents[0]

            result = res.PyAemResult(response)
            result.failure(message)
            return result

        params = {
            'authorizableId': user_or_group_name,
            'changelog': 'path:{0},{1}'.format(path, permissions)
        }

        _handlers = {
            200: _handler_ok,
            404: _handler_not_found
        }

        method = 'post'
        url = '{0}/.cqactions.html'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def create_agent(self, agent_name, agent_type, dest_username, dest_password, dest_url, run_mode, **kwargs):

        def _handler_ok_created(response):

            message = '{0} agent {1} created'.format(run_mode, agent_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_ok_updated(response):

            message = '{0} agent {1} updated'.format(run_mode, agent_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        if agent_type == 'flush':
            params = {
                'jcr:content/cq:name': 'flush',
                'jcr:content/protocolHTTPHeaders': ['CQ-Action:{action}', 'CQ-Handle:{path}', 'CQ-Path:{path}'],
                'jcr:content/protocolHTTPHeaders@TypeHint': 'String[]',
                'jcr:content/protocolHTTPMethod': 'GET',
                'jcr:content/serializationType': 'flush',
                'jcr:content/noVersioning': 'true',
                'jcr:content/jcr:mixinTypes': 'cq:ReplicationStatus',
                'jcr:content/triggerReceive': 'true',
                'jcr:content/triggerSpecific': 'true',
                'jcr:content/transportUri': '{0}/dispatcher/invalidate.cache'.format(dest_url.rstrip('/'))
            }
        else:
            params = {
                'jcr:content/serializationType': 'durbo',
                'jcr:content/transportUri': '{0}/bin/receive?sling:authRequestLogin=1'.format(dest_url.rstrip('/'))
            }

        params['jcr:primaryType'] = 'cq:Page'
        params['jcr:content/sling:resourceType'] = '/libs/cq/replication/components/agent'
        params['jcr:content/cq:template'] = '/libs/cq/replication/templates/agent'
        params['jcr:content/enabled'] = 'true'

        if dest_username is not None:
            params['jcr:content/transportUser'] = dest_username
        if dest_password is not None:
            params['jcr:content/transportPassword'] = dest_password

        _handlers = {
            200: _handler_ok_updated,
            201: _handler_ok_created
        }

        method = 'post'
        url = '{0}/etc/replication/agents.{1}/{2}'.format(self.url, run_mode, agent_name)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def delete_agent(self, agent_name, run_mode, **kwargs):

        def _handler_ok(response):
            message = '{0} agent {1} deleted'.format(run_mode, agent_name)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_not_found(response):
            message = '{0} agent {1} not found'.format(run_mode, agent_name)
            result = res.PyAemResult(response)
            result.warning(message)
            return result

        params = {
        }

        _handlers = {
            204: _handler_ok,
            404: _handler_not_found
        }

        method = 'delete'
        url = '{0}/etc/replication/agents.{1}/{2}'.format(self.url, run_mode, agent_name)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def set_property(self, path, property_name, property_value, **kwargs):

        def _handler_ok(response):
            message = 'Set property {0}={1} on path {2}'.format(property_name, property_value, path)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        params = {
            property_name: property_value
        }

        _handlers = {
            200: _handler_ok,
            201: _handler_ok
        }

        method = 'post'
        url = '{0}/{1}'.format(self.url, path.lstrip('/'))
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def enable_workflow(self, workflow, glob, edit, node_type, run_mode, **kwargs):

        return self._set_workflow(workflow, glob, edit, True, node_type, run_mode, **kwargs)

    def disable_workflow(self, workflow, glob, edit, node_type, run_mode, **kwargs):

        return self._set_workflow(workflow, glob, edit, False, node_type, run_mode, **kwargs)

    def _does_node_exist(self, node_path, node_desc, **kwargs):

        def _handler_ok(response):
            message = '{0} {1} exists'.format(node_desc, node_path)
            result = res.PyAemResult(response)
            result.success(message)
            return result

        def _handler_not_found(response):
            message = '{0} {1} does not exist'.format(node_desc, node_path)
            result = res.PyAemResult(response)
            result.failure(message)
            return result

        _handlers = {
            200: _handler_ok,
            404: _handler_not_found
        }

        method = 'get'
        url = '{0}/{1}'.format(self.url, node_path.lstrip('/'))
        params = kwargs
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def _set_workflow(self, workflow, glob, edit, is_enabled, node_type, run_mode, **kwargs):

        def _handler_ok(response):
            message = 'Workflow {0} {1}'.format(workflow, 'enabled' if is_enabled else 'disabled')
            result = res.PyAemResult(response)
            result.success(message)
            return result

        params = {
            ':status': 'browser',
            '_charset_': 'utf-8',
            'condition': kwargs.get('condition', ''),
            'description': kwargs.get('description', ''),
            'edit': edit,
            'enabled': 'true' if is_enabled else 'false',
            'eventType': '16',
            'excludeList': kwargs.get('excludeList', ''),
            'glob': glob,
            'nodetype': node_type,
            'runModes': run_mode,
            'workflow': workflow
        }

        _handlers = {
            200: _handler_ok
        }

        method = 'post'
        url = '{0}/libs/cq/workflow/launcher'.format(self.url)
        params = dict(params.items() | kwargs.items())
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)

    def get_cluster_list(self, **kwargs):

        def _handler_ok(response):
            message = 'Cluster list retrieved'
            result = res.PyAemResult(response)
            result.success(message)
            return result

        _handlers = {
            200: _handler_ok
        }

        method = 'get'
        url = '{0}/libs/granite/cluster/content/admin/cluster.list.json'.format(self.url)
        params = kwargs
        _handlers = dict(self.handlers.items() | _handlers.items())
        opts = self.kwargs

        return bag.request(method, url, params, _handlers, **opts)
