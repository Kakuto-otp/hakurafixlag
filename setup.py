from setuptools import setup, find_packages

setup(
    name="hakurafixlag",
    version="1.0.0",
    description="Fix lag Android và gửi file Telegram tự động.",
    author="Kakuto-otp",
    packages=find_packages(),
    package_dir={"hakurafixlag": "hakurafixlag"}, 
    install_requires=["pyTelegramBotAPI"],
    entry_points={
        "console_scripts": [
            "fixlag=hakurafixlag.cli:main"
        ]
    }
)
