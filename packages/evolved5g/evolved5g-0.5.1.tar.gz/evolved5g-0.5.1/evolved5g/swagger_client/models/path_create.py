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

class PathCreate(object):
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
        'description': 'str',
        'points': 'list[Point]',
        'start_point': 'Point',
        'end_point': 'Point',
        'color': 'str'
    }

    attribute_map = {
        'description': 'description',
        'points': 'points',
        'start_point': 'start_point',
        'end_point': 'end_point',
        'color': 'color'
    }

    def __init__(self, description=None, points=None, start_point=None, end_point=None, color=None):  # noqa: E501
        """PathCreate - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._points = None
        self._start_point = None
        self._end_point = None
        self._color = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if points is not None:
            self.points = points
        if start_point is not None:
            self.start_point = start_point
        if end_point is not None:
            self.end_point = end_point
        if color is not None:
            self.color = color

    @property
    def description(self):
        """Gets the description of this PathCreate.  # noqa: E501


        :return: The description of this PathCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PathCreate.


        :param description: The description of this PathCreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def points(self):
        """Gets the points of this PathCreate.  # noqa: E501


        :return: The points of this PathCreate.  # noqa: E501
        :rtype: list[Point]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this PathCreate.


        :param points: The points of this PathCreate.  # noqa: E501
        :type: list[Point]
        """

        self._points = points

    @property
    def start_point(self):
        """Gets the start_point of this PathCreate.  # noqa: E501


        :return: The start_point of this PathCreate.  # noqa: E501
        :rtype: Point
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this PathCreate.


        :param start_point: The start_point of this PathCreate.  # noqa: E501
        :type: Point
        """

        self._start_point = start_point

    @property
    def end_point(self):
        """Gets the end_point of this PathCreate.  # noqa: E501


        :return: The end_point of this PathCreate.  # noqa: E501
        :rtype: Point
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this PathCreate.


        :param end_point: The end_point of this PathCreate.  # noqa: E501
        :type: Point
        """

        self._end_point = end_point

    @property
    def color(self):
        """Gets the color of this PathCreate.  # noqa: E501


        :return: The color of this PathCreate.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this PathCreate.


        :param color: The color of this PathCreate.  # noqa: E501
        :type: str
        """

        self._color = color

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
        if issubclass(PathCreate, dict):
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
        if not isinstance(other, PathCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
