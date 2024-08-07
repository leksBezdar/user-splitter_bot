#  User-splitter bot


## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

- Docker
- Docker Compose
- GNU Make

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/leksbezdar/user-splitter_bot.git
    cd user-splitter_bot
    ```

2. Create a `.env` file in the project root directory and add your environment variables. You can use the `.env.example` as a reference.

    ```sh
    cp .env.example .env
    ```

### Create .env with:

   ```sh
    cp .env.example .env
   ```

Then you should use any tunneling like ngrok.
Put your host link to TELEGRAM_WEBHOOK_HOST variable.

### Start the app with:

   ```sh
   make all
   ```

You can ensure that the app has started by following the healthcheck link /api/internal/healthcheck
Also you can inspect your http requests by following the link localhost:4040/inspect/http
