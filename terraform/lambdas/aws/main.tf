module "weather-test-app" {
  source = "../../modules/python_lambda"

  app_name = "weather-app"
  source_path = "../src"
}

#module "different-app" {
#  source = "../../modules/python_lambda"
#
#  app_name = "different-app"
#  source_path = "../src/different"
#}