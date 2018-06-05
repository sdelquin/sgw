import sendgrid


class SendGrid:

    def __init__(self, apikey, from_addr, from_name):
        self.sg = sendgrid.SendGridAPIClient(apikey=apikey)
        self.data = {
            "personalizations": [{
                "to": [],
                "subject": None
            }],
            "from": {
                "email": from_addr,
                "name": from_name
            },
            "content": [{
                "type": "text/plain",
                "value": None
            }]
        }

    def send(self, to, subject, msg, cc=[], bcc=[]):
        # personalizations -> to
        addrs = to if type(to) == list else [to]
        for addr in addrs:
            self.data["personalizations"][0]["to"].append({"email": addr})
        # personalizations -> subject
        self.data["personalizations"][0]["subject"] = subject
        # content -> value
        self.data["content"][0]["value"] = msg
        # personalizations -> cc
        if cc:
            self.data["personalizations"][0]["cc"] = []
            addrs = cc if type(cc) == list else [cc]
            for addr in addrs:
                self.data["personalizations"][0]["cc"].append({"email": addr})
        # personalizations -> bcc
        if bcc:
            self.data["personalizations"][0]["bcc"] = []
            addrs = bcc if type(bcc) == list else [bcc]
            for addr in addrs:
                self.data["personalizations"][0]["bcc"].append({"email": addr})

        self.response = self.sg.client.mail.send.post(request_body=self.data)

        # print(self.response.status_code)
        # print(self.response.body)
        # print(self.response.headers)
