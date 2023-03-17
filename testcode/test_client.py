#!/usr/bin/env python3

import sys
sys.path.append("../")
import time
from   mini_socket_sdk.libclient import MiniSocketClient
import logging

logging.basicConfig(level=logging.INFO, 
format='%(filename)s,%(funcName)s,%(lineno)d,%(name)s ,%(process)d, %(levelname)s,%(libclient_obj)s')

def test_msg_integrity():
    m_sock_client = MiniSocketClient('net_commu_config.json')

    for i in range(2000):
        m_sock_client.push_sender_queu("client sent msg: " +str(i))
        while True:
            one_frame=m_sock_client.pop_receiver_queue()
            if(one_frame is not False): 
                 print("---- received from server data: "+str(one_frame))
            else: 
                break
        time.sleep(0.01)
    sys.exit()

def test_msg_punctuality():
    pass
    #todo...
if __name__ == '__main__':
    test_msg_integrity()

