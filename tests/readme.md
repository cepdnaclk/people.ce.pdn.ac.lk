# End-to-end tests for people.ce.pdn.ac.lk

How to run:

1. Ensure the site is available locally (default <http://localhost:4000/>).
2. Install dependencies and Playwright browsers:
       pip install -r requirements.txt
       playwright install
3. Run the Playwright pytest suite:
       pytest --base-url=<http://localhost:4000/>
