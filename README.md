Python script to send an email with SendGrid using a SendGrid API Key

# Install
```
pip install sendgridsend
```

# Use:
```bash
# Python GIt Clone version

.\SG.py `
  -ApiKey "SG.xxxxxx" `
  -From you@example.com `
  -To alice@example.com,bob@example.com `
  -Subject "Hello" `
  -Text "This is a test." `
  -Cc carol@example.com `
  -Bcc dan@example.com

# PIP version
sendgridsend `
  -ApiKey "SG.xxxxxx" `
  -From you@example.com `
  -To alice@example.com,bob@example.com `
  -Subject "Hello" `
  -Text "This is a test." `
  -Cc carol@example.com `
  -Bcc dan@example.com

  ```
