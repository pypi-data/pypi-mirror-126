import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "serverless-container-constructs",
    "version": "0.1.19",
    "description": "CDK patterns for modern application with serverless containers on AWS",
    "license": "UNLICENSED",
    "url": "https://github.com/aws-samples/serverless-container-constructs",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<hunhsieh@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws-samples/serverless-container-constructs"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "serverless_container_constructs",
        "serverless_container_constructs._jsii"
    ],
    "package_data": {
        "serverless_container_constructs._jsii": [
            "serverless-container-constructs@0.1.19.jsii.tgz"
        ],
        "serverless_container_constructs": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-certificatemanager>=1.95.2, <2.0.0",
        "aws-cdk.aws-ec2>=1.95.2, <2.0.0",
        "aws-cdk.aws-ecs>=1.95.2, <2.0.0",
        "aws-cdk.aws-efs>=1.95.2, <2.0.0",
        "aws-cdk.aws-elasticloadbalancingv2>=1.95.2, <2.0.0",
        "aws-cdk.aws-events-targets>=1.95.2, <2.0.0",
        "aws-cdk.aws-events>=1.95.2, <2.0.0",
        "aws-cdk.aws-iam>=1.95.2, <2.0.0",
        "aws-cdk.aws-lambda>=1.95.2, <2.0.0",
        "aws-cdk.aws-logs>=1.95.2, <2.0.0",
        "aws-cdk.aws-rds>=1.95.2, <2.0.0",
        "aws-cdk.aws-route53-targets>=1.95.2, <2.0.0",
        "aws-cdk.aws-route53>=1.95.2, <2.0.0",
        "aws-cdk.aws-s3>=1.95.2, <2.0.0",
        "aws-cdk.aws-secretsmanager>=1.95.2, <2.0.0",
        "aws-cdk.core>=1.95.2, <2.0.0",
        "cdk-nag>=0.1.19, <0.2.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.42.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
