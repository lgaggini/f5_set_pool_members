#! /usr/bin/env python

from f5.bigip import ManagementRoot
import argparse
import logging
from settings import ENDPOINT, USER, PASS, POOLS

STATES = ['enabled', 'disabled', 'forced_offline']

description = 'enables, disables and forces offline f5 pools members'
parser = argparse.ArgumentParser(description=description)

parser.add_argument('-p', '--pool', required=True, choices=POOLS,
                    help='pool to work with')
parser.add_argument('-s', '--state', required=True, choices=STATES,
                    help='pool to work with')
parser.add_argument('-r', '--readonly', dest='readonly',
                    action='store_true',
                    help='readonly mode for debug (default disabled)')

cli_options = parser.parse_args()
FORMAT = '%(asctime)s %(levelname)s %(module)s %(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger('set_pool_members_state')

mgmt = ManagementRoot(ENDPOINT, USER, PASS)

pool = mgmt.tm.ltm.pools.pool.load(name=cli_options.pool,
                                   partition='Common')

for member in pool.members_s.get_collection():

    logger.info('%s: %s %s' % (member.name, member.session, member.state))

    if cli_options.state == 'enabled':
        # enables member
        logger.info('enables member %s, previous state: %s' %
                    (member.name, member.state))
        member.session = 'user-enabled'
    elif cli_options.state == 'disabled':
        # disables member
        logger.info('disables member %s, previous state: %s' %
                    (member.name, member.state))
        member.session = 'user-disabled'
    elif cli_options.state == 'forced_offline':
        # forces online member
        logger.info('forces online member %s, previous state: %s' %
                    (member.name, member.state))
        member.state = 'user-down'
        member.session = 'user-disabled'

    if not cli_options.readonly:
        member.update()
    else:
        logger.info('readonly mode, no changes applied')

    logger.info('%s: %s %s' % (member.name, member.session, member.state))
