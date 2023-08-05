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

class UECreate(object):
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
        'supi': 'str',
        'name': 'str',
        'description': 'str',
        'g_nb_id': 'int',
        'cell_id': 'int',
        'ip_address_v4': 'str',
        'ip_address_v6': 'str',
        'mac_address': 'str',
        'dnn': 'str',
        'mcc': 'int',
        'mnc': 'int',
        'external_identifier': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'speed': 'AllOfUECreateSpeed',
        'path_id': 'int'
    }

    attribute_map = {
        'supi': 'supi',
        'name': 'name',
        'description': 'description',
        'g_nb_id': 'gNB_id',
        'cell_id': 'Cell_id',
        'ip_address_v4': 'ip_address_v4',
        'ip_address_v6': 'ip_address_v6',
        'mac_address': 'mac_address',
        'dnn': 'dnn',
        'mcc': 'mcc',
        'mnc': 'mnc',
        'external_identifier': 'external_identifier',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'speed': 'speed',
        'path_id': 'path_id'
    }

    def __init__(self, supi=None, name=None, description=None, g_nb_id=None, cell_id=None, ip_address_v4='169.254.46.5', ip_address_v6='fe80::349d:33ff:fe76:2cee', mac_address=None, dnn=None, mcc=None, mnc=None, external_identifier=None, latitude=None, longitude=None, speed=None, path_id=None):  # noqa: E501
        """UECreate - a model defined in Swagger"""  # noqa: E501
        self._supi = None
        self._name = None
        self._description = None
        self._g_nb_id = None
        self._cell_id = None
        self._ip_address_v4 = None
        self._ip_address_v6 = None
        self._mac_address = None
        self._dnn = None
        self._mcc = None
        self._mnc = None
        self._external_identifier = None
        self._latitude = None
        self._longitude = None
        self._speed = None
        self._path_id = None
        self.discriminator = None
        self.supi = supi
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.g_nb_id = g_nb_id
        self.cell_id = cell_id
        if ip_address_v4 is not None:
            self.ip_address_v4 = ip_address_v4
        if ip_address_v6 is not None:
            self.ip_address_v6 = ip_address_v6
        if mac_address is not None:
            self.mac_address = mac_address
        if dnn is not None:
            self.dnn = dnn
        if mcc is not None:
            self.mcc = mcc
        if mnc is not None:
            self.mnc = mnc
        if external_identifier is not None:
            self.external_identifier = external_identifier
        self.latitude = latitude
        self.longitude = longitude
        if speed is not None:
            self.speed = speed
        if path_id is not None:
            self.path_id = path_id

    @property
    def supi(self):
        """Gets the supi of this UECreate.  # noqa: E501


        :return: The supi of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this UECreate.


        :param supi: The supi of this UECreate.  # noqa: E501
        :type: str
        """
        if supi is None:
            raise ValueError("Invalid value for `supi`, must not be `None`")  # noqa: E501

        self._supi = supi

    @property
    def name(self):
        """Gets the name of this UECreate.  # noqa: E501


        :return: The name of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UECreate.


        :param name: The name of this UECreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UECreate.  # noqa: E501


        :return: The description of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UECreate.


        :param description: The description of this UECreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def g_nb_id(self):
        """Gets the g_nb_id of this UECreate.  # noqa: E501


        :return: The g_nb_id of this UECreate.  # noqa: E501
        :rtype: int
        """
        return self._g_nb_id

    @g_nb_id.setter
    def g_nb_id(self, g_nb_id):
        """Sets the g_nb_id of this UECreate.


        :param g_nb_id: The g_nb_id of this UECreate.  # noqa: E501
        :type: int
        """
        if g_nb_id is None:
            raise ValueError("Invalid value for `g_nb_id`, must not be `None`")  # noqa: E501

        self._g_nb_id = g_nb_id

    @property
    def cell_id(self):
        """Gets the cell_id of this UECreate.  # noqa: E501


        :return: The cell_id of this UECreate.  # noqa: E501
        :rtype: int
        """
        return self._cell_id

    @cell_id.setter
    def cell_id(self, cell_id):
        """Sets the cell_id of this UECreate.


        :param cell_id: The cell_id of this UECreate.  # noqa: E501
        :type: int
        """
        if cell_id is None:
            raise ValueError("Invalid value for `cell_id`, must not be `None`")  # noqa: E501

        self._cell_id = cell_id

    @property
    def ip_address_v4(self):
        """Gets the ip_address_v4 of this UECreate.  # noqa: E501


        :return: The ip_address_v4 of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_v4

    @ip_address_v4.setter
    def ip_address_v4(self, ip_address_v4):
        """Sets the ip_address_v4 of this UECreate.


        :param ip_address_v4: The ip_address_v4 of this UECreate.  # noqa: E501
        :type: str
        """

        self._ip_address_v4 = ip_address_v4

    @property
    def ip_address_v6(self):
        """Gets the ip_address_v6 of this UECreate.  # noqa: E501


        :return: The ip_address_v6 of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_v6

    @ip_address_v6.setter
    def ip_address_v6(self, ip_address_v6):
        """Sets the ip_address_v6 of this UECreate.


        :param ip_address_v6: The ip_address_v6 of this UECreate.  # noqa: E501
        :type: str
        """

        self._ip_address_v6 = ip_address_v6

    @property
    def mac_address(self):
        """Gets the mac_address of this UECreate.  # noqa: E501


        :return: The mac_address of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this UECreate.


        :param mac_address: The mac_address of this UECreate.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def dnn(self):
        """Gets the dnn of this UECreate.  # noqa: E501


        :return: The dnn of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._dnn

    @dnn.setter
    def dnn(self, dnn):
        """Sets the dnn of this UECreate.


        :param dnn: The dnn of this UECreate.  # noqa: E501
        :type: str
        """

        self._dnn = dnn

    @property
    def mcc(self):
        """Gets the mcc of this UECreate.  # noqa: E501


        :return: The mcc of this UECreate.  # noqa: E501
        :rtype: int
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this UECreate.


        :param mcc: The mcc of this UECreate.  # noqa: E501
        :type: int
        """

        self._mcc = mcc

    @property
    def mnc(self):
        """Gets the mnc of this UECreate.  # noqa: E501


        :return: The mnc of this UECreate.  # noqa: E501
        :rtype: int
        """
        return self._mnc

    @mnc.setter
    def mnc(self, mnc):
        """Sets the mnc of this UECreate.


        :param mnc: The mnc of this UECreate.  # noqa: E501
        :type: int
        """

        self._mnc = mnc

    @property
    def external_identifier(self):
        """Gets the external_identifier of this UECreate.  # noqa: E501


        :return: The external_identifier of this UECreate.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this UECreate.


        :param external_identifier: The external_identifier of this UECreate.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def latitude(self):
        """Gets the latitude of this UECreate.  # noqa: E501


        :return: The latitude of this UECreate.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this UECreate.


        :param latitude: The latitude of this UECreate.  # noqa: E501
        :type: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this UECreate.  # noqa: E501


        :return: The longitude of this UECreate.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this UECreate.


        :param longitude: The longitude of this UECreate.  # noqa: E501
        :type: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def speed(self):
        """Gets the speed of this UECreate.  # noqa: E501

        This value decribes UE's speed. Possible values are \"STATIONARY\" (e.g, IoT device), \"LOW(e.g, pedestrian)\" and \"HIGH (e.g., vehicle)\"  # noqa: E501

        :return: The speed of this UECreate.  # noqa: E501
        :rtype: AllOfUECreateSpeed
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this UECreate.

        This value decribes UE's speed. Possible values are \"STATIONARY\" (e.g, IoT device), \"LOW(e.g, pedestrian)\" and \"HIGH (e.g., vehicle)\"  # noqa: E501

        :param speed: The speed of this UECreate.  # noqa: E501
        :type: AllOfUECreateSpeed
        """

        self._speed = speed

    @property
    def path_id(self):
        """Gets the path_id of this UECreate.  # noqa: E501


        :return: The path_id of this UECreate.  # noqa: E501
        :rtype: int
        """
        return self._path_id

    @path_id.setter
    def path_id(self, path_id):
        """Sets the path_id of this UECreate.


        :param path_id: The path_id of this UECreate.  # noqa: E501
        :type: int
        """

        self._path_id = path_id

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
        if issubclass(UECreate, dict):
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
        if not isinstance(other, UECreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
