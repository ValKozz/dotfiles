#!/bin/bash
PIID = $(pidof picom)
TEST = "test"
echo $PIID

if ( ps aux | grep "picom" | grep -v grep > /dev/null )
then
	echo running
else
	echo not running
fi
	
