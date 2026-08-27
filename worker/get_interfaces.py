from netmiko import ConnectHandler
import textfsm

def get_interfaces(ip, username, password):
    router = {"device_type": "cisco_ios",
              "ip": ip,
              "username": username,
              "password": password,
              "disabled_algorithms": {"pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]},
              }
    
    with ConnectHandler(**router) as ssh:
        return ssh.send_command("show ip int br", use_textfsm=True)

if __name__ == "__main__":
    print(get_interfaces("172.31.67.11", "cisco", "cisco"))
