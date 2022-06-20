#!/usr/bin/env python3
import json

{
  "datacenter": {
    "children": {
      "sdwan": {
        "vmanage": {
          "ansible_host": "172.16.1.121",
          "ansible_port": "8443"
        }
      },
      "routers_iosxe": {
        "hosts": {
          "csr1": {
            "ansible_host": "192.168.199.1"
          },
          "csr2": {
            "ansible_host": "192.168.199.2"
          },
          "csr3": {
            "ansible_host": "192.168.199.3"
          }
        }
      },
      "routers_ios": {
        "hosts": "192.168.199.1[1:3]"
      },
      "vcenter": {
        "hosts": {
          "vcsa": {
            "ansible_host": "172.16.1.146"
          }
        },
        "vars": {
          "vmware_user": "administrator@vsphere.local",
          "vmware_password": "!!EDlew1987"
        }
      },
      "esx": {
        "hosts": {
          "esx147": {
            "ansible_host": "172.16.1.147"
          },
          "esx148": {
            "ansible_host": "172.16.1.148"
          },
          "esx149": {
            "ansible_host": "172.16.1.149",
            "ansible_user": "root",
            "ansible_password": "!!EDlew1987"
          }
        },
        "vars": {
          "ansible_user": "root",
          "ansible_password": "password",
          "ansible_connection": "ssh"
        }
      },
      "win": {
        "hosts": {
          "win1": {
            "ansible_host": "Win2k16@edlab.net",
            "ansible_connection": "winrm",
            "ansible_user": "administrator@EDLAB.NET",
            "ansible_password": "!!EDlew1987",
            "ansible_port": 5985,
            "ansible_winrm_server_cert_validation": "ignore",
            "ansible_winrm_transport": "kerberos"
          }
        }
      }
    },
    "vars": {
      "ansible_connection": "network_cli",
      "ansible_network_os": "ios",
      "ansible_become": "yes",
      "ansible_become_method": "enable",
      "ntp_servers": "172.16.255.255",
      "ansible_python_interpreter": "/usr/bin/python3"
    }
  }
}

