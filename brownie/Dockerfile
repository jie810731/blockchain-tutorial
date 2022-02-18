FROM alpine AS base

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       gcc\
                       g++\
                       gcompat\
                       python3-dev\
                       python3\
                       py3-pip\
                       linux-headers\
                       make\
                       nodejs=16.14.0-r0\
                       npm

RUN python3 -m pip install --user pipx; \
    python3 -m pipx ensurepath

ENV PATH="/root/.local/bin:$PATH" 

RUN pipx install eth-brownie

RUN npm install ganache --global

CMD ["/bin/sh"]
