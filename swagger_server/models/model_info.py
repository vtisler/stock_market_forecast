# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ModelInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, model_id: str=None, model_name: str=None, comment: str=None, dataset_id: int=None, status: str=None, training_time: int=None, created_at: str=None):  # noqa: E501
        """ModelInfo - a model defined in Swagger

        :param model_id: The model_id of this ModelInfo.  # noqa: E501
        :type model_id: str
        :param model_name: The model_name of this ModelInfo.  # noqa: E501
        :type model_name: str
        :param comment: The comment of this ModelInfo.  # noqa: E501
        :type comment: str
        :param dataset_id: The dataset_id of this ModelInfo.  # noqa: E501
        :type dataset_id: int
        :param status: The status of this ModelInfo.  # noqa: E501
        :type status: str
        :param training_time: The training_time of this ModelInfo.  # noqa: E501
        :type training_time: int
        :param created_at: The created_at of this ModelInfo.  # noqa: E501
        :type created_at: str
        """
        self.swagger_types = {
            'model_id': str,
            'model_name': str,
            'comment': str,
            'dataset_id': int,
            'status': str,
            'training_time': int,
            'created_at': str
        }

        self.attribute_map = {
            'model_id': 'modelId',
            'model_name': 'modelName',
            'comment': 'comment',
            'dataset_id': 'datasetId',
            'status': 'status',
            'training_time': 'trainingTime',
            'created_at': 'createdAt'
        }

        self._model_id = model_id
        self._model_name = model_name
        self._comment = comment
        self._dataset_id = dataset_id
        self._status = status
        self._training_time = training_time
        self._created_at = created_at

    @classmethod
    def from_dict(cls, dikt) -> 'ModelInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The modelInfo of this ModelInfo.  # noqa: E501
        :rtype: ModelInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model_id(self) -> str:
        """Gets the model_id of this ModelInfo.


        :return: The model_id of this ModelInfo.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id: str):
        """Sets the model_id of this ModelInfo.


        :param model_id: The model_id of this ModelInfo.
        :type model_id: str
        """

        self._model_id = model_id

    @property
    def model_name(self) -> str:
        """Gets the model_name of this ModelInfo.


        :return: The model_name of this ModelInfo.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name: str):
        """Sets the model_name of this ModelInfo.


        :param model_name: The model_name of this ModelInfo.
        :type model_name: str
        """

        self._model_name = model_name

    @property
    def comment(self) -> str:
        """Gets the comment of this ModelInfo.


        :return: The comment of this ModelInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this ModelInfo.


        :param comment: The comment of this ModelInfo.
        :type comment: str
        """

        self._comment = comment

    @property
    def dataset_id(self) -> int:
        """Gets the dataset_id of this ModelInfo.


        :return: The dataset_id of this ModelInfo.
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id: int):
        """Sets the dataset_id of this ModelInfo.


        :param dataset_id: The dataset_id of this ModelInfo.
        :type dataset_id: int
        """

        self._dataset_id = dataset_id

    @property
    def status(self) -> str:
        """Gets the status of this ModelInfo.


        :return: The status of this ModelInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ModelInfo.


        :param status: The status of this ModelInfo.
        :type status: str
        """

        self._status = status

    @property
    def training_time(self) -> int:
        """Gets the training_time of this ModelInfo.


        :return: The training_time of this ModelInfo.
        :rtype: int
        """
        return self._training_time

    @training_time.setter
    def training_time(self, training_time: int):
        """Sets the training_time of this ModelInfo.


        :param training_time: The training_time of this ModelInfo.
        :type training_time: int
        """

        self._training_time = training_time

    @property
    def created_at(self) -> str:
        """Gets the created_at of this ModelInfo.


        :return: The created_at of this ModelInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this ModelInfo.


        :param created_at: The created_at of this ModelInfo.
        :type created_at: str
        """

        self._created_at = created_at
