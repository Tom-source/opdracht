terraform {
  required_version = "~> 1.8.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "twijn"
    key            = "tfstate/terraform.tfstate"
    dynamodb_table = "twijntable"
    region         = "us-east-1"
  }
}
provider "aws" {
  region = "us-east-1"
}
