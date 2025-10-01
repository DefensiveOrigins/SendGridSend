#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.request

API_URL = "https://api.sendgrid.com/v3/mail/send"

def main():
    p = argparse.ArgumentParser(description="Send a plain-text email via SendGrid")
    p.add_argument("--api-key", required=True, help="SendGrid API key (SG.xxxxx)")
    p.add_argument("--from", dest="from_email", required=True, help="From email")
    p.add_argument("--to", required=True, nargs="+", help="To email(s), space-separated")
    p.add_argument("--subject", required=True, help="Email subject")
    p.add_argument("--text", required=True, help="Plain text body")
    p.add_argument("--cc", nargs="*", default=[], help="CC email(s)")
    p.add_argument("--bcc", nargs="*", default=[], help="BCC email(s)")
    args = p.parse_args()

    def add_personalizations(emails, field):
        return [{ "email": e } for e in emails] if emails else None

    payload = {
        "personalizations": [{
            "to": add_personalizations(args.to, "to"),
            **({"cc": add_personalizations(args.cc, "cc")} if args.cc else {}),
            **({"bcc": add_personalizations(args.bcc, "bcc")} if args.bcc else {}),
            "subject": args.subject
        }],
        "from": { "email": args.from_email },
        "content": [{
            "type": "text/plain",
            "value": args.text
        }]
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, method="POST", headers={
        "Authorization": f"Bearer {args.api_key}",
        "Content-Type": "application/json"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            # SendGrid returns 202 Accepted on success with an empty body
            if resp.status == 202:
                print("Email accepted by SendGrid (202).")
            else:
                print(f"Unexpected status: {resp.status}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"SendGrid error {e.code}:\n{body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
