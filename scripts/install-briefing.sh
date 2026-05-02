#!/bin/bash
set -e

COGITO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PLIST_NAME="com.cogito.briefing"
PLIST_SRC="$COGITO_DIR/com.cogito.briefing.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/$PLIST_NAME.plist"
SCRIPT_PATH="$COGITO_DIR/scripts/daily-briefing.py"

echo ""
echo "Cogito — Daily Briefing Setup"
echo "─────────────────────────────"
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3 to continue."
    exit 1
fi

# Install anthropic if needed
if ! python3 -c "import anthropic" &>/dev/null; then
    echo "Installing anthropic Python package..."
    pip3 install anthropic --quiet
fi

# Collect credentials
read -rp "Anthropic API key: " ANTHROPIC_API_KEY
read -rp "Gmail address (used to send the briefing): " GMAIL_USER
read -rsp "Gmail app password: " GMAIL_APP_PASSWORD
echo ""
read -rp "Send briefing to (email address): " BRIEFING_EMAIL
read -rp "Send time (24h HH:MM, e.g. 07:30): " SEND_TIME

SEND_HOUR=$(echo "$SEND_TIME" | cut -d: -f1 | sed 's/^0//')
SEND_MINUTE=$(echo "$SEND_TIME" | cut -d: -f2 | sed 's/^0//')

# Store credentials in macOS Keychain
echo ""
echo "Storing credentials in Keychain..."

security add-generic-password -U -s "cogito" -a "anthropic_api_key" -w "$ANTHROPIC_API_KEY"
security add-generic-password -U -s "cogito" -a "gmail_user" -w "$GMAIL_USER"
security add-generic-password -U -s "cogito" -a "gmail_app_password" -w "$GMAIL_APP_PASSWORD"
security add-generic-password -U -s "cogito" -a "briefing_email" -w "$BRIEFING_EMAIL"

echo "Credentials stored."

# Write launchd plist
PYTHON_BIN=$(which python3)

cat > "$PLIST_DEST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$PLIST_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON_BIN</string>
        <string>$SCRIPT_PATH</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>$SEND_HOUR</integer>
        <key>Minute</key>
        <integer>$SEND_MINUTE</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$HOME/.claude/cogito-briefing.log</string>
    <key>StandardErrorPath</key>
    <string>$HOME/.claude/cogito-briefing.log</string>
</dict>
</plist>
EOF

# Load the plist
launchctl unload "$PLIST_DEST" 2>/dev/null || true
launchctl load "$PLIST_DEST"

echo ""
echo "Done. Your daily briefing will arrive at $SEND_TIME every morning."
echo "Log: ~/.claude/cogito-briefing.log"
echo ""
echo "To test immediately:"
echo "  python3 $SCRIPT_PATH"
echo ""
echo "To uninstall:"
echo "  launchctl unload $PLIST_DEST && rm $PLIST_DEST"
