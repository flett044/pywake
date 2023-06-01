#!/usr/bin/env python3
import wakeonlan
import ping3
import colored
import sys
from colored import fg, attr

# Requires wakeonlan, ping3, colored, sys
# This is a pretty basic WOL script I wrote for usage in my homelab. Simply put the mac address you want to WOL as well as the
# ip address of the host and the hostname of the host in each variable. This is my first functional python script so
# it's not perfect. I would suggest running this on a raspberry pi or equivalent. You can use a
# cronjob to schedule when it runs. In my lab I run it every one minute. Written by Fleet.



# -------------CONFIG------------------
# Mac address to WOL
mac = "Ur mac here!"
# Host name/name of device to monitor
host = "Ur host here!"
# IP address to ping
ip = "Ur ip here!"  # Can be IP/Hostname
# -------------CONFIG------------------



# -------------CHANGE NOTHING BELOW THIS LINE------------------
# Timeout for each ping in seconds
timeout = 4
# Console colors
error_color = fg('red')
normal_color = fg('green')
# Don't change
reset = attr('reset')


def send_ping(ip):
    print(normal_color + "Pinging host:", host + reset)
    # Ping the IP address and return the result
    return ping3.ping(ip, timeout=timeout)


p = send_ping(ip)

try:
    if p is None:
        print(error_color + "Host has timed out! Sending magic packet to:", host + reset)
        wakeonlan.send_magic_packet(mac)
        print(normal_color + "Magic packet sent." + reset)  # Debugging: Print a message to confirm the magic packet is sent
    elif p is False:
        print(error_color + "Can't resolve:", host + reset)
        sys.exit()
    else:
        print(normal_color + "Ping succeeded to:", host + reset)
except OSError as e:
    print(error_color + "Error:", str(e) + reset)  # Convert the OSError object to a string before concatenating
    sys.exit()
except Exception as e:
    print(error_color + "Error:", str(e) + reset)  # Convert the exception object to a string before concatenating
    sys.exit()
