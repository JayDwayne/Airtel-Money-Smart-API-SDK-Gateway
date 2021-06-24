import os

URL = {}

# Sandbox Urls
URL["sandbox"] = {}
URL["sandbox"]["v1"] = {}
URL["sandbox"]["v1"]["activate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/activation" \
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["sandbox"]["v1"]["deactivate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/deactivation" \
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["production"]["v1"]["charge_subscriber"] = "https://{ip}:{port}/smartapi/services/payment/v1/charge"\
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["production"]["v1"]["discovery"] = "http://<IP>:<Port>/wli/sb/transports/http?siNumber=xxxxxxxxxx&lob=Mobility"\
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))

# Prod Urls
URL["production"] = {}
URL["production"]["v1"] = {}
URL["production"]["v1"]["activate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/activation" \
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["production"]["v1"]["deactivate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/deactivation" \
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["production"]["v1"]["charge_subscriber"] = "https://{ip}:{port}/smartapi/services/payment/v1/charge"\
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
URL["production"]["v1"]["discovery"] = "http://<IP>:<Port>/wli/sb/transports/http?siNumber=xxxxxxxxxx&lob=Mobility"\
    .format(ip=os.environ.get('SERVER_IP'), port=os.environ.get('SERVER_PORT'))
