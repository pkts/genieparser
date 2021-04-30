# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_bgp_detail import ShowBgpVrfAllAllDetail

#=========================================================
# Unit test for show bgp vrf all all detail
#=========================================================
class test_show_bgp_vrf_all_all_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "vrf":{
            "default":{
                "address_family":{
                    "ipv4 unicast":{
                        "prefixes":{
                            "10.1.2.0/24":{
                                "available_path":"1",
                                "best_path":"1",
                                "index":{
                                    "1":{
                                    "best":true,
                                    "state":"local",
                                    "status_codes":"*>",
                                    "route_info":"NONE",
                                    "route_origin_info":"path locally originated",
                                    "next_hop":"0.0.0.0",
                                    "next_hop_igp_metric":"0",
                                    "gateway":"0.0.0.0",
                                    "originator":"100.65.1.1",
                                    "origin_codes":"i",
                                    "metric":"not set",
                                    "localpref":100,
                                    "weight":"32768"
                                    }
                                }
                            },
                            "100.65.1.1/32":{
                                "available_path":"1",
                                "best_path":"1",
                                "index":{
                                    "1":{
                                    "best":true,
                                    "state":"local",
                                    "status_codes":"*>",
                                    "route_info":"NONE",
                                    "route_origin_info":"path locally originated",
                                    "next_hop":"0.0.0.0",
                                    "next_hop_igp_metric":"0",
                                    "gateway":"0.0.0.0",
                                    "originator":"100.65.1.1",
                                    "origin_codes":"i",
                                    "metric":"not set",
                                    "localpref":100,
                                    "weight":"32768"
                                    }
                                }
                            },
                            "100.65.1.2/32":{
                                "available_path":"1",
                                "best_path":"1",
                                "index":{
                                    "1":{
                                    "route_status":"received and used",
                                    "best":true,
                                    "state":"external",
                                    "status_codes":"*>",
                                    "in_rib":"in rib",
                                    "route_info":"65002",
                                    "route_origin_info":"path sourced external to AS",
                                    "next_hop":"100.64.1.2",
                                    "next_hop_igp_metric":"0",
                                    "gateway":"100.64.1.2",
                                    "originator":"100.64.1.2",
                                    "origin_codes":"i",
                                    "metric":"0",
                                    "localpref":100,
                                    "weight":"0"
                                    }
                                }
                            },
                            "100.65.2.2/32":{
                                "available_path":"2",
                                "best_path":"1",
                                "index":{
                                    "1":{
                                    "route_status":"received and used",
                                    "best":true,
                                    "state":"external",
                                    "status_codes":"*>",
                                    "in_rib":"in rib",
                                    "route_info":"65002",
                                    "route_origin_info":"path sourced external to AS",
                                    "next_hop":"100.64.1.2",
                                    "next_hop_igp_metric":"0",
                                    "gateway":"100.64.1.2",
                                    "originator":"100.64.1.2",
                                    "origin_codes":"i",
                                    "metric":"0",
                                    "localpref":100,
                                    "weight":"0"
                                    },
                                    "2":{
                                    "route_status":"received and used",
                                    "best":false,
                                    "state":"external",
                                    "status_codes":"* ",
                                    "not_best_reason":"newer EBGP path",
                                    "route_info":"65003",
                                    "route_origin_info":"path sourced external to AS",
                                    "next_hop":"100.64.1.6",
                                    "next_hop_igp_metric":"0",
                                    "gateway":"100.64.1.6",
                                    "originator":"100.65.2.2",
                                    "origin_codes":"i",
                                    "metric":"not set",
                                    "localpref":100,
                                    "weight":"0"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        switch# sh bgp vrf all all detail
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

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpVrfAllAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpVrfAllAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()