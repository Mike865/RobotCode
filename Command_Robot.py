import requests
import asyncio
from urllib.parse import urlparse

def get_ports(http_url):
    # Example HTTP URL
    # Parse the URL
    parsed_url = urlparse(http_url)
    # Get the port number (defaulting to 80 if not specified)
    port_num = parsed_url.port or 80
    # Print the port number
    return port_num

async def APICall(ip_address):
    try:
        # Make an asynchronous GET request using requests library
        response = await asyncio.to_thread(requests.get, ip_address)

        # Check if the response status code is in the 2xx range (indicating success)
        if 200 <= response.status_code < 300:
            # Read and return the response body as a string
            return response.text
        else:
            # Handle non-successful responses here if needed
            print(f"Request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        # Handle exceptions here if needed
        print(f"An error occurred: {str(e)}")
        return None

session = requests.Session()
client = session
base_address = '192.168.0.1'
baseIP = 'http://' + base_address
port = get_ports(baseIP)
baseIP = 'http://' + base_address + ':'+str(port) + '/'
robot_head = baseIP + 'motor?id='
robot_motion = baseIP + 'motion/'

def walk_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_left'))
    if response_body:
        print(f"Response Body: {response_body}")

def walk_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_right'))
    if response_body:
        print(f"Response Body: {response_body}")

def walk_forward_short(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_short'))
    if response_body:
        print(f"Response Body: {response_body}")

def turn_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_right'))
    if response_body:
        print(f"Response Body: {response_body}")

def turn_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_left'))
    if response_body:
        print(f"Response Body: {response_body}")

def sit_down(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'sit_down'))
    if response_body:
        print(f"Response Body: {response_body}")

def standing_position(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'reset'))
    if response_body:
        print(f"Response Body: {response_body}")

def walking_position(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'basic_motion'))
    if response_body:
        print(f"Response Body: {response_body}")



# Usage
#response_body = asyncio.run(APICall(baseIP))
#if response_body:
#    print(f"Response Body: {response_body}")
