resource "aws_ecr_repository" "ecr" {
  for_each             = toset(var.ecr_name)
  name                 = each.key
  
  image_scanning_configuration {
    scan_on_push = false
  }
  tags = var.tags
}
