import yaml
from flathunter.sender_telegram import *

config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
t = SenderTelegram(config)
t.send_msg("foobar")
