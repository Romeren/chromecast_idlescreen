import pychromecast as pyc
import controller as cont
import time


class cast_idle_sceen(object):

    def __init__(self, device, new_idle_app_id):
        self.backdrop_id = 'E8C28D3C'
        self.device = device
        self.socket_client = self.device.socket_client

        self.receiver_controller = self.socket_client.receiver_controller
        self.receiver_controller.register_status_listener(self)
        self.new_idle_app_id = new_idle_app_id

    def register_controller(self, controller):
        self.idle_controller = controller
        self.device.register_handler(controller)

    def new_cast_status(self, status):
        print(status)
        if(status.is_stand_by and status.app_id == self.backdrop_id):
            self.on_idle_state(status)
        if(status.is_stand_by and
                status.app_id == self.new_idle_app_id and
                status.status_text == 'Reciever ready...'):
            self.on_idle_app_start()

    def on_idle_state(self, status):
        # print(status)
        print("Starting idle app")
        self.device.start_app(self.new_idle_app_id)
        print("DONE starting")

    def on_idle_app_start(self):
        print('On Start Command')
        self.idle_controller.on_app_start()

chromecasts = pyc.get_chromecasts()

idle_screen = cast_idle_sceen(chromecasts[0], 'F6EF1BA7')

controller = cont.DashboardController('http://192.168.123.23:8080/home')
idle_screen.register_controller(controller)
