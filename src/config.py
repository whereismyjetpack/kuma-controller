import os


class KumaConfig():
  url = os.environ.get('UPTIME_KUMA_URL')
  username = os.environ.get('UPTIME_KUMA_USERNAME')
  password = os.environ.get('UPTIME_KUMA_PASSWORD')



