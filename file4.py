#!/usr/bin/env python3

import os

whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)

ls_return = os.popen('ls')
ls_contents = ls_return.read()
print('ls_contents:',ls_contents)

ifconfig_return = os.popen('ifconfig')
ifconfig_contents = ifconfig_return.read()
print('The contents of ifconfig_return:',ifconfig_contents)
