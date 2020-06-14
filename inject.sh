#!/usr/bin/env bash

inject(){
  faust -L uvloop -A "$1" send @compute "$2"
}

inject_bwserver(){
  inject "bwserver" "$1"
}
inject_serverusagebw(){
  inject "serverusagebw" "$1"
}
inject_bwserver '{"nblisteners":120, "bitrate":64.8}'
inject_bwserver '{"nblisteners":10, "bitrate":256.1}'
inject_bwserver '{"nblisteners":55, "bitrate":96.8}'
inject_bwserver '{"nblisteners":432, "bitrate":512}'
inject_bwserver '{"nblisteners":32, "bitrate":384}'
inject_bwserver '{"nblisteners":1, "bitrate":1048}'
inject_bwserver '{"nblisteners":74, "bitrate":1025.8}'
inject_bwserver '{"nblisteners":42, "bitrate":2056}'
inject_bwserver '{"nblisteners":432, "bitrate":9082.4}'
inject_bwserver '{"nblisteners":65465, "bitrate":750.3}'
inject_bwserver '{"nblisteners":3132, "bitrate":432.6}'
inject_bwserver '{"nblisteners":121, "bitrate":43243.77}'
inject_serverusagebw '{"nblisteners":120, "bitrate":64.8, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":10, "bitrate":256.1, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":55, "bitrate":96.8, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":432, "bitrate":512, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":32, "bitrate":384, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":1, "bitrate":1048, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":74, "bitrate":1025.8, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":42, "bitrate":2056, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":432, "bitrate":9082.4, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":65465, "bitrate":750.3, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":3132, "bitrate":432.6, "nbdays":1, "nbhours":24}'
inject_serverusagebw '{"nblisteners":121, "bitrate":43243.77, "nbdays":1, "nbhours":24}'