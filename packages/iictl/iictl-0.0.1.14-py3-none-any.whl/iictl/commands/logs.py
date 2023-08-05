import click
import shutil
from iictl.commands import cli
from iictl.crud.pod import get_pod_name_by_label_selector
from iictl.crud.pod import get_pod_log
from iictl.kubectl.kubectl import get_kubectl_logs_command, get_executable
from iictl.utils.exception import NotFoundError
from iictl.utils.click import global_option
from iictl.utils.kube import verify_object_name

@cli.command(help='Print instance log')
@click.option('-f', '--follow', is_flag=True, help='Print previous logs and continuously printed.')
@click.option('--tail', type=int, default=-1, help='Print last n lines.')
@click.option('-r', '--raw', is_flag=True, help='[DEPRECATED] Use python-implemented consosle.')
@click.option('-n', '--namespace', type=str, help='Namespace', callback=global_option)
@click.argument('name')
def logs(follow, tail, raw, namespace, name):
    verify_object_name(name)
    
    try:
        pod_name = get_pod_name_by_label_selector(
            namespace=namespace,
            label_selector=f'deep.est.ai/app={name}'
        )
    except NotFoundError as e:
        click.echo('Pod not found')
        return
        
    executable = get_executable()
    # TODO: listing ii with name and error if ii is not exist or deployment is not ready
    if executable:
        # TODO: logging change to use logging module
        kubectl_command = get_kubectl_logs_command(
            pod_name=pod_name,
            namespace=namespace,
            follow=follow,
            tail=tail,
            executable=executable,
        )
        
        import subprocess
        subprocess.call(kubectl_command)
    else:
        click.echo('use python logs')
        resp = get_pod_log(
            name=pod_name,
            namespace=namespace,
            follow=follow,
            tail=tail,
        )
    
        for line in resp:
            click.echo(line.decode('utf-8'), end='')
