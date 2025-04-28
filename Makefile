NAME = Flagle
ENV_NAME = venv

all: env

# Create the virtual environment if it does not exist.
env:
	@if [ ! -d $(ENV_NAME) ]; then \
		python3 -m venv $(ENV_NAME); \
		. $(ENV_NAME)/bin/activate; \
		pip install Pillow > /dev/null 2>&1; \
		pip install screeninfo > /dev/null 2>&1; \
		echo "$(GREEN)[$(NAME)]:\t $(ENV_NAME) created$(RESET)"; \
	fi


# Run the app
run: env
	@echo "$(BLUE)[$(NAME)]:\t RUN$(RESET)"
	$(ENV_NAME)/bin/python source/$(NAME).py


build: env

clean:
	@rm -rf source/__pycache__/
	@rm -rf source/Gui/__pycache__/
	@echo "$(RED)[$(NAME)]:\t CLEAN$(RESET)"

fclean: clean
	@rm -fr ./$(ENV_NAME)
	@rm -fr build/
	@rm -fr dist/
	@rm -f *.spec
	@echo "$(RED)[$(NAME)]:\t FCLEAN$(RESET)"

re: fclean all

#COLORS

GREEN=\033[0;32m
RED=\033[0;31m
BLUE=\033[0;34m
RESET=\033[0m