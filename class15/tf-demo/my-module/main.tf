variable "server_name" {}

variable "instance_type" {
  default = "t2.nano"
}

resource "aws_instance" "web" {
  ami = "ami-0b898040803850657"
  instance_type = var.instance_type
  tags = {
    Name = var.server_name
  }
}

output "server_address" {
  value = aws_instance.web.public_dns
}