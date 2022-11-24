load('ext://namespace', 'namespace_create', 'namespace_inject')
load('ext://syncback', 'syncback')

namespace = os.getenv('NAMESPACE', default='kuma-controller')

namespace_create(namespace)
local_resource('k8s-namespace', cmd="kubectl ns kuma-controller")

docker_build('harbor.k8s.libraries.psu.edu/library/kuma-operator', '.', live_update=[
  sync('.', '/app')
])

k8s_yaml(namespace_inject('./deploy/deployment.yaml', namespace))
k8s_yaml(namespace_inject('./deploy/crd.yaml', namespace))
k8s_yaml(namespace_inject('./deploy/rbac.yaml', namespace))


syncback('syncback', 'deploy/kuma-controller',
         '/app/',
         target_dir='.'
         )