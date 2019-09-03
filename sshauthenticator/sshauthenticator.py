# Copyright (c) Andreas Hilboll

from jupyterhub.auth import Authenticator
from tornado import gen
from paramiko import SSHClient, AuthenticationException, AutoAddPolicy
from traitlets import Int, Unicode


class SSHAuthenticator(Authenticator):
    server_address = Unicode(
        config=True,
        help='Address of LDAP server to contact'
    )
    server_port = Int(
        config=True,
        help='Port on which to contact LDAP server',
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        with SSHClient() as ssh:
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            try:
                ssh.connect(self.server_address, port=self.server_port,
                            username=data['username'],
                            password=data['password'])
            except AuthenticationException:
                return
            return data['username']
