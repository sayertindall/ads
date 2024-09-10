

# Ad Campaign Manager

## Overview

Ad Campaign Manager is an AI-driven system designed to automate and optimize digital advertising campaigns. It integrates advanced AI/ML capabilities with ad management tools to create, test, and refine ad campaigns for maximum effectiveness.

## Features

- AI-powered copywriting and image generation
- Automated A/B testing for ads and landing pages
- Integration with Meta (Facebook/Instagram) ad platforms
- Real-time performance tracking and analytics
- Customer Acquisition Cost (CAC) calculation
- Workflow automation for campaign optimization

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/ad_campaign_manager.git
cd ad_campaign_manager
```

2. Set up a virtual environment:
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Set up the environment variables:
Copy the `.env.example` file to `.env` and fill in the required values.

5. Initialize the database:
```
python scripts/setup_db.py
```

## Usage
To start the application, run:
```
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## Development
To set up the development environment:
1. Install development dependencies:
```
pip install -e ".[dev]"
```

2. Run tests:
```
pytest
```

3. Check code style:
```
flake8 .
black .
isort .
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
