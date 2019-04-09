

def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = (s.getsockname()[0])
    s.close()
    return ip


def get_time():
    from time import gmtime, strftime
    time = strftime("%H:%M:%S", gmtime())
    return time



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'IP Address: ' + get_ip() + ' Time NOW: ' + get_time()

if __name__ == '__main__':
  app.run(host='127.0.0.1')



