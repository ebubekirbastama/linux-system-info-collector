import paramiko

host = ""
port = 
user = "root"
password = ""

commands = [
    "lscpu",
    "free -h",
    "df -h",
    "uptime",
    "cat /etc/os-release"
]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=password)

with open("system_info.txt", "w") as file:
    for cmd in commands:
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode()
        file.write(f"\n===== {cmd.upper()} =====\n")
        file.write(output)

client.close()
print("Bilgiler system_info.txt dosyasına kaydedildi.")
