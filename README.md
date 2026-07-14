# Page Turner

## Project Outline
Page Turner is a web application that allows users to browse a collection of books, read user-submitted reviews, and check average star ratings.

## Development Environment
- **Language:** Python
- **Package Manager / Venv:** [uv](https://github.com/astral-sh/uv)

## Tools Configuration
- **Linting & Formatting:** [Ruff](https://github.com/astral-sh/ruff)
- **Testing & Coverage:** `pytest` & `pytest-cov`

## Setup Instructions
1. Install `uv` if you haven't already.
2. Clone this repository.
3. Run `uv sync` to install dependencies and set up the virtual environment.

## API / URL Routing (Exercise 6)
The following basic view functions and URLs have been implemented:
- **Home Page (Book List)**: `/` -> `views.index`
- **Book Detail Page**: `/book/<int:book_id>/` -> `views.book_detail`
- **Submit Review (Process Request)**: `/book/<int:book_id>/review/` -> `views.submit_review`
