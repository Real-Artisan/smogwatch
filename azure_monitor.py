from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient, MonitorManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = MonitorManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)


def get_vm_metrics(resource_group, vm_name):
    # Fetch and process VM metrics
    pass
