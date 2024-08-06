#  User-splitter bot


## Beginning of work

### Create .env with:

   ```sh
    cp .env.example .env
   ```

Then you should use any tunneling like ngrok. 
Put your host link to TELEGRAM_WEBHOOK_HOST variable.

### Start the app with:

   ```sh
    python setup.py
   ```

You can ensure that the app has started by following the healthcheck link /api/internal/healthcheck
