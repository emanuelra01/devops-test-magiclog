############CREATING A ECS CLUSTER#############

resource "aws_ecs_cluster" "cluster" {
  name = "cluster"
  setting {
    name  = "test-magiclog-dev"
    value = "enabled"
  }
}