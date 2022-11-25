from uptime_kuma_api import UptimeKumaApi, MonitorType
from config import KumaConfig
import logging

def monitor_data(body):
    api = UptimeKumaApi(KumaConfig.url)
    api.login(KumaConfig.username, KumaConfig.password)
    notification_ids = []
    notifications = api.get_notifications()
    spec = body.get("spec")

    if spec.get("keyword"):
        monitor_type = MonitorType.KEYWORD
    else:
        monitor_type = MonitorType.HTTP

    request_body = {
        "type": monitor_type,
        "name": spec.get("name", body.get("metadata").get("name")),
        "accepted_statuscodes": [str(s) for s in spec.get('accepted_statuscodes')],
        "interval": spec.get('interval'),
        "upsideDown": spec.get('upsideDown'),
        "resendInterval": spec.get('resendInterval'),
        "keyword": spec.get('keyword'),
        "maxretries": spec.get('maxretries'),
        "maxredirects": spec.get('maxredirects'),
        "retryInterval": spec.get('retryInterval'),
        "expiryNotification": spec.get('expiryNotification'),
        "url": spec.get('url'),
        "ignoreTls": spec.get('ignoreTls'),
        "method": spec.get('method'),
        "body": spec.get('body'),
        "headers": spec.get('headers')
    }

    if spec.get("defaultNotifiers"):
        default_notifiers = [n["id"] for n in notifications if n["isDefault"]]
        notification_ids.extend(default_notifiers)

    if spec.get("notifiers"):
        notifiers = [
            n["id"]
            for n in api.get_notifications()
            if n["name"] in spec.get("notifiers")
        ]
        if not notifiers:
            logging.warn(f"notifiers {spec.get('notifiers')} not found")
        notification_ids.extend(notifiers)

    if not notification_ids:
        logging.warn(
            f"notification list is empty. there will be no notifications for this monitor"
        )

    request_body["notificationIDList"] = notification_ids

    return request_body
 



