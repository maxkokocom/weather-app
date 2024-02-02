module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "${var.app_name}-lambda-with-layer"
  description   = "My awesome lambda function"
  handler       = "main.lambda_handler"
  runtime       = "python3.9"
  publish       = true

  source_path = "../src/lambda-function1"

  store_on_s3 = true
  s3_bucket   = "${var.app_name}-my-bucket-id-with-lambda-builds"

  layers = [
    module.lambda_layer_s3.lambda_layer_arn,
  ]

  environment_variables = {
    Serverless = "Terraform"
  }

  tags = {
    Module = "lambda-with-layer"
  }
}

module "lambda_layer_s3" {
  source = "terraform-aws-modules/lambda/aws"

  create_layer = true

  layer_name          = var.app_name
  description         = "My amazing lambda layer (deployed from S3)"
  compatible_runtimes = var.python_versions

  source_path = var.source_path

  store_on_s3 = true
  s3_bucket   = "${var.app_name}-my-bucket-id-with-lambda-builds"
}