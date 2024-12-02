# MITRA - DOJ Navigation Assistant

MITRA (Modern Interactive Tool for Resource Access) is an AI-powered navigation assistant built for the Department of Justice website. It helps visitors easily find information, navigate services, and understand legal processes through natural conversation.

## Features

- Natural language chat interface using Dialogflow
- Voice input support for hands-free interaction
- Integration with Groq LLM API for intelligent responses
- Content filtering for appropriate responses
- Responsive design that works on desktop and mobile
- Accessibility features for screen readers
- Intuitive DOJ website navigation assistance
- Quick access to legal resources and documents
- Information about DOJ services and processes
- Natural language understanding powered by Dialogflow
- Voice input support for hands-free interaction
- Integration with Groq LLM for intelligent responses
- Content filtering for appropriate responses
- Responsive design that works on desktop and mobile
- Accessibility features for screen readers

## Technologies Used

- Frontend:
  - HTML/CSS/JavaScript 
  - Dialogflow Messenger
  - Web Speech API for voice input
  
- Backend:
  - FastAPI
  - Groq API for LLM capabilities
  - Python 3.8+

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mitra-doj-assistant.git
cd mitra-doj-assistant
```

## Project Structure

```
mitra-doj-assistant/
├── server.py           # FastAPI backend server
├── index.html         # Frontend interface
├── .env              # Environment variables
├── intents/          # Dialogflow intents
│   └── intents.json  # Pre-configured intents for DOJ navigation
├── ngrok.exe         # Ngrok executable for HTTPS tunneling
└── README.md
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install fastapi uvicorn groq python-dotenv
```

4. Configure environment variables:
- Create a `.env` file in the project root
- Add your Groq API key:
```
GROQ_API_KEY="your_groq_api_key_here"
```

5. Set up Dialogflow:
- Create a new project in Dialogflow
- Set up intents for navigation and legal queries
- Import the pre-configured intents from `intents/intents.json`
- Get your Dialogflow Messenger code
- Add it to the `index.html` file where indicated

## Running the Project

1. Start the FastAPI backend:
```bash
uvicorn server:app --reload --port 8000
```

2. (Optional) Set up HTTPS with ngrok:
```bash
# Start ngrok tunnel to your FastAPI server
./ngrok http 8000

# Copy the HTTPS URL provided by ngrok
# Update your Dialogflow webhook URL with the ngrok HTTPS URL
```

2. Serve the frontend:
- For development, you can use Python's built-in server:
```bash
# Python 3
python -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080
```
- For production, use a proper web server like Nginx or Apache

3. Access the application:
- Open your browser and go to `http://localhost:8080`
- The MITRA chatbot interface should appear in the bottom right corner

## Dialogflow Setup Details

1. Import Intents:
   - Navigate to your Dialogflow project
   - Go to Settings > Import/Export
   - Import the `intents/intents.json` file
   - This will set up pre-configured intents for:
     - DOJ navigation queries
     - Legal document searches
     - Service information requests
     - Contact information queries

2. Configure Webhook:
   - In Dialogflow, go to Fulfillment
   - Enable webhook
   - Set the URL to your FastAPI endpoint:
     - Local: `https://<ngrok-url>/dialogflow-webhook`
     - Production: `https://your-domain.com/dialogflow-webhook`

## Usage Tips

- Click the chat icon to open MITRA
- Type your question or click the microphone icon for voice input
- Ask about:
  - Navigation help
  - Legal documents and resources
  - DOJ services and processes
  - Contact information
  - Department locations and hours

## Troubleshooting

Common issues and solutions:

1. Chatbot not appearing:
   - Check if Dialogflow code is properly added to index.html
   - Ensure JavaScript is enabled in your browser

2. Voice input not working:
   - Make sure you're using a supported browser (Chrome recommended)
   - Grant microphone permissions when prompted

3. Backend connection issues:
   - Verify the FastAPI server is running
   - Check CORS settings if needed
   - Ensure GROQ_API_KEY is properly set

4. Webhook issues:
   - Verify ngrok is running and URL is correct
   - Check ngrok tunnel status
   - Ensure webhook URL is properly set in Dialogflow
   - Check FastAPI logs for any errors

## Development

To modify or extend MITRA:

1. Backend changes:
   - Edit `server.py` to modify response logic
   - Add new routes for additional functionality

2. Frontend changes:
   - Modify the chat interface in `index.html`
   - Adjust styles for the chat window
   - Update voice input handling

3. Dialogflow updates:
   - Add new intents for different types of queries
   - Improve entity recognition
   - Update training phrases
   - Modify existing intents in `intents/intents.json`

## License

This project is licensed under the MIT License.
