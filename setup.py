from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ad_campaign_manager",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-driven ad campaign management system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ad_campaign_manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fastapi>=0.68.0,<0.69.0",
        "pydantic>=1.8.0,<2.0.0",
        "uvicorn>=0.15.0,<0.16.0",
        "sqlalchemy>=1.4.0,<1.5.0",
        "alembic>=1.6.0,<1.7.0",
        "python-jose[cryptography]>=3.3.0,<3.4.0",
        "passlib[bcrypt]>=1.7.4,<1.8.0",
        "python-multipart>=0.0.5,<0.0.6",
        "requests>=2.26.0,<2.27.0",
        "transformers>=4.11.0,<4.12.0",
        "torch>=1.9.0,<1.10.0",
        "pillow>=8.3.0,<8.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5,<6.3.0",
            "pytest-cov>=2.12.1,<2.13.0",
            "flake8>=3.9.2,<3.10.0",
            "black>=21.9b0,<21.10b0",
            "isort>=5.9.3,<5.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ad-campaign-manager=app.main:main",
        ],
    },
)
