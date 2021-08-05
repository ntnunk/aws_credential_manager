import os
import boto3
import configparser

from pathlib import Path

def get_local_aws_config() -> configparser.ConfigParser:
    path = os.path.join(str(Path.home()), '.aws', 'credentials')
    config = configparser.ConfigParser()
    if os.path.exists(path):
        config.read(path)
    return config

def get_local_accounts() -> list:
    config = get_local_aws_config()
    if config is None:
        return []
    return config.sections()

def get_aws_regions() -> list:
    regions_file = os.path.join(str(Path.home()), '.aws', 'regions')
    if not os.path.exists(regions_file):
        return ['eu-west-1', 'us-east-1']

    regions = []
    f = open(regions_file, 'r')
    for line in f.readlines():
        regions.append(str.strip(line))
    return regions

def update_aws_regions(region, account) -> dict:
    session = boto3.Session(profile_name=account)
    client = session.client('ec2')

    try:
        response: dict = client.describe_regions()
    except Exception as e:
        if type(e).__name__ == 'ClientError':
            if 'RequestExpired' in str(e):
                return {'success': False, 'error': 'RequestExpired' }
        return {'success': False, 'error': e}

    regions = []
    if 'Regions' in response.keys():
        regions = response['Regions']
    else:
        return {'success': False, 'error': regions}

    path = os.path.join(str(Path.home()), '.aws', 'regions')
    f = open(path, 'w')
    for region in regions:
        f.write(f"{region['RegionName']}\n")
    f.close()
    return {'success': True, 'error': None}

def get_profile_region(profile: str) -> str:
    config = get_local_aws_config()
    if not config.has_section(profile):
        return ''

    if not config.has_option(profile, 'region'):
        return ''
    return config.get(profile, 'region')

def parse_input(account: str, region: str, creds: str) -> bool:
    credentials = get_creds_platform(creds)
    if len(credentials.keys()) >= 3:
        return save_credentials(account, region, credentials)
    return False

def get_creds_platform(creds: str) -> dict:
    credentials = None
    lines = str.split(creds, '\n')
    if len(lines) < 3:
        print('Something is wrong with the pasted credentials.')

    line = str.strip(lines[0])
    if line[0] == '[': 
        if len(lines) >= 4:
            credentials = parse_cred_file_credentials(lines)
        else:
            print("It looks like a config file credentials were copied but there are't enough lines.")
            return {}
    elif str.find(line, '=') == -1:
        print(f'Unrecognized line: "{line}"')
        return {}

    tokens = str.split(line, '=')
    if tokens[0][0:7] == 'export ':
        credentials = parse_unix_credentials(lines)
    elif tokens[0][0:4] == 'SET ':
        credentials = parse_windows_credentials(lines)
    elif tokens[0][0:5] == '$Env:':
        credentials = parse_powershell_credentials(lines)
    return credentials

def parse_cred_file_credentials(credentials: list) -> dict:
    creds = {}
    for line in credentials:
        if line[0] == '[':
            continue
        tokens = str.split(line, '=')
        if len(tokens) < 2:
            return {}
        key = str.strip(tokens[0]).lower()
        creds[key] = str.replace(tokens[1], '"', '').str.strip(tokens[1])
    return creds

def parse_windows_credentials(credentials: list) -> dict:
    creds = {}
    for line in credentials:
        tokens = str.split(line, '=')
        key = tokens[0][4:].lower()
        creds[key] = str.replace(tokens[1], '"', '')
    return creds

def parse_unix_credentials(credentials: list) -> dict:
    creds = {}
    for line in credentials:
        tokens = str.split(line, '=')
        key = tokens[0][7:].lower()
        creds[key] = str.replace(tokens[1], '"', '')
    return creds

def parse_powershell_credentials(credentials: list) -> dict:
    creds = {}
    for line in credentials:
        tokens = str.split(line, '=')
        key = tokens[0][5:].lower()
        creds[key] = str.replace(tokens[1], '"', '')
    return creds

def save_credentials(account: str, region: str, credentials: dict) -> bool:
    config = get_local_aws_config()
    if not config.has_section(account):
        config.add_section(account)

    for key, value in credentials.items():
        config.set(account, key, value)

    config.set(account, 'region', region)

    path = os.path.join(str(Path.home()), '.aws')
    if not os.path.exists(path):
        os.makedirs(path)
    path = os.path.join(path, 'credentials')
    f = open(path, 'w')
    config.write(f)
    return True


