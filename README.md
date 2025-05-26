# Sample AI Agent (Google API Key Demo)

This project provides a basic template for an AI agent that might use a Google API key. It includes a simulated AI function and unit tests.

**IMPORTANT SECURITY NOTICE:**
The API key `AIzaSyDYyffXJ0yk818WAp1RHb5sGPALbxv0x94` included in this README and in the `agent.py` (as a fallback) is for **demonstration purposes only**. 
*   **Do NOT use this key for production applications.**
*   **Avoid hardcoding API keys directly into your code.**
*   The recommended way to handle API keys is through environment variables.

## Files

*   `agent.py`: A Python script with a simulated AI function (`run_ai_agent`) that shows how an API key might be used.
*   `test_agent.py`: Unit tests for `agent.py`.

## Setup

### API Key Configuration

For the script to work (even in its simulated state demonstrating API key usage), it's best to set the `GOOGLE_API_KEY` environment variable.

**Linux/macOS:**
```bash
export GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"
```

Replace `"YOUR_ACTUAL_API_KEY"` with your real Google API key. If this variable is not set, `agent.py` will use the demonstration key `AIzaSyDYyffXJ0yk818WAp1RHb5sGPALbxv0x94` and print a warning.

## Running the Agent

To run the simulated agent:

```bash
python agent.py
```

The script will prompt you to enter some text, and it will display a simulated AI response.

## Running Unit Tests

To run the unit tests:

```bash
python test_agent.py
```

## Disclaimer

This is a template and a demonstration. The `run_ai_agent` function in `agent.py` **does not make any actual calls to Google AI services**. You will need to:
1.  Identify the specific Google AI service you intend to use.
2.  Install the appropriate Google Cloud client libraries or SDKs.
3.  Replace the simulated logic in `run_ai_agent` with actual calls to the Google AI service, using the API key.
4.  Ensure your API key has the necessary permissions and billing is configured for the Google Cloud project if required.