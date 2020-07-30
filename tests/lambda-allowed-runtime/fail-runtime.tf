resource "aws_lambda_function" "process_scans" {
  filename         = var.lambda_zip_location
  source_code_hash = filebase64sha256(var.lambda_zip_location)
  function_name    = "sample lambda"
  role             = aws_iam_role.sample_lambda_role.arn
  handler          = "sample_lambda.main"
  runtime          = "nodejs12.x"
  timeout          = "900"
  memory_size      = 2048
}
