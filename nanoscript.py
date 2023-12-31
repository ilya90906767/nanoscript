import subprocess 
import os
import tempfile
import pexpect
import paramiko

myfile = "/home/common/kumondorova.a/16s/input"
hostname="calc.cod.phystech.edu"
username='kumondorova.a'
password="Gq~#aCztH%6A}u"
tofolderinclust='/home/common/kumondorova.a/16s/input'
destination = "kumondorova.a@calc.cod.phystech.edu:/home/common/kumondorova.a/16s/input"
#p = subprocess.Popen(["scp", myfile, destination])
#sts = os.waitpid(p.pid, 0)
#
def scp(host, user, password, from_dir, to_dir, timeout=300, recursive=False):
    fname = tempfile.mktemp()
    fout = open(fname, 'w')

    scp_cmd = 'scp'
    if recursive:
        scp_cmd += ' -r'
    scp_cmd += f' {user}@{host}:{from_dir} {to_dir}'
    child = pexpect.spawnu(scp_cmd, timeout=timeout)
    child.expect(['[pP]assword: '])
    child.sendline(str(password))
    child.logfile = fout
    child.expect(pexpect.EOF)
    child.close()
    fout.close()

    fin = open(fname, 'r')
    stdout = fin.read()
    fin.close()

    if 0 != child.exitstatus:
        raise Exception(stdout)

    return stdout

def scptrans(host,user,passw,filefrom,fileto):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=f'{passw}')
    scp = ssh.open_sftp()
    scp.put(filefrom,fileto)
    # Close the SCP client
    scp.close()

    # Close the SSH client
    ssh.close() 
    
    return print('File was transfered to cluster via SCP')

