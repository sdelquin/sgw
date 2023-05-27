# SGW (SendGrid Wrapper)

Python wrapper for [SendGrid](https://github.com/sendgrid/sendgrid-python).

> Sending emails is that easy!

## Usage

1. Grab your [SendGrid API Key](https://docs.sendgrid.com/ui/account-and-settings/api-keys).
2. Code!

```python
>>> from sendgrid import SendGrid
>>> handler = SendGrid('YOUR_SENDGRID_API_KEY', 'from_addr@example.com', 'From Name')
>>> handler.send(to='hello@example.com', subject='Hi there', msg='This is just a test')
```

### Advanced usage

Function `send()` also admits some more parameters:

- `cc`: as a list of emails for carbon copy.
- `bcc`: as a list of emails for blind carbon copy.
- `attachments`: as a list of paths for file attachments.
- `as_markdown`: as a boolean (if True msg will be rendered from Markdown).
