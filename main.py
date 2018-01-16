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
        # device.wait()

    def register_controller(self, controller):
        self.idle_controller = controller
        self.device.register_handler(controller)
        self.new_cast_status(self.device.status)

    def new_cast_status(self, status):
        print(status)
        if(status.is_stand_by and
                status.app_id == self.backdrop_id):
            self.on_idle_state(status)
        elif(status.app_id == self.new_idle_app_id and
             status.status_text == 'Reciever ready...'):
            self.on_idle_app_start()

    def on_idle_state(self, status):
        print("Starting idle app")
        self.device.start_app(self.new_idle_app_id)
        # print('Start_app sent')

    def on_idle_app_start(self):
        print('On Start Command')
        self.idle_controller.on_app_start()


def get_chromecast():
    chromecasts = pyc.get_chromecasts()
    cast = None
    if(len(chromecasts) == 0):
        cast = pyc.Chromecast('192.168.2.3')
    else:
        cast = chromecasts[0]
    cast.wait()
    return cast


def cast_website(web_site):
    cast = get_chromecast()
    raw_input('GET')
    idle_screen = cast_idle_sceen(cast, 'A27D4C78')
    raw_input('GET')
    controller = cont.DashboardController(web_site)
    raw_input('GET')
    idle_screen.register_controller(controller)

cast_website('http://google.nl')
raw_input('ENTER to quit')
print('exiting')
