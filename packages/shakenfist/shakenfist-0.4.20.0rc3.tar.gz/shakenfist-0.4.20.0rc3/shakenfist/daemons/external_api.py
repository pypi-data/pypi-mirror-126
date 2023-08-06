import os

from shakenfist.config import config
from shakenfist.daemons import daemon
from shakenfist import logutil
from shakenfist.util import process as util_process


LOG, _ = logutil.setup(__name__)


class Monitor(daemon.Daemon):
    def run(self):
        LOG.info('Starting')
        util_process.execute(None, (config.API_COMMAND_LINE
                                    % {
                                        'port': config.API_PORT,
                                        'timeout': config.API_TIMEOUT,
                                        'name': daemon.process_name('api')
                                    }),
                             env_variables=os.environ)
