import boto3
from botocore.exceptions import ClientError
class AWSClient :
    
    @staticmethod
    def get_parameter_store(name: str, region:str ='ap-south-2') :
        try:
            ssm_client = boto3.client('ssm', region_name=region)
            response = ssm_client.get_parameter(Name=name, WithDecryption=True)
            parameter_value = response['Parameter']['Value']
            return parameter_value 
        except ssm_client.exceptions.ParameterNotFound as e:
            raise Exception(f"Parameter does not exists. Name : {name}, Region : {region}") from e
        except ClientError as e:
            raise Exception(f"AWS client error occured in parameter store {e}") from e
        except Exception as e:
            raise Exception(f"Something went wrong error: {e}")
        