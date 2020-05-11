import logging
import asyncio
from concurrent.futures import ThreadPoolExecutor
from aiohttp import web

from . import const, mailer, wti, zendesk, routes, notifier, stats, translate
from . import executor
from .middleware import stats_middleware, status_logging_middleware

logger = logging.getLogger(__name__)


async def stop_http_clients(app):
    await app[const.ZENDESK_DC].shutdown()
    await app[const.SLACK_NOTIFIER].shutdown()
    await app[const.WTI_DYNAMIC_CONTENT].shutdown()
    await app[const.TRANSLATE_CLIENT].shutdown()
    await app[const.VALIDATION_WTI].shutdown()


async def start_http_clients(app):
    await app[const.ZENDESK_DC].bootstrap()
    await app[const.SLACK_NOTIFIER].bootstrap()
    await app[const.WTI_DYNAMIC_CONTENT].bootstrap()
    await app[const.TRANSLATE_CLIENT].bootstrap()
    await app[const.VALIDATION_WTI].bootstrap()


def app(global_config, **settings):
    logger.info('Loading configuration')
    loop = asyncio.get_event_loop()
    loop.set_debug(False)

    app = web.Application(logger=logger, loop=loop, middlewares=[status_logging_middleware, stats_middleware])
    threads = settings.get('worker_threads', const.DEFAULT_WORKER_THREADS)
    app[const.EXECUTOR_THREAD] = ThreadPoolExecutor(max_workers=int(threads))
    loop.set_default_executor(app[const.EXECUTOR_THREAD])

    app[const.APP_SETTINGS] = settings
    app[const.EMAIL_PROVIDER] = mailer.SendgridProvider(settings)
    app[const.WTI_DYNAMIC_CONTENT] = wti.WtiClient(settings['wti.api_key'])
    app[const.VALIDATION_WTI] = wti.WtiClient()
    app[const.ZENDESK_DC] = zendesk.ZendeskDynamicContent(settings)
    app[const.SLACK_NOTIFIER] = notifier.SlackNotifier(settings)
    app[const.TRANSLATE_CLIENT] = translate.GoogleTranslateClient(settings['translate.google_api_key'])
    dd_stats = stats.Stats(settings['datadog_api_key'], settings['datadog_app_key'])
    app[const.STATS] = executor.AsyncWrapper(dd_stats, app[const.EXECUTOR_THREAD])

    routes.init(app.router)
    app.on_startup.append(start_http_clients)
    app.on_cleanup.append(stop_http_clients)

    return app
