from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import MonitorManagementClient
import os

# Azure Authentication
sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = MonitorManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)



def get_vms_in_resource_group(resource_group_name):
    vm_list = []
    
    vm_paged = client.virtual_machines.list(resource_group_name)
    for vm in vm_paged:
        vm_list.append(vm.name)
    
    return vm_list


def get_vm_metrics(vm_name, resource_group_name):
    metrics = client.virtual_machines.list_metrics(
        resource_group_name,
        vm_name,
        "Microsoft.Compute",
        "virtualMachines",
        timespan="PT1H",  # Last hour
        interval="PT5M",  # 5-minute intervals
        metricnames="Percentage CPU"
    )
    return metrics

