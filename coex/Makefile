.PHONY: dev test iac-plan iac-apply release

dev:
	@echo "starting dev stack"

test:
	PYTHONPATH=.. pytest

iac-plan:
	terraform -chdir=iac/terraform/envs/$(ENV) plan

iac-apply:
		terraform -chdir=iac/terraform/envs/$(ENV) apply

release:
		@echo "release"
