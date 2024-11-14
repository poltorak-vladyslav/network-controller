import requests

class RyuControllerAPI:
    def __init__(self, controller_ip='127.0.0.1', controller_port=8080):
        self.base_url = f"http://{controller_ip}:{controller_port}"

    def get_switches(self):
        url = f"{self.base_url}/v1.0/topology/switches"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні комутаторів: {e}")
            return None

    def display_switches_info(self):
        switches = self.get_switches()
        if switches:
            print("Комутатори підключені до контролера:")
            for switch in switches:
                print(f"\nКомутатор DPID: {switch['dpid']}")
                print(f"  Кількість хостів: {len(switch['ports'])}")
                for port in switch['ports']:
                    print(f"    Хост: {port['name']}")
                    print(f"      - Номер: {port['port_no']}")
                    print(f"      - MAC-адреса: {port['hw_addr']}")
        else:
            print("Не знайдено жодного комутатора.")

if __name__ == "__main__":
    controller_api = RyuControllerAPI(controller_ip="127.0.0.1", controller_port=8080)
    controller_api.display_switches_info()