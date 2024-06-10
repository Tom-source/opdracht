locals {
  hf_token = var.hf_token
}

resource "aws_apprunner_service" "chatbot" {
  service_name = "chatbot"

  source_configuration {
    image_repository {
      image_configuration {
        runtime_environment_variables = {
          HUGGINGFACEHUB_API_TOKEN = local.hf_token
        }
      }
      image_identifier      = "public.ecr.aws/k4w0q8w8/mlops-course-ehb:1" # Ensure this is the correct image
      image_repository_type = "ECR_PUBLIC" # Change to "ECR" if using AWS ECR
    }
    auto_deployments_enabled = false
  }

  instance_configuration {
    cpu    = "1024" # Adjust CPU and memory according to your application's needs
    memory = "2048"
  }

  network_configuration {
    egress_configuration {
      egress_type = "DEFAULT" # Default egress configuration
    }
  }
}
