## rpi wiring: 
## Description: 

    This project is a socket api to communicate between server and client .
    It supports multiple clients connet to one server, and server will send the same data
    to each clients, ie. broadcasting mode.  

## Program working flow: 
    It has two queues. One is send queue, the other is receive queue.
    The class MiniSocketServer, MiniSocketClient  will create a thread to monitor if send queue 
    is empty, if not, it will pop out a data and send to client(s).
    It uses pythone's selectors to continuously check socket events, for example read events. 
    If read events is generated, it will read data and push data to receive queue.



## References
    https://realpython.com/python-sockets/

## Requirements

- [Python] 3.6 or later.

