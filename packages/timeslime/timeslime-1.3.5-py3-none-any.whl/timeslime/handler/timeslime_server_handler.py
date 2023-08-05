"""handler to a timeslime-server"""
from datetime import datetime
from urllib.parse import urljoin

from requests import get, post

from timeslime.models import Setting, SettingResponse, Timespan, TimespanResponse
from timeslime.serializer import SettingSerializer, TimespanSerializer


class TimeslimeServerHandler():
    """handler to a timeslime-server"""
    def __init__(self, server_url):
        self.server_url = server_url
        self.timespan_route = urljoin(self.server_url, "api/v1/timespans")
        self.setting_route = urljoin(self.server_url, "api/v1/settings")

    def send_setting(self, setting: Setting) -> Setting:
        """send a POST request to create a setting"""
        if setting is None or setting.key is None:
            raise TypeError

        if not self.server_url:
            return setting

        setting_serializer = SettingSerializer()
        data = setting_serializer.serialize(setting)
        response = post(self.setting_route, json=data)
        response.raise_for_status()
        response_setting = setting_serializer.deserialize(response.json())

        return response_setting

    def send_setting_list(self, settings: list) -> list:
        """send a POST request to create a setting"""
        if settings is None:
            raise TypeError

        if isinstance(settings, Setting):
            settings = [settings]

        if not self.server_url:
            return settings

        setting_serializer = SettingSerializer()
        data = setting_serializer.serialize_list(settings)
        response = post(self.setting_route, json=data)
        response.raise_for_status()

        settings = []
        for setting in response.json():
            try:
                settings.append(setting_serializer.deserialize(setting))
            except KeyError:
                pass

        return settings

    def get_settings(self, date: datetime = None) -> SettingResponse:
        """send a GET request to get all settings"""
        if not self.server_url:
            return SettingResponse()

        response = get(self.setting_route, json={"filter_datetime": str(date)})
        response.raise_for_status()

        setting_serializer = SettingSerializer()
        settings = []
        response_json = response.json()
        for setting in response_json["data"]:
            try:
                settings.append(setting_serializer.deserialize(setting))
            except KeyError:
                pass

        setting_response = SettingResponse()
        setting_response.settings = settings
        setting_response.request_time = datetime.strptime(
            response_json["request_time"], "%Y-%m-%d %H:%M:%S.%f"
        )

        return setting_response

    def send_timespan(self, timespan: Timespan) -> Timespan:
        """send a POST request to create a timespan"""
        if timespan is None or timespan.start_time is None:
            raise TypeError

        if not self.server_url:
            return timespan

        timespan_serializer = TimespanSerializer()
        data = timespan_serializer.serialize(timespan)
        response = post(self.timespan_route, json=data)
        response.raise_for_status()
        response_timespan = timespan_serializer.deserialize(response.text)

        return response_timespan

    def send_timespan_list(self, timespans: list) -> list:
        """send a POST request to create timespans"""
        if timespans is None:
            raise TypeError

        if isinstance(timespans, Timespan):
            timespans = [timespans]

        if not self.server_url:
            return timespans

        timespan_serializer = TimespanSerializer()
        data = timespan_serializer.serialize_list(timespans)
        response = post(self.timespan_route, json=data)
        response.raise_for_status()

        timespans = []
        for timespan in response.json():
            try:
                timespans.append(timespan_serializer.deserialize(timespan))
            except KeyError:
                pass

        return timespans

    def get_timespans(self, date: datetime = None) -> TimespanResponse:
        """send a GET request to get all timespans"""
        if not self.server_url:
            return TimespanResponse()

        response = get(self.timespan_route, json={"filter_datetime": str(date)})
        response.raise_for_status()

        timespan_serializer = TimespanSerializer()
        timespans = []
        response_json = response.json()
        for timespan in response_json["data"]:
            try:
                timespans.append(timespan_serializer.deserialize(timespan))
            except KeyError:
                pass

        timespan_response = TimespanResponse()
        timespan_response.timespans = timespans
        timespan_response.request_time = datetime.strptime(
            response_json["request_time"], "%Y-%m-%d %H:%M:%S.%f"
        )

        return timespan_response
