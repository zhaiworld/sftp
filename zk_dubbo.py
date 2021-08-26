#!/usr/bin/env python
# coding=utf-8

import logging
from dubbo.client import DubboClient, ZkRegister

zk = ZkRegister('XXXX')
idCenterService = DubboClient('com.xxx.service', zk_register=zk)
print(zk.zk.hosts)
print(zk.zk)
result = idCenterService.call("getTimestamp", ("999"))
print(result)
