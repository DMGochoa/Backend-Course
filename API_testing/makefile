DEATULT_TAGS=tc_01
TAGS="$(DEATULT_TAGS)"
REPORT_FILE=./reports/cucumber_report.json
ENV="testing"

DEFAULT_CONFIG_JSON=.configuration.json
CONFIG_JSON="${DEFAULT_CONFIG_JSON}"
DEFAULT_ENVIRONMENT_JSON=.environment.json
ENVIRONMENT_JSON="${DEFAULT_ENVIRONMENT_JSON}"


setup:
	@echo "Settin up"
	@echo "Installing PIPENV package..."
	python -m pip install pipenv
	@echo "Activating virtualenv"
	pipenv shell
	@echo "Installing dependencies..."
	pipenv install -d

static_code_analysis:
	@echo "Static Code analysis"
	pylint main/
	pylint tests/
	flake8 main/ --benchmark
	flake8 tests/ --benchmark
	pycodestyle main/ --benchmark
	pycodestyle tests/ --benchmark

test:
	@echo "Executing testing scenarios with TAGS: $(TAGS)"
	@echo "Report file: $(REPORT_FILE)"
	python -m pytest --cache-clear --cucumber-json="$(REPORT_FILE)" -vsm "$(TAGS) and not refactor"
	@echo "Finished testing."

report:
	@echo "Generating html report"
	pipenv run node cucumberReportGenerator.js