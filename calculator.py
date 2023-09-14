# Python Subnet Calculator

# This calculator can take an IP address as input, validate its correctness,
# determine its class (A, B, or C), and provide CIDR notation either
# given by the user or inferred from the IP class.

# IP Validation:
# 1. Ensure the input IP is in the correct format (xxx.xxx.xxx.xxx)
# 2. Ensure each segment (octet) is between 0 and 255
# 3. Identify the IP class (A, B, C)
def ip_validate(ip):
  ip_list = ip.split('.')
  if len(ip_list) != 4:
    return False
  for value in ip_list:
    if not value.isdigit():
      return False
    value = int(value)
    if not 0 <= value <= 255:
      return False
  return True

# CIDR Notation:
# 1. Ensure the input is in the correct format.
# 2. User can input CIDR notation if known.
# 3. If CIDR is not provided, it is inferred based on the IP class.
def cidr_validate(cidr):
  if cidr.isdigit():
    cidr = int(cidr)
    if 0 <= cidr <= 32:
      return True
    else:
      print("Invalid input.")
      return False
  else:
    print("Invalid input.")
    return False

#Calculate Class Type:
# 1. Ask the user to input the number
# 2. Validation input
# 3. Calculate Subnet ( A - 255.0.0.0, B - 255.255.0.0, C - 255.255.255.0)
# 4. Get Subner from CIDR
def determine_class(ip):
  ip_list = ip.split('.')
  octet = ip_list[0]
  octet = int(octet)
  if 0 <= octet <= 127:
    return 'Class A'
  elif 0 <= octet <= 127:
    return 'Class B'
  elif 128 <= octet <= 191:
    return 'Class C'
  elif 192 <= octet <= 223:
    return 'Class D'
  elif 224 <= octet <= 255:
    return 'Class E'
  else:
    return 'Something is wrong'

def class_bit(ip):
  det = determine_class(ip)
  if det == 'Class A':
    return 24
  elif det == 'Class B':
    return 16
  elif det == 'Class C':
    return 8
  else:
    return 'Not applicable'
# Inputs:
# 1. IP Address: A valid IPv4 address.
# 2. CIDR Notation (optional): If not provided, the tool infers it from the IP class.
# 3. Partitioning Preference: Whether the user wants to
# partition based on the number of hosts or subnets.
# 4. Number: Depending on the above choice, the number of hosts or subnets.
def get_hosts_number(ip, cidr):
    ip_class = determine_class(ip)
    hosts = 0
    cidr = int(cidr)
    if ip_class == 'Class A' or ip_class == 'Class B' or ip_class == 'Class C':
        hosts = 2 ** (32 - cidr) - 2
        return hosts

def get_subnets_number(ip, cidr):
    ip_class = class_bit(ip)
    if ip_class != 'Not applicable':
      subnets = 2 ** (cidr - ip_class)

def subnet_mask(cidr):
  subnet = '0.0.0.0'
  cidr = int(cidr)
  if 0 < cidr <= 8:
    subnet_list = subnet.split('.')
    octet = subnet_list[0]
    subnet_list[0] = str(256 - 2 ** (8 - cidr))
    subnetmask = '.'.join(subnet_list)
    return subnetmask
  elif 9 <= cidr <= 16:
    subnet_list = subnet.split('.')
    subnet_list[0] = '255'
    octet = subnet_list[1]
    subnet_list[1] = str(256 - (2 ** (16 - cidr)))
    subnetmask = '.'.join(subnet_list)
    return subnetmask
  elif 17 <= cidr <= 24:
    subnet_list = subnet.split('.')
    subnet_list[0] = '255'
    subnet_list[1] = '255'
    octet = subnet_list[2]
    subnet_list[2] = str(256 - (2 ** (24 - cidr)))
    subnetmask = '.'.join(subnet_list)
    return subnetmask
  elif 25 <= cidr <= 32:
    subnet_list = subnet.split('.')
    subnet_list[0] = '255'
    subnet_list[1] = '255'
    subnet_list[2] = '255'
    octet = subnet_list[3]
    subnet_list[3] = str(256 - (2 ** (32 - cidr)))
    subnetmask = '.'.join(subnet_list)
    return subnetmask
  else:
    return "Something is wrong"


def calculate_by_choice(ip, user_partition_choice, initial_class_cidr):
  if user_partition_choice == 'hosts':
    flag = True
    while flag:
      hosts_number = int(input("Enter the number of hosts you want in each network"))
      if

    flag = False
    bits = 0
    while not flag:
      if 2 ** bits > hosts_number and bits < (32 - initial_class_cidr)
        flag = True
        cidr = 32 - bits
        return cidr
      bits += 1
  elif user_partition_choice == 'subnets'
    subnets_number = int(input("Enter the number of subnets you want in each network"))



def partition_by_user_choice(ip)
  initial_cidr = class_bit(ip)
  partition_choice = input("Enter your partitioning choice (type hosts or subnets): ")
  while partition_choice != 'hosts' or partition_choice != 'subnets':
      partition_choice = input("Invalid partitioning choice (type hosts or subnets): ")
  calculate_by_choice(ip, partition_choice, initial_cidr)

  return cidr

# Outputs:
# 1. Subnet Mask: Displayed in decimal format.
# 2. CIDR Notation: (/24)
# 3. Number of Hosts: Total possible hosts in the subnet.
# 4. Number of Subnets: Total possible subnets.
# 5. Network and Broadcast Addresses: For the first two and the last two subnets.
# Usage:
# Provide the required inputs and get the relevant subnetting information in return.
def get_ip_info(ip,cidr):
  print(f' Class type: {determine_class(ip)}')
  print(f'Number of Avaliable Hosts: {get_hosts_number(ip, cidr)}')
  print(f'Number of Subnets: {get_subnets_number(ip, cidr)}')
  print(f'Subnet Mask: {subnet_mask(cidr)}')


def input_ip_cidr():
  ip = input("Enter an IP address (e.g., 192.168.1.1): ")
  while not ip_validate(ip):
    ip = input("Enter an VALID IP address (e.g., 192.168.1.1): ")

  cidr = input("Enter a CIDR block (e.g., 24): ")
  while not cidr_validate(cidr):
    if cidr == '':
      break;
    cidr = input("Enter a VALID CIDR block (e.g., 24): ")

  if cidr == '':
    cidr = partition_by_user_choice(ip)

  get_ip_info(ip, cidr)

input_ip_cidr()
