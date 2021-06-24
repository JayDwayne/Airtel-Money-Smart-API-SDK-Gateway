#!/usr/bin/python

"""
Airtel Money Rest API for Python
"""
import json
import os
import logging
import requests

from airtel.urls import URL

logger = logging.getLogger()


class RequestHandler:
    def __init__(self, access_token, env=os.environ.get('ENV'), version="v1", timeout=None):
        self.headers = {"Authorization": "Bearer %s" % access_token}
        self.env = env
        self.version = version
        self.timeout = timeout

    def make_request(self, url, payload, method):
        """
        Invoke url and return a python request object.
        :param url:
        :param payload:
        :param method:
        :return response (obj):
        """
        if self.timeout:
            return requests.request(method, url, headers=self.headers, json=payload,
                                    timeout=self.timeout)
        else:
            return requests.request(method, url, headers=self.headers, json=payload)


class Auth:
    def __init__(self, token, env=os.environ.get('ENV'), version="v1", timeout=None):
        self.headers = {
            "Authorization": "Basic %s" % token,
            "Content-type": "application/x-www-form-urlencoded"
        }
        self.env = env
        self.version = version
        self.timeout = timeout

    def generate_access_token(self):
        """
        https://<IP><Port>/smartapi/services/oauth/v1/token
        :return:
        """
        url = URL[self.env][self.version]["activate_subscription"]
        data = {
            "grant_type": "authorization_code&client_id=d6340cac48f764ae2735aa3b0220c762&redire",
            "ct_uri": "http://merchant.site.com/webservice/callback&code=550e8400-e29b-41d4- a716-446655440000",
            "code": "",
            "redirect_uri": "client_id"
        }
        r = requests.request("POST", url, headers=self.headers, json=json.dumps(data), timeout=self.timeout)
        return r


class Subscription:
    def __init__(self):
        pass

    @staticmethod
    def request(access_token):
        base = RequestHandler(access_token)
        return base

    def activate_subscription(self, data):
        """,
        Activate Subscription:
        https://<IP><Port>/smartapi/services/subscription/v1/activation
        This method activates a subscription for the subscriber identified by the token
        and the channel. Status notification is sent to the subscriber.
        :param data:
        :return response:
        """
        expected_keys = ["channel"]
        payload = process_data(expected_keys, data)
        url = URL[self.env][self.version]["activate_subscription"]
        r = self.make_request(url, payload, "POST")
        if r.status_code != 200:
            logger.error("Activate Subscription has not been completed")
        response = r.json()
        return response

    def deactivate_subscription(self, data):
        """
        Deactivate Subscription:
        This method deactivates a subscription for the subscriber.
        Status notification is sent to the subscriber.
        :param data:
        :return response:
        """
        expected_keys = ["address", "productId"]
        payload = process_data(expected_keys, data)
        url = URL[self.env][self.version]["deactivate_subscription"]
        r = self.make_request(url, payload, "POST")
        if r.status_code != 200:
            logger.error("Deactivate Subscription has not been completed")
        response = r.json()
        return response


class Payment:
    def charge_subscriber(self, data):
        """
        Charge a subscriber:
        https://<IP><Port>/smartapi/services/payment/v1/charge
        This method charges a subscriber for a service provided by your application.
        By default the charge will be applied immediately and a suitable response
        returned to the initial request.
        :param data:
        :return response:
        """
        expected_keys = ["channel", "cpTransactionId", "resourceUrl", "amount"]
        payload = process_data(expected_keys, data)
        url = URL[self.env][self.version]["charge_subscriber"]
        r = self.make_request(url, payload, "POST")
        if r.status_code != 200:
            logger.error("Charge subscriber has not been completed")
        response = r.json()
        return response


class OperatorDiscovery(Base):
    def discovery(self, data):
        """
        This API enables the partners to fetch the operator and circle details for
        the given mobile number.
        http://<IP>:<Port>/wli/sb/transports/http?siNumber=xxxxxxxxxx&lob=Mobility
        :param data:
        :return:
        """
        expected_keys = ["channel", "cpTransactionId", "resourceUrl", "amount"]
        payload = process_data(expected_keys, data)
        url = URL[self.env][self.version]["charge_subscriber"]
        r = self.make_request(url, payload, "GET")
        if r.status_code != 200:
            logger.error("Charge subscriber has not been completed")
        response = r.json()
        return response


def process_data(expected_keys, data):
    """
    Check for any expected but missing keyword arguments
    and raise a TypeError else return the keywords arguments
    repackaged in a dictionary i.e the payload.
    :param expected_keys:
    :param data:
    :return payload:
    """
    payload = {}
    for key in expected_keys:
        value = data.pop(key, False)
        if not value:
            raise TypeError("Missing value on key {0}".format(key))
        else:
            payload[key] = value
    return payload
