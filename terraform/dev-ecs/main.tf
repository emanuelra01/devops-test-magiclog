############CREATING A ECS CLUSTER#############

resource "aws_ecs_cluster" "cluster" {
  name = "test-magiclog-dev"
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}