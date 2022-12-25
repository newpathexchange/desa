#!/bin/bash

vertag=$1

APP="desa/producer"
REG="dreg1.lab.newpathexchange.com"
TAG=$(git log -1 --pretty=%H)
IMG="${REG}/${APP}:${TAG}"
LATEST="${REG}/${APP}:latest"

set -x

docker build -t ${IMG} .

if [ "$?" == "0" ]; then
  docker tag ${IMG} ${LATEST}
  [ ! -z "$vertag" ] && docker tag ${IMG} "${REG}/${APP}:$vertag"
  docker push "${REG}/${APP}" --all-tags
fi

if [ "$?" == "0" ]; then
  docker rmi $LATEST
  docker rmi $IMG
  [ ! -z "$vertag" ] && docker rmi "${REG}/${APP}:$vertag"
fi

