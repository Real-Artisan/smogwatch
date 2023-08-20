from azure_monitor import get_vm_metrics, get_vms_in_resource_group
from dynatrace_integration import fetch_dynatrace_metrics
from splunk_integration import send_data_to_splunk
from pagerduty_integration import create_pagerduty_incident
from slack_integration import send_slack_alert

threshold = 70
resource_group_name = ""

def main():
    # Azure Monitoring
    metrics = []
    vms = get_vms_in_resource_group(resource_group_name)
    for vm_name in vms:
       metrics.append(get_vm_metrics(vm_name, resource_group_name=resource_group_name))
    
    # Dynatrace Integration
    dynatrace_metrics = fetch_dynatrace_metrics()

    # Splunk Integration
    send_data_to_splunk(azure_metrics + dynatrace_metrics)

    # PagerDuty Integration
    for azure_metrics in metrics:
        if sum(azure_metrics) > threshold:
            create_pagerduty_incident("High resource utilization detected.")

    # Slack Integration
    for azure_metrics in metrics:
        if any(metric > threshold for metric in azure_metrics):
            send_slack_alert("Resource utilization is above threshold.")

if __name__ == "__main__":
    main()
