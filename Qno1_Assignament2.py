# Q1 design a python program that stimulates the 
# web server handling incoming requests using a queue 
# models different type of request with varying processing 
# times and simulates their  processing orders ?

import queue
import threading
import time
import random

class WebServer:
    def _init_(self):
        self.request_queue = queue.Queue()

    def handle_request(self, request_type, processing_time):
        time.sleep(processing_time)
        print(f"Processed {request_type} request in {processing_time} seconds")

    def start_processing(self):
        while True:
            if not self.request_queue.empty():
                request_type, processing_time = self.request_queue.get()
                self.handle_request(request_type, processing_time)
            else:
                time.sleep(1)

def generate_requests(web_server):
    request_types = ["GET", "POST", "PUT", "DELETE"]
    
    while True:
        request_type = random.choice(request_types)
        processing_time = random.uniform(0.5, 3.0)
        web_server.request_queue.put((request_type, processing_time))
        time.sleep(random.uniform(0.1, 1.0))

if "name" == "_main_":
    web_server = WebServer()

    processing_thread = threading.Thread(target=web_server.start_processing)
    request_generator_thread = threading.Thread(target=generate_requests, args=(web_server,))

    processing_thread.start()
    request_generator_thread.start()

    processing_thread.join()
    request_generator_thread.join()