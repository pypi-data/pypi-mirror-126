# coding: utf-8

"""
    NEF_Emulator

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UsageThreshold(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'duration': 'int',
        'total_volume': 'int',
        'downlink_volume': 'int',
        'uplink_volume': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'total_volume': 'totalVolume',
        'downlink_volume': 'downlinkVolume',
        'uplink_volume': 'uplinkVolume'
    }

    def __init__(self, duration=None, total_volume=None, downlink_volume=None, uplink_volume=None):  # noqa: E501
        """UsageThreshold - a model defined in Swagger"""  # noqa: E501
        self._duration = None
        self._total_volume = None
        self._downlink_volume = None
        self._uplink_volume = None
        self.discriminator = None
        if duration is not None:
            self.duration = duration
        if total_volume is not None:
            self.total_volume = total_volume
        if downlink_volume is not None:
            self.downlink_volume = downlink_volume
        if uplink_volume is not None:
            self.uplink_volume = uplink_volume

    @property
    def duration(self):
        """Gets the duration of this UsageThreshold.  # noqa: E501

        A period of time in units of seconds  # noqa: E501

        :return: The duration of this UsageThreshold.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UsageThreshold.

        A period of time in units of seconds  # noqa: E501

        :param duration: The duration of this UsageThreshold.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def total_volume(self):
        """Gets the total_volume of this UsageThreshold.  # noqa: E501

        A volume in units of bytes  # noqa: E501

        :return: The total_volume of this UsageThreshold.  # noqa: E501
        :rtype: int
        """
        return self._total_volume

    @total_volume.setter
    def total_volume(self, total_volume):
        """Sets the total_volume of this UsageThreshold.

        A volume in units of bytes  # noqa: E501

        :param total_volume: The total_volume of this UsageThreshold.  # noqa: E501
        :type: int
        """

        self._total_volume = total_volume

    @property
    def downlink_volume(self):
        """Gets the downlink_volume of this UsageThreshold.  # noqa: E501

        A volume in units of bytes  # noqa: E501

        :return: The downlink_volume of this UsageThreshold.  # noqa: E501
        :rtype: int
        """
        return self._downlink_volume

    @downlink_volume.setter
    def downlink_volume(self, downlink_volume):
        """Sets the downlink_volume of this UsageThreshold.

        A volume in units of bytes  # noqa: E501

        :param downlink_volume: The downlink_volume of this UsageThreshold.  # noqa: E501
        :type: int
        """

        self._downlink_volume = downlink_volume

    @property
    def uplink_volume(self):
        """Gets the uplink_volume of this UsageThreshold.  # noqa: E501

        A volume in units of bytes  # noqa: E501

        :return: The uplink_volume of this UsageThreshold.  # noqa: E501
        :rtype: int
        """
        return self._uplink_volume

    @uplink_volume.setter
    def uplink_volume(self, uplink_volume):
        """Sets the uplink_volume of this UsageThreshold.

        A volume in units of bytes  # noqa: E501

        :param uplink_volume: The uplink_volume of this UsageThreshold.  # noqa: E501
        :type: int
        """

        self._uplink_volume = uplink_volume

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UsageThreshold, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsageThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
