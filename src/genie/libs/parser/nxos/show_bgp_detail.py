'''
Author: Vanish Pattni
Contact: vanish.pattni@ipkts.net
'''
"""show_bgp_detail.py

NXOS parsers for the following show commands:
    * 'show bgp vrf {vrf} ipv4 unicast detail'

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


# =================================
# Schema for:
#   * 'show bgp vrf all all detail'
#   * 'show bgp vrf {vrf} ipv4 unicast detail'
# =================================
class ShowBgpAllDetailSchema(MetaParser):
    ''' Schema for:
        * 'show bgp vrf all all detail'
        * 'show bgp vrf {vrf} {address_family} detail'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {Optional('prefixes'):
                            {Any():
                                {Optional('available_path'): str,
                                Optional('best_path'): str,
                                Optional('table_version'): str,
                                Optional('index'):
                                    {Any():
                                        {Optional('next_hop'): str,
                                        Optional('next_hop_igp_metric'): str,
                                        Optional('gateway'): str,
                                        Optional('route_info'): str,
                                        Optional('route_origin_info'): str,
                                        Optional('best'): bool,
                                        Optional('state'): str,
                                        Optional('route_status'): str,
                                        Optional('status_codes'): str,
                                        Optional('origin_codes'): str,
                                        Optional('metric'): str,
                                        Optional('localpref'): int,
                                        Optional('weight'): str,
                                        Optional('originator'): str,
                                        Optional('not_best_reason'): str,
                                        Optional('in_rib'): str, 
                                        }
                                    }
                                },
                            },
                        },
                    },
                },
            },
        }

# =================================
# Super Parser for:
#   * 'show bgp vrf all all detail'
#   * 'show bgp vrf {vrf} ipv4 unicast detail'
# =================================
class ShowBgpDetailSuperParser(ShowBgpAllDetailSchema):

    ''' Super Parser for:
        * 'show bgp vrf all all detail'
        * 'show bgp vrf <WORD> ipv4 unicast detail'
    '''
    """
    BGP routing table information for VRF default, address family IPv4 Unicast
    BGP routing table entry for 10.1.2.0/24, version 19
    Paths: (1 available, best #1)
    Flags: (0x080002) (high32 00000000) on xmit-list, is not in urib

    Advertised path-id 1
    Path type: local, path is valid, is best path, no labeled nexthop
    AS-Path: NONE, path locally originated
        0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
        Origin IGP, MED not set, localpref 100, weight 32768

    Path-id 1 advertised to peers:
        100.64.1.2         100.64.1.6     
    BGP routing table entry for 100.65.1.1/32, version 23
    Paths: (1 available, best #1)
    Flags: (0x080002) (high32 00000000) on xmit-list, is not in urib

    Advertised path-id 1
    Path type: local, path is valid, is best path, no labeled nexthop
    AS-Path: NONE, path locally originated
        0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
        Origin IGP, MED not set, localpref 100, weight 32768

    Path-id 1 advertised to peers:
        100.64.1.2         100.64.1.6     
    BGP routing table entry for 100.65.1.2/32, version 11
    Paths: (1 available, best #1)
    Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

    Advertised path-id 1
    Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
    AS-Path: 65002 , path sourced external to AS
        100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
        Origin IGP, MED 0, localpref 100, weight 0

    Path-id 1 advertised to peers:
        100.64.1.6     
    BGP routing table entry for 100.65.2.2/32, version 16
    Paths: (2 available, best #1)
    Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

    Advertised path-id 1
    Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
    AS-Path: 65002 , path sourced external to AS
        100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
        Origin IGP, MED 0, localpref 100, weight 0

    Path type: external, path is valid, received and used, not best reason: newer EBGP path, no labeled nexthop
    AS-Path: 65003 , path sourced external to AS
        100.64.1.6 (metric 0) from 100.64.1.6 (100.65.2.2)
        Origin IGP, MED not set, localpref 100, weight 0

    Path-id 1 advertised to peers:
        100.64.1.6     
    """
    def cli(self, address_family='', vrf='', output=None):
        # Init dictionary
        ret_dict = {}
        # subdict = ''
        # next_line_update_group = False
        # route_distinguisher = ''
        new_address_family = ''
        original_address_family = address_family
        # refresh_epoch_flag = False
        # route_info = ''
        # route_status = ''
        # aggregated_by_as = ''
        # aggregated_by_address = ''
        # imported_path_from = ''
        # imported_safety_path = False
        # refresh_epoch = None
        # cmd_vrf = vrf if vrf else None
        # default_vrf = None

        # BGP routing table information for VRF default, address family IPv4 Unicast
        p1 = re.compile(r'^BGP +routing +table +information +for +VRF'
                        r' +(?P<vrf>[a-zA-Z0-9\-\s]+),'
                        r' +address +family +(?P<address_family>[a-zA-Z0-9\-\s]+)$')
        
        # BGP routing table entry for 100.65.1.1/32, version 9
        # BGP routing table entry for 100.65.1.2/32, version 11
        # BGP routing table entry for 100.65.2.2/32, version 13
        p2 = re.compile(r'^BGP +routing +table +entry +for'
                        r' +(?P<prefix>\d+\.\d+\.\d+\.\d+\/\d+),'
                        r' +version +(?P<prefix_table_version>\d+)$')

        # Paths: (1 available, best #1)
        # Paths: (2 available, best #1)
        p3 = re.compile(r'^Paths: +\((?P<available_path>\d+) +available,'
                        r' +best +\#(?P<best_path>\d+)\)$')


        # Path type: local, path is valid, is best path, no labeled nexthop
        # Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
        # Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
        # Path type: external, path is valid, received and used, not best reason: newer EBGP path, no labeled nexthop
        # Path type: redist, path is valid, is best path
        p5_1 = re.compile(r'^Path +type: +(?P<state>(redist|local|internal|external)),'
                        r'(?: +path +is +(?P<valid>valid),?)?'
                        r'(?: +(?P<route_status>(received +and +used|received +only)),?)?'
                        r'(?: +is +(?P<best>best) +path,?)?'
                        r'(?: +not +best +reason: +(?P<not_best_reason>[\w\s]+),?)?'
                        r'(?: +no +labeled +nexthop,?)?'
                        r'(?: +(?P<in_rib>in +rib),?)?')

        #   Origin IGP, MED not set, localpref 100, weight 32768
        #   Origin IGP, MED not set, localpref 100, weight 32768
        #   Origin IGP, MED 0, localpref 100, weight 0
        #   Origin IGP, MED 0, localpref 100, weight 0
        #   Origin IGP, MED not set, localpref 100, weight 0
        p5_2 = re.compile(r'^Origin +(?P<origin>[a-zA-Z]+),'
                        r'(?: +MED +(?P<metric>[a-zA-Z0-9 ]+),?)'
                        r'(?: +localpref +(?P<locprf>[0-9]+),?)'
                        r'(?: +weight +(?P<weight>[0-9]+),?)$')

        #   AS-Path: NONE, path locally originated
        #   AS-Path: NONE, path locally originated
        #   AS-Path: 65002 , path sourced external to AS
        #   AS-Path: 65002 , path sourced external to AS
        #   AS-Path: 65003 , path sourced external to AS
        #   AS-Path: 4826 , path sourced external to AS
        #   AS-Path: 4826 13335 , path sourced external to AS
        #   AS-Path: NONE, path sourced internal to AS
        #   AS-Path: NONE, path locally originated
        p17 = re.compile(r'^AS-Path: (?P<route_info>[a-zA-Z0-9\-\.\{\}\s\(\)\/\:\[\]]+),?'
                        r' +(?P<route_origin_info>[a-zA-Z0-9\s]+)')

        # 0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
        # 0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
        # 100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
        # 100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
        # 100.64.1.6 (metric 0) from 100.64.1.6 (100.65.2.2)
        p4 = re.compile(r'^(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                        r' +\(metric +(?P<next_hop_igp_metric>[0-9]+)\)'
                        r' +from +(?P<gateway>[a-zA-Z0-9\.\:]+)'
                        r' +\((?P<originator>[0-9\.]+)\)$')

        for line in output.splitlines():
            line = line.strip()

            # BGP routing table information for VRF default, address family IPv4 Unicast
            m = p1.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                vrf = m.groupdict()['vrf']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    vrf_dict = ret_dict['vrf'].setdefault(vrf, {})
                if 'address_family' not in vrf_dict:
                    vrf_dict['address_family'] = {}
                if address_family not in vrf_dict['address_family']:
                    address_family_dict = vrf_dict['address_family'].setdefault(address_family, {})
                continue

            # BGP routing table entry for 100.65.1.1/32, version 9
            # BGP routing table entry for 100.65.1.2/32, version 11
            # BGP routing table entry for 100.65.2.2/32, version 13
            m = p2.match(line)
            if m:
                index = 0 # available path index
                prefix = m.groupdict()['prefix']
                if 'prefixes' not in address_family_dict:
                    address_family_dict['prefixes'] = {}
                if prefix not in address_family_dict['prefixes']:
                    prefix_dict = address_family_dict['prefixes'].setdefault(prefix, {})
                continue

            # Paths: (1 available, best #1)
            # Paths: (2 available, best #1)
            m = p3.match(line)
            if m:
                available_path = m.groupdict()['available_path']
                best_path = m.groupdict()['best_path']
                prefix_dict['available_path'] = available_path
                prefix_dict['best_path'] = best_path
                if 'index' not in prefix_dict:
                    prefix_dict['index'] = {}
                continue

            # Path type: local, path is valid, is best path, no labeled nexthop
            # Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
            # Path type: external, path is valid, received and used, is best path, no labeled nexthop, in rib
            # Path type: external, path is valid, received and used, not best reason: newer EBGP path, no labeled nexthop
            # Path type: redist, path is valid, is best path
            m = p5_1.match(line)
            if m:
                index += 1
                if 'index' not in prefix_dict:
                    prefix_dict['index'] = {}
                if index not in prefix_dict['index']:
                    path_dict = prefix_dict['index'].setdefault(index, {})
                group = m.groupdict()
                status_codes = ''

                if group['valid']:
                    status_codes += '* '
                if group['route_status']:
                    path_dict['route_status'] = group['route_status']
                if group['best']:
                    path_dict['best'] = True
                    status_codes = status_codes.rstrip()
                    status_codes += '>'
                else:
                    path_dict['best'] = False
                if group['state']:
                    path_dict['state'] = group['state']
                    if group['state'] == 'internal':
                        status_codes += 'i'
                path_dict['status_codes'] = status_codes
                if group['not_best_reason']:
                    path_dict['not_best_reason'] = group['not_best_reason']
                if group['in_rib']:
                    path_dict['in_rib'] = group['in_rib']
                continue

            #   Origin IGP, MED not set, localpref 100, weight 32768
            #   Origin IGP, MED not set, localpref 100, weight 32768
            #   Origin IGP, MED 0, localpref 100, weight 0
            #   Origin IGP, MED 0, localpref 100, weight 0
            #   Origin IGP, MED not set, localpref 100, weight 0
            m = p5_2.match(line)
            if m:
                group = m.groupdict()

                if group['origin']:
                    origin = str(group['origin'])
                    if origin == 'incomplete':
                        path_dict['origin_codes'] = '?'
                    elif origin == 'EGP':
                        path_dict['origin_codes'] = 'e'
                    else:
                        path_dict['origin_codes'] = 'i'

                if group['metric']:
                     path_dict['metric'] = group['metric']
                if group['locprf']:
                     path_dict['localpref'] = int(group['locprf'])
                if group['weight']:
                    path_dict['weight'] = group['weight']
                continue

            # 0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
            # 0.0.0.0 (metric 0) from 0.0.0.0 (100.65.1.1)
            # 100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
            # 100.64.1.2 (metric 0) from 100.64.1.2 (100.64.1.2)
            # 100.64.1.6 (metric 0) from 100.64.1.6 (100.65.2.2)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for i in ['next_hop', 'next_hop_igp_metric', 'gateway', 'originator']:
                    if group[i]:
                        path_dict[i] = group[i]
                continue

            #   AS-Path: NONE, path locally originated
            #   AS-Path: NONE, path locally originated
            #   AS-Path: 65002 , path sourced external to AS
            #   AS-Path: 65002 , path sourced external to AS
            #   AS-Path: 65003 , path sourced external to AS
            #   AS-Path: 4826 , path sourced external to AS
            #   AS-Path: 4826 13335 , path sourced external to AS
            #   AS-Path: NONE, path sourced internal to AS
            #   AS-Path: NONE, path locally originated
            m = p17.match(line)
            if m:
                group = m.groupdict()

                if group['route_info']:
                     path_dict['route_info'] = group['route_info'].rstrip()
                if group['route_origin_info']:
                     path_dict['route_origin_info'] = group['route_origin_info']
                continue


        return ret_dict

# =================================================
# Parser for:
#   * 'show bgp vrf all all detail'
#   * 'show bgp vrf {vrf} ipv4 unicast detail'
#   * 'show bgp vrf {vrf} ipv4 unicast {route}'
# =================================================
class ShowBgpVrfAllAllDetail(ShowBgpDetailSuperParser, ShowBgpAllDetailSchema):

    ''' Parser for:
        * 'show bgp vrf all all detail'
        * 'show bgp vrf {vrf} {address_family} detail'
        * 'show bgp vrf {vrf} {address_family} {route}'
    '''

    cli_command = ['show bgp vrf all all detail',
                    'show bgp vrf {vrf} {address_family} detail',
                    'show bgp vrf {vrf} {address_family} {route}'
                   ]
    exclude = ['table_version', 'refresh_epoch', 'best_path', 'status_codes', 'transfer_pathid', 'paths']


    def cli(self, vrf='', route='', address_family='',output=None):
        if output is None:
            if vrf and address_family:
                if route:
                    cmd = self.cli_command[2].format(vrf=vrf,
                        route=route,
                        address_family=address_family)
                else:
                    cmd = self.cli_command[1].format(vrf=vrf,
                        address_family=address_family)
            else:
                cmd = self.cli_command[0]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(address_family=address_family,output=show_output)


