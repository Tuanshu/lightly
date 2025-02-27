# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DockerWorkerConfig(object):
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
        'worker_type': 'DockerWorkerType',
        'docker': 'dict(str, object)',
        'lightly': 'dict(str, object)',
        'selection': 'SelectionConfig'
    }

    attribute_map = {
        'worker_type': 'workerType',
        'docker': 'docker',
        'lightly': 'lightly',
        'selection': 'selection'
    }

    def __init__(self, worker_type=None, docker=None, lightly=None, selection=None, _configuration=None):  # noqa: E501
        """DockerWorkerConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._worker_type = None
        self._docker = None
        self._lightly = None
        self._selection = None
        self.discriminator = None

        self.worker_type = worker_type
        self.docker = docker
        self.lightly = lightly
        if selection is not None:
            self.selection = selection

    @property
    def worker_type(self):
        """Gets the worker_type of this DockerWorkerConfig.  # noqa: E501


        :return: The worker_type of this DockerWorkerConfig.  # noqa: E501
        :rtype: DockerWorkerType
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        """Sets the worker_type of this DockerWorkerConfig.


        :param worker_type: The worker_type of this DockerWorkerConfig.  # noqa: E501
        :type: DockerWorkerType
        """
        if self._configuration.client_side_validation and worker_type is None:
            raise ValueError("Invalid value for `worker_type`, must not be `None`")  # noqa: E501

        self._worker_type = worker_type

    @property
    def docker(self):
        """Gets the docker of this DockerWorkerConfig.  # noqa: E501

        docker run configurations, keys should match the structure of https://github.com/lightly-ai/lightly-core/blob/develop/onprem-docker/lightly_worker/src/lightly_worker/resources/docker/docker.yaml   # noqa: E501

        :return: The docker of this DockerWorkerConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._docker

    @docker.setter
    def docker(self, docker):
        """Sets the docker of this DockerWorkerConfig.

        docker run configurations, keys should match the structure of https://github.com/lightly-ai/lightly-core/blob/develop/onprem-docker/lightly_worker/src/lightly_worker/resources/docker/docker.yaml   # noqa: E501

        :param docker: The docker of this DockerWorkerConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._docker = docker

    @property
    def lightly(self):
        """Gets the lightly of this DockerWorkerConfig.  # noqa: E501

        lightly configurations which are passed to a docker run, keys should match structure of https://github.com/lightly-ai/lightly/blob/master/lightly/cli/config/config.yaml   # noqa: E501

        :return: The lightly of this DockerWorkerConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._lightly

    @lightly.setter
    def lightly(self, lightly):
        """Sets the lightly of this DockerWorkerConfig.

        lightly configurations which are passed to a docker run, keys should match structure of https://github.com/lightly-ai/lightly/blob/master/lightly/cli/config/config.yaml   # noqa: E501

        :param lightly: The lightly of this DockerWorkerConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._lightly = lightly

    @property
    def selection(self):
        """Gets the selection of this DockerWorkerConfig.  # noqa: E501


        :return: The selection of this DockerWorkerConfig.  # noqa: E501
        :rtype: SelectionConfig
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """Sets the selection of this DockerWorkerConfig.


        :param selection: The selection of this DockerWorkerConfig.  # noqa: E501
        :type: SelectionConfig
        """

        self._selection = selection

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
        if issubclass(DockerWorkerConfig, dict):
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
        if not isinstance(other, DockerWorkerConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerWorkerConfig):
            return True

        return self.to_dict() != other.to_dict()
