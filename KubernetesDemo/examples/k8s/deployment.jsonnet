function(app_conf)
  {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "%s-deployment" % app_conf.name
    },
    "spec": {
      "selector": {
        "matchLabels": {
          "app": app_conf.name
        }
      },
      "template": {
        "metadata": {
          "labels": {
            "app": app_conf.name
          }
        },
        "spec": {
          "containers": [
            {
              "name": app_conf.name,
              "image": "alwaysprep/flask-kubernetes",
              "ports": [
                {
                  "containerPort": app_conf.port
                }
              ]
            }
          ]
        }
      }
    }
  }
