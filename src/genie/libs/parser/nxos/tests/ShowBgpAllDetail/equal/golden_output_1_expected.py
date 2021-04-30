expected_output = {
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