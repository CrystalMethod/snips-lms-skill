from LMSTools import LMSServer, LMSPlayer
from snipslms.shared.use_case import UseCase


class MuteUseCase(UseCase):

    def __init__(self, device_discovery_service, device_transport_control_service):
        self.device_discovery_service = device_discovery_service
        self.device_transport_control_service = device_transport_control_service

    def process_request(self, request_object):
        """

        :param request_object:
        :return:
        """