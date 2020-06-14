#!/usr/bin/env bash

inject(){
  faust -A serverusagebw send @compute "$1"
}

inject '{"nblisteners":120, "bitrate":64.8, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":10, "bitrate":256.1, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":55, "bitrate":96.8, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":432, "bitrate":512, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":32, "bitrate":384, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":1, "bitrate":1048, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":74, "bitrate":1025.8, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":42, "bitrate":2056, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":432, "bitrate":9082.4, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":65465, "bitrate":750.3, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":3132, "bitrate":432.6, "nbdays":1, "nbhours":24}'
inject '{"nblisteners":121, "bitrate":43243.77, "nbdays":1, "nbhours":24}'