import attr


class DlmsWrapper:

    def __init__(self, source_wport, destination_wport, version=1):
        self.source_wport = source_wport
        self.destination_wport = destination_wport
        self.version = version


class DlmsPushMessage:
    BASE_TOPIC = 'new_dlms_push_message'

    def __init__(self, payload: bytes, dlms_wrapper: DlmsWrapper,
                 transport: str, source_address: str, source_port: int,
                 application_context: str):
        self.payload = payload
        self.dlms_wrapper = dlms_wrapper
        self.transport = transport
        self.source_address = source_address
        self.source_port = source_port
        self.application_context = application_context

    def format_topic(self, schema_version):
        return (
            f'{self.BASE_TOPIC}'
            # f'.{self.source_address}'
            # f'.{self.source_port}'
            f'.{schema_version}'
        )


class MeterValue:
    """
    New Meter Value are meter readings for input in Utilitarian. They
    have not yet been validated and not all information is known about them.

    :param str meter: Meter Identification.name of the
        meter.

    :param str series: Meter Reading Series name. What series on the meter this
        value refers to.
    :param str timestamp: Time when the value was registered.
    :param str value: Value

    """
    BASE_TOPIC = 'new_meter_value'

    def __init__(self, meter, series, timestamp, value):

        self.meter = meter
        self.series = series
        self.timestamp = timestamp
        self.value = value

        # TODO: handle dots in series name.

    def format_topic(self, schema_version):
        return (
            f'{self.BASE_TOPIC}'
            f'.{self.meter}'
            f'.{self.series}'
            f'.{schema_version}'
        )
