import textfsm
from netmiko import ConnectHandler

with open('mikrotikSanTon.txt', 'r') as f:
    listMikrotik = f.readlines()
for ipOfMikrotik in listMikrotik:
    mikrotik_router_1 = {
    'device_type': 'mikrotik_routeros',
    'host': '',
    'port': '22',
    'username': 'admin',
    'password': 'admin'
    }
    mikrotik_router_1 ["host"] = ipOfMikrotik
    sshCli = ConnectHandler(**mikrotik_router_1)
    output = sshCli.send_command("/ip address print")
    with open('gucci.template.txt') as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseText(output)
    if not result:
        print(mikrotik_router_1.get("host") + " Этот микротик не имеет 192.168.x.y/zz или не доступен!")
    else:
        for result2 in result:
            for result3 in result2:
                iphost = mikrotik_router_1.get("host").strip()
                print(iphost + ":" + result3)
# import paramiko
# import time
# import socket
# from pprint import pprint
#
#
# def send_show_command(
#     ip,
#     username,
#     password,
#     command,
#     max_bytes=60000,
#     short_pause=1,
#     long_pause=5,
# ):
#     cl = paramiko.SSHClient()
#     cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     cl.connect(
#         hostname=ip,
#         username=username,
#         password=password,
#         look_for_keys=False,
#         allow_agent=False,
#     )
#     with cl.invoke_shell() as ssh:
#
#         time.sleep(short_pause)
#         ssh.recv(max_bytes)
#
#         result = {}
#         for command in commands:
#             ssh.send(f"{command}\n")
#             ssh.settimeout(5)
#
#             output = ""
#             while True:
#                 try:
#                     part = ssh.recv(max_bytes).decode("utf-8")
#                     output += part
#                     time.sleep(0.5)
#                 except socket.timeout:
#                     break
#             result[command] = output
#
#         return result
#
#
# if __name__ == "__main__":
#     devices = ["10.21.13.4"]
#     commands = ["ip address print"]
#     result = send_show_command("10.21.13.4", "scriptdg", "Irjkmybr5", commands)
#     pprint(result, width=120)
#
#
#
#
#
#
#
#
#
#
#
# # This is a sample Python script.
# #from scrapli import Scrapli
# #from textfsm import TextFSM
# #from scrapli.helper import textfsm_parse
# #import jtextfsm as textfsm
# #from tabulate import tabulate
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# # Комментарий
# #r1 = {
#   # "host": "172.16.123.59",
#   # "auth_username": "admin",
#   # "auth_password": "irjkmybr",
#   # "auth_strict_key": False,
#   # "platform": "mikrotik_routeros",
#   # "transport": "ssh2",
# #}
#
#
# #ssh = Scrapli(**r1)
# #ssh.open()
# #ssh.get_prompt()
#
# #.send_command("terminal 0")
# #reply = ssh.send_command("show interfaces brief")
# #reply = ssh.send_command("/interface print without-paging")
# #myGucci = reply.result
# #print(myGucci)
# #with open('gucci.template.txt') as template:
#  #  fsm = textfsm.TextFSM(template)
#  #  result = fsm.ParseText(myGucci)
# #print(tabulate(result, headers=['Interface', 'State'], tablefmt='orgtbl'))
#
#
#
#
#
