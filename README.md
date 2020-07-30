# Allowed Lambda Runtime Checkov extension

A Checkov extension to ensure correct lambda runtimes are in use.

## Introduction

This repository provides an extension to
[Checkov](https://www.checkov.io/), "_a static code analysis tool for
infrastructure-as-code. It scans cloud infrastructure managed in
Terraform, Cloudformation or kubernetes and detects misconfigurations._", to detect
Lambda functions using an undesired runtime such as NodeJS if you are a python
based platform.

    Check: DW_AWS_01: "Lambda runtime is allowed"
      FAILED for resource: aws_lambda_function.process_scans
      File: /fail-runtime.tf:1-10

      1  | resource "aws_lambda_function" "process_scans" {
      ... snip ...
      7  |   runtime          = "nodejs12.x"

## Usage

Once you've installed `checkov`, which can be achieved using `pip install
checkov`, you can use its `--external-checks-git` option to download
third party checks at runtime

    checkov --external-checks-git https://github.com/deanwilson/checkov-extension-lambda-runtime.git//extra_checks -d .

## Testing the check - developers

To test the check, install `checkov` and clone this repository. Once
you're in the root directory you can run `checkov` against the provided
test files

    # should fail
    checkov --external-checks-dir my_extra_checks -f tests/lambda-allowed-runtime/fail-runtime.tf

    Check: DW_AWS_01: "Lambda runtime is allowed"
      FAILED for resource: aws_lambda_function.process_scans
      File: /fail-runtime.tf:1-10
    
        1  | resource "aws_lambda_function" "process_scans" {
        2  |   filename         = var.lambda_zip_location
        3  |   source_code_hash = filebase64sha256(var.lambda_zip_location)
        4  |   function_name    = "sample lambda"    
        5  |   role             = aws_iam_role.sample_lambda_role.arn
        6  |   handler          = "sample_lambda.main"
        7  |   runtime          = "nodejs12.x"
        8  |   timeout          = "900"
        9  |   memory_size      = 2048
        10 | }


    # should pass
    checkov --external-checks-dir my_extra_checks -f tests/lambda-allowed-runtime/pass-runtime.tf

    Check: DW_AWS_01: "Lambda runtime is allowed"
      PASSED for resource: aws_lambda_function.process_scans
      File: /pass-runtime.tf:1-10

### Author

 * [Dean Wilson](https://www.unixdaemon.net)
