load("@io_bazel_rules_jsonnet//jsonnet:jsonnet.bzl", "jsonnet_to_json")
load("@io_bazel_rules_k8s//k8s:objects.bzl", "k8s_objects")
load("@k8s_dev_deploy//:defaults.bzl", "k8s_dev_deploy")
load("@k8s_dev_service//:defaults.bzl", "k8s_dev_service")


package(default_visibility = ["//visibility:public"])

exports_files([
        "app_b.conf.json"
])

jsonnet_to_json(
    name = "deployment_json",
    src = "//examples/k8s:deployment.jsonnet",
    outs = ["cusa.deployment.json"],
    tla_code_files = {":app_b.conf.json": "app_conf"}
)


jsonnet_to_json(
    name = "service_json",
    src = "//examples/k8s:service.jsonnet",
    outs = ["cusa.service.json"],
    tla_code_files = {":app_b.conf.json": "app_conf"}
)


k8s_dev_service(
    name = "service",
    template = ":service_json",
)


k8s_dev_deploy(
    name = "deployment",
    template = ":deployment_json",
    images = {
        "alwaysprep/flask-kubernetes": "//examples/apps/app_b/docker:app"
    }
)

k8s_objects(
    name="app_b",
    objects = [
        ":deployment",
        ":service"
    ]
)

