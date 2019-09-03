# SSH Authenticator for JupyterHub

This is a small authenticator for JupyterHub which uses SSH to validate credentials.

There are two configuration parameters:

    c.SSHAuthenticator.server_address = 'sshauthhost.example.com
    c.SSHAuthenticator.server_port = 22

You can enable the authenticator by setting

    c.JupyterHub.authenticator_class = 'sshauthenticator.SSHAuthenticator'

in your JupyterHub config.


## Installation

You can install by using
	
	pip install https://github.com/andreas-h/sshauthenticator/archive/master.zip
