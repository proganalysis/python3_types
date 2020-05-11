#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Created on 2017/1/29 18:02
# Project: ddns
# __author__ = 'ihipop'

import click
import os

import  logging,sys

ECHO=60
logging.addLevelName(60,'ECHO')
def _debugEcho(self:logging.Logger, message, *args, **kwargs):
    if self.isEnabledFor(ECHO):
        self._log(ECHO, message, args, **kwargs)
logging.Logger.echo = _debugEcho


logger = logging.getLogger()
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
screen = logging.StreamHandler(sys.stdout)
screen.setFormatter(format)
logger.addHandler(screen)



def read_config(ctx, param, value):
    if not value:
        return {}
    import json

    def underline_dict(d):
        if not isinstance(d, dict):
            return d
        return dict((k.replace('-', '_'), underline_dict(v)) for k, v in d.items())
    v=[]
    for line in value.read().replace("\r\n","\n").replace("\r","\n").split("\n"):
        if not line.strip().startswith('//'):
            v.append(line)
    v="\n".join(v)
    config = underline_dict(json.loads(v))
    #config = json.load(value)
    config['self'] = value.name
    ctx.default_map = config
    return config

@click.group(invoke_without_command=True)
@click.option('-c', '--config', callback=read_config, type=click.File('r'),
              help='A json file with default values for commands. {"command": {"options":5001}}')
@click.option('-d','--debug', envvar='DEBUG', default=0, help='Debug mode,Multiply to increase Level',count=True,type=click.IntRange(0, 5, clamp=True)) # '''is_flag=True'''
@click.pass_context
def cli(ctx,**kwargs):
    sys.path.append(os.getcwd())
    # print(kwargs)
    debug = logging.CRITICAL - kwargs['debug'] * 10
    # print(debug)
    logger.setLevel(debug)
    if ctx.invoked_subcommand:
        logger.echo('I am about to invoke %s' % ctx.invoked_subcommand)
    else:
        logger.echo('No SubCommand set.')
    ctx.obj = {}
    return ctx.obj.update(kwargs)

@cli.command()
@click.option('--username', help='password',required=True)
@click.option('--password', help='username',required=True)
@click.option('--ddnsname', help='Domain',required=True)
@click.option('--api-url', help='Api-URL to Override',required=True,default='http://members.3322.net/dyndns/update')
@click.pass_context
def pubyun(self,**kwargs):
    '''
    PUBYUN(公云) www.pubyun.com in China
    '''
    from .updater.pubyun import PubYunUpdater
    client = PubYunUpdater(kwargs['ddnsname'],kwargs['username'],kwargs['password'],api_url=kwargs['api_url'])
    result = client.updater()
    print(result)

@cli.command()
@click.option('--token', help='TOKEN is the API token for authentication/authorization',required=True)
@click.option('--domains', help='DOMAINS is either a single domain or a comma separated list of domains',required=True)
@click.option('--api-url', help='Api-URL to Override',required=True,default='https://www.duckdns.org/update')
@click.pass_context
def duckdns(self,**kwargs):
    '''
    Duck DNS is a free dynamic DNS hosted on Amazon VPC
    '''
    from .updater.duckdns import DuckDNSUpdater
    client = DuckDNSUpdater(kwargs['domains'],kwargs['token'],api_url=kwargs['api_url'])
    result = client.updater()
    print(result)


def main():
    cli()

if __name__ == "__main__":
    main()