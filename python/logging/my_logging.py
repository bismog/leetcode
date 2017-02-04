#!/usr/bin/env python
# -*- coding:utf-8 -*-

from oslo_config import cfg
from oslo_log import log

LOG = log.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "demo"

log.register_options(CONF)
log.setup(CONF, DOMAIN)

log.info("oslo info")
log.warn("oslo warning")
log.error("oslo error")
