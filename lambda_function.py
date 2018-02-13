from storage.RDSClient import RDSClient


def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    client = RDSClient.instance()
