run:
	cd app && uvicorn main:app --reload

docker-build:
	cd app && docker build -t runtime-authority-lab .

docker-run:
	docker run -p 8000:8000 runtime-authority-lab

scan:
	./scripts/scan.sh

deploy:
	./scripts/deploy.sh

verify:
	./scripts/verify.sh