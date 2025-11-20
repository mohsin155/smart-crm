from src.infrastructure.integrations.aws_client import AWSClient
from unittest.mock import patch, MagicMock
import json
from botocore.exceptions import ClientError
import pytest

@patch("src.infrastructure.integrations.aws_client.boto3.client")
def test_get_parameter_store_success(mock_boto):
    ssm_mock = MagicMock()
    ssm_mock.get_parameter.return_value = {
        "Parameter": {"Value": json.dumps({"config": "value"})}
    }
    mock_boto.return_value = ssm_mock

    result = AWSClient.get_parameter_store("test", region="ap-south-2")
    assert result == {"config": "value"}

@patch("src.infrastructure.integrations.aws_client.boto3.client")
def test_get_parameter_store_error(mock_boto):
    ssm_mock = MagicMock()
    class FakeExceptions:
        class ParameterNotFound(Exception):
            pass

    ssm_mock.exceptions = FakeExceptions

    error_response = {
        "Error": {
            "Code": "Invalid Parameter",
            "Message": "Invalid Parameter"
        }
    }   
    ssm_mock.get_parameter.side_effect = ClientError(error_response, "GetParameter")
    mock_boto.return_value = ssm_mock

    with pytest.raises(Exception) as exc:
        AWSClient.get_parameter_store("test", region="ap-south-2")

    assert "AWS client error occured in parameter store " in str(exc.value)

@patch("src.infrastructure.integrations.aws_client.boto3.client")
def test_get_parameter_store_code_error(mock_data):
    ssm_mock = MagicMock()

    class FakeExcetions:
        class ParameterNotFound(Exception):
            pass
    ssm_mock.exceptions = FakeExcetions    

    ssm_mock.get_parameter.side_effect = Exception("Something went wrong")

    mock_data.return_value = ssm_mock

    with pytest.raises(Exception) as exc:
        AWSClient.get_parameter_store("test")

    assert "Something went wrong" in str(exc.value)    