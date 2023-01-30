function(app_conf)
  {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
      "name": "%s-service" % app_conf.name
    },
    "spec": {
      "selector": {
        "app": app_conf.name
      },
      "ports": [
        {
          "port": app_conf.port,
          "targetPort": app_conf.port
        }
      ],
      "type": "LoadBalancer"
    }
  }
