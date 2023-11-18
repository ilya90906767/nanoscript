from flask import Flask
import paramiko
import time


@celery.task(bind=True)
def send_and_process_fastq(host, username, secret, port, file_to_cluster):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=secret)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(abs_dir,f'/home/common/kumondorova.a/16s/input/{file_to_cluster.filename}')
    db.session.query(Upload).get(id).status = 1
    db.session.commit()
    flash('Ваш файл был успешно отправлен на кластер для обработки', category='success')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=secret)
    process_fastq_file_on_cluster = 'bash'
    comands_to_execute=[f'mkdir /home/common/kumondorova.a/16s/results/{file_to_cluster.date}','source 16s/16s/bin/activate',f'bash 16s/processing.py /home/common/kumondorova.a/16s/input/{file_to_cluster.filename}', f'/home/common/kumondorova.a/16s/expression/results/{file_to_cluster.date} ']
    #папка создается по времени
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comands_to_execute[0])
    time.sleep(5)
    print('1st')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comands_to_execute[1])
    time.sleep(5)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comands_to_execute[2])
    print('2nd')
    time.sleep(180)
    sftp.get(f'/home/common/kumondorova.a/16s/results/{file_to_cluster.date}/testData.zip', '/root/nanoscript/results/testData.zip')
    flash('Кластер обработал ваши файлы.', category='success')
    sftp.close()
    transport.close()
    ssh.close()
    flash(f'{file_to_cluster.filename} обработан 16s скриптом. Сформирован ZIP архив',category='success')
    return 