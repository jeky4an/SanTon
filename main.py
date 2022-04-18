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
