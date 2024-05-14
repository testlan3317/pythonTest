#!/bin/bash
function usage() {
    echo "+++++++++++ Manual Start +++++++++++++++++++++++++++"
    echo "usage: "
    echo "./reg_scripts switch_number"
    echo "+++++++++++ Manual End   +++++++++++++++++++++++++++"
}

[ $# -lt 1 ]&&usage&&exit -1

case "$1" in
  1)
    echo "hello world 1"
    ;;
  2)
    echo "test world 2"
    ;;
  3)
    echo "sorry, invalid"
    ;;
  check):
    echo "starting...check..."
    ;;
  *)
    echo "you just don't give up"
esac

