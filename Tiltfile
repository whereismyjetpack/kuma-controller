load('ext://namespace', 'namespace_create', 'namespace_inject')
load('ext://syncback', 'syncback')
load('ext://secret', 'secret_from_dict')
namespace = os.getenv('NAMESPACE', default='kuma-controller')

namespace_create(namespace)
local_resource('k8s-namespace', cmd="kubectl ns kuma-controller")

docker_build('harbor.k8s.libraries.psu.edu/library/kuma-operator', '.', live_update=[
  sync('.', '/app')
])

k8s_yaml(namespace_inject('./deploy/deployment.yaml', namespace))
k8s_yaml(namespace_inject('./deploy/crd.yaml', namespace))
k8s_yaml(namespace_inject('./deploy/rbac.yaml', namespace))

k8s_yaml(secret_from_dict("kuma-controller", inputs = {
    'UPTIME_KUMA_URL' : os.getenv('UPTIME_KUMA_URL'),
    'UPTIME_KUMA_USERNAME' : os.getenv('UPTIME_KUMA_USERNAME'),
    'UPTIME_KUMA_PASSWORD' : os.getenv('UPTIME_KUMA_PASSWORD')
}))

syncback('syncback', 'deploy/kuma-controller',
         '/app/',
         target_dir='.'
         )