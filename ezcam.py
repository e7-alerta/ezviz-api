from pyezviz import EzvizClient, EzvizCamera

if __name__ == '__main__':

    client = EzvizClient(
        account='e7canasta@gmail.com',
        password='sdnadmin4',
        url='apiisa.ezvizlife.com'
    )

    client.login()

    print(f" token generated: {client.get_token()}")

    print(f" devices :  {client.get_device()}")
    # print(f" devices :  {client.get_device()}")
    # print(f" devices :  {client.get_device_infos('BA4755780')}")
    print(f" devices :  {client.get_device_infos('BA6594418')}")

    client.load_cameras()

    # print(f" cameras :  {client.get_cameras()}")

    # camera = client.get_camera('BA4755780')

    # print(f" camera :  {camera}")

    # print(f" status : {camera.status()}")

    # camera = EzvizCamera(client, "BA4755780", client.get_device_infos("BA4755780"))
    camera = EzvizCamera(client, "BA7069394", client.get_device_infos("BA7069394"))

    print(f" camera :  {camera.status()}")

    print(f" camera :  {camera.get_alarm_list()}")

    # camera.collect_image()

    response = camera.get_image()

    print(f" photos :  {response}")

