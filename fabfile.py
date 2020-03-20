print('DEPLOY HERE')
from fabric.api import env, run as fabric_run
from fabric.contrib.project import rsync_project

env.app_path = '/home/backend'
env.user = 'circle'

env.use_ssh_config = True
env.disable_knodwn_hosts = True
env.colorize_errors = True

def run(cmd, *args, **kwargs):
    fabric_run('cd %s && %s' % (env.app_path, cmd), *args, **kwargs)


def run_in_venv(cmd):
    run('cd %s && . venv/bin/activate && %s' % (env.app_path, cmd))


def manage_py(*args):
    run_in_venv('cd src && ./manage.py %s' % ' '.join(args))


def upload():
    return rsync_project(
        local_dir='src/',
        remote_dir=env.app_path + '/src/',
        delete=True,
        exclude=[
            '.git',
            '.env',
            '__pycache__',
            '*.pyc',
            'celerybeat-schedule',
            'celerybeat.pid',
        ],
        extra_opts='--links --omit-dir-times',
    )

def deploy():
    upload()

    run_in_venv('pip install -r src/requirements.txt')  # install new requirements

    manage_py('migrate', '--noinput')
    manage_py('compilemessages')
    manage_py('remove_stale_contenttypes', '--noinput')

    manage_py('collectstatic', '--noinput', '--clear')

    run('touch reload')  # tell uwsgi to reload application code

    # restart background celery workers
    run('sudo /usr/bin/supervisorctl restart default-worker')
    run('sudo /usr/bin/supervisorctl restart beat')
    

# from fabric.api import env, run, cd, task

# debug = False

# if debug:
#     import paramiko
#     paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

# env.venv_name = 'django-circleci-example'
# env.path = '~/django-circleci-example'
# env.user = 'admin'


# @task
# def production():
#     env.branch = 'master'
#     env.hosts = ['timmyomahony.com', ]


# @task
# def staging():
#     env.branch = 'develop'
#     env.hosts = ['timmyomahony.com', ]


# @task
# def venv(cmd):
#     run('workon {0} && {1}'.format(env.venv_name, cmd))


# @task
# def deploy():
#     with cd(env.path):
#         run('git pull origin {0}'.format(env.branch))
#         venv('pip install -r requirements/production.txt')
#         venv('python manage.py migrate')
#         venv('python manage.py collectstatic --noinput')
#         run('supervisorctl reread')
#         run('supervisorctl update')
#         run('supervisorctl restart django-circleci-example')
