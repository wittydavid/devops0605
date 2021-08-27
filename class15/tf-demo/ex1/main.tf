provider "aws" {
  region = "us-east-1"
}

module "my_dev" {
  source = "../my-module"
  server_name = "moshe"
  instance_type = "t2.micro"
}

module "my_prod" {
  source = "../my-module"
  server_name = "david"
  instance_type = "t2.medium"
}

output "dev" {
  value = module.my_dev.server_address
}

output "prod" {
  value = module.my_prod.server_address
}