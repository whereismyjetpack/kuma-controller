import kopf
import logging
from uptime_kuma_api import UptimeKumaApi, MonitorType
from config import KumaConfig
import sys
from monitors import monitor_data


@kopf.on.delete("uptimekumahttpmonitors")
def delete_fn(body, **kwargs):
    api = UptimeKumaApi(KumaConfig.url)
    api.login(KumaConfig.username, KumaConfig.password)
    monitor_id = body.status.get("create_fn", {}).get("monitorID")
    result = api.delete_monitor(monitor_id)
    return result


@kopf.on.update("uptimekumahttpmonitors")
@kopf.on.create("uptimekumahttpmonitors")
def create_fn(body, **kwargs):
    api = UptimeKumaApi(KumaConfig.url)
    api.login(KumaConfig.username, KumaConfig.password)
    monitor_id = body.status.get("create_fn", {}).get("monitorID")
    request_body = monitor_data(body)

    if monitor_id:
        result = api.edit_monitor(monitor_id, **request_body)
    else:
        result = api.add_monitor(**request_body)

    return result


@kopf.on.cleanup()
async def cleanup_fn(logger, **kwargs):
    sys.exit(0)
    pass
