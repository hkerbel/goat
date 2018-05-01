from fabric.api import run
from fabric.context_managers import settings, shell_env

_SITES_ROOT_PATH = '/var/local/sites'          # Root path of web site folders on server.

def _get_manage_dot_py(host):
    return f'{_SITES_ROOT_PATH}/{host}/virtualenv/bin/python {_SITES_ROOT_PATH}/{host}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'shart@{host}'):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    env_lines = run(f'cat {_SITES_ROOT_PATH}/{host}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    print('>>>>>[s] host:', host)
    with settings(host_string=f'shart@{host}'):
        env_vars = _get_server_env_vars(host)
        ####print('>>>>> env_vars')
        print(env_vars)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            # # # if session_key:
            # # #     print(f'!!>>> on server, vars: "{vars(session_key)}"')
            # # #     print(f'!!>>> on server, type: "{type(session_key)}"')
            # # #     print(f'!!>>> on server, session_key: "{session_key.strip()}"')
            # # #     print(f'!!>>> on server, length: {len(session_key.strip())}')
            # # # else:
            # # #     print('>>>>> on server, session_key: (None)')
            return session_key.strip()