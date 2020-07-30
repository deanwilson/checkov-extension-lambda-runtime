from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class LambdaAllowedRuntime(BaseResourceCheck):
    def __init__(self):
        name = "Lambda runtime is allowed"
        id = "DW_AWS_01"
        supported_resources = ['aws_lambda_function']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
             Looks for Lambdas that use language runtimes we do not want
             to support in production.

        :param conf: aws_lambda_function configuration
        :return: <CheckResult>
        """
        allowed_runtimes = [
            "python3.6",
            "python3.7",
            "python3.8",
            "ruby2.7",
        ]

        runtime = conf['runtime'][0]

        if runtime in allowed_runtimes:
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED

scanner = LambdaAllowedRuntime()
