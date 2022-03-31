import paramiko

nbytes = 4096
hostname = ['172.16.13.164', '172.16.12.176']
port = 22
username = "meditab"
password = "99$inmedi"
command = 'notify-send "HELLO"'

for host in range(len(hostname)):
    client = paramiko.Transport((hostname[host], port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print ("exit status: ", session.recv_exit_status())
    print (stdout_data)
    print (stderr_data)

    session.close()
    client.close()