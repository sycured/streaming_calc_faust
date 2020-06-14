#!/usr/bin/env bash

inject(){
  faust -A bwserver send @compute "$1"
}

inject '{"nblisteners":120, "bitrate":64.8}'
inject '{"nblisteners":10, "bitrate":256.1}'
inject '{"nblisteners":55, "bitrate":96.8}'
inject '{"nblisteners":432, "bitrate":512}'
inject '{"nblisteners":32, "bitrate":384}'
inject '{"nblisteners":1, "bitrate":1048}'
inject '{"nblisteners":74, "bitrate":1025.8}'
inject '{"nblisteners":42, "bitrate":2056}'
inject '{"nblisteners":432, "bitrate":9082.4}'
inject '{"nblisteners":65465, "bitrate":750.3}'
inject '{"nblisteners":3132, "bitrate":432.6}'
inject '{"nblisteners":121, "bitrate":43243.77}'