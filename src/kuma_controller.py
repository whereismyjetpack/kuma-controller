import kopf
import logging
from uptime_kuma_api import UptimeKumaApi, MonitorType
from config import KumaConfig

@kopf.on.delete('uptimekumahttpmonitors')
def delete_fn(body, **kwargs):
    monitor_id = body.status.get('create_fn').get('monitorID')
    api = UptimeKumaApi(KumaConfig.url)
    api.login(KumaConfig.username, KumaConfig.password)
    result = api.delete_monitor(monitor_id)
    return result


@kopf.on.create('uptimekumahttpmonitors')
def create_fn(body, **kwargs):
    spec = body.get('spec')
    url = spec.get('url')
    interval = spec.get('interval')
    name = spec.get('name', body.get('metadata').get('name'))
    

    api = UptimeKumaApi(KumaConfig.url)
    api.login(KumaConfig.username, KumaConfig.password)
    result = api.add_monitor(
        type=MonitorType.HTTP,
        name=name,
        url=url,
        interval=interval,
    )

    return result